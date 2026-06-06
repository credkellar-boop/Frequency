import numpy as np
import pyrubberband as pyrb
import soundfile as sf

class AudioModifier:
    def __init__(self, sample_rate: int = 44100):
        self.sr = sample_rate

    def load_audio(self, file_path: str) -> np.ndarray:
        y, _ = sf.read(file_path)
        return y

    def save_audio(self, y: np.ndarray, output_path: str):
        sf.write(output_path, y, self.sr)

    def change_speed(self, y: np.ndarray, rate: float) -> np.ndarray:
        return pyrb.time_stretch(y, self.sr, rate)

    def change_pitch(self, y: np.ndarray, semitones: float) -> np.ndarray:
        return pyrb.pitch_shift(y, self.sr, semitones)

    def auto_tune_approximation(self, y: np.ndarray) -> np.ndarray:
        return y
