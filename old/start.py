

from googleapiclient.discovery import build
from datetime import datetime
from google_auth_oauthlib.flow import InstalledAppFlow




API_KEY = 'AIzaSyCuwe-XejChol09J02h5rStmbtdcQpob60'
CLIENT_SECRET_FILE = 'client_secret.json'
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]


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




while True:

    # to get input with no empty input and right form
    timeYear = input("input a year :")
    timeMonth = input("input a Month 1/2/..12 :")
    keyWord = input("input a keyword :")
    insertComment = input("input Your Comment: ")
    if timeYear == '' or timeMonth == '' or insertComment == '' or keyWord == '':
        print('some missing data________')
        print()
        print()
        break

    print('right inputs')

    # set the right date
    timeDay = '30'
    if timeMonth == '2':
        timeDay = '28'

    if timeMonth == '1' \
            or timeMonth == '3' or timeMonth == '5' or timeMonth == '7'\
            or timeMonth == '8' or timeMonth == '10' or timeMonth == '12':
        timeDay = '31'


    print('end Time: ' + timeYear + ' / ' + timeMonth+ ' / ' +timeDay )

    youtube = build('youtube', 'v3', developerKey=API_KEY)


    # '%Y-%m-%dT%H:%M:%SZ' form out Eg. 2019-01-01T00:00:00Z
    start_time = datetime(year=int(timeYear), month=int(timeMonth), day=1).strftime('%Y-%m-%dT%H:%M:%SZ')
    end_time = datetime(year=int(timeYear), month=int(timeMonth), day=int(timeDay)).strftime('%Y-%m-%dT%H:%M:%SZ')

    # create http request
    req = youtube.search().list(q=keyWord, part='snippet', type="video", maxResults=3, publishedAfter=start_time, publishedBefore=end_time)
    response = req.execute()



    # start to Authentication with google Account
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
    credentials = flow.run_console()
    youtube = build('youtube', 'v3', credentials=credentials)


    print(len(response['items']))

    #print(response['items'][0])

    successComment = 0
    for item in response['items']:
        try:
            # get the data from item
            channelId = item['snippet']['channelId']
            videoId = item['id']['videoId']
            videoTitle = item['snippet']['title']
            # print the link
            print(videoTitle + ' : https://www.youtube.com/watch?v=' + videoId)
            # like this video
            #youtube.videos().rate(rating='like', id=videoId).execute()
            # insert the comment
            #insert_comment(youtube, channelId, videoId, insertComment)
            successComment = successComment + 1

        except:
            print('exception: ______________________')

    print('success add num' + str(successComment))

    print('last time from : '+ start_time + ' to '+ end_time )
    endWait = input("End od the comment, press any key to tra one more time")









