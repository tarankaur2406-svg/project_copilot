import streamlit as st
from streamlit_mic_recorder import mic_recorder

st.title("🎤 Voice Input App")

audio = mic_recorder(
    start_prompt="🎙️ Start Recording",
    stop_prompt="⏹️ Stop Recording",
    key="mic"
)

if audio:
    st.success("Recording done!")

    st.audio(audio["bytes"])