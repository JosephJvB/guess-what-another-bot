import os
import base64
from spotipy import Spotify, util
import requests

class Spotify_Bot(object):
    def __init__(self):
        self.auth = None
        # self.get_playlist()
        self.get_oauth_token()
        return

    def get_cc_token(self): # no scopes, basic auth
        u = 'https://accounts.spotify.com/api/token'
        h = {
            'Authorization': f'Basic {self.get_spotty_base64()}'
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

    def get_oauth_token(self):
        scopes = 'playlist-read-private%20playlist-read-collaborative%20user-read-currently-playing%20user-read-private'
        redirect_uri = ''.join([
            'https://accounts.spotify.com/en/authorize?',
            f'client_id={os.getenv("SPOTIFY_ID")}',
            '&redirect_uri=https://jvb-spotty-auth.herokuapp.com/success',
            f'&scope={scopes}'
            '&response_type=code'
            # f'&state={state}', # jukebot had this??
        ])
        d = {
            'grant_type': 'authorization_code',
            'code': os.getenv('SPOTIFY_CODE'),
            'redirect_uri': redirect_uri
        }
        h = {
            'Authorization': f'Basic {self.get_spotty_base64()}'
        }
        u = 'https://accounts.spotify.com/api/token'
        res = requests.post(u, data=d, headers=h)
        print(res)
        print(res.json())
        print('DONE')
        self.auth = res.json()
        return

    def get_spotty_base64(self):
        s = f'{os.getenv("SPOTIFY_ID")}:{os.getenv("SPOTIFY_SECRET")}'
        return str(base64.b64encode(s.encode('utf-8')), 'utf-8')


if __name__ == '__main__':
    Spotify_Bot()