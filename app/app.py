


# 🖥️ Streamlit App (`app/app.py`)


import streamlit as st
from toolkit import generate_scale, build_chord, chord_progression_major

st.title("🎶 Python Music Theory Toolkit")

option = st.selectbox(
    "Choose a tool:",
    ["Scale Generator", "Chord Builder", "Chord Progression"]
)

if option == "Scale Generator":
    root = st.selectbox("Select root note:", ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"])
    scale_type = st.selectbox("Select scale type:", ["major", "natural_minor", "harmonic_minor", "melodic_minor"])
    scale = generate_scale(root, scale_type)
    st.write(f"Scale ({scale_type}) starting at {root}:")
    st.write(scale)

elif option == "Chord Builder":
    root = st.selectbox("Select root note:", ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"])
    chord_type = st.selectbox("Select chord type:", ["major","minor","diminished","augmented","dom7","maj7","min7"])
    chord = build_chord(root, chord_type)
    st.write(f"Chord {root} {chord_type}:")
    st.write(chord)

elif option == "Chord Progression":
    key = st.selectbox("Select key:", ["C","D","E","F","G","A","B"])
    progression = st.text_input("Enter Roman numerals (comma separated):", "I,V,vi,IV")
    numerals = [n.strip() for n in progression.split(",")]
    try:
        prog = chord_progression_major(key, numerals)
        st.write(f"Chord progression in {key}:")
        st.write(prog)
    except Exception as e:
        st.error(str(e))
