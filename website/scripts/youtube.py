import os
import pprint

import json
import googleapiclient.discovery
import googleapiclient.errors
import googleapiclient

API_KEY = "AIzaSyB8tF_u2E19Poo147OkY02zNwpNfFdVnYI"
CHANNEL_ID = "UC1aXDYhzYCzOCNxJV6hYdLA"

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=API_KEY)

    request = youtube.search().list(
        part="snippet",
        channelId=CHANNEL_ID,
        maxResults=50
    )
    response = request.execute()
    print(type(response))
    items = response['items']

    response_less = {}
    for item in items:
        pprint.pprint(item)
        id = item['id']
        print(type(id))
        title = item['snippet']['title']
        timestamp = item['snippet']['publishedAt']
        description = item['snippet']['description']
        response_less[timestamp] = {
            'id':id,
            'title':title,
            'description':description
        }

    with open('50videos.json', 'w') as f:
        json.dump(response_less, f, sort_keys=True)



if __name__ == "__main__":
    main()
