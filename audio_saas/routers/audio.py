from fastapi import APIRouter, UploadFile, File
from services.audio_service import save_audio

router = APIRouter(
    prefix="/audio",
    tags=["audio"]
)

@router.get("/")
async def audio_status():
    return {"message": "audio router working"}

@router.post("/upload")
async def upload_audio(file: UploadFile = File(...)):
    file_path = await save_audio(file)

    return {
        "message": "audio uploaded successfully",
        "file_path": file_path
    }