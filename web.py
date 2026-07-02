import streamlit as st

st.set_page_config(page_title="Website Opener")

st.title("🌐 Website Opener")

url = st.text_input(
    "Enter Website URL",
    placeholder="https://www.google.com"
)

if url:
    # Agar user ne http/https nahi likha
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    st.link_button("🚀 Open Website", url)

    st.write("Selected URL:")
    st.code(url)