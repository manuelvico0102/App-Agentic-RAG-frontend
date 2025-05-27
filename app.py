import streamlit as st
import requests
import uuid

API_URL = "http://backend:8000/streaming-rag/submit-messages/stream"

st.set_page_config(page_title="RAG MultiChat", layout="wide")

# Inicializar estado de sesión
if "chats" not in st.session_state:
    st.session_state.chats = {}  # thread_id: [mensajes]
if "current_chat" not in st.session_state:
    st.session_state.current_chat = None

# Función para crear un nuevo chat
def create_new_chat():
    thread_id = str(uuid.uuid4())
    st.session_state.chats[thread_id] = []
    st.session_state.current_chat = thread_id

# Sidebar: Lista de chats
st.sidebar.title("Chats")
for thread_id in st.session_state.chats:
    button_label = f"🗨️ {thread_id[:8]}"
    if st.sidebar.button(button_label, key=thread_id):
        st.session_state.current_chat = thread_id

st.sidebar.markdown("---")
if st.sidebar.button("➕ Nuevo chat"):
    create_new_chat()

# Si no hay chat seleccionado, crear uno por defecto
if not st.session_state.current_chat:
    create_new_chat()

current_id = st.session_state.current_chat
st.title(f"Chat: {current_id[:8]}")
chat_history = st.session_state.chats[current_id]

# Mostrar historial
for entry in chat_history:
    st.chat_message(entry["role"]).write(entry["content"])

# Entrada del usuario
if prompt := st.chat_input("Haz una pregunta..."):
    st.chat_message("user").write(prompt)
    st.session_state.chats[current_id].append({"role": "user", "content": prompt})

    # Streaming desde el backend
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            response = requests.post(
                API_URL,
                json={"question": prompt, "thread_id": current_id},
                stream=True,
            )
            answer = ""
            for chunk in response.iter_lines(decode_unicode=True):
                if chunk:
                    st.write(chunk)
                    answer += chunk
            st.session_state.chats[current_id].append({"role": "assistant", "content": answer})