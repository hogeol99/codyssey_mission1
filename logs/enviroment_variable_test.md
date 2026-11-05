# 환경 변수 활용 Compose 실습

# 1 파일 준비

- app.py [확인](../app/enviroment_variable_test/app.py)
- Dockerfile[확인](../app/enviroment_variable_test/Dockerfile)
- docker-compose.yml[확인](../app/enviroment_variable_test/docker-compose.yml)

# 2 환경 변수 설정

enviroment_variable_test 디렉토리에 .env파일 생성

```bash
# .env 파일 내용
MY_PORT=8080
MY_MODE=운영(PROD)
```

# 3 container 생성 후 실행 확인

```bash
PS C:\Users\homec\Desktop\codyssey_mission1\app\enviroment_variable_test> docker compose up -d
[+] Building 7.6s (12/12) FINISHED                      
 => [internal] load local bake definitions         0.0s
 => => reading from stdin 637B                     0.0s
 => [internal] load build definition from Dockerf  0.0s
 => => transferring dockerfile: 135B               0.0s
 => [internal] load metadata for docker.io/librar  1.5s
 => [auth] library/python:pull token for registry  0.0s
 => [internal] load .dockerignore                  0.0s
 => => transferring context: 2B                    0.0s
 => CACHED [1/4] FROM docker.io/library/python:3.  0.0s
 => => resolve docker.io/library/python:3.9-slim@  0.0s
 => [internal] load build context                  0.0s
 => => transferring context: 529B                  0.0s
 => [2/4] WORKDIR /app                             0.0s
 => [3/4] RUN pip install flask                    4.2s
 => [4/4] COPY app.py .                            0.0s
 => exporting to image                             1.2s
 => => exporting layers                            0.7s
 => => exporting manifest sha256:a01b016e09bfe443  0.0s
 => => exporting config sha256:a8da93cec09c32108f  0.0s
 => => exporting attestation manifest sha256:436c  0.0s
 => => exporting manifest list sha256:632d758b3d7  0.0s
 => => naming to docker.io/library/enviroment_var  0.0s
 => => unpacking to docker.io/library/enviroment_  0.4s
 => resolving provenance for metadata file         0.0s
[+] up 3/3
 ✔ Image enviroment_variable_test-my-web    Built   8.2s
 ✔ Network enviroment_variable_test_default Created 0.0s
 ✔ Container enviroment_variable_test-my... Started 0.6s
PS C:\Users\homec\Desktop\codyssey_mission1\app\enviroment_variable_test> curl http://localhost:8080       
현재 모드: 운영(PROD) / 실행 포트: 8080
```