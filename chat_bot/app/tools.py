from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.tools.retriever import create_retriever_tool
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient


embeddings = OpenAIEmbeddings()

client = QdrantClient(url="localhost")
vectorstore = QdrantVectorStore(client, "cv", embeddings)

retriever = vectorstore.as_retriever()

retriever_tool = create_retriever_tool(
    retriever,
    "retrieve_spnc",
    "Contains and retrieve all informations",
)

tools = [retriever_tool]
