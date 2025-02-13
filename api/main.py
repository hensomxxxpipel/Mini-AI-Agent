from fastapi import FastAPI
from langchain_ollama.llms import OllamaLLM
from pydantic import BaseModel

app = FastAPI()

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
    chat_history.append(chat_entry)
    return chat_entry

@app.get("/")
def root():
    return chat_history