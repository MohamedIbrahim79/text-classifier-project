from langclassifier import detect_language
from arabictext import classify_arabic
from englishtext import classify_english

# Get input from user
text = input("Enter text: ")

# Detect language
lang = detect_language(text)

# Choose the appropriate model
if lang == "arabic":
    result = classify_arabic(text)
elif lang == "english":
    result = classify_english(text)
else:
    result = "Unknown language"

# Print results
print("Language:", lang)
print("Prediction:", result)
