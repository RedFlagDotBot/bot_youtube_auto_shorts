import requests
import json
import os
import yt_dlp
import ffmpeg
import google.auth
import google.auth.transport.requests
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# Configuration
TWITCH_CLIENT_ID = "_À remplacer_"
TWITCH_OAUTH_TOKEN = "À remplacer_"
TWITCH_CHANNELS_FILE = "twitch_channels.txt"  # Fichier contenant les noms des chaînes Twitch
OUTPUT_DIR = "./clips" #Le dossier est créé automtiquement
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
TOKEN_FILE = "token.json"

# Création du dossier de sortie
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Fonction pour récupérer l'ID de la chaîne Twitch
def get_twitch_user_id(channel_name):
    url = f"https://api.twitch.tv/helix/users?login={channel_name}"
    headers = {
        "Client-ID": TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {TWITCH_OAUTH_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data["data"][0]["id"] if "data" in data and len(data["data"]) > 0 else None

# Fonction pour récupérer les clips Twitch
def get_twitch_clips(user_id):
    url = f"https://api.twitch.tv/helix/clips?broadcaster_id={user_id}&first=5"
    headers = {
        "Client-ID": TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {TWITCH_OAUTH_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    clips = response.json().get("data", [])
    return clips

# Fonction pour télécharger les clips
def download_clip(clip_url, output_path):
    ydl_opts = {
        'outtmpl': output_path,
        'format': 'bestvideo+bestaudio/best'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([clip_url])

# Fonction pour convertir en format Shorts (9:16) avec meilleure qualité
def convert_to_shorts(input_path, output_path):
    (
        ffmpeg
        .input(input_path)
        .filter('scale', 1080, 1920)
        .output(output_path, format='mp4', vcodec='libx264', crf=23, preset='slow')
        .run()
    )

# Fonction pour gérer l'authentification Google et éviter la ré-authentification
def get_authenticated_service():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = google.auth.load_credentials_from_file(TOKEN_FILE)[0]
    if not creds or not creds.valid:
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            "client_secret.json", SCOPES
        )
        creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())
    return googleapiclient.discovery.build("youtube", "v3", credentials=creds)

# Fonction pour uploader sur YouTube
def upload_to_youtube(video_path, title, description, tags):
    youtube = get_authenticated_service()
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "tags": tags,
                "categoryId": "20"
            },
            "status": {
                "privacyStatus": "public"
            }
        },
        media_body=googleapiclient.http.MediaFileUpload(video_path, chunksize=-1, resumable=True)
    )
    response = request.execute()
    print(f"Vidéo uploadée : {response['id']}")

# Récupération et traitement des clips
def main():
    if not os.path.exists(TWITCH_CHANNELS_FILE):
        print(f"Erreur : Le fichier {TWITCH_CHANNELS_FILE} n'existe pas.")
        return
    
    with open(TWITCH_CHANNELS_FILE, "r") as file:
        channels = [line.strip() for line in file.readlines()]
    
    for channel in channels:
        print(f"Traitement de la chaîne : {channel}")
        user_id = get_twitch_user_id(channel)
        if not user_id:
            print(f"Erreur : Impossible de récupérer l'ID de la chaîne Twitch {channel}.")
            continue
        
        clips = get_twitch_clips(user_id)
        for clip in clips:
            clip_url = clip['url']
            clip_title = clip['id']
            output_path = os.path.join(OUTPUT_DIR, f"{clip_title}.mp4")
            short_output_path = os.path.join(OUTPUT_DIR, f"{clip_title}_short.mp4")
            
            print(f"Téléchargement de : {clip_url}")
            download_clip(clip_url, output_path)
            
            print(f"Conversion en format Shorts...")
            convert_to_shorts(output_path, short_output_path)
            
            print(f"Upload sur YouTube...")
            upload_to_youtube(short_output_path, f"Clip Twitch : {clip_title}", "Clip Twitch converti en Shorts.", ["Twitch", "Shorts", "Gaming"])
            
            print(f"Clip prêt : {short_output_path}")

if __name__ == "__main__":
    main()
