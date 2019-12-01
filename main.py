import os
from threading import Thread
import slack
from game import Game
from spotify_bot.main import Spotify_Bot


# # todo
# @slack.RTMClient.run_on(event='message')
# def on_message(**payload):
#     print('hi')

try:
    # dump to file
    s = Spotify_Bot()
    tracks = s.get_playlist_tracks()
    if tracks:
        f = open('dump.txt', 'w+')
        for t in tracks:
            f.write(t['track']['name'] + ' BY ' + t['track']['artists'][0]['name'] + '\n')
        f.close()
    # g = Game()
    # g.start_game()
    # Thread(target=g.start_game, daemon=True).start()
    # slack.RTMClient(token=os.getenv('SLACK_TOKEN')).start()
except KeyboardInterrupt:
    pass
finally:
    pass