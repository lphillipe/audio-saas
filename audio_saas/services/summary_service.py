from transformers import pipeline


summarizer = pipeline(
    "summarization",
    model="google/flan-t5-base"
)


def generate_summaries(text: str):

    short_summary = summarizer(
        f"Summarize the following text in 2 sentences: {text}",
        max_length=60,
        min_length=20,
        do_sample=False
    )

    medium_summary = summarizer(
        f"Summarize the following text in one paragraph: {text}",
        max_length=120,
        min_length=40,
        do_sample=False
    )

    detailed_summary = summarizer(
        f"Provide a detailed summary of the following text: {text}",
        max_length=200,
        min_length=80,
        do_sample=False
    )

    return {
        "short_summary": short_summary[0]["summary_text"],
        "medium_summary": medium_summary[0]["summary_text"],
        "detailed_summary": detailed_summary[0]["summary_text"]
    }