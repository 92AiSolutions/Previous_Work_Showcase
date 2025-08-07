def extract_dialogues(script):
    lines = script.split("\n")
    return [line for line in lines if line.strip()]
