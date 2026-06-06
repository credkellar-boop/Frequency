from pathlib import Path
from .separator import separate_audio
from .transcriber import Transcriber

class QuantumUnit:
    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.uploads_dir = self.data_dir / "uploads"
        self.stems_dir = self.data_dir / "stems"
        self.outputs_dir = self.data_dir / "outputs"
        
        self._ensure_directories()
        self.transcriber = Transcriber(model_size="base")

    def _ensure_directories(self):
        for directory in [self.uploads_dir, self.stems_dir, self.outputs_dir]:
            directory.mkdir(parents=True, exist_ok=True)

    def process_track(self, filename: str, translate: bool = False) -> dict:
        input_path = self.uploads_dir / filename
        
        stem_dir = separate_audio(str(input_path), str(self.stems_dir))
        
        song_name = input_path.stem
        vocals_path = Path(stem_dir) / "htdemucs" / song_name / "vocals.wav"
        
        transcription_data = {}
        if vocals_path.exists():
            transcription_data = self.transcriber.process_vocals(
                str(vocals_path), 
                translate=translate
            )
        
        return {
            "song": song_name,
            "stems_location": str(stem_dir),
            "vocals_data": transcription_data
        }
