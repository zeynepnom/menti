# === Terminal Uyarılarını Kapatmak İçin ===
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # TensorFlow uyarılarını gizle

from transformers.utils import logging
logging.set_verbosity_error()  # HuggingFace indirme loglarını kapat

# === Gerekli Kütüphaneler ===
import json
import random
import numpy as np
from collections import defaultdict
from datetime import datetime
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from config import CATEGORY_QUESTIONS, SUGGESTIONS, MODEL_NAME, KEYWORD_MAP

class MotivationResponseSystem:
    def __init__(self):
        self.category_questions = CATEGORY_QUESTIONS
        self.suggestions = SUGGESTIONS
        self.keyword_map = KEYWORD_MAP

        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        self.model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
        self.sentiment_analyzer = pipeline(
            "sentiment-analysis",
            model=self.model,
            tokenizer=self.tokenizer
        )
        self.motivation_level = "medium"
        self.motivation_history = []
        self.used_questions = set()

    def analyze_sentiment(self, text):
        try:
            result = self.sentiment_analyzer(text)[0]
            label = result['label'].lower()
            score = result['score']
            if label == "positive":
                self.motivation_history.append(score)
            else:
                self.motivation_history.append(1 - score)

            if len(self.motivation_history) >= 3:
                avg_score = np.mean(self.motivation_history[-3:])
                if avg_score > 0.7:
                    self.motivation_level = "high"
                elif avg_score > 0.4:
                    self.motivation_level = "medium"
                else:
                    self.motivation_level = "low"
            return label, score
        except Exception as e:
            print(f"Sentiment analysis error: {e}")
            return "neutral", 0.5

    def detect_category_from_text(self, text):
        text_lower = text.lower()
        category_scores = defaultdict(float)
        sentiment, score = self.analyze_sentiment(text)

        for category, keywords in self.keyword_map.items():
            match_count = sum(1 for keyword in keywords if keyword in text_lower)
            if match_count > 0:
                base_score = match_count * 1.0
                if sentiment == "positive":
                    category_scores[category] += base_score * (0.5 + score)
                elif sentiment == "negative":
                    category_scores[category] += base_score * (0.5 - score)
                else:
                    category_scores[category] += base_score
        return category_scores

    def get_next_question(self, detected_categories):
        top_categories = sorted(detected_categories.items(), key=lambda x: x[1], reverse=True)[:2]
        candidate_questions = []

        if top_categories:
            for cat, _ in top_categories:
                if cat in self.category_questions:
                    questions = self.category_questions[cat][self.motivation_level]
                    filtered = [q for q in questions if q not in self.used_questions]
                    candidate_questions.extend(filtered)

        if not candidate_questions:
            fallback_categories = [
                cat for cat in self.category_questions
                if cat not in [c[0] for c in top_categories]
            ]
            for cat in random.sample(fallback_categories, min(2, len(fallback_categories))):
                questions = self.category_questions[cat][self.motivation_level]
                filtered = [q for q in questions if q not in self.used_questions]
                candidate_questions.extend(filtered)

        if not candidate_questions:
            generic_questions = {
                "low": [
                    "Bugün sana iyi gelen küçük bir şey yapmayı denedin mi?",
                    "Şu anda en çok neye ihtiyacın olduğunu düşünüyorsun?"
                ],
                "medium": [
                    "Bugün kendin için ne yapabilirsin?",
                    "Son zamanlarda seni mutlu eden şeyler neler?"
                ],
                "high": [
                    "Bu pozitif enerjini nasıl değerlendireceksin?",
                    "Başkalarına ilham vermek için ne yapıyorsun?"
                ]
            }
            candidate_questions = generic_questions[self.motivation_level]

        selected_question = random.choice(candidate_questions)
        self.used_questions.add(selected_question)
        return selected_question

    def generate_final_recommendations(self, detected_categories):
        recommendations = {}
        top_categories = sorted(detected_categories.items(), key=lambda x: x[1], reverse=True)[:3]
        for category, _ in top_categories:
            if category in self.suggestions:
                level_suggestions = self.suggestions[category][self.motivation_level]
                recs = random.sample(level_suggestions, min(3, len(level_suggestions)))
                recommendations[category] = recs
        if len(recommendations) < 3:
            additional_cats = [
                cat for cat in self.suggestions
                if cat not in recommendations and cat not in [c[0] for c in top_categories]
            ]
            for cat in random.sample(additional_cats, min(2, len(additional_cats))):
                level_suggestions = self.suggestions[cat][self.motivation_level]
                recs = random.sample(level_suggestions, min(2, len(level_suggestions)))
                recommendations[cat] = recs
        return recommendations

def menti_sohbet():
    sohbet_kaydi = {
        "tarih": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "kullanici": "",
        "motivasyon_skoru": 0,
        "motivasyon_seviyesi": "",
        "kategoriler": [],
        "sohbet": [],
        "oneriler": {}
    }

    print("\n" + "="*50)
    print("MENTİ - Akıllı Motivasyon Asistanı".center(50))
    print("="*50 + "\n")

    isim = input("Merhaba! Ben MENTİ, senin kişisel motivasyon asistanın. İsmin nedir?\n> ").strip()
    sohbet_kaydi["kullanici"] = isim

    print(f"\nTanıştığımıza memnun oldum {isim}! Bugün benimle konuşmak istediğin özel bir konu var mı? (İş, okul, ilişkiler, sağlık, kişisel gelişim vb.)")
    response_system = MotivationResponseSystem()
    detected_categories = defaultdict(float)

    initial_response = input(f"{isim}> ").strip()
    initial_categories = response_system.detect_category_from_text(initial_response)
    for cat, score in initial_categories.items():
        detected_categories[cat] += score

    sohbet_kaydi["sohbet"].append({
        "soru": "Konu belirleme sorusu",
        "cevap": initial_response,
        "zaman": datetime.now().strftime("%H:%M:%S")
    })

    for i in range(7):
        current_question = response_system.get_next_question(detected_categories)
        print(f"\nMENTİ: {current_question}")
        user_input = input(f"{isim}> ").strip()

        if user_input.lower() in ["çık", "exit", "quit", "hayır", "teşekkürler"]:
            break

        sentiment, score = response_system.analyze_sentiment(user_input)
        new_categories = response_system.detect_category_from_text(user_input)
        for cat, cat_score in new_categories.items():
            detected_categories[cat] += cat_score

        sohbet_kaydi["sohbet"].append({
            "soru": current_question,
            "cevap": user_input,
            "duygu": sentiment,
            "duygu_skoru": float(score),
            "zaman": datetime.now().strftime("%H:%M:%S")
        })

    avg_motivation = np.mean(response_system.motivation_history) if response_system.motivation_history else 0.5
    motivation_level = "high" if avg_motivation > 0.7 else "low" if avg_motivation <= 0.4 else "medium"
    sohbet_kaydi["motivasyon_skoru"] = float(avg_motivation)
    sohbet_kaydi["motivasyon_seviyesi"] = motivation_level
    sohbet_kaydi["kategoriler"] = list(detected_categories.keys())

    recommendations = response_system.generate_final_recommendations(detected_categories)
    sohbet_kaydi["oneriler"] = recommendations

    try:
        try:
            with open("sohbet_kaydi.json", "r", encoding="utf-8") as f:
                kayitlar = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            kayitlar = []

        kayitlar.append(sohbet_kaydi)

        with open("sohbet_kaydi.json", "w", encoding="utf-8") as f:
            json.dump(kayitlar, f, ensure_ascii=False, indent=4)

        print("\nSohbet kaydınız başarıyla kaydedildi.")
    except Exception as e:
        print(f"\nKayıt sırasında hata oluştu: {e}")

    print("\n" + "="*50)
    print("MENTİ Değerlendirme Sonuçları".center(50))
    print("="*50 + "\n")

    feedback = {
        "low": [
            f"{isim}, bazı zorluklar yaşıyor gibi görünüyorsun (Motivasyon skorun: %{avg_motivation*100:.1f}).",
            "Unutma, zor zamanlar geçicidir. İşte sana özel önerilerim:"
        ],
        "medium": [
            f"{isim}, dengeli bir ruh halindesin (Motivasyon skorun: %{avg_motivation*100:.1f}).",
            "Bu önerilerle kendini daha da iyi hissedebilirsin:"
        ],
        "high": [
            f"{isim}, muhteşem bir enerjin var! (Motivasyon skorun: %{avg_motivation*100:.1f})",
            "Bu pozitifliği sürdürmen için önerilerim:"
        ]
    }

    for line in feedback[motivation_level]:
        print(line)

    print("\n💡 Sana Özel Öneriler 💡\n")
    for category, recs in recommendations.items():
        print(f"🌟 {category.replace('_', ' ').title()} için:")
        for i, rec in enumerate(recs, 1):
            print(f"{i}. {rec}")
        print()

    print("\n" + "="*50)
    print(f"Görüşmek güzeldi {isim}! Motivasyon skorun: %{avg_motivation*100:.1f}")
    print("Kendine iyi bak ve ihtiyacın olduğunda buradayım. 🌟")
    print("="*50 + "\n")

if __name__ == "__main__":
    menti_sohbet()
