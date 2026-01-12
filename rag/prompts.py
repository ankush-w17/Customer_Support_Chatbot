from langchain_core.prompts import ChatPromptTemplate


def get_rag_prompt():
    return ChatPromptTemplate.from_template(
        """
You are a customer support knowledge base assistant.

Rules:
- Answer ONLY using the provided context.
- If the answer is not present, say:
  "I could not find this information in the knowledge base."

Context:
{context}

Question:
{question}
"""
    )
