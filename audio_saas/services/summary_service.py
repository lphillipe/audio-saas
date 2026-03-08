from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Carrega o modelo e tokenizer uma única vez (mais eficiente)
# FLAN-T5 é um modelo que entende instruções em linguagem natural
model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


def _summarize(text: str, max_length: int, instruction: str) -> str:
    """
    Função interna que gera um resumo com tamanho específico.
    
    Args:
        text: Texto original para resumir
        max_length: Tamanho máximo do resumo em tokens
        instruction: Instrução para o modelo (curto, médio, detalhado)
        
    Returns:
        Texto resumido
    """
    # Cria o prompt com instrução
    prompt = f"{instruction} {text[:500]}"  # Limita texto de entrada para não exceder
    
    # Tokeniza
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
    
    # Gera resumo
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=max_length,
            num_beams=4,
            early_stopping=True
        )
    
    # Decodifica
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return summary


def generate_summaries(text: str) -> dict:
    """
    Gera três níveis de resumo para uma transcrição.
    
    Args:
        text: Texto completo da transcrição
        
    Returns:
        Dicionário com três resumos: curto, medio e detalhado
    """
    return {
        "curto": _summarize(
            text,
            max_length=30,
            instruction="Resuma em uma frase curta:"
        ),
        "medio": _summarize(
            text,
            max_length=100,
            instruction="Resuma em um parágrafo destacando os pontos principais:"
        ),
        "detalhado": _summarize(
            text,
            max_length=300,
            instruction="Faça um resumo detalhado com os principais pontos:"
        )
    }
