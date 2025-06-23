# preprocess.py
import re

def clean_text(text):
    """Remove special characters, URLs, and lowercase text."""
    if isinstance(text, str):
        text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)
        text = re.sub(r'\W', ' ', text)
        return text.lower().strip()
    return ""
