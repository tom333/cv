"""Indexe les fichiers markdown de ./data dans Qdrant.

Découpe par sections markdown (H1/H2/H3) : chaque chunk garde sa hiérarchie de
titres en métadonnées, réutilisée par le RAG pour citer les sections.

Recrée la collection à chaque exécution (obligatoire si le modèle ou les
dimensions d'embedding changent).
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from langchain_text_splitters import MarkdownHeaderTextSplitter

load_dotenv()

from embeddings import COLLECTION_NAME, get_embeddings  # noqa: E402 (après load_dotenv)

splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=[("#", "h1"), ("##", "h2"), ("###", "h3")]
)

docs = []
for path in sorted(Path("./data").glob("*.md")):
    for doc in splitter.split_text(path.read_text()):
        doc.metadata["source"] = path.name
        docs.append(doc)

if not docs:
    raise SystemExit("Aucun fichier markdown trouvé dans ./data")

print(f"{len(docs)} chunks à indexer dans la collection '{COLLECTION_NAME}'")

QdrantVectorStore.from_documents(
    docs,
    get_embeddings(),
    collection_name=COLLECTION_NAME,
    url=os.environ["QDRANT_HOST"],
    force_recreate=True,
)

print("Ingestion terminée")
