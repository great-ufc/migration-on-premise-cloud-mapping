import os
import shutil
import logging

from langchain.schema.document import Document
from langchain_community.vectorstores import Chroma

from src.config import settings
from src.common.service.utils import calculate_chunk_ids
from src.common.service.ollama import get_embedding_function

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CHROMA_PATH = settings.CHROMA_PATH

db = Chroma(persist_directory=CHROMA_PATH, embedding_function=get_embedding_function())


def add_to_chroma(chunks: list[Document]) -> None:
    # Calculate Page IDs.
    chunks_with_ids = calculate_chunk_ids(chunks)

    # Add or Update the documents.
    existing_items = db.get(include=[])  # IDs are always included by default
    existing_ids = set(existing_items["ids"])
    logger.info(f"Number of existing documents in DB: {len(existing_ids)}")

    # Only add documents that don't exist in the DB.
    new_chunks = []
    for chunk in chunks_with_ids:
        if chunk.metadata["id"] not in existing_ids:
            new_chunks.append(chunk)

    if len(new_chunks):
        logger.info(f"👉 Adding new documents: {len(new_chunks)}")
        new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
        db.add_documents(new_chunks, ids=new_chunk_ids)
        db.persist()
    else:
        logger.info("✅ No new documents to add")

def delete_from_chroma(ids: list[str]) -> None:
    db.delete(ids)
    db.persist()

def clear_database():
    logger.info("✨ Clearing Database")
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)
    logger.info("✅ Database Cleared")

def similarity_search_with_score(query_text: str, k: int = 5):
    return db.similarity_search_with_score(query_text, k=k)
