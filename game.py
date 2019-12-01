import os
import random
from threading import Timer
import threading

from slack_bot.main import Slack_Bot
from spotify_bot.main import Spotify_Bot

class Game(object):
    def __init__(self):
        self.timer = None
        self.current_track = ''
        self.answer_emoji = ''
        self.spotify = Spotify_Bot()
        self.slack = Slack_Bot()
    
    def start_game(self):
        self.log_game_state('START GAME IN')
        to = int(os.getenv('GAME_TIMEOUT'))
        t = self.spotify.get_current_track()
        if t == None:
            self.set_timeout(to, self.start_game)
            self.log_game_state('START GAME OUT: NO SONG PLAYING')
            return
        self.start_round(t)
        self.log_game_state('START GAME OUT')
        return

    def start_round(self, t):
        self.log_game_state('START ROUND IN')
        to = int(os.getenv('ROUND_TIMEOUT'))
        all_tracks = [t['track']['name'] for t in self.spotify.get_playlist_tracks()]
        if t in all_tracks:
            all_tracks.remove(t)
        track_options = [t, *random.sample(all_tracks, 3)]
        random.shuffle(track_options)
        ans_idx = track_options.index(t)
        self.current_track = t
        self.answer_emoji = self.slack.get_emoji(ans_idx)
        self.slack.start_round_msg(track_options)
        self.set_timeout(to, self.check_round_end)
        self.log_game_state('START ROUND OUT')
        return

    def check_round_end(self):
        self.log_game_state('CHECK ROUND IN')
        to = int(os.getenv('CHECK_TIMEOUT'))
        t = self.spotify.get_current_track()
        if t == self.current_track:
            self.set_timeout(to, self.check_round_end)
            self.log_game_state('CHECK ROUND OUT: NO NEW SONG')
            return
        self.slack.post_end_msg(
            self.answer_emoji,
            self.current_track)
        self.start_round(t)
        self.log_game_state('CHECK ROUND OUT: NEW SONG, NEW ROUND')
        return

    def set_timeout(self, t, fn):
        if self.timer:
            self.timer.cancel()
            self.timer = None
        self.timer = Timer(t, fn)
        self.timer.start()
        return

    def log_game_state(self, game_state):
        print(game_state)
        print('THREADCOUNT:', threading.active_count())
        return