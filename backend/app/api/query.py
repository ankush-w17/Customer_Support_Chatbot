import datetime
from fastapi import APIRouter
from fastapi.concurrency import run_in_threadpool
from app.schemas.query import QueryRequest, QueryResponse
from app.services.rag_service import RAGService
from app.db import mongo_db

router = APIRouter()
rag_service = RAGService()


@router.post("/query", response_model=QueryResponse)
async def query_rag(request: QueryRequest):
    # Run sync RAG query in threadpool
    result = await run_in_threadpool(rag_service.query, request.question)
    
    # Log to MongoDB
    await mongo_db.db.chat_history.insert_one({
        "question": request.question,
        "answer": result["answer"],
        "grounded": result["grounded"],
        "timestamp": datetime.datetime.utcnow()
    })
    
    return QueryResponse(**result)
