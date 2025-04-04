import os
import torch
from transformers import BertTokenizer, BertForSequenceClassification

# Define model directory (ensure the path is correct)
MODEL_DIR = r"D:\fake_news_detectors\backend\fake_news_detector\fake_news_model"

# Load tokenizer and model
try:
    tokenizer = BertTokenizer.from_pretrained(MODEL_DIR)
    model = BertForSequenceClassification.from_pretrained(MODEL_DIR)
    model.eval()  # Set model to evaluation mode
    print("✅ BERT model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading BERT model: {e}")

def predict_news(news_text):
    """Predict whether news text is FAKE or REAL using TinyBERT."""
    try:
        # Tokenize the input news text
        inputs = tokenizer(news_text, truncation=True, padding=True, max_length=512, return_tensors="pt")

        # Perform prediction without gradient calculations (inference mode)
        with torch.no_grad():
            outputs = model(**inputs)

        # Get the predicted class index (0: REAL, 1: FAKE)
        prediction = torch.argmax(outputs.logits, dim=1).item()

        # Return the prediction as a string
        return "FAKE" if prediction == 1 else "REAL"
    except Exception as e:
        print(f"❌ Error in prediction: {e}")
        return "ERROR"
