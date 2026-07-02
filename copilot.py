import streamlit as st

st.title("🤖 My Copilot")

prompt = st.chat_input("Ask me anything...")

if prompt:
    st.chat_message("user").write(prompt)

    st.chat_message("assistant").write(
        "Test successful! Your Copilot app is working correctly."
    )