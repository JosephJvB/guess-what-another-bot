import os
from threading import Thread
import slack
from game import Game


# # todo
# @slack.RTMClient.run_on(event='message')
# def on_message(**payload):
#     print('hi')

try:
    g = Game()
    Thread(target=g.start_game, daemon=True).start()
    slack.RTMClient(token=os.getenv('SLACK_TOKEN')).start()
except KeyboardInterrupt:
    pass
finally:
    pass