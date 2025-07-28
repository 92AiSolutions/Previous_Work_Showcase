import requests

ELEVEN_API_KEY = "YOUR_API_KEY"
text = "Hello, this is ElevenLabs."

headers = {
    "xi-api-key": ELEVEN_API_KEY,
    "Content-Type": "application/json"
}

response = requests.post(
    "https://api.elevenlabs.io/v1/text-to-speech/voice-id",
    headers=headers,
    json={"text": text}
)

with open("output.mp3", "wb") as f:
    f.write(response.content)
