def on_msg_evt(self, payload):
    data = payload['data']
    if not data.get('text'): return 
    if data['channel'] != self.channel: return

    if data['text'].startswith('!leaderboard') or data['text'].startswith('!lb'):
        lb = self.redis.get_leaderboard()
        t = '*Leaderboard:*\n'
        for i, u in enumerate(lb):
            t += f'*{i + 1}.* {u.name}: *{u.points}*\n'
        self.post_msg(t)
        return

    if data['text'].startswith('!points'):
        u_id = data['user']
        user = self.get_user_name(u_id)
        p = self.redis.get_user_points(user)
        t = f'*{user}* is on {p}'
        t += 'point!' if p == 1 else 'points!'
        self.post_msg(t)
        return