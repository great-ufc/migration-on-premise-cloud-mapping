from langchain.schema.document import Document
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.config import settings
from src.common.service.utils import calculate_chunk_ids
from src.common.service.chroma_db import (
    add_to_chroma,
    clear_database,
    delete_from_chroma,
)

DATA_PATH = settings.DATA_PATH
_docs: list[Document] = []


def load_documents() -> list[Document]:
    document_loader = PyPDFDirectoryLoader(DATA_PATH)
    _docs = document_loader.load()
    chunks = split_documents(_docs)
    add_to_chroma(chunks)
    return _docs

def get_documents() -> list[Document]:
    return _docs

def get_documents_id() -> list[str]:
    chunks_ids = calculate_chunk_ids(_docs)
    return [chunk.metadata["id"] for chunk in chunks_ids]

def get_document_by_id(id: str) -> Document | None:
    for doc in _docs:
        if doc.metadata["id"] == id:
            return doc
    return None

def delete_documents_by_id(ids: list[str]) -> None:
    for doc in _docs:
        if doc.metadata["id"] in ids:
            _docs.remove(doc)
    delete_from_chroma(ids)

def clear_documents() -> None:
    _docs.clear()
    clear_database()

def split_documents(documents: list[Document]) -> list[Document]:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.split_documents(documents)
