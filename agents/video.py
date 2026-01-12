import subprocess

def make_video(audio, out, vertical=False):
    if vertical:
        size = "1080x1920"
    else:
        size = "1920x1080"

    cmd = [
        "ffmpeg", "-y",
        "-f", "lavfi",
        "-i", f"color=c=black:s={size}",
        "-i", audio,
        "-shortest",
        "-c:v", "libx264",
        "-c:a", "aac",
        out
    ]

    subprocess.run(cmd, check=True)
    return out

