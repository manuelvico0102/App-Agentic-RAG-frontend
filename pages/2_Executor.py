import streamlit as st
import uuid
from utils.api import ask_executor

st.set_page_config(page_title="Chat Executor", layout="centered")
st.title("⚙️ Chat con Executor Agent")

# Inicializar estructura de chats
if "chats_executor" not in st.session_state:
    st.session_state.chats_executor = {}

# Manejo de nuevo chat
if "new_executor_chat_id" in st.session_state:
    st.session_state.active_executor_chat = st.session_state.new_executor_chat_id
    del st.session_state.new_executor_chat_id
    st.rerun()

# Crear nuevo chat
if st.button("➕ Nuevo chat"):
    new_id = str(uuid.uuid4())
    st.session_state.chats_executor[new_id] = []
    st.session_state.new_executor_chat_id = new_id
    st.rerun()

# Asegurar que haya uno activo
if "active_executor_chat" not in st.session_state:
    if st.session_state.chats_executor:
        st.session_state.active_executor_chat = list(st.session_state.chats_executor.keys())[0]
    else:
        new_id = str(uuid.uuid4())
        st.session_state.chats_executor[new_id] = []
        st.session_state.active_executor_chat = new_id

# Selector de conversación
chat_ids = list(st.session_state.chats_executor.keys())
selected_chat = st.selectbox(
    "Selecciona una conversación",
    chat_ids,
    index=chat_ids.index(st.session_state.active_executor_chat),
    format_func=lambda x: f"Chat {x[:6]}"
)
st.session_state.active_executor_chat = selected_chat

# Mostrar historial
chat_history = st.session_state.chats_executor[selected_chat]
with st.container():
    for msg in chat_history:
        st.chat_message(msg["role"]).markdown(msg["content"])

# Input
prompt = st.chat_input("Haz una pregunta...")

if prompt:
    chat_history.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    with st.spinner("Pensando..."):
        answer = ask_executor(prompt, thread_id=selected_chat)

    chat_history.append({"role": "assistant", "content": answer})
    st.chat_message("assistant").markdown(answer)
