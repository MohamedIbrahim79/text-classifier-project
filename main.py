from langclassifier import detect_language
from arabictext import classify_arabic
from englishtext import classify_english

# خد input من المستخدم
text = input("Enter text: ")

# تحديد اللغة
lang = detect_language(text)

# اختيار الموديل المناسب
if lang == "arabic":
    result = classify_arabic(text)
elif lang == "english":
    result = classify_english(text)
else:
    result = "Unknown language"

# عرض النتيجة
print("Language:", lang)
print("Prediction:", result)