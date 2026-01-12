def get_retriever(vectorstore, k: int = 5):
    return vectorstore.as_retriever(
        search_kwargs={"k": k}
    )
