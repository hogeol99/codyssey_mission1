FROM python:3.9-slim
WORKDIR /code
# 필요한 라이브러리 설치
RUN pip install flask redis
COPY . .
CMD ["python", "app.py"]