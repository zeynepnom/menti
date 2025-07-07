from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import random
import numpy as np
from collections import defaultdict
from config import CATEGORY_QUESTIONS, SUGGESTIONS, CATEGORY_KEYWORDS

# Model yükleme
model_name = "savasy/bert-base-turkish-sentiment-cased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
sentiment_analyzer = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

class MotivationResponseSystem:
    def __init__(self):
        self.category_questions = CATEGORY_QUESTIONS
        self.suggestions = SUGGESTIONS
        self.category_keywords = CATEGORY_KEYWORDS

    # Diğer metodlar aynı şekilde kalacak...
    def analyze_sentiment(self, text):
        try:
            result = sentiment_analyzer(text)[0]
            return result['label'].lower(), result['score']
        except:
            return "neutral", 0.5

    def get_next_question(self, detected_categories, conversation_history):
        # Önceki implementasyon aynı
        pass

    def generate_final_recommendations(self, detected_categories):
        # Önceki implementasyon aynı
        pass

def menti_sohbet():
    # Önceki implementasyon aynı
    pass

if __name__ == "__main__":
    menti_sohbet()