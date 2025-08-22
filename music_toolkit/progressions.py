# progressions.py
from music_toolkit.chords import build_chord

degree_map = {"I": "major", "ii": "minor", "iii": "minor", "IV": "major",
              "V": "major", "vi": "minor", "vii°": "dim"}

def chord_progression_major(root, degrees=["I","V","vi","IV"]):
    progression = []
    for degree in degrees:
        chord_type = degree_map.get(degree, "major")
        chord = build_chord(root, chord_type)
        progression.append(chord)
    return progression
