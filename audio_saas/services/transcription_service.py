import whisper


model = whisper.load_model("small")


def transcribe_audio(file_path: str) -> str:
    result = model.transcribe(
        file_path,
        language="pt"
    )

    return result["text"]