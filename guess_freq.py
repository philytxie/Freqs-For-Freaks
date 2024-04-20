"""
FREQUENCY HEARING CHALLENGE
Simple script for training your perfect pitch in terms of frequencies too


Piano range for reference:
- min = A0 = 27.50 Hz
- max = C8 = 4186.01 Hz


Functionality:
- play random note automatically
- type r to repeat
- type to guess frequency
    - calculate octave error (remember freqs are log scale)
- gamify:
    - over 5 trials, computes the average octave error
    - may roast you if you do badly


Phil's current high score over 5 rounds is 0.015 

"""


import numpy as np
import random
import time
import pyaudio

from math import log2

def play_freq(freq):
    p = pyaudio.PyAudio()

    volume = 0.5  # range [0.0, 1.0]
    if freq < 160:
        volume = max(volume + 0.1, 1)
    elif freq < 120:
        volume = max(volume + 0.2, 1)
    elif freq < 80:
        volume = max(volume + 0.3, 1)
    elif freq < 40:
        volume = max(volume + 0.4, 1)

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
    print("WELCOME TO FREQS FOR FREAKS 🎵👂")
    print("Made by Phil Xie 🎹")
    print("==============================")
    print("Friendly Reminder: adjust volume to a comfortable level.")
    keep_score = input("Keep Score? (press 'y')")
    keep_score = (keep_score == 'y')
    if keep_score:
        print("Keeping Score. Game on!")
    else:
        print("You're in experimental mode :)")

    
    count = 0
    num_rounds = 5
    total_octave_error = 0
    while True:
        print("\n==============================")
        if keep_score:
            print("ROUND ", count + 1)

        min_freq, max_freq = 30, 3500 # change frequency range here!
        log2_freq = np.random.uniform(np.log2(min_freq), np.log2(max_freq))
        freq = 2 ** log2_freq
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
                print("Feedback: "),
                if avg_octave_error > 0.415:
                    print("SKILL ISSUE DETECTED")
                    print("Your average error was more than 2 whole tones. Try harder :)")
                elif avg_octave_error > 0.166:
                    print("Your errors averaged between a major third and a perfect fourth. Try harder :)")
                elif avg_octave_error > 0.083:
                    print("you did ok")
                    print("Your errors averaged within a whole tone. That's not bad")
                elif avg_octave_error > 0.041:
                    print("okkk i see you")
                    print("Your errors averaged within a semitone. That's decent!")
                else:
                    print("Superior Ears! Your errors averaged within a quarter tone. That's pretty impressive!")
                print()
                start_over = input("Start over? (y/n)")
                if start_over != 'y':
                    print("Thanks for playing! \n")
                    exit()




            
