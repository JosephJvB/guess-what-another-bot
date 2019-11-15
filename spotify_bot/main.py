import os
import base64
from spotipy import Spotify, util
import requests

class Spotify_Bot(object):
    def __init__(self):
        self.get_playlist()
        return

    def get_cc_token(self): # no scopes, basic auth
        s = f'{os.getenv("SPOTIFY_ID")}:{os.getenv("SPOTIFY_SECRET")}'
        a = str(base64.b64encode(s.encode('utf-8')), 'utf-8')
        u = 'https://accounts.spotify.com/api/token'
        h = {
            'Authorization': f'Basic {a}'
        }
        d = { 'grant_type': 'client_credentials' }
        res = requests.post(u, data=d, headers=h)
        return res.json()['access_token']

    def get_playlist(self):
        playlist_id = os.getenv('SPOTIFY_PLAYLIST')
        u = f'https://api.spotify.com/v1/playlists/{playlist_id}'
        token = self.get_cc_token()
        h = { 'Authorization': f'Bearer {token}' }
        res = requests.get(u, headers=h)
        print(res)
        print(res.json())
        return


if __name__ == '__main__':
    Spotify_Bot()