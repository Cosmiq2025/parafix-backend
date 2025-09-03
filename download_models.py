import spacy
try:
    spacy.cli.download("en_core_web_sm")
except Exception as e:
    print(f"EN model download failed: {e}")

try:
    spacy.cli.download("ru_core_news_sm")
except Exception as e:
    print(f"RU model download failed: {e}")
