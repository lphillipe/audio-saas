from transformers import pipeline

# Carrega o modelo de sumarização uma única vez (mais eficiente)
# FLAN-T5 é um modelo que entende instruções em linguagem natural
summarizer = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)


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
    prompt = f"""
    {instruction}
    Transcript:
    {text}
    """
    
    result = summarizer(prompt, max_length=max_length)
    return result[0]["generated_text"]


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
            max_length=50,
            instruction="Resuma em 1-2 frases muito curtas:"
        ),
        "medio": _summarize(
            text,
            max_length=150,
            instruction="Resuma em um parágrafo médio destacando os pontos principais:"
        ),
        "detalhado": _summarize(
            text,
            max_length=400,
            instruction="Faça um resumo detalhado com os principais pontos e contexto:"
        )
    }
