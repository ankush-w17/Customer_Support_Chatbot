from fastapi import APIRouter, UploadFile, File, HTTPException
from app.schemas.ingest import IngestResponse
from app.services.rag_service import RAGService

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

    with open(file.filename, "wb") as f:
        f.write(contents)

    elements = partition(filename=file.filename)

    text = "\n".join(
        element.text for element in elements if element.text
    )

    if not text.strip():
        raise HTTPException(
            status_code=400,
            detail="No extractable text found in document."
        )

    rag_service.ingest_text(text)
    print("Extracted text length:", len(text))
    print("Preview:", text[:500])


    return IngestResponse(status="ingested")
