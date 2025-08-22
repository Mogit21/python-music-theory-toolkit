# chords.py
from music_toolkit.scales import notes_sharp

chord_intervals = {
    "major": [0, 4, 7],
    "minor": [0, 3, 7],
    "dim": [0, 3, 6],
    "aug": [0, 4, 8]
}

def build_chord(root, chord_type="major"):
    idx = notes_sharp.index(root)
    intervals = chord_intervals.get(chord_type, [0,4,7])
    chord = [notes_sharp[(idx+i)%12] for i in intervals]
    return chord
