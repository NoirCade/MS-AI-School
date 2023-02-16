import pyaudio
import numpy as np


def sound():
    # Parameters for the sine wave
    frequency = 150000  # Hz
    duration = 5  # seconds
    sample_rate = 144000  # samples per second
    volume = 1  # range [0.0, 1.0]

    # Generate the sine wave
    num_samples = int(sample_rate * duration)
    samples = (np.sin(2 * np.pi * frequency * np.arange(num_samples) / sample_rate) * volume).astype(np.float32)

    # Play the sine wave
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=sample_rate, output=True)
    stream.write(samples)
    stream.close()
    p.terminate()
