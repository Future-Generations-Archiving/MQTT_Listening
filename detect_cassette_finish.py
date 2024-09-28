import sounddevice as sd
import numpy as np
from numpy.typing import ArrayLike
fs = 48000
standard_duration = 2 # seconds
new_recording = sd.rec(int(standard_duration * fs), samplerate=fs, channels=2)

def get_amplitude(recording: ArrayLike) -> ArrayLike:
    amplitudes = np.zeros(recording.size, dtype=float)
    looking_for_max = True
    prev_val = recording[0]
    previous_amplitude_index = 0
    for sample in recording:
        if sample < prev_val and looking_for_max:
            amplitudes[previous_amplitude_index] = sample
            previous_amplitude_index+=1
            looking_for_max = False
        elif sample > prev_val and not looking_for_max:
            amplitudes[previous_amplitude_index]
        prev_val = sample
    amplitudes = np.resize(amplitudes, previous_amplitude_index+1)
    np.absolute(amplitudes, out=amplitudes)
    return amplitudes



while True:
    sd.wait()
    previous_recording = new_recording.copy()
    new_recording = sd.rec(int(standard_duration * fs), samplerate=fs, channels=1)
    amplitudes = get_amplitude(previous_recording)
    mean = np.mean(amplitudes)

