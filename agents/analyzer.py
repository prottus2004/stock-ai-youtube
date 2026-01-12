import os
import requests

HF_API = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
HEADERS = {"Authorization": f"Bearer {os.getenv('HF_API_KEY')}"}

def pick_best_news(news):
    text = "\n".join([n["title"] for n in news])

    prompt = f"""
Pick the SINGLE most important stock market news that can move the market today:

{text}

Reply only with the exact headline.
"""

    r = requests.post(HF_API, headers=HEADERS, json={"inputs": prompt}, timeout=60)
    best_title = r.json()[0]["generated_text"].strip()

    for n in news:
        if best_title.lower() in n["title"].lower():
            return n

    return news[0]

