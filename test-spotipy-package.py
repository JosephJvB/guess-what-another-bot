# hahahahahah I rolled my own, it was really fun ahahahahaha
import os
import spotipy
from spotipy import util

scope = 'playlist-read-private playlist-read-collaborative user-read-currently-playing'

username = os.getenv('SPOTIFY_UNAME')

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_playing_track()
    print(results)
else:
    print("Can't get token for", username)