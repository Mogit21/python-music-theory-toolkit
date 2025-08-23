# midi_tools.py
from typing import List, Tuple
from mido import Message, MidiFile, MidiTrack, bpm2tempo

from music_toolkit.scales import generate_scale
from music_toolkit.chords import build_chord
from music_toolkit.progressions import chord_progression_major

# Map note name + octave -> MIDI number (A4=69)
def midi_number(note: str, octave: int = 4) -> int:
    if note not in NOTES:
        raise ValueError(f"Unknown note: {note}")
    semitone_from_C = NOTES.index(note)
    return 12 * (octave + 1) + semitone_from_C  # C-1 = 0

def add_note(track: MidiTrack, note_num: int, velocity: int, ticks: int):
    track.append(Message('note_on', note=note_num, velocity=velocity, time=0))
    track.append(Message('note_off', note=note_num, velocity=0, time=ticks))

def write_scale_midi(filename: str, scale_notes: List[Tuple[str, int]], bpm: int = 90):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    track.append(Message('program_change', program=0, time=0))
    tempo = bpm2tempo(bpm)
    track.append(MetaMessage(time=0))  # placeholder; mido handles tempo via MetaMessage
    from mido import MetaMessage
    track.append(MetaMessage('set_tempo', tempo=tempo))
    # quarter note ticks
    mid.ticks_per_beat = 480
    q = 480
    for (n, o) in scale_notes:
        add_note(track, midi_number(n, o), velocity=80, ticks=q)
    mid.save(filename)

def write_chord_progression_midi(filename: str, key: str, numerals: List[str],
                                 bpm: int = 80, bars_per_chord: int = 1,
                                 octave: int = 4):
    """
    Writes block triads, one chord per bar.
    """
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    from mido import MetaMessage
    track.append(MetaMessage('set_tempo', tempo=bpm2tempo(bpm)))
    mid.ticks_per_beat = 480
    q = 480
    bar = 4 * q

    prog = chord_progression_major(key, numerals)  # list of note names

    # program_change 0 = Acoustic Grand
    track.append(Message('program_change', program=0, time=0))

    for chord in prog:
        # write a block chord (simultaneous notes)
        # start notes
        for i, n in enumerate(chord):
            track.append(Message('note_on', note=midi_number(n, octave), velocity=90, time=0 if i else 0))
        # hold for bar length
        track.append(Message('note_off', note=midi_number(chord[0], octave), velocity=0, time=bar))
        # turn off remaining notes with 0-time (they’ll be already off due to bar hold)
        for n in chord[1:]:
            track.append(Message('note_off', note=midi_number(n, octave), velocity=0, time=0))

    mid.save(filename)
