from flask import Flask, request, jsonify
from flask_cors import CORS
from motivation_chatbot import MotivationResponseSystem
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Frontend'den gelen isteklere izin ver

# Sistem örneği oluştur
system = MotivationResponseSystem()

@app.route('/api/start', methods=['POST'])
def start_conversation():
    data = request.json
    name = data.get('name')
    initial_message = data.get('message')
    
    # Kategorileri ve motivasyonu analiz et
    initial_categories = system.detect_category_from_text(initial_message)
    
    # İlk soruyu al
    first_question = system.get_next_question(initial_categories, [])
    
    return jsonify({
        'success': True,
        'question': first_question,
        'categories': initial_categories
    })

@app.route('/api/chat', methods=['POST'])
def continue_chat():
    data = request.json
    user_message = data.get('message')
    
    # Duygu analizi yap
    sentiment, score = system.analyze_sentiment(user_message)
    categories = system.detect_category_from_text(user_message)
    next_question = system.get_next_question(categories, [])
    
    return jsonify({
        'success': True,
        'question': next_question,
        'sentiment': sentiment,
        'score': score,
        'categories': categories
    })

@app.route('/api/finish', methods=['POST'])
def finish_chat():
    data = request.json
    categories = data.get('categories', {})
    
    # Önerileri oluştur
    recommendations = system.generate_final_recommendations(categories)
    motivation_level = system.motivation_level
    
    return jsonify({
        'success': True,
        'recommendations': recommendations,
        'motivation_level': motivation_level
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # 5000 portunda çalışacak