import os
import redis

class Redis_Client(object):
    def __init__(self):
        h = os.getenv('REDIS_HOST')
        p = int(os.getenv('REDIS_PORT'))
        db = os.getenv('REDIS_DB')
        if h and p and db:
            self.redis = redis.Redis(host=h, port=p, db=db)
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