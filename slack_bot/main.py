import os
import time
import random
from slack_bot.base import Base

emojis = {
    0: 'one',
    1: 'two',
    2: 'three',
    3: 'four',
}

class Slack_Bot(Base):
    def __init__(self):
        super(Slack_Bot, self).__init__()

    def start_round_msg(self, opts):
        txt = '*What\'s that track?*\n\n'
        for i, o in enumerate(opts):
            txt += f'*{i + 1}.*  "_{o}_"\n'
        self.post_msg(txt)
        for i in range(len(opts)):
            self.add_msg_react(self.get_emoji(i))
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
        txt = f'*Answer:* "_{track}_"\n\nWinners:'
        if len(winner_names) > 0:
            for name in winner_names:
                txt += f' {name},'
        else: 
            txt +=' No one! '
        self.post_msg(txt[:-1])
        return

    def get_emoji(self, n):
        return emojis.get(n)