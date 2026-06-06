import whisper
from pathlib import Path

class Transcriber:
    def __init__(self, model_size: str = "base"):
        self.model = whisper.load_model(model_size)

    def process_vocals(self, audio_path: str | Path, translate: bool = False) -> dict:
        task = "translate" if translate else "transcribe"
        
        result = self.model.transcribe(
            str(audio_path),
            task=task,
            fp16=False
        )
        
        return {
            "text": result["text"],
            "language": result.get("language", "unknown"),
            "segments": result.get("segments", [])
        }
