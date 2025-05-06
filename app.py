import streamlit as st

st.set_page_config(page_title="Inicio", layout="centered")
st.title("🤖 Chat Multiagente")

st.markdown("Selecciona cómo deseas interactuar con el agente:")

st.page_link("pages/1_RAG.py", label="💬 Chat Retriever", icon="🧠")
st.page_link("pages/2_Executor.py", label="⚙️ Chat Executor", icon="🤖")
