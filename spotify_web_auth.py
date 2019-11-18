import os
import base64
from flask import Flask, render_template, redirect, request
import requests

api = Flask(
  __name__
#   template_folder="", # html
#   static_folder="" # js/css
)

s_id = os.getenv('SPOTIFY_ID')
s_secret = os.getenv('SPOTIFY_SECRET')
token = str(base64.b64encode(f'{s_id}:{s_secret}'.encode('utf-8')), 'utf-8')
basic_auth = f'Basic {token}'

@api.route('/success', methods=['GET']) 
def succeed():
    print(request.args)
    d = {
        'grant_type': 'authorization_code',
        'code': request.args.get('code'),
        'redirect_uri': 'https://jvb-spotty-auth.herokuapp.com/success'
    }
    h = { 'Authorization': basic_auth }
    u = 'https://accounts.spotify.com/api/token'
    res = requests.post(u, data=d, headers=h)
    print(res)
    j = res.json()
    print('oauth success:', j)
    return j

@api.route('/', methods=['GET'])
def init_spotty_auth():
    scopes = 'playlist-read-private playlist-read-collaborative user-read-currently-playing'
    url = ''.join([
        'https://accounts.spotify.com/authorize?',
        f'client_id={os.getenv("SPOTIFY_ID")}',
        '&redirect_uri=https://jvb-spotty-auth.herokuapp.com/success',
        f'&scope={scopes}'
        '&response_type=code'
    ])
    return redirect(url, code=302)

if __name__ == '__main__':
    p = int(os.getenv('PORT', 3000))
    api.run(host='0.0.0.0', port=p)