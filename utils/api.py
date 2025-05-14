import requests
import time

def ask_rag(question: str, thread_id: str) -> str:
    max_retries = 5
    for i in range(max_retries):
        try:
            response = requests.post(
                "http://backend:8000/ask",
                json={"question": question, "thread_id": thread_id},
                stream=True,
                timeout=5,
            )
            response.raise_for_status()
            break
        except requests.exceptions.ConnectionError:
            print(f"Backend no disponible, reintentando ({i+1}/{max_retries})...")
            time.sleep(2)
    else:
        raise RuntimeError("No se pudo conectar con el backend tras varios intentos")

    # Construir la respuesta progresivamente
    full_response = ""
    for line in response.iter_lines(decode_unicode=True):
        if line:
            full_response += line
    return full_response

def ask_executor(question: str, thread_id: str):
    response = requests.post(
        "http://backend:8000/ask-executor",
        json={"question": question, "thread_id": thread_id}
    )
    response.raise_for_status()
    return response.json()["response"]
