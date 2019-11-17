import os
import time
import random
from slack_bot.base import Base
from slack_bot.redis_client import Redis_Client

_emojis = {
    0: 'one',
    1: 'two',
    2: 'three',
    3: 'four',
}

class Slack_Bot(Base):
    def __init__(self):
        super(Slack_Bot, self).__init__()
        self.redis = Redis_Client()

    def start_round_msg(self, opts):
        txt = '*What\'s that track?*\n\n'
        for i, o in enumerate(opts):
            txt += f'*{i + 1}.*  "_{o}_"\n'
        self.post_msg(txt)
        self.add_msg_react(self.get_emoji(0))
        self.add_msg_react(self.get_emoji(1))
        self.add_msg_react(self.get_emoji(2))
        self.add_msg_react(self.get_emoji(3))
        return

    def post_end_msg(self, win_emoji, track):
        msg_reacts = self.get_msg_reacts()
        users_list = []
        winner_ids = []
        for r in msg_reacts:
            users_list += r['users']
            if r['name'] == win_emoji:
                winner_ids = r['users']
        winner_names = [self.get_user_name(i) for i in winner_ids if users_list.count(i) == 1]
        txt = f'*Answer:* "_{track}_"\n\n*Winners:*'
        if len(winner_names) > 0:
            for name in winner_names:
                txt += f' {name},'
        else: 
            txt +=' No one! '
        self.post_msg(txt[:-1])
        self.redis.save_winners(winner_names)
        return

    def get_emoji(self, n):
        return _emojis.get(n)