# Quizbot

### prog:
- chill brother
- exploit fix: only react to one message at once haha. Two solutions:
    1. use rtm client to respond to on-reaction event
    2. if someone reacts to more than one answer, exclude them
- want to do both, except I cant do 1. - cos I can only remove bot reactions, not users reactions :(

### todo:
- bug: sometimes reactions are added out of order?
- bug: this event loop is already running
1. Redis
    - Leaderboard from redis records
2. Monday:
    - spin up web dynos
    - get grant to auth his account
    - save env vars in heroku
        - SPOTIFY_CODE
        - SPOTIFY_ACCESS
        - SPOTIFY_REFRESH

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