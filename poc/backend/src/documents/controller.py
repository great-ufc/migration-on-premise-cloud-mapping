import asyncio
from fastapi import APIRouter
from concurrent.futures import ThreadPoolExecutor 

from src.documents.service import (
    load_documents, 
    clear_documents, 
    get_documents,
    get_documents_id,
    get_document_by_id,
    delete_documents_by_id
)

document_router = APIRouter(prefix="/document", tags=["Document"])

@document_router.get("/load-docs")
async def load():
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        documents = await loop.run_in_executor(pool, load_documents)
    return {"message": "Loaded documents", "documents": documents}

@document_router.get("/clear-docs")
async def clear():
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        await loop.run_in_executor(pool, clear_documents)
    return {"message": "Cleared documents"}

@document_router.get("/get-docs")
async def get():
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        documents = await loop.run_in_executor(pool, get_documents)
    return {"documents": documents}

@document_router.get("/get-docs-ids")
async def get_docs_ids():
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        documents = await loop.run_in_executor(pool, get_documents_id)
    return {"documents": documents}

@document_router.get("/get-doc-by-id/{id}")
async def get_doc_by_id(id: str):
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        document = await loop.run_in_executor(pool, get_document_by_id, id)
    return {"document": document}

@document_router.delete("/delete-docs")
async def delete_docs(ids: list[str]):
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        await loop.run_in_executor(pool, delete_documents_by_id, ids)
    return {"message": "Deleted documents"}