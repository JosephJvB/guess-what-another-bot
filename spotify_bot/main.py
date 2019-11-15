import os
import base64
from spotipy import Spotify, util
import requests

class Spotify_Bot(object):
    def __init__(self):
        t = self.req1()
        self.req2(t)

    def req1(self):
        s = f'{os.getenv("SPOTIFY_ID")}:{os.getenv("SPOTIFY_SECRET")}'
        a = str(base64.b64encode(s.encode('utf-8')), 'utf-8')
        u = 'https://accounts.spotify.com/api/token'
        h = {
            'Authorization': f'Basic {a}'
        }
        d = { 'grant_type': 'client_credentials' }
        res = requests.post(u, data=d, headers=h)
        return res.json()['access_token']

    def req2(self, t):
        print(t)
        u = 'https://api.spotify.com/v1/me/playlists'
        h = { 'Authorization': f'Bearer {t}' }
        res = requests.get(u, headers=h)
        print(res.json())


if __name__ == '__main__':
    Spotify_Bot()