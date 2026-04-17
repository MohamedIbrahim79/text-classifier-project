import joblib

# تحميل الموديل
arabic_model = joblib.load("arabic_model.pkl")
vectorizer_ar = joblib.load("vectorizer_ar.pkl")

def classify_arabic(text):
    vec = vectorizer_ar.transform([text])
    return arabic_model.predict(vec)[0]