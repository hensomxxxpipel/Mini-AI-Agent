from fastapi import FastAPI
from langchain_ollama.llms import OllamaLLM
#from langchain_core.runnables import Runnable
from pydantic import BaseModel
import langsmith

# Inisialisasi FastAPI
app = FastAPI()

# Konfigurasi LangSmith untuk monitoring (Opsional)
#langsmith.init(api_key="lsv2_pt_41621bfea0fd49bd902a2246e6a7a00e", project="pr-uncommon-consumer-87")

# Inisialisasi model
llm = OllamaLLM(model="deepseek-r1:1.5b")

# Schema untuk input query
class QueryRequest(BaseModel):
    prompt: str

# Global list untuk menyimpan riwayat percakapan
chat_history = []

@app.post("/chat")
def chat(query: QueryRequest):
    response = llm.invoke(query.prompt)
    chat_entry = {"input": query.prompt, "response": response}
    chat_history.append(chat_entry)  # Simpan ke dalam riwayat
    return chat_entry

@app.get("/")
def root():
    return chat_history  # Tampilkan seluruh riwayat percakapan