from fastapi import FastAPI

app = FastAPI(
    title="Audio SaaS",
    description="Audio transcription and summarization API",
    version="0.1.0"
)


@app.get("/health")
async def health_check():
    return {"status": "ok"}