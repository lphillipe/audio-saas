import whisper
import os

# Carrega o modelo Whisper uma única vez (mais eficiente)
# Opções: "tiny", "base", "small", "medium", "large", "turbo"
# "medium" é recomendado para palestras - melhor precisão com termos religiosos
# Forçamos uso de CPU para evitar erros com CUDA
model = whisper.load_model("medium", device="cpu")


def transcribe_audio(audio_path: str) -> str:
    """
    Transcreve um arquivo de áudio para texto usando Whisper.
    
    Args:
        audio_path: Caminho completo do arquivo de áudio
        
    Returns:
        Texto transcrito em português
    """
    # Define o idioma para português para melhor precisão
    # Adiciona prompt para contexto religioso (ajuda com termos bíblicos)
    result = model.transcribe(
        audio_path, 
        language="pt",
        condition_on_previous_text=True,
        initial_prompt="Esta é uma palestra religiosa. Pode conter termos bíblicos, nomes de livros da Bíblia, e referências religiosas."
    )
    
    return result["text"]
