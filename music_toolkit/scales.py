# scales.py
notes_sharp = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
notes_flat  = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']

major_intervals = [2,2,1,2,2,2,1]  # whole, whole, half...
minor_intervals = [2,1,2,2,1,2,2]

def generate_scale(root, scale_type="major"):
    scale = []
    notes = notes_sharp  # for simplicity, use sharps
    start_idx = notes.index(root)
    intervals = major_intervals if scale_type=="major" else minor_intervals
    idx = start_idx
    scale.append(notes[idx])
    for step in intervals:
        idx = (idx + step) % 12
        scale.append(notes[idx])
    return scale
