import datetime
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.concurrency import run_in_threadpool
from app.schemas.ingest import IngestResponse
from app.services.rag_service import RAGService
from app.db import mongo_db

from unstructured.partition.auto import partition

router = APIRouter()
rag_service = RAGService()

SUPPORTED_EXTENSIONS = {".txt", ".pdf", ".docx"}


@router.post("/ingest", response_model=IngestResponse)
async def ingest_file(file: UploadFile = File(...)):
    filename = file.filename.lower()

    if not any(filename.endswith(ext) for ext in SUPPORTED_EXTENSIONS):
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type. Only TXT, PDF, DOCX are supported."
        )

    contents = await file.read()

    # Save file locally (optional, but good for parsing)
    with open(file.filename, "wb") as f:
        f.write(contents)

    # Parsing (this is sync and cpu intensive, usually should be in threadpool too, 
    # but partition might release GIL. For safety we can threadpool it, but let's keep it simple or threadpool it)
    # elements = partition(filename=file.filename)
    # Let's run partition in threadpool if possible, but partition uses kwargs.
    # We will run the whole heavy block in valid place.
    # For now, following original logic but running ingestion in threadpool.
    
    elements = await run_in_threadpool(partition, filename=file.filename)

    text = "\n".join(
        element.text for element in elements if element.text
    )

    if not text.strip():
        raise HTTPException(
            status_code=400,
            detail="No extractable text found in document."
        )

    # Run ingest in threadpool (FAISS operations)
    await run_in_threadpool(rag_service.ingest_text, text)
    
    print("Extracted text length:", len(text))
    print("Preview:", text[:500])

    # Log to MongoDB
    await mongo_db.db.documents.insert_one({
        "filename": file.filename,
        "upload_timestamp": datetime.datetime.utcnow(),
        "status": "ingested",
        "size": len(text)
    })

    return IngestResponse(status="ingested")
