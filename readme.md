# Quizbot

### prog:
- spotify api auth sucks
- https://developer.spotify.com/documentation/web-api/reference/playlists/get-a-list-of-current-users-playlists/

### todo:
- Spotify api:
    - ping my bot on track change
    - get list of songs from spotify
- Set up redis & use python redis client to save and get data
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

Seems simple enough?