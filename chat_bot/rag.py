import os

import chainlit as cl
from langchain.agents import create_agent
from langchain_core.messages import AIMessageChunk
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_qdrant import QdrantVectorStore
from langgraph.checkpoint.memory import MemorySaver
from qdrant_client import QdrantClient

from embeddings import COLLECTION_NAME, get_embeddings

################################################################
#
# Retrieval
#
################################################################

client = QdrantClient(url=os.environ["QDRANT_HOST"])
vectorstore = QdrantVectorStore(client, COLLECTION_NAME, get_embeddings())
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})


@tool
def search_cv(query: str) -> str:
    """Recherche des informations dans le CV de Thomas Guyader."""
    docs = retriever.invoke(query)
    if not docs:
        return "Aucune information pertinente trouvée dans le CV."

    snippets = []
    for i, doc in enumerate(docs, start=1):
        section = " > ".join(
            doc.metadata[k] for k in ("h1", "h2", "h3") if doc.metadata.get(k)
        )
        header = f"Extrait {i} (section : {section})" if section else f"Extrait {i}"
        snippets.append(f"{header}\n{doc.page_content}")
    return "\n\n".join(snippets)


################################################################
#
# Agent
#
################################################################

# Endpoint OpenAI-compatible (OpenRouter aujourd'hui ; LocalAI ou autre
# gateway demain : seul l'env change).
llm = ChatOpenAI(
    model=os.environ.get("MODEL_NAME", "deepseek/deepseek-v4-flash"),
    base_url=os.environ["LLM_BASE_URL"],
    api_key=os.environ["LLM_API_KEY"],
    temperature=0,
    streaming=True,
)

system_prompt = (
    "Tu es le représentant de Thomas Guyader et tu connais son curriculum vitae. "
    "Ton objectif est de le faire recruter par ceux qui te questionnent. "
    "Utilise l'outil search_cv pour récupérer des informations factuelles du CV avant de répondre. "
    "Mentionne la section du CV d'où provient l'information quand c'est pertinent. "
    "Si l'information n'est pas disponible, dis simplement que tu n'as pas été formé sur ce sujet."
)

agent = create_agent(
    model=llm,
    tools=[search_cv],
    system_prompt=system_prompt,
    checkpointer=MemorySaver(),
)


################################################################
#
# Chainlit
#
################################################################


@cl.on_chat_start
async def init():
    await cl.Message(
        content="Bonjour. \n Je suis le représentant virtuel de Thomas Guyader, "
        "Machine Learning Engineer / MLOps Architect. \n "
        "Comment puis je vous convaincre de l'embaucher ?"
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    answer = cl.Message(content="")
    try:
        async for msg, _metadata in agent.astream(
            {"messages": [("user", message.content)]},
            # Un thread par session Chainlit : chaque visiteur a sa propre
            # mémoire de conversation.
            {"configurable": {"thread_id": cl.context.session.id}},
            stream_mode="messages",
        ):
            if (
                isinstance(msg, AIMessageChunk)
                and isinstance(msg.content, str)
                and msg.content
            ):
                await answer.stream_token(msg.content)
    except Exception as exc:
        cl.logger.exception("Erreur agent : %s", exc)
        await cl.Message(
            content="Une erreur interne est survenue, merci de réessayer."
        ).send()
        return

    if not answer.content:
        answer.content = "Je n'ai pas de réponse pour le moment."
    await answer.send()
