import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = """
This is paragraph
"""
text = text.lower()

words = text.split()
stop_words = set(stopwords.words("english"))
filtered_words = [word for word in words if word.lower() not in stop_words]
cleaned_text = " ".join(filtered_words)

print("Original Text:", text)
print("---" * 20)
print("Text after Stop Word Removal:", cleaned_text)