
# https://developers.google.com/youtube/v3/docs/search/list

from googleapiclient.discovery import build
from datetime import datetime

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

api_key = 'AIzaSyCuwe-XejChol09J02h5rStmbtdcQpob60'

youtube = build('youtube', 'v3', developerKey=api_key)

# '%Y-%m-%dT%H:%M:%SZ' form out Eg. 2019-01-01T00:00:00Z
start_time = datetime(year=2019, month=1, day=1).strftime('%Y-%m-%dT%H:%M:%SZ')
end_time = datetime(year=2019, month=9, day=1).strftime('%Y-%m-%dT%H:%M:%SZ')

# create http request
req = youtube.search().list(q='Halloween', part='snippet', type="video", maxResults=49,publishedAfter=start_time, publishedBefore=end_time)

response = req.execute()
print(len(response))

print (response['items'][0])
#for item in response['items']:
    #print(item['snippet']['title'])
    #print('https://www.youtube.com/watch?v=' + item['id']['videoId'])


