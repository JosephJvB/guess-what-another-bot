import os
import random
from threading import Timer
from slack_bot.main import Slack_Bot
from spotify_bot.main import Spotify_Bot


class Game(object):
    def __init__(self):
        self.spotify = Spotify_Bot()
        self.slack = Slack_Bot()
        self.current_track = ''
        self.answer_emoji = ''
        self.start_game()
    
    def start_game(self):
        print('START GAME IN')
        t = self.spotify.get_current_track()
        if t == None:
            Timer(15, self.start_game).start()
            print('START GAME OUT: NO SONG PLAYING')
            return

        self.start_round(t)
        Timer(30, self.check_round_end).start()
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
        Timer(30, self.check_round_end).start()
        print('START ROUND OUT')
        return

    def check_round_end(self):
        print('CHECK ROUND IN')
        t = self.spotify.get_current_track()
        if t == self.current_track:
            Timer(15, self.check_round_end).start()
            print('CHECK ROUND OUT: NO NEW SONG')
            return
        self.slack.post_end_msg(
            self.answer_emoji,
            self.current_track)
        self.start_round(t)
        print('CHECK ROUND OUT: NEW SONG, NEW ROUND')
        return
        
Game()