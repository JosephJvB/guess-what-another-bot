import os
import random
from threading import Timer, Thread
import slack
import asyncio

from slack_bot.main import Slack_Bot
from spotify_bot.main import Spotify_Bot

TIMEOUT = int(os.getenv('TIMEOUT'))

class Game(object):
    def __init__(self):
        self.timer = None
        self.thread = None
        self.current_track = ''
        self.answer_emoji = ''
        self.spotify = Spotify_Bot()
        self.slack = Slack_Bot()
    
    def start_game(self):
        print('START GAME IN')
        t = self.spotify.get_current_track()
        if t == None:
            self.set_timeout(15, self.start_game, 'start_game')
            print('START GAME OUT: NO SONG PLAYING')
            return
        self.start_round(t)
        print('START GAME OUT')
        return

    def start_round(self, t):
        print('START ROUND IN')
        all_tracks = self.spotify.get_playlist_tracks()
        if t in all_tracks:
            all_tracks.remove(t)
        track_options = [t, *random.sample(all_tracks, 3)]
        random.shuffle(track_options)
        ans_idx = track_options.index(t)
        self.current_track = t
        self.answer_emoji = self.slack.get_emoji(ans_idx)
        self.slack.start_round_msg(track_options)
        self.set_timeout(TIMEOUT, self.check_round_end, 'check_round_end')
        print('START ROUND OUT')
        return

    def check_round_end(self):
        print('CHECK ROUND IN')
        t = self.spotify.get_current_track()
        if t == self.current_track:
            self.set_timeout(TIMEOUT, self.check_round_end, 'check_round_end')
            print('CHECK ROUND OUT: NO NEW SONG')
            return
        self.slack.post_end_msg(
            self.answer_emoji,
            self.current_track)
        self.start_round(t)
        print('CHECK ROUND OUT: NEW SONG, NEW ROUND')
        return

    def set_timeout(self, t, fn, n):
        if self.timer and self.thread:
            self.timer.cancel()
            self.thread.join()
            self.timer = None
            self.thread = None
        self.timer = Timer(t, fn)
        self.thread = Thread(target=self.timer.start, name=n)
        self.thread.start()
        return


@slack.RTMClient.run_on(event='message')
def on_message(**payload):
    print('hi')

l = asyncio.get_event_loop()
c = slack.RTMClient(token=os.getenv('SLACK_TOKEN'), loop=l)

g = Game()
t = Thread(target=g.start_game, daemon=True, name='init_game_thread')

try:
    t.start()
    l.run_forever(c.start())
except KeyboardInterrupt:
    l.close()
finally:
    l.close()