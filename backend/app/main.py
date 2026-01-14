from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import config
from app.api.ingest import router as ingest_router
from app.api.query import router as query_router
from app.db import mongo_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await mongo_db.connect()
    yield
    await mongo_db.close()

app = FastAPI(
    title="Customer Support Knowledge Base Assistant",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ingest_router)
app.include_router(query_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
