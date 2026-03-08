import whisper
import os

# Carrega o modelo Whisper uma única vez (mais eficiente)
# Opções: "tiny", "base", "small", "medium", "large"
# "base" é um bom equilíbrio entre velocidade e precisão
model = whisper.load_model("base")


def transcribe_audio(audio_path: str) -> str:
    """
    Transcreve um arquivo de áudio para texto usando Whisper.
    
    Args:
        audio_path: Caminho completo do arquivo de áudio
        
    Returns:
        Texto transcrito em português
    """
    # Define o idioma para português para melhor precisão
    result = model.transcribe(audio_path, language="pt")
    
    return result["text"]
