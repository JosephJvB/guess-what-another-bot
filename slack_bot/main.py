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
        self.answer = (None, None) # emoji, songname
        self.handle_new_track()
        time.sleep(5)
        self.handle_answer()

    def handle_answer(self):
        msg_reactions = self.get_msg_reacts()
        winners = next(r['users'] for r in msg_reactions if r['name'] == self.answer[0])
        winners.remove(self.bot_id)
        txt = f'*Answer:* "_{self.answer[1]}_"\n\nWinners:'
        if len(winners) > 0:
            for u in winners:
                txt += f' <@{u}>,' # dont actually tag winners in live
        else: 
            txt +=' No one! '
        self.post_msg(txt[:-1])
        return
    
    # likely pass in options from spotify bot
    def handle_new_track(self):
        opts = self.get_opts()
        txt = '*What\'s that track!*\n\n'
        for i, o in enumerate(opts):
            txt += f'*{i + 1}.*  "_{o}_"\n'
        self.post_msg(txt)
        for i in range(len(opts)):
            self.add_msg_react(emojis.get(i))
        return

    # get current song from spotify
    # choose 3 more songs from spotify, add to array
    # todo: allow for chance to add 'none of the above'
    def get_opts(self):
        ans = 'song 1'
        opts = [ans, 'song 2', 'song 3', 'song 4'][:4]
        random.shuffle(opts)
        answer_idx = opts.index(ans)
        self.answer = (emojis.get(answer_idx), ans)
        return opts