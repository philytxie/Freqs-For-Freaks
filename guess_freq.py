"""
FREQUENCY HEARING CHALLENGE
Simple script for training my perfect pitch in terms of freqs too

Piano range:
- min = A0 = 27.50 Hz
- max = C8 = 4186.01 Hz


Functionality:
- play random note automatically
- type r to repeat
- type guess frequency
    - calculate octave error (remember freqs are log scale)

"""


import numpy as np
import random
import time
import pyaudio

from math import log2

def play_freq(freq):
    p = pyaudio.PyAudio()

    volume = 0.5  # range [0.0, 1.0]
    fs = 44100  # sampling rate (Hz) (must be int)
    duration = 1.3  # seconds

    samples = (np.sin(2 * np.pi * np.arange(fs * duration) * freq / fs)).astype(np.float32)

    output_bytes = (volume * samples).tobytes()

    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    stream.write(output_bytes)

    stream.stop_stream()
    stream.close()

    p.terminate()

if __name__ == "__main__":
    while True:
        print("\n==============================")
        freq = random.uniform(27.5, 4186.01)
        print("Playing new note...")
        play_freq(freq)

        guess = input("Guess frequency (press 'r' to repeat): ")
        while guess == 'r':
            print("Playing again:")
            play_freq(freq)
            guess = input("Guess frequency (press 'r' to repeat): ")
        
        guess = float(guess)
        octave_diff = log2(freq) - log2(guess)

        print("\nActual Frequency:", round(freq, 3))
        print("Octave Error:", round(octave_diff, 3))
