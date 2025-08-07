import re

def parse_emotions(script_text):
    pattern = r"\[(.*?)\] \((.*?)\): (.*)"
    dialogues = []

    for line in script_text.split("\n"):
        match = re.match(pattern, line.strip())
        if match:
            character, emotion, text = match.groups()
            dialogues.append({
                "character": character,
                "emotion": emotion,
                "text": text
            })

    return dialogues
