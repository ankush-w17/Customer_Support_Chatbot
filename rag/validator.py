def validate_answer(answer: str) -> dict:
    if not answer or "could not find" in answer.lower():
        return {
            "answer": answer,
            "grounded": False,
        }

    return {
        "answer": answer,
        "grounded": True,
    }
