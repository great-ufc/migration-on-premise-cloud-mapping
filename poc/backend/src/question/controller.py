from fastapi import APIRouter

from src.question.service import query_rag 
# 
question_router = APIRouter(prefix="/question", tags=["Question"])

@question_router.post("/ask", summary="Ask a question to the RAG model")
def response_question(req: dict):
    question = req.get("question", None)
    return {"question": question,  **query_rag(question)}