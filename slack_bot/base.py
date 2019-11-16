import os
import slack

_reacts = ['one', 'two', 'three', 'four']

class Base(object):
    def __init__(self):
        token = os.getenv('SLACK_TOKEN', None)
        channel = os.getenv('SLACK_CHANNEL', None)
        if token and channel:
            self.channel = channel
            self.client = slack.WebClient(token=token)
            self.msg = None
        else:
            raise Exception('Slack env vars missing')
    
    def post_msg(self, text):
        self.msg = self.client.chat_postMessage(
            channel=self.channel,
            text=text)
        return

    def add_msg_react(self, name):
        if not self.msg: return
        self.client.reactions_add(
            name=name,
            channel=self.msg['channel'],
            timestamp=self.msg['ts'])
        return

    def get_msg_reacts(self):
        if not self.msg: return
        res = self.client.reactions_get(
            channel=self.channel,
            timestamp=self.msg['ts'])
        return [r for r in res['message']['reactions'] if r['name'] in _reacts]

    def get_user_name(self, user_id):
        if not self.msg: return
        res = self.client.users_info(user=user_id)
        return res['user']['real_name']