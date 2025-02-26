from fastapi import FastAPI
from backend.query_agent import process_query

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Titanic Chatbot API"}

@app.get("/query/")
def query(question: str):
    response = process_query(question)
    return {"response": response}
