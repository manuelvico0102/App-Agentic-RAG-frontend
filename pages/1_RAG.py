import streamlit as st
import uuid
from utils.api import ask_rag
import requests

st.set_page_config(page_title="Chat Clásico", layout="centered")
st.title("💬 Chat RAG (Clásico)")

# Inicializar estructura de chats
if "chats" not in st.session_state:
    st.session_state.chats = {}

# Manejar creación diferida del nuevo chat
if "new_chat_id" in st.session_state:
    st.session_state.active_chat = st.session_state.new_chat_id
    del st.session_state.new_chat_id
    st.rerun()

# Botón para nuevo chat
if st.button("➕ Nuevo chat"):
    new_id = str(uuid.uuid4())
    st.session_state.chats[new_id] = []
    st.session_state.new_chat_id = new_id  # Guardar el nuevo chat y recargar
    st.rerun()

# Asegurarse de que haya un chat activo
if "active_chat" not in st.session_state:
    if st.session_state.chats:
        st.session_state.active_chat = list(st.session_state.chats.keys())[0]
    else:
        new_id = str(uuid.uuid4())
        st.session_state.chats[new_id] = []
        st.session_state.active_chat = new_id

# Selector de conversación
chat_ids = list(st.session_state.chats.keys())
selected_chat = st.selectbox(
    "Selecciona una conversación",
    chat_ids,
    index=chat_ids.index(st.session_state.active_chat),
    format_func=lambda x: f"Chat {x[:6]}"
)
st.session_state.active_chat = selected_chat

# Mostrar historial
chat_history = st.session_state.chats[st.session_state.active_chat]
with st.container():
    for msg in chat_history:
        st.chat_message(msg["role"]).markdown(msg["content"])

prompt = st.chat_input("Haz una pregunta...")

if prompt:
    chat_history.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        response = requests.post(
            "http://backend:8000/ask",
            json={"question": prompt, "thread_id": st.session_state.active_chat},
            stream=True,
        )
        response.raise_for_status()

        for line in response.iter_lines(decode_unicode=True):
            if line:
                full_response += line
                message_placeholder.markdown(full_response + "▌")

        message_placeholder.markdown(full_response)

    chat_history.append({"role": "assistant", "content": full_response})

