# Quizbot

### prog:
- scale worker dyno on and off with cronjob
    - https://realpython.com/automatically-scale-heroku-dynos/
    - https://gist.github.com/mjhea0/e1436b693cc56ca82277

### blocked
- Game design issues:
    1. disable slash commands: remake !whom @user
        - dunno how to
        - other option: remove jukebot and recreate all the commands, kind of a big yikes..
    2. public reactions
        - if everyone can see reactions, you're just gonna pick the number that everyone has reacted to...

### todo:
- make output msgs prettier

### tech:
- Slackbot
- Spotify API
- Heroku
- Redis
- http://everynoise.com/ ?

### flow:
- Track starts
- Bot registers song change
- Bot creates list of song names: 1 correct, and 3 @ random
- Sends message: which song is playing? react 1, 2, 3, 4
- All users who reacted to the right thing get a point
