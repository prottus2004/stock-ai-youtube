import subprocess

def generate_voice(text, out):
    with open("temp.txt", "w", encoding="utf-8") as f:
        f.write(text)

    subprocess.run([
        "edge-tts",
        "--voice", "en-US-GuyNeural",
        "--text", text,
        "--write-media", out
    ], check=True)

    return out

