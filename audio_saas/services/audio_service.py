from fastapi import UploadFile
import os
import uuid

from services.transcription_service import transcribe_audio
from services.summary_service import generate_summaries


UPLOAD_DIR = "uploads"


async def process_audio(file: UploadFile):

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_id = f"{uuid.uuid4()}_{file.filename}"
    file_path = os.path.join(UPLOAD_DIR, file_id)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    transcription = transcribe_audio(file_path)

    summaries = generate_summaries(transcription)

    return {
        "file_path": file_path,
        "transcription": transcription,
        "summaries": summaries
    }