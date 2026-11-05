import time
import redis
from flask import Flask

app = Flask(__name__)
# 서비스 이름인 'redis-db'를 호스트 이름으로 사용합니다! (중요)
cache = redis.Redis(host='redis-db', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0: raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return f'어서오세요! {count}번째 방문자이시군요!\n'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)