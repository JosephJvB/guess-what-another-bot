import os
import time
import base64
import requests

# use cc token for get-playlist
# use oauth token for get-current-track

class Auth(object):
    def __init__(self):
        self.auth = None

    def refresh_auth(self):
        d = {
            'grant_type': 'refresh_token',
            'refresh_token': os.getenv('SPOTIFY_REFRESH')
        }
        h = { 'Authorization': self.get_basic_auth() }
        u = 'https://accounts.spotify.com/api/token'
        res = requests.post(u, data=d, headers=h)
        self.auth = res.json()
        self.last_refresh = time.time()
        return

    def get_oauth_token(self): # only need once..
        d = {
            'grant_type': 'authorization_code',
            'code': os.getenv('SPOTIFY_CODE'),
            'redirect_uri': 'https://jvb-spotty-auth.herokuapp.com/success'
        }
        h = { 'Authorization': self.get_basic_auth() }
        u = 'https://accounts.spotify.com/api/token'
        res = requests.post(u, data=d, headers=h)
        print(res)
        print('oauth success:', res.json())
        return

    def get_cc_token(self): # no scopes, basic auth
        u = 'https://accounts.spotify.com/api/token'
        h = { 'Authorization': self.get_basic_auth() }
        d = { 'grant_type': 'client_credentials' }
        res = requests.post(u, data=d, headers=h)
        return res.json()['access_token']

    def get_basic_auth(self):
        s = f'{os.getenv("SPOTIFY_ID")}:{os.getenv("SPOTIFY_SECRET")}'
        token = str(base64.b64encode(s.encode('utf-8')), 'utf-8')
        return f'Basic {token}'

    def need_refresh(self):
        if not self.auth: return True
        now = time.time()
        if now - self.last_refresh > 3500:
            return True
        else:
            return False