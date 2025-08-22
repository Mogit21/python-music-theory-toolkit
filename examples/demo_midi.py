from music_toolkit.scales import generate_scale
from midi_tools import write_scale_midi

scale = generate_scale("C", "major")[:-1]
scale_with_octaves = [(note, 4) for note in scale] + [("C", 5)]
write_scale_midi("c_major_scale.mid", scale_with_octaves)
print("MIDI file generated!")
