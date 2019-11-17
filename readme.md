# Quizbot

### prog:

### todo:
- !points and !leaderboard command
    - whom and song guess are in seperate databases.
    - wanna make redis shared
    - migrate existing mysql data to redis
    - connect /whom to shared
- Game design issues:
    1. /whom
        - /whom @user ruins guessing game: /whom prints song title
        - /current track ruins game too
        - disable /current & /whom for jukebot
        - re-implement whomgame as !whom @user
    2. public reactions
        - if everyone can see reactions, you're just gonna pick the number that everyone has reacted to...
- make output msgs prettier
- scale worker dyno on and off with cronjob

### tech:
- Slackbot
- Spotify API
- Heroku
- Redis

### flow:
- Track starts
- Bot registers song change
- Bot creates list of song names: 1 correct, and 3 @ random
- Sends message: which song is playing? react 1, 2, 3, 4
- All users who reacted to the right thing get a point
