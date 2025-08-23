import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import os
from midi_tools import write_scale_midi  # since midi_tools.py is outside music_toolkit

def test_write_scale_midi_creates_file(tmp_path):
    test_file = tmp_path / "test_scale.mid"
    scale = [('C', 4), ('D', 4), ('E', 4), ('F', 4), ('G', 4)]
    write_scale_midi(str(test_file), scale)
    assert test_file.exists()

