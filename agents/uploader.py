import os
import json
import tempfile
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def upload_video(video, thumb, meta, is_short=False):
    secret = json.loads(os.getenv("YT_CLIENT_SECRET"))

    flow = InstalledAppFlow.from_client_config(secret, SCOPES)
    creds = flow.run_console()

    youtube = build("youtube", "v3", credentials=creds)

    body = {
        "snippet": {
            "title": meta["title"],
            "description": meta["description"],
            "tags": ["stock market","finance","investing","trading"],
            "categoryId": "25"
        },
        "status": {
            "privacyStatus": "public"
        }
    }

    if is_short:
        body["snippet"]["title"] = "SHORT: " + body["snippet"]["title"]

    req = youtube.videos().insert(
        part="snippet,status",
        body=body,
        media_body=MediaFileUpload(video)
    )

    res = req.execute()
    print("Uploaded:", res["id"])

