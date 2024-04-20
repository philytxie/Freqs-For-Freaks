# Freqs for Freaks

This is a library of fun audio and frequency stuff in the making, starting with the Frequency Hearing Challenge!


## Frequency Hearing Challenge
This simple game can help you map perfect pitch onto the frequency space. You'll be an analog frequency decomposition machine in no time!

To get started:
0. [Clone] (https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this repo if you haven't already
1. run `guess_freq.py` in your Terminal/Command Prompt by `cd`ing into this folder and running
```
python3 guess_freq.py
```

The program will:
- Play a tone, then ask you to guess the frequency
    - type 'r' to repeat the tone
- Show octave error after each round (remember frequencies are on log scale!)
- If you choose to gamify and keep score, the program will show your average (absolute) octave error after 5 rounds, and may roast you if you do badly.


Feel free to change the code to adjust frequency range or number of rounds in the code. Have fun!

It might be helpful to refer to a note name to frequency [conversion chart] (https://muted.io/note-frequencies/) while learning. I'd encourage you to try not to on it when playing the game though!

Phil's current high score (or rather, low score, since we're talking about errors) over 5 rounds is 0.015 :)




A guide to get started:
1. Open up your computer's Terminal (Mac) or Command Prompt (Windows), and `cd` into a folder of your choice
```
cd ~/Desktop/some_folder/
```
1. clone this repository into a folder of your choice your computer by doing:
```
git clone https://github.com/philytxie/Freqs-For-Freaks.git
```
2. Now cd into that folder, then run 
```
python3 guess_freq.py
```
and the program should start. Have fun!