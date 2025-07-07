# -*- coding: utf-8 -*-
"""
TÜRKÇE SENTIMENT ANALİZ - BERT MODELİYLE
"""

# 1. GEREKLİ KÜTÜPHANELER
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import re
import nltk
from nltk.corpus import stopwords
from transformers import BertTokenizer, TFBertForSequenceClassification
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import os
import logging
import warnings

# 2. AYARLAR
warnings.filterwarnings('ignore')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 3. METİN ÖN İŞLEME
class TurkishTextPreprocessor:
    def __init__(self):
        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('stopwords')
        self.stop_words = set(stopwords.words('turkish'))
        self.emoji_map = {
            ':)': 'mutlu', ':(': 'uzgun', '<3': 'sevgi',
            ':-)': 'mutlu', ':-(': 'uzgun', ';)': 'saka',
            ':D': 'mutlu', 'xD': 'mutlu', ':/': 'supheli'
        }

    def preprocess(self, text):
        if not isinstance(text, str):
            return ""
        for emoji, replacement in self.emoji_map.items():
            text = text.replace(emoji, f' {replacement} ')
        text = text.lower()
        text = re.sub(r'[^\w\s]', ' ', text)
        text = re.sub(r'\d+', '', text)
        text = ' '.join([
            word for word in text.split() 
            if word not in self.stop_words and len(word) > 2
        ])
        text = re.sub(r'\s+', ' ', text).strip()
        return text

# 4. VERİYİ YÜKLE VE TEMİZLE
logger.info("📁 Veri yükleniyor...")
df = pd.read_csv("data.csv", encoding="latin1")
df.rename(columns={"comment": "text", "Label": "label"}, inplace=True)

preprocessor = TurkishTextPreprocessor()
df['text'] = df['text'].apply(preprocessor.preprocess)

# 5. EĞİTİM VE TEST BÖLÜNMESİ
train_texts, test_texts, train_labels, test_labels = train_test_split(
    df['text'].tolist(), df['label'].tolist(), test_size=0.2, random_state=42)

# 6. TOKENIZER ve ENCODING
logger.info("🔤 Tokenizer yükleniyor...")
tokenizer = BertTokenizer.from_pretrained("dbmdz/bert-base-turkish-uncased")

train_encodings = tokenizer(train_texts, truncation=True, padding=True, max_length=128, return_tensors="tf")
test_encodings = tokenizer(test_texts, truncation=True, padding=True, max_length=128, return_tensors="tf")

train_dataset = tf.data.Dataset.from_tensor_slices((dict(train_encodings), train_labels)).batch(16)
test_dataset = tf.data.Dataset.from_tensor_slices((dict(test_encodings), test_labels)).batch(16)

# 7. MODEL OLUŞTURMA
logger.info("🔧 Model oluşturuluyor...")
model = TFBertForSequenceClassification.from_pretrained("dbmdz/bert-base-turkish-uncased", num_labels=2)

optimizer = tf.keras.optimizers.Adam(learning_rate=2e-5)
model.compile(optimizer=optimizer, loss=model.compute_loss, metrics=["accuracy"])

# 8. CALLBACKS
callbacks = [
    EarlyStopping(monitor="val_loss", patience=2, restore_best_weights=True),
    ModelCheckpoint("model_best.h5", save_best_only=True, save_weights_only=True)
]

# 9. EĞİTİM
logger.info("🚀 Model eğitiliyor...")
history = model.fit(
    train_dataset,
    validation_data=test_dataset,
    epochs=4,
    callbacks=callbacks
)

# 10. DEĞERLENDİRME
logger.info("📊 Model test ediliyor...")
preds = model.predict(test_dataset).logits
y_pred = np.argmax(preds, axis=1)

print("\nClassification Report:")
print(classification_report(test_labels, y_pred))

print("\nConfusion Matrix:")
conf_matrix = confusion_matrix(test_labels, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()
