from fastapi import UploadFile
import os
import uuid

UPLOAD_DIR = "uploads"

async def save_audio(file: UploadFile) -> str:
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_id = f"{uuid.uuid4()}_{file.filename}"
    file_path = os.path.join(UPLOAD_DIR, file_id)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    return file_path