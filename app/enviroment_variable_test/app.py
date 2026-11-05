import os
from flask import Flask

app = Flask(__name__)

# 핵심! 코드가 직접 값을 갖지 않고, 밖에서(os) 주는 환경 변수를 읽어옵니다.
# 만약 밖에서 안 주면 기본값(5000, '기본모드')을 씁니다.
PORT = int(os.getenv('APP_PORT', 5000))
MODE = os.getenv('APP_MODE', '기본모드')

@app.route('/')
def hello():
    return f"현재 모드: {MODE} / 실행 포트: {PORT}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)