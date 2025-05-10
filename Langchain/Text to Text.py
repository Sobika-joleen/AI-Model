import streamlit as st
import cohere
import os

# Load your Cohere API key
COHERE_API_KEY = "WWCf2ZaYiofhEN70CSuXExt8AhA3FsjBAnjYRiKa"

# Initialize Cohere
co = cohere.Client(COHERE_API_KEY)

st.set_page_config(page_title="Text-to-Text with Cohere", layout="centered")

st.title("📝 Text-to-Text AI App")
st.write("Enter a prompt below and get a generated response using Cohere's LLM.")

# User input
prompt = st.text_area("Your Prompt", height=200)

if st.button("Generate"):
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating..."):
            response = co.generate(
                model='command',  # 'command' is a strong default model
                prompt=prompt,
                max_tokens=300,
                temperature=0.7
            )
            st.success("Done!")
            st.subheader("Response:")
            st.write(response.generations[0].text.strip())