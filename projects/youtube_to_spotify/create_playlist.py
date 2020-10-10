import os
import json
import requests
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import youtube_dl
from secrets import spotify_user_id, spotify_token
from exceptions import ResponseException

class CreatePlaylist:

    def __init__(self):
        #self.youtube_client = self.get_youtube_client()
        self.all_song_info = {}


    # Connect to YT
    def get_youtube_client(self):

        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        # api_key = 'AIzaSyA5BrV-fk1A6sjQ_nm1tV2DZ0-o4dltRm8'


        client_secrets_file = "client_secret.json"

        # Get credentials and create an API client
        scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
        # Get credentials and create an API client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)
        credentials = flow.run_console()


        youtube_client = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)

        return youtube_client

    # Get YT videos
    def get_liked_videos(self):
        request = self.youtube_client.videos().list(
            part='snippet,contentDetails,statistics',
            myRating = 'like'
        )
        response = request.execute()

        # get information for each video
        for item in response['items']:
            video_title = item['snippet']['title']
            youtube_url = 'https://youttube.com/watch?v={}'.format(item['id'])

            # use youtub dl to get song and artist name
            video = youtube_dl.YoutubeDL({}).extract_info(youtube_url,download=False)
            song_name = video['track']
            artist = video['artist']

            # save all the info
            if song_name is not None and artist is not None:
                self.all_song_info[video_title] = {
                    "youtube_url": youtube_url,
                    "song_name": song_name,
                    "artist": artist,

                    # add the uri, easy to get song to put into playlist
                    "spotify_uri": self.get_spotify_uri(song_name, artist)

                }


    # Create a spotify playlist
    def create_playlist(self):
        request_body = json.dumps({
            "name": "Success?",
            "description": "New playlist description",
            "public": False
        })
        print(spotify_user_id, spotify_token)
        query = "https://api.spotify.com/v1/users/{}/playlists".format(spotify_user_id)

        response = requests.post(
            query,
            data = request_body,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )

        response_json = response.json()

        print(response_json)
        return


    # Find the song on spotify
    def get_spotify_uri(self, song_name, artist):
        query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
            song_name,
            artist
        )

        response = requests.get(
            query,
            headers={
                "Content-Type":"application/json",
                "Authorization":"Bearer {}".format(spotify_token)
            }

        )

        response_json = response.json()
        songs = response_json["tracks"]["items"]

        # get the first one
        uri = songs[0]["uri"]

        return uri

    # And finally, add song to spotify playlist
    def add_song_to_playlist(self):
        # populate the dictionary
        self.get_liked_videos()

        # collect all uris
        uris = []
        for song, infos in self.all_song_info.items():
            uris.append(info['spotify_uri'])

        # create a new playlist
        playlist_id = self.create_playlist()

        # add all songs into playlist
        request_data = json.dumps(uris)

        query = 'https://api.spotify.com/v1/playlists/{}/tracks'.format(playlist_id)

        response = requests.post(
            query,
            data = request_data,
            headers={
                "Content-Type":"application/json",
                "Authorization":"Bearer {}".format(spotify_token)
            }
        )

        # check for valid response status
        if response.status_code != 200:
            raise ResponseException(response.status_code)

        response_json = response.json()
        return response_json


if __name__ == '__main__':
    cp = CreatePlaylist()
    cp.create_playlist()
    #cp.add_song_to_playlist()
