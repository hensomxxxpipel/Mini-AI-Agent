import streamlit as st
import requests

st.set_page_config(page_title="Chatbot LLM", layout="centered")
st.title("Chatbot dengan LangChain & FastAPI")

user_input = st.text_area("Masukkan pertanyaan:")
if st.button("Kirim"):
    if user_input:
        response = requests.post("http://127.0.0.1:8000/chat", json={"prompt": user_input})
        st.write("Model:", response.json()["response"])
    else:
        st.warning("Masukkan teks sebelum mengirim.")
