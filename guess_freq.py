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

    print()
    print("\n==============================")
    print("WELCOME TO FREQS FOR FREAKS")
    print("Made by Phil Xie")
    print("==============================")
    keep_score = input("Keep Score? (press 'y')")
    keep_score = (keep_score == 'y')
    
    count = 1
    num_rounds = 5
    total_octave_error = 0
    while True:
        print("\n==============================")
        if keep_score:
            print("ROUND ", count)
        freq = random.uniform(50, 500)
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

        # keep score
        if keep_score:
            count += 1
            total_octave_error += abs(octave_diff)
            if count % num_rounds == 0: # game ends
                count = 0
                avg_octave_error = round(total_octave_error / num_rounds, 3)
                print()
                print("SUMMARY: =============================")
                print("Average Octave Error:", avg_octave_error)
                if avg_octave_error > 0.4:
                    print("this is a guessing game after all")
                elif avg_octave_error > 0.15:
                    print("you did well!")
                elif avg_octave_error > 0.05:
                    print("okkk i see you")
                else:
                    print("superior ears!")
                print()
                start_over = input("Start over? (y/n)")
                if start_over != 'y':
                    print("Thanks for playing! \n")
                    exit()




            
