import os
import redis

class Redis_Client(object):
    def __init__(self):
        u = os.getenv('REDIS_URL')
        if u:
            self.redis = redis.Redis.from_url(u)
        else:
            raise Exception('Redis env vars missing')

    def save_winners(self, winners):
        for w in winners:
            self.redis.incr(w)
        return

    def get_leaderboard(self):
        keys = self.redis.keys()
        vals = self.redis.mget(keys)
        scores = []
        for i, k in enumerate(keys):
            scores.append({
                'name': k,
                'points': int(vals[i])
            })
        return scores

    def get_user_points(self, user):
        return self.redis.get(user)
