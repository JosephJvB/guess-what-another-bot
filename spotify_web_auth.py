import os
from flask import Flask, render_template, redirect, request

api = Flask(
  __name__
#   template_folder="", # serve html from here
#   static_folder="" # js/css
)

@api.route('/success', methods=['GET']) 
def succeed():
    d = {
        'all:': request.args,
        'code:': request.args.get('code'),
        'state:': request.args.get('state'),
        'error:': request.args.get('error'),
    }
    print(d)
    return d

@api.route('/', methods=['GET'])
def init_spotty_auth():
#   api.send_static_file("index.js")
#   return render_template("index.html")
    scopes = 'playlist-read-private playlist-read-collaborative user-read-currently-playing user-read-private'
    url = ''.join([
        'https://accounts.spotify.com/authorize?',
        f'client_id={os.getenv("SPOTIFY_ID")}',
        '&redirect_uri=https://jvb-spotty-auth.herokuapp.com/success/',
        f'&scope={scopes}'
        '&response_type=code'
        # f'&state={state}', # jukebot had this??
    ])
    return redirect(url, code=302)

if __name__ == '__main__':
    p = int(os.getenv('PORT', 3000))
    api.run(host='0.0.0.0', port=p)

x = 'https://accounts.spotify.com/authorize?client_id=9e65a5b32a91465da947ea3621cdba37&redirect_uri=https%3A%2F%2Fjvb-spotty-auth.herokuapp.com%2Fsuccess&scope=playlist-read-private%20playlist-read-collaborative%20user-read-currently-playing%20user-read-private&response_type=code'

y = 'https://accounts.spotify.com/en/login?continue=https:%2F%2Faccounts.spotify.com%2Fauthorize%3Fscope%3Dplaylist-read-private%2Bplaylist-read-collaborative%2Bplaylist-modify-private%2Bplaylist-modify-public%2Bstreaming%2Buser-read-currently-playing%2Buser-read-email%2Buser-read-private%2Buser-modify-playback-state%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fgetjukebot.com%252Fspotify%252Fauth%26state%3D61gch1YLqYUeAbGQYoUqA3xI9idK3SzZeHgksuXq%26client_id%3Df5328ccd31d0450d85b25136db719464%26show_dialog%3D0'