

from apiclient.discovery import build
#import apiclient.discovery
from google_auth_oauthlib.flow import InstalledAppFlow




CLIENT_SECRET_FILE = 'client_secret.json'
#SCOPES = ['https://www.googleapis.com/auth/youtube']
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
credentials = flow.run_console()
youtube = build('youtube', 'v3', credentials=credentials)

youtube.videos().rate(rating = 'like', id='Nr-gYadj5dw').execute()

def insert_comment(youtube, channel_id, video_id, text):
    insert_result = youtube.commentThreads().insert(
        part="snippet",
        body=dict(
            snippet=dict(
                channelId=channel_id,
                videoId=video_id,
                topLevelComment=dict(
                    snippet=dict(
                        textOriginal=text)
                )
            )
        )
    ).execute()

    comment = insert_result["snippet"]["topLevelComment"]
    author = comment["snippet"]["authorDisplayName"]
    text = comment["snippet"]["textDisplay"]
    print("Inserted comment for %s: %s" % (author, text))

insert_comment(youtube, 'UCkUq-s6z57uJFUFBvZIVTyg', 'Nr-gYadj5dw', "first Comment ....")