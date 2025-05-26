from fastapi import FastAPI, Form
import requests
app = FastAPI()
def call_llm(prompt: str):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama2", "prompt": prompt, "stream": False},
        timeout=30
    )
    return response.json()["response"].strip()
@app.post("/analyze/")
def analyze_legal(text: str = Form(...)):
    prompts = {
        "summary": f"Summarize this legal document:\n\n{text}",
        "clauses": f"Extract key clauses from this legal text: \n\n{text}",
        "entities": f"Extract all named entities: \n\n{text}"
}
    results = {k: call_llm(p) for k, p in prompts.items()}
    return results