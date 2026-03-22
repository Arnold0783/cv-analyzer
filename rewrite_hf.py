import os
import requests

# ✅ Use HuggingFace Inference API instead of local model
HF_TOKEN = os.environ.get("HF_TOKEN")  # 👈 replace with your HuggingFace token
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-small"

def rewrite_cv_hf(cv_text):
    """
    Rewrite CV text professionally using HuggingFace API.
    Lightweight — works on Render free tier.
    """
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {"inputs": f"Rewrite this CV professionally:\n{cv_text[:300]}"}

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=15)
        response.raise_for_status()
        result = response.json()
        return result[0]["generated_text"]
    except Exception as e:
        print("AI rewrite error:", e)
        return "AI rewrite temporarily unavailable."