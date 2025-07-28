import streamlit as st
import openai

openai.api_key = "YOUR_API_KEY"

st.title("AI Story Generator")

prompt = st.text_area("Enter your story prompt")

if prompt:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    st.write(response.choices[0].text.strip())
