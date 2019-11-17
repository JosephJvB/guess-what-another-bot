# Quizbot

thought: whom game and song guess game are saving points in different databases. To a user that is confusing. Im gonna have to resolve that, either merge game points or remove whom.
Merging means using shared redis database

### prog:
- Game live in office

### todo:
- !points and !leaderboard command
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