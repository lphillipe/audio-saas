from fastapi import APIRouter, UploadFile, File

from services.audio_service import process_audio


router = APIRouter(
    prefix="/audio",
    tags=["audio"]
)


@router.post("/upload")
async def upload_audio(file: UploadFile = File(...)):
    result = await process_audio(file)

    return {
        "message": "audio processed",
        "transcription": result["transcription"]
    }