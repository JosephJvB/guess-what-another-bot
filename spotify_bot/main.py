import os
import requests
from spotify_bot.auth import Auth

class Spotify_Bot(Auth):
    def __init__(self):
        super(Spotify_Bot, self).__init__()
        self.refresh_auth()

    def get_playlist_tracks(self):
        token = self.get_cc_token()
        h = { 'Authorization': f'Bearer {token}' }
        playlist_id = os.getenv('SPOTIFY_PLAYLIST')
        u = f'https://api.spotify.com/v1/playlists/{playlist_id}'
        res = requests.get(u, headers=h)
        j = res.json()
        names = [t['track']['name'] for t in j['tracks']['items']]
        return names

    def get_current_track(self):
        if self.need_refresh(): 
            self.refresh_auth()
        h = { 'Authorization': f'Bearer {self.auth["access_token"]}' }
        u = 'https://api.spotify.com/v1/me/player/currently-playing'
        res = requests.get(u, headers=h)
        if res.status_code is not 200:
            return None

        return res.json()['item']['name']