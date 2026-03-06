from fastapi import FastAPI

from routers import audio, summary, auth

app = FastAPI(
    title="Audio SaaS",
    description="Audio transcription and summarization API",
    version="0.1.0"
)

app.include_router(audio.router)
app.include_router(summary.router)
app.include_router(auth.router)

@app.get("/health")
async def health_check():
    return {"status": "ok"}

