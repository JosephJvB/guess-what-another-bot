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

    def post_end_msg(self, emoji, track):
        msg_reacts = self.get_msg_reacts()
        winner_ids = next(r['users'] for r in msg_reacts if r['name'] == emoji)
        winner_ids.remove(os.getenv('SLACK_BOT_ID'))
        txt = f'*Answer:* "_{track}_"\n\nWinners:'
        if len(winner_ids) > 0:
            for u_id in winner_ids:
                name = self.get_user_name(u_id)
                txt += f' {name},'
        else: 
            txt +=' No one! '
        self.post_msg(txt[:-1])
        return

    def get_emoji(self, n):
        return emojis.get(n)