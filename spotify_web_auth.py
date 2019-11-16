import os
from flask import Flask, render_template, redirect, request

api = Flask(
  __name__
#   template_folder="", # html
#   static_folder="" # js/css
)

@api.route('/success', methods=['GET']) 
def succeed():
    d = {
        'all:': request.args,
        'code:': request.args.get('code'),
        'error:': request.args.get('error'),
    }
    print(d)
    return d

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