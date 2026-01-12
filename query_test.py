from dotenv import load_dotenv
load_dotenv()

from rag.embeddings import get_embedding_model
from rag.vectorstore import load_faiss_index
from rag.retriever import get_retriever
from rag.chain import build_rag_chain
from rag.validator import validate_answer



embeddings = get_embedding_model()
db = load_faiss_index(embeddings)
retriever = get_retriever(db)

rag_chain = build_rag_chain(retriever)

question = "How do I reset my password?"

answer = rag_chain.invoke(question)

print("\n RAG Answer:")
print(answer)


validated = validate_answer(answer)

print("\n Validated Output:")
print(validated)
