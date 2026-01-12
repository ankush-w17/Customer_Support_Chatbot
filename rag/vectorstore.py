from pathlib import Path
from langchain_community.vectorstores import FAISS

INDEX_PATH = Path("faiss_index")


def create_faiss_index(documents, embeddings):
    db = FAISS.from_documents(documents, embeddings)
    db.save_local(INDEX_PATH)
    return db


def load_faiss_index(embeddings):
    if not INDEX_PATH.exists():
        raise FileNotFoundError("FAISS index not found")

    return FAISS.load_local(
        INDEX_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )
