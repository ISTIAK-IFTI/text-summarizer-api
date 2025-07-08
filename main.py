# main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from summarizer import summarize_text  # assuming summarizer.py has a function named summarize_text

app = FastAPI()

# Allow requests from Flutter
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify only your device's IP if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/summarize")
async def summarize(request: Request):
    data = await request.json()
    text = data.get("text", "")
    summary = summarize_text(text)
    return {"summary": summary}
=======
# main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from summarizer import summarize_text  # assuming summarizer.py has a function named summarize_text

app = FastAPI()

# Allow requests from Flutter
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify only your device's IP if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/summarize")
async def summarize(request: Request):
    data = await request.json()
    text = data.get("text", "")
    summary = summarize_text(text)
    return {"summary": summary}

