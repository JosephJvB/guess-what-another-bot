import os
import slacker
from slacker import Slacker
from requests.sessions import Session

_reacts = ['one', 'two', 'three', 'four']

class Slack_Sessions(object):
    def __init__(self):
        token = os.getenv('SLACK_TOKEN')
        channel = os.getenv('SLACK_CHANNEL')
        if token and channel:
            self.channel = channel
            with Session() as sesshie:
                self.client = Slacker(token, session=sesshie)
                self.msg = None
        else:
            raise Exception('Slack env vars missing')
    
    def post_msg(self, text):
        self.msg = self.client.chat.post_message(
            channel=self.channel,
            text=text).body
        return

    def add_msg_react(self, name):
        if not self.msg: return
        self.client.reactions.add(
            name=name,
            channel=self.channel,
            timestamp=self.msg['ts'])
        return

    def get_msg_reacts(self):
        if not self.msg: return
        res = self.client.reactions.get(
            channel=self.channel,
            timestamp=self.msg['ts']).body
        return [r for r in res['message']['reactions'] if r['name'] in _reacts]

    def get_user_name(self, user_id):
        if not self.msg: return
        res = self.client.users.info(user=user_id).body
        return res['user']['real_name']