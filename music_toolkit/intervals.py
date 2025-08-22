# intervals.py
# Simple interval recognition
interval_names = ["unison","minor 2nd","major 2nd","minor 3rd","major 3rd",
                  "perfect 4th","tritone","perfect 5th","minor 6th","major 6th",
                  "minor 7th","major 7th","octave"]

def interval_name(semitones):
    return interval_names[semitones % 12]
