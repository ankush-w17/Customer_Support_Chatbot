from langchain_groq import ChatGroq
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from rag.prompts import get_rag_prompt


def build_rag_chain(retriever):
    llm = ChatGroq(
        model="llama-3.3-70b-versatile", 
        temperature=0.2,
        max_tokens=512,
    )

    prompt = get_rag_prompt()

    rag_chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain
