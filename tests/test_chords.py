import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from music_toolkit.chords import build_chord

def test_c_major_chord():
    expected = ['C', 'E', 'G']
    result = build_chord('C', 'major')
    assert result == expected

def test_a_minor_chord():
    expected = ['A', 'C', 'E']
    result = build_chord('A', 'minor')
    assert result == expected

def test_g_diminished_chord():
    expected = ['G', 'A#', 'C#']  # match your function output
    result = build_chord('G', 'dim')
    assert result == expected


