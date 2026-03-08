from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path
from audio_saas.routers import audio

# Obtém o diretório base onde este arquivo está
BASE_DIR = Path(__file__).parent

app = FastAPI(
    title="Audio SaaS",
    description="Audio transcription and summarization API",
    version="0.1.0"
)

# Monta a pasta de arquivos estáticos (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

# Inclui apenas o router de áudio (não precisamos de auth e summary separados)
app.include_router(audio.router)


@app.get("/")
async def root():
    """Retorna a página principal do frontend."""
    return FileResponse(str(BASE_DIR / "static" / "index.html"))


@app.get("/health")
async def health_check():
    """Endpoint para verificar se a API está funcionando."""
    return {"status": "ok"}

