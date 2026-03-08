from fastapi import UploadFile
import os
import uuid

from audio_saas.services.transcription_service import transcribe_audio
from audio_saas.services.summary_service import generate_summaries


UPLOAD_DIR = "uploads"


async def process_audio(file: UploadFile) -> dict:
    """
    Processa um arquivo de áudio: transcreve e gera resumos.
    
    Args:
        file: Arquivo de áudio enviado
        
    Returns:
        Dicionário com transcrição e resumos
    """
    # Cria pasta de uploads se não existir
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    # Gera nome único para o arquivo
    file_id = f"{uuid.uuid4()}_{file.filename}"
    file_path = os.path.join(UPLOAD_DIR, file_id)

    # Salva o arquivo
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Transcreve o áudio
    transcription = transcribe_audio(file_path)

    # Gera os três resumos
    summaries = generate_summaries(transcription)

    return {
        "file_path": file_path,
        "transcription": transcription,
        "summaries": summaries
    }
