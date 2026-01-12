import os
import requests

HF_API = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
HEADERS = {"Authorization": f"Bearer {os.getenv('HF_API_KEY')}"}

def ask(prompt):
    r = requests.post(HF_API, headers=HEADERS, json={"inputs": prompt}, timeout=120)
    return r.json()[0]["generated_text"]

def generate_scripts(news):
    base = f"""
News:
{news['title']}
{news['summary']}
"""

    long_script = ask(base + "\nExplain this in 5-6 minutes for beginners. Simple language.")
    short_script = ask(base + "\nExplain this in 30 seconds for YouTube Shorts.")

    title = ask(base + "\nGenerate a powerful YouTube title.")
    desc = ask(base + "\nGenerate YouTube description with hashtags.")

    return short_script, long_script, {
        "title": title.strip(),
        "description": desc.strip()
    }

