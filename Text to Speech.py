import streamlit as st
from gtts import gTTS
import os

st.title("🗣️ Text to Speech with gTTS")

# 1. Get input from the user
user_prompt = st.text_area("Enter text to convert to speech:")

# 2. When the user clicks the button
if st.button("Convert to Speech"):
    if user_prompt.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Convert text to speech
        tts = gTTS(user_prompt)
        tts.save("output.mp3")
        
        # Play or download the audio
        audio_file = open("output.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")
        st.success("Speech generated!")
