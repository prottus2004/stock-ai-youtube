from agents.news_fetcher import fetch_news
from agents.analyzer import pick_best_news
from agents.script_writer import generate_scripts
from agents.voice import generate_voice
from agents.video import make_video
from agents.thumbnail import make_thumbnail
from agents.uploader import upload_video

def main():
    print("🔎 Fetching news...")
    news = fetch_news()

    print("🧠 Picking best news...")
    best = pick_best_news(news)

    print("✍️ Generating scripts...")
    short_script, long_script, meta = generate_scripts(best)

    print("🎙️ Generating voice...")
    short_audio = generate_voice(short_script, "short.wav")
    long_audio = generate_voice(long_script, "long.wav")

    print("🎬 Making videos...")
    short_video = make_video(short_audio, "short.mp4", vertical=True)
    long_video = make_video(long_audio, "long.mp4", vertical=False)

    print("🖼️ Making thumbnails...")
    short_thumb = make_thumbnail(meta["title"], "short_thumb.png")
    long_thumb = make_thumbnail(meta["title"], "long_thumb.png")

    print("📤 Uploading to YouTube...")
    upload_video(long_video, long_thumb, meta, is_short=False)
    upload_video(short_video, short_thumb, meta, is_short=True)

    print("✅ DONE")

if __name__ == "__main__":
    main()

