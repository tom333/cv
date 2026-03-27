import os

import chainlit as cl
from langchain_core.messages import AIMessage
from langchain_core.tools import tool
from langchain_core.runnables import RunnableConfig
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from qdrant_client import QdrantClient

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


@tool
def search_cv(query: str) -> str:
    """Recherche des informations dans le CV de Thomas Guyader."""
    docs = retriever.invoke(query)
    if not docs:
        return "Aucune information pertinente trouvée dans le CV."

    snippets = []
    for i, doc in enumerate(docs, start=1):
        snippets.append(f"Extrait {i}:\n{doc.page_content}")
    return "\n\n".join(snippets)


system_prompt = (
    "Tu es le représentant de Thomas Guyader et tu connais son curriculum vitae. "
    "Ton objectif est de le faire recruter par ceux qui te questionnent. "
    "Utilise l'outil search_cv pour récupérer des informations factuelles du CV avant de répondre. "
    "Si l'information n'est pas disponible, dis simplement que tu n'as pas été formé sur ce sujet."
)

memory = MemorySaver()
app = create_react_agent(
    model=llm,
    tools=[search_cv],
    prompt=system_prompt,
    checkpointer=memory,
)


config = {}

################################################################
#
# Chainlit
#
################################################################


@cl.on_chat_start
async def init():
    cl.user_session.set("agent", app)
    msg = cl.Message(
        content="Bonjour. \n Je suis le représentant virtuel de Thomas Guyader, Machine Learning Engineer / MLOps Architect. \n Comment puis je vous convaincre de l'embaucher ?"
    )
    await msg.send()


@cl.on_message
async def on_message(message: cl.Message):
    agent = cl.user_session.get("agent")
    if agent is None:
        await cl.Message(content="Erreur interne: agent non initialise.").send()
        return

    print("########### message ##############²²")
    print(message)
    res = await agent.ainvoke(
        {"messages": [("user", message.content)]},
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
    final_answer = "Je n'ai pas de reponse pour le moment."
    for msg in reversed(res.get("messages", [])):
        if isinstance(msg, AIMessage) and msg.content:
            if isinstance(msg.content, str):
                final_answer = msg.content
            else:
                final_answer = "\n".join(
                    part if isinstance(part, str) else str(part)
                    for part in msg.content
                )
            break

    await cl.Message(content=final_answer).send()
