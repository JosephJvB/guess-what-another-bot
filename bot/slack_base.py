import os
import slack

class Base(object):
    def __init__(self):
        token = os.getenv('SLACK_TOKEN', None)
        channel = os.getenv('SLACK_CHANNEL', None)
        bot_id = os.getenv('SLACK_BOT_ID', None)
        if token is not None or channel is not None or bot_id is not None:
            self.channel = channel
            self.bot_id = bot_id
            self.client = slack.WebClient(token=token)
        else:
            raise Exception('missing env vars')
    
    def post_msg(self, text):
        self.msg = self.client.chat_postMessage(
            channel=self.channel,
            text=text)
        return

    def add_msg_react(self, name):
        if self.msg is None: return
        self.client.reactions_add(
            name=name,
            channel=self.msg['channel'],
            timestamp=self.msg['ts'])
        return

    def get_msg_reacts(self):
        if self.msg is None: return
        res = self.client.reactions_get(
            channel=self.channel,
            timestamp=self.msg['ts'])
        return res['message']['reactions']