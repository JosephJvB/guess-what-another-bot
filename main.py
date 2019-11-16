import os
import random
from threading import Timer, Thread
import slack
import asyncio

from slack_bot.main import Slack_Bot
from spotify_bot.main import Spotify_Bot

class Game(object):
    def __init__(self):
        self.timer = None
        self.current_track = ''
        self.answer_emoji = ''
        self.spotify = Spotify_Bot()
        self.slack = Slack_Bot()
        self.start_game()
    
    def start_game(self):
        print('START GAME IN')
        t = self.spotify.get_current_track()
        if t == None:
            self.set_timeout(15, self.start_game)
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
        self.set_timeout(30, self.check_round_end)
        print('START ROUND OUT')
        return

    def check_round_end(self):
        print('CHECK ROUND IN')
        t = self.spotify.get_current_track()
        if t == self.current_track:
            self.set_timeout(15, self.check_round_end)
            print('CHECK ROUND OUT: NO NEW SONG')
            return
        self.slack.post_end_msg(
            self.answer_emoji,
            self.current_track)
        self.start_round(t)
        print('CHECK ROUND OUT: NEW SONG, NEW ROUND')
        return

    def set_timeout(self, t, fn):
        if self.timer: self.timer.cancel()
        self.timer = Timer(t, fn)
        self.timer.start()
        return

Game()

@slack.RTMClient.run_on(event='message')
def on_message(**payload):
    print('hi')
# loop2 = asyncio.new_event_loop()
# asyncio.set_event_loop(loop2)
# rtm_client = slack.RTMClient(token=os.getenv('SLACK_TOKEN'))
# loop2.run_forever(rtm_client.start())

# def on_msg_evt(self, payload):
#     data = payload['data']
#     if not data.get('text'): return 
#     if data['channel'] != self.channel: return

#     if data['text'].startswith('!leaderboard') or data['text'].startswith('!lb'):
#         lb = self.redis.get_leaderboard()
#         t = '*Leaderboard:*\n'
#         for i, u in enumerate(lb):
#             t += f'*{i + 1}.* {u.name}: *{u.points}*\n'
#         self.post_msg(t)
#         return

#     if data['text'].startswith('!points'):
#         u_id = data['user']
#         user = self.get_user_name(u_id)
#         p = self.redis.get_user_points(user)
#         t = f'*{user}* is on {p}'
#         t += 'point!' if p == 1 else 'points!'
#         self.post_msg(t)
#         return
