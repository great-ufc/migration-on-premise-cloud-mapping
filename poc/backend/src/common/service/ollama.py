from langchain_community.embeddings.ollama import OllamaEmbeddings

from src.config import settings


def get_embedding_function():
    embeddings = OllamaEmbeddings(model="llama2", base_url=settings.OLLAMA_BASE_URL)
    return embeddings
