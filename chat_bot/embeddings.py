"""Configuration des embeddings, partagée entre l'ingestion et le RAG.

Le modèle et les dimensions DOIVENT être identiques à l'ingestion et à la
requête : un écart rend la recherche vectorielle silencieusement inutilisable.

qwen3-embedding-8b est MRL : les dimensions sont tronquées à la demande via le
paramètre `dimensions`. Changer la valeur impose de ré-indexer la collection.
"""

import os

from langchain_openai import OpenAIEmbeddings

EMBEDDING_MODEL = os.environ.get("EMBEDDING_MODEL", "qwen/qwen3-embedding-8b")
EMBEDDING_DIMENSIONS = int(os.environ.get("EMBEDDING_DIMENSIONS", "1024"))
COLLECTION_NAME = os.environ.get("QDRANT_COLLECTION", "cv")


def get_embeddings() -> OpenAIEmbeddings:
    return OpenAIEmbeddings(
        model=EMBEDDING_MODEL,
        dimensions=EMBEDDING_DIMENSIONS,
        base_url="https://openrouter.ai/api/v1",
        api_key=os.environ["OPENROUTER_API_KEY"],
        # OpenRouter n'accepte pas les tableaux de tokens tiktoken que
        # langchain-openai envoie par défaut : envoyer les textes bruts.
        check_embedding_ctx_length=False,
    )
