import openai

openai.api_key = "YOUR_API_KEY"

text = "Paste your paragraph here."

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="Summarize this:\n\n" + text,
    max_tokens=100
)

print(response.choices[0].text.strip())
