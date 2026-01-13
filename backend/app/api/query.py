from fastapi import APIRouter
from app.schemas.query import QueryRequest, QueryResponse
from app.services.rag_service import RAGService

router = APIRouter()
rag_service = RAGService()


@router.post("/query", response_model=QueryResponse)
def query_rag(request: QueryRequest):
    result = rag_service.query(request.question)
    return QueryResponse(**result)
