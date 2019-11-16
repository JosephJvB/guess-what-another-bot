# Quizbot

### prog:
- make output msgs prettier

### todo:
- figure out event loop so I can use rtm client for points and leaderboard cmd
- bug: this event loop is already running
2. Monday:
    - spin up web dynos
    - get grant to auth his account
    - save env vars in heroku
        - SPOTIFY_CODE
        - SPOTIFY_ACCESS
        - SPOTIFY_REFRESH
        etc etc

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