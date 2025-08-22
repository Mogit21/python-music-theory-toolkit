# toolkit.py
from music_toolkit.scales import generate_scale
from music_toolkit.intervals import interval_name
from music_toolkit.chords import build_chord
from music_toolkit.progressions import chord_progression_major

# Optional: you can add helper functions that combine modules
def demo():
    print("C major scale:", generate_scale("C", "major"))
    print("A minor chord:", build_chord("A", "minor"))
    print("C chord progression:", chord_progression_major("C"))
