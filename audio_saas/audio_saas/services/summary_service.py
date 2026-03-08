from transformers import pipeline

summarizer = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

def generate_summaries(text: str):

    prompt = f"""
    Summarize the following meeting transcript:

    {text}
    """

    result = summarizer(prompt, max_length=200)

    return result[0]["generated_text"]