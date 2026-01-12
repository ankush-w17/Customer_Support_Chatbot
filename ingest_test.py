from dotenv import load_dotenv
load_dotenv()

from langchain_core.documents import Document
from rag.embeddings import get_embedding_model
from rag.vectorstore import create_faiss_index

with open("sample_kb.txt", "r", encoding="utf-8") as f:
    text = f.read()

documents = [
    Document(
        page_content=text,
        metadata={"source": "sample_kb.txt"}
    )
]

embeddings = get_embedding_model()
create_faiss_index(documents, embeddings)

print(" FAISS index created successfully")
