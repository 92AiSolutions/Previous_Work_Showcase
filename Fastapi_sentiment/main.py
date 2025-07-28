from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob

app = FastAPI()

class InputText(BaseModel):
    text: str

@app.post("/sentiment")
def analyze_sentiment(data: InputText):
    analysis = TextBlob(data.text)
    return {"polarity": analysis.polarity}
