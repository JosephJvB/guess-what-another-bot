# Quizbot

### prog:
- spotify api auth sucks
- https://developer.spotify.com/documentation/web-api/reference/playlists/get-a-list-of-current-users-playlists/

### todo:
1. Spotify api:
    - ping my bot on track change
    - get list of songs from spotify
    - maybe I have to Authorize bot with my account just ONE time, and can then use refresh token for further auth. It SEEMS as though that is how Jukebot works, from the outside. TODO: re-add Jukebot and take note of auth steps
2. Redis
    - Leaderboard from redis records


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