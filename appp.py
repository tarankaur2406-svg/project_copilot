import streamlit as st
from streamlit_mic_recorder import speech_to_text
from assistant.brain import get_response
from myutils.voice import speak, stop_speaking

st.set_page_config("AI Copilot", "🤖", layout="centered")

st.title("🤖 Voice AI Copilot")

if "chat" not in st.session_state:
    st.session_state.chat = []

# ⏹ STOP BUTTON (IMPORTANT)
if st.button("⏹ Stop Voice"):
    stop_speaking()
    st.success("Voice stopped")

# chat history
for msg in st.session_state.chat:
    with st.chat_message(msg["role"]):
        st.write(msg["text"])

# mic input
voice_text = speech_to_text(language="en", just_once=True, key="mic")

user_input = st.text_input("Ask something...", value=voice_text or "")

# SEND
if st.button("Send 🚀"):

    if user_input.strip():

        stop_speaking()  # ⛔ instant stop old voice

        st.session_state.chat.append({"role": "user", "text": user_input})

        with st.chat_message("user"):
            st.write(user_input)

        with st.spinner("Thinking..."):
            response = get_response(user_input)

        st.session_state.chat.append({"role": "assistant", "text": response})

        with st.chat_message("assistant"):
            st.write(response)

        # 🔊 VOICE OUTPUT (IMPORTANT FIX)
        audio_file = speak(response)

        audio_bytes = open(audio_file, "rb").read()

        st.audio(audio_bytes, format="audio/mp3", autoplay=True)