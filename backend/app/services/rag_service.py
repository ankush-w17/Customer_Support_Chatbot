from langchain_core.documents import Document

from rag.embeddings import get_embedding_model
from rag.vectorstore import create_faiss_index, load_faiss_index
from rag.retriever import get_retriever
from rag.chain import build_rag_chain
from rag.validator import validate_answer


class RAGService:
    def __init__(self):
        self.embeddings = get_embedding_model()
        self._load_chain()

    def _load_chain(self):
        db = load_faiss_index(self.embeddings)
        retriever = get_retriever(db)
        self.chain = build_rag_chain(retriever)

    def ingest_text(self, text: str):
        documents = [Document(page_content=text)]
        create_faiss_index(documents, self.embeddings)
        self._load_chain()

    def query(self, question: str) -> dict:
        answer = self.chain.invoke(question)
        return validate_answer(answer)
