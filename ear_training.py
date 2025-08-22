# ear_training.py
import random
import time
from typing import Tuple, List

import numpy as np
import pygame

from toolkit import NOTES, INTERVALS, build_chord

SAMPLE_RATE = 44100

def note_to_freq(note: str, octave: int = 4) -> float:
    """
    A4 = 440 Hz; NOTES index gives semitone offset relative to C.
    We'll compute MIDI number and convert to frequency.
    """
    if note not in NOTES:
        raise ValueError(f"Unknown note: {note}")
    # MIDI numbers: A4 = 69, C4 = 60
    semitone_from_C = NOTES.index(note)
    midi = 12 * (octave + 1) + semitone_from_C  # C-1 = 0
    # A4 (440Hz) => midi 69
    return 440.0 * (2 ** ((midi - 69) / 12))

def sine_tone(freq: float, duration: float = 0.8, volume: float = 0.5) -> np.ndarray:
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    wave = np.sin(2 * np.pi * freq * t)
    wave = (wave * (32767 * volume)).astype(np.int16)
    return np.stack([wave, wave], axis=-1)  # stereo

def play_array(arr: np.ndarray):
    sound = pygame.sndarray.make_sound(arr)
    sound.play()
    # block until finished
    pygame.time.delay(int(1000 * len(arr) / SAMPLE_RATE))

def play_notes(notes: List[Tuple[str, int]], duration=0.8, gap=0.1):
    for n, octv in notes:
        freq = note_to_freq(n, octv)
        play_array(sine_tone(freq, duration))
        pygame.time.delay(int(gap * 1000))

def play_chord(notes: List[Tuple[str, int]], duration=1.2):
    waves = []
    for n, octv in notes:
        waves.append(sine_tone(note_to_freq(n, octv), duration))
    mix = np.sum(waves, axis=0)
    # prevent clipping
    mix = np.clip(mix, -32767, 32767).astype(np.int16)
    play_array(mix)

def init_audio():
    pygame.mixer.pre_init(SAMPLE_RATE, size=-16, channels=2)
    pygame.init()

def quiz_intervals(rounds: int = 5):
    """
    Plays two sequential notes (root then target).
    User types the interval name (e.g., 'Perfect 5th' or 'Major 3rd').
    """
    print("🎧 Interval Quiz — type the interval name (e.g., 'Perfect 5th').")
    score = 0
    for i in range(1, rounds + 1):
        root = random.choice(NOTES)
        target = random.choice(NOTES)
        # normalize to a pleasant octave range
        octv = random.choice([3, 4, 5])

        print(f"\nRound {i}: listen...")
        play_notes([(root, octv), (target, octv)], duration=0.7, gap=0.15)
        # figure out correct name
        i_name = INTERVALS[((NOTES.index(target) - NOTES.index(root)) % 12)]

        ans = input("Your answer: ").strip()
        if ans.lower() == i_name.lower():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ It was: {i_name}")
    print(f"\nYour score: {score}/{rounds}")

def quiz_chords(rounds: int = 5):
    """
    Plays a triad and asks the user to guess quality: major/minor/diminished/augmented
    """
    print("🎹 Chord Quality Quiz — answer with: major/minor/diminished/augmented")
    qualities = ["major", "minor", "diminished", "augmented"]
    score = 0
    for i in range(1, rounds + 1):
        root = random.choice(NOTES)
        quality = random.choice(qualities)
        octv = random.choice([3, 4])
        chord_notes = build_chord(root, quality)
        to_play = [(n, octv) for n in chord_notes]

        print(f"\nRound {i}: listen...")
        play_chord(to_play, duration=1.0)

        ans = input("Your answer: ").strip().lower()
        if ans == quality:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ It was: {quality} ({root} {quality})")
    print(f"\nYour score: {score}/{rounds}")

if __name__ == "__main__":
    init_audio()
    print("Ear Training\n1) Intervals  2) Chords")
    choice = input("Choose 1 or 2: ").strip()
    if choice == "1":
        quiz_intervals()
    else:
        quiz_chords()
    time.sleep(0.2)
    pygame.quit()
