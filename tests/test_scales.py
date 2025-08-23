import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from music_toolkit.scales import generate_scale

def test_c_major_scale():
    expected = ['C','D','E','F','G','A','B','C']
    result = generate_scale('C', 'major')
    assert result == expected

def test_a_minor_scale():
    expected = ['A','B','C','D','E','F','G','A']
    result = generate_scale('A', 'minor')
    assert result == expected
