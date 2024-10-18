import os
from typing import Sequence

import chainlit as cl
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts.chat import MessagesPlaceholder
from langchain_core.runnables import RunnableConfig
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, StateGraph
from langgraph.graph.message import add_messages
from qdrant_client import QdrantClient
from typing_extensions import Annotated, TypedDict

embeddings = OpenAIEmbeddings()
client = QdrantClient(
    url=os.environ["QDRANT_HOST"],
)
vectorstore = QdrantVectorStore(client, "cv", embeddings)  #

retriever = vectorstore.as_retriever()
################################################################
#
# Création de la chain
#
################################################################


llm = ChatOpenAI(temperature=0, model="gpt-4o-mini", streaming=True)


### Contextualize question ###
contextualize_q_system_prompt = (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, "
    "just reformulate it if needed and otherwise return it as is."
)
contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_q_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)
history_aware_retriever = create_history_aware_retriever(
    llm, retriever, contextualize_q_prompt
)


system_prompt = (
    "Tu es le représentant de Thomas Guyader dont tu connais le curriculum vitae. "
    "Ton objectif est de le faire recruter par ceux qui te questionnent"
    "Si tu ne connais pas la réponse, dis simplement que tu n'as pas été formé sur ce sujet"
    "\n\n"
    "{context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

### Statefully manage chat history ###


class State(TypedDict):
    input: str
    chat_history: Annotated[Sequence[BaseMessage], add_messages]
    context: str
    answer: str


def call_model(state: State):
    response = rag_chain.invoke(state)
    return {
        "chat_history": [
            HumanMessage(state["input"]),
            AIMessage(response["answer"]),
        ],
        "context": response["context"],
        "answer": response["answer"],
    }


workflow = StateGraph(state_schema=State)
workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

memory = MemorySaver()
app = workflow.compile(checkpointer=memory)


config = {}

################################################################
#
# Chainlit
#
################################################################


@cl.on_chat_start
async def init():
    cl.user_session.set("rag_chain", app)
    msg = cl.Message(
        content="Bonjour. \n Je suis le représentant virtuel de Thomas Guyader, Data Architect. \n Comment puis je vous convaincre de l'embaucher ?"
    )
    await msg.send()


@cl.on_message
async def on_message(message: cl.Message):
    rag_chain = cl.user_session.get("rag_chain")

    res = rag_chain.invoke(
        {"input": message.content},
        config=RunnableConfig(
            callbacks=[
                cl.LangchainCallbackHandler(
                    to_ignore=[
                        "ChannelRead",
                        "RunnableLambda",
                        "ChannelWrite",
                        "__start__",
                        "_execute",
                        "call_model",
                    ]
                    # can add more into the to_ignore: "agent:edges", "call_model"
                    # to_keep=
                )
            ],
            configurable={"thread_id": "abc123"},
        ),
    )

    await cl.Message(content=res["answer"]).send()
