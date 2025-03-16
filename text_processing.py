import re
import spacy

nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'[^\w\s]', '', text)  # Remove special characters
    return text.lower().strip()

def preprocess_text(text):
    doc = nlp(clean_text(text))
    tokens = [token.lemma_ for token in doc if not token.is_stop]
    return " ".join(tokens)
