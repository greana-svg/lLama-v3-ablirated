from fastapi import FastAPI, Request
import requests

app = FastAPI()

LLAMA_URL = "http://127.0.0.1:8001/v1/chat/completions"

@app.post("/v1/chat/completions")
async def chat(req: Request):
    data = await req.json()

    # Future:
    # Count tokens
    # Summarize old messages if too large

    return requests.post(LLAMA_URL, json=data).json()