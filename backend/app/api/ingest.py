from fastapi import APIRouter, UploadFile, File
from app.schemas.ingest import IngestResponse
from app.services.rag_service import RAGService

router = APIRouter()
rag_service = RAGService()


@router.post("/ingest", response_model=IngestResponse)
async def ingest_file(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8")

    rag_service.ingest_text(text)

    return IngestResponse(status="ingested")
