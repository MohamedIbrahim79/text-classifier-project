import joblib

english_model = joblib.load("english_model.pkl")
vectorizer_en = joblib.load("vectorizer_en.pkl")

def classify_english(text):
    vec = vectorizer_en.transform([text])
    return english_model.predict(vec)[0]