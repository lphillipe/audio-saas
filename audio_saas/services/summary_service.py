import re
from collections import Counter


def _split_sentences(text: str) -> list:
    """
    Divide o texto em sentenças.
    """
    # Divide por pontuação final
    sentences = re.split(r'[.!?]+', text)
    # Remove sentenças vazias ou muito curtas
    return [s.strip() for s in sentences if len(s.strip()) > 20]


def _score_sentence(sentence: str, word_freq: Counter) -> float:
    """
    Calcula score de uma sentença baseado na frequência das palavras.
    """
    words = sentence.lower().split()
    if not words:
        return 0
    
    score = sum(word_freq.get(word, 0) for word in words)
    return score / len(words)


def _summarize_extractive(text: str, num_sentences: int) -> str:
    """
    Gera resumo extrativo selecionando as frases mais importantes.
    
    Args:
        text: Texto original
        num_sentences: Número de frases para incluir no resumo
        
    Returns:
        Texto resumido
    """
    sentences = _split_sentences(text)
    
    # Se tiver poucas frases, retorna o texto original
    if len(sentences) <= num_sentences:
        return ". ".join(sentences) + "." if sentences else text
    
    # Calcula frequência de palavras (exceto stop words)
    stop_words = {
        'de', 'do', 'da', 'dos', 'das', 'um', 'uma', 'uns', 'umas',
        'o', 'a', 'os', 'as', 'e', 'ou', 'mas', 'que', 'se', 'na', 
        'no', 'em', 'para', 'com', 'por', 'ao', 'à', 'é', 'são',
        'foi', 'foram', 'ser', 'estar', 'ter', 'haver', 'como',
        'mais', 'menos', 'muito', 'pouco', 'todo', 'toda', 'todos',
        'todas', 'este', 'esta', 'esse', 'essa', 'isto', 'aquilo',
        'ele', 'ela', 'eles', 'elas', 'meu', 'minha', 'seu', 'sua',
        'nosso', 'nossa', 'qual', 'quais', 'quem', 'onde', 'quando',
        'porque', 'porquê', 'também', 'só', 'apenas', 'até', 'já',
        'bem', 'cada', 'tal', 'tais', 'mesmo', 'próprio', 'outro',
        'outros', 'outras', 'algum', 'alguns', 'alguma', 'algumas',
        'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x'
    }
    
    all_words = []
    for sentence in sentences:
        words = sentence.lower().split()
        all_words.extend([w for w in words if w not in stop_words and len(w) > 2])
    
    word_freq = Counter(all_words)
    
    # Score de cada sentença
    scored = []
    for i, sentence in enumerate(sentences):
        score = _score_sentence(sentence, word_freq)
        # Dá prioridade para as primeiras frases
        if i < 3:
            score *= 1.2
        scored.append((i, sentence, score))
    
    # Pega as melhores sentenças
    scored.sort(key=lambda x: x[2], reverse=True)
    top_sentences = scored[:num_sentences]
    
    # Ordena pela posição original no texto
    top_sentences.sort(key=lambda x: x[0])
    
    # Junta as sentenças
    summary = ". ".join([s[1] for s in top_sentences]) + "."
    
    return summary


def generate_summaries(text: str) -> dict:
    """
    Gera três níveis de resumo para uma transcrição usando método extrativo.
    
    Args:
        text: Texto completo da transcrição
        
    Returns:
        Dicionário com três resumos: curto, medio e detalhado
    """
    return {
        "curto": _summarize_extractive(text, num_sentences=2),
        "medio": _summarize_extractive(text, num_sentences=5),
        "detalhado": _summarize_extractive(text, num_sentences=10)
    }
