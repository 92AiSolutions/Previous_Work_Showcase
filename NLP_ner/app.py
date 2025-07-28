import spacy

nlp = spacy.load("en_core_web_sm")
text = "Barack Obama was the president of the United States."

doc = nlp(text)
for ent in doc.ents:
    print(ent.text, ent.label_)
