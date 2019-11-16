# Quizbot

### prog:
- Run game loop and rtm client at same time
    - Joe learns about blocking function calls..ouch the learning hurts
    - Works: but spawns threads on new round up to a cap of ~24
    - I dont really know why
    - I was always spawning threads, before I was doing Game() and RTM at same time..
    - so I shouldnt worry? unsure

### todo:
- make output msgs prettier
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