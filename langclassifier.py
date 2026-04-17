import joblib
import re

model = joblib.load("lang_model.pkl")
vectorizer = joblib.load("vectorizer_lang.pkl")

def clean_text(text):
    text = str(text)
    text = text.lower()
    text = re.sub(r'[^\u0600-\u06FFa-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def detect_language(text):
    text = clean_text(text)
    vec = vectorizer.transform([text])
    return model.predict(vec)[0]