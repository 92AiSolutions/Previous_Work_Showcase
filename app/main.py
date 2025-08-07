import streamlit as st
from auth.login import login
from app.controllers.teaser_generator import generate_teaser

def run_app():
    st.set_page_config(page_title="Cinematic Audiobook Generator", layout="centered")

    if not login():
        st.stop()

    st.title("🎬 Cinematic Multi-Voice Audiobook Generator")

    st.info("Upload your formatted script and generate a cinematic MP3 with voices, emotions, and effects.")

    uploaded_file = st.file_uploader("📤 Upload Story Script", type=["txt"])

    if uploaded_file:
        script_text = uploaded_file.read().decode("utf-8")
        st.text_area("📝 Preview Script", value=script_text, height=300)

        if st.button("🎧 Generate Teaser"):
            with st.spinner("Processing..."):
                teaser_path = generate_teaser(script_text)
                st.success("Teaser Generated!")
                st.audio(teaser_path, format="audio/mp3")
                st.download_button("⬇ Download Teaser", teaser_path)
