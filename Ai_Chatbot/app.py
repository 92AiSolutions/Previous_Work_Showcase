import streamlit as st
import openai

openai.api_key = "YOUR_API_KEY"

st.title("AI Chatbot")

query = st.text_input("You:", "")

if query:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": query}]
    )
    st.write("Bot:", response['choices'][0]['message']['content'])
