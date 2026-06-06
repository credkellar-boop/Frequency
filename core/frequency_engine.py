import numpy as np
import librosa
from scipy.signal import butter, lfilter

class FrequencyEngine:
    def __init__(self, sample_rate: int = 44100):
        self.sr = sample_rate

    def get_stft(self, y: np.ndarray) -> np.ndarray:
        return np.abs(librosa.stft(y))

    def get_peak_frequencies(self, y: np.ndarray) -> np.ndarray:
        fft_result = np.fft.fft(y)
        frequencies = np.fft.fftfreq(len(y), 1 / self.sr)
        magnitudes = np.abs(fft_result)
        
        positive_freqs = frequencies[:len(frequencies)//2]
        positive_mags = magnitudes[:len(magnitudes)//2]
        
        return positive_freqs[np.argsort(positive_mags)[-10:]]

    def _butter_bandpass(self, lowcut: float, highcut: float, order: int = 5) -> tuple:
        nyquist = 0.5 * self.sr
        low = lowcut / nyquist
        high = highcut / nyquist
        b, a = butter(order, [low, high], btype='band')
        return b, a

    def apply_bandpass_filter(self, y: np.ndarray, lowcut: float, highcut: float, order: int = 5) -> np.ndarray:
        b, a = self._butter_bandpass(lowcut, highcut, order)
        return lfilter(b, a, y)
