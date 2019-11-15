import os
import base64
import time
from spotipy import Spotify, util
import requests

class Spotify_Bot(object):
    def __init__(self):
        self.auth = None
        self.last_refresh = 0
        self.refresh_auth()
        return

    def get_cc_token(self): # no scopes, basic auth
        u = 'https://accounts.spotify.com/api/token'
        h = { 'Authorization': self.get_basic_auth() }
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

    def get_oauth_token(self):
        d = {
            'grant_type': 'authorization_code',
            'code': os.getenv('SPOTIFY_CODE'),
            'redirect_uri': 'https://jvb-spotty-auth.herokuapp.com/success'
        }
        h = { 'Authorization': self.get_basic_auth() }
        u = 'https://accounts.spotify.com/api/token'
        res = requests.post(u, data=d, headers=h)
        print(res)
        print(res.json())
        print('DONE')
        return

    def get_me(self):
        h = { 'Authorization': f'Bearer {self.auth.access_token}' }
        u = 'https://api.spotify.com/v1/me/playlists'
        res = requests.get(u, headers=h)
        print(res)
        print(res.json())
        return

    def refresh_auth(self):
        d = {
            'grant_type': 'refresh_token',
            'refresh_token': os.getenv('SPOTIFY_REFRESH')
        }
        h = { 'Authorization': self.get_basic_auth() }
        u = 'https://accounts.spotify.com/api/token'
        res = requests.post(u, data=d, headers=h)
        print(res)
        print(res.json())
        self.auth = res.json()
        self.last_refresh = time.time()
        return

    def need_refresh(self):
        if not self.auth: return True
        now = time.time()
        if now - self.last_refresh > 3500:
            return True
        else:
            return False


    def get_basic_auth(self):
        s = f'{os.getenv("SPOTIFY_ID")}:{os.getenv("SPOTIFY_SECRET")}'
        token = str(base64.b64encode(s.encode('utf-8')), 'utf-8')
        return f'Basic {token}'


if __name__ == '__main__':
    Spotify_Bot()