from app import config  

from fastapi import FastAPI
from app.api.ingest import router as ingest_router
from app.api.query import router as query_router

app = FastAPI(
    title="Customer Support Knowledge Base Assistant",
    version="1.0.0"
)

app.include_router(ingest_router)
app.include_router(query_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
