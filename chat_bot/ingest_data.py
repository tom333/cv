from langchain_community.vectorstores import Qdrant

from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_openai import OpenAIEmbeddings

import os 
################################################################
#
# Calcul des embeddings
#
################################################################

embeddings = OpenAIEmbeddings()

loader = DirectoryLoader(
    "./data/",
    glob="*.md",
    show_progress=True,
    loader_cls=UnstructuredMarkdownLoader,
)

docs = loader.load()

db = Qdrant.from_documents(docs, embeddings,
                            collection_name="cv",
                            url=os.environ["QDRANT_HOST"],)
                            

retriever = db.as_retriever()
