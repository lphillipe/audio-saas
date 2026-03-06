from fastapi import APIRouter

router = APIRouter(
    prefix="/audio",
    tags=["audio"]
)

@router.get("/")
async def audio_status():
    return {"message": "audio router working"}