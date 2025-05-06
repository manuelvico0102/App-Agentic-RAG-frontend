import requests

def ask_rag(question: str, thread_id: str):
    response = requests.post(
        "http://localhost:8000/ask",
        json={"question": question, "thread_id": thread_id}
    )
    response.raise_for_status()
    return response.json()["response"]

def ask_executor(question: str, thread_id: str):
    response = requests.post(
        "http://localhost:8000/ask-executor",
        json={"question": question, "thread_id": thread_id}
    )
    response.raise_for_status()
    return response.json()["response"]
