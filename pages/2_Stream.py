import streamlit as st
from utils.api import stream_rag

st.set_page_config(page_title="Chat Streaming", layout="centered")
st.title("💬 Chat RAG (Streaming)")

if "chat_history_stream" not in st.session_state:
    st.session_state.chat_history_stream = []

with st.container():
    for msg in st.session_state.chat_history_stream:
        st.chat_message(msg["role"]).markdown(msg["content"])

prompt = st.chat_input("Haz una pregunta...")

if prompt:
    st.session_state.chat_history_stream.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    with st.spinner("Pensando..."):
        response_chunks = []
        message_placeholder = st.empty()

        for chunk in stream_rag(prompt):
            response_chunks.append(chunk)
            message_placeholder.markdown("".join(response_chunks))

        answer = "".join(response_chunks)

    st.session_state.chat_history_stream.append({"role": "assistant", "content": answer})
    st.chat_message("assistant").markdown(answer)
