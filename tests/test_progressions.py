import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from music_toolkit.progressions import chord_progression_major
from music_toolkit.chords import build_chord

def test_i_v_vi_iv_progression():
    degrees = ['I','V','vi','IV']
    result = chord_progression_major('C', degrees)
    expected = [
        build_chord('C','major'),  # I
        build_chord('G','major'),  # V
        build_chord('A','minor'),  # vi
        build_chord('F','major')   # IV
    ]
    assert result == expected
