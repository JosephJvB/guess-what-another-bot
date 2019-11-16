import os
import time
import base64
import requests

# use cc token for get-playlist
# use oauth token for get-current-track

class Auth(object):
    def __init__(self):
        r = os.getenv('SPOTIFY_REFRESH')
        s_id = os.getenv('SPOTIFY_ID')
        s_secret = os.getenv('SPOTIFY_SECRET')
        s_code = os.getenv('SPOTIFY_CODE')
        if r and s_id and s_secret and s_code:
            self.auth = None
            self.refresh = r
            self.s_id = s_id
            self.s_secret = s_secret
            self.s_code = s_code
        else:
            raise Exception('Spotify auth vars missing')

    def refresh_auth(self):
        d = {
            'grant_type': 'refresh_token',
            'refresh_token': self.refresh
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
            'code': self.s_code,
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
        s = f'{self.s_id}:{self.s_secret}'
        token = str(base64.b64encode(s.encode('utf-8')), 'utf-8')
        return f'Basic {token}'

    def need_refresh(self):
        if not self.auth: return True
        now = time.time()
        if now - self.last_refresh > 3500:
            return True
        else:
            return False