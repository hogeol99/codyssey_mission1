# Service Discovery 실습을 위한 방문자 수 카운터

## 1. 기반 파일들 

[Redis에 접속해서 숫자를 1씩 올리는 간단한 코드입니다.](../app/multi_container_test/app.py)

[웹 서버 이미지용 Dockerfile](../app/multi_container_test/Dockerfile)

[docker-compose.yml](../app/multi_container_test/docker-compose.yml)

## 2. 실행 및 검증
```bash
discovery_test> docker compose up -d
[+] up 10/10
 ✔ Image redis:alpine Pulled                        5.6s
[+] Building 14.8s (12/12) FINISHED                     
 => [internal] load local bake definitions         0.0s
 => => reading from stdin 645B                     0.0s
 => [internal] load build definition from Dockerf  0.0s
 => => transferring dockerfile: 175B               0.0s
 => [internal] load metadata for docker.io/librar  2.2s
 => [auth] library/python:pull token for registry  0.0s
 => [internal] load .dockerignore                  0.0s
 => => transferring context: 2B                    0.0s
 => [1/4] FROM docker.io/library/python:3.9-slim@  4.2s
 => => resolve docker.io/library/python:3.9-slim@  0.0s
 => => sha256:ea56f685404adf81680322f 251B / 251B  0.2s
 => => sha256:fc74430849022d13b 13.88MB / 13.88MB  1.3s
 => => sha256:38513bd7256313495 29.78MB / 29.78MB  2.2s
 => => sha256:b3ec39b36ae8c03a3e0 1.29MB / 1.29MB  0.8s
 => => extracting sha256:38513bd7256313495cdd83b3  1.1s
 => => extracting sha256:b3ec39b36ae8c03a3e09854d  0.2s
 => => extracting sha256:fc74430849022d13b0d44b89  0.7s
 => => extracting sha256:ea56f685404adf81680322f1  0.0s
 => [internal] load build context                  0.0s
 => => transferring context: 1.05kB                0.0s
 => [2/4] WORKDIR /code                            0.2s
 => [3/4] RUN pip install flask redis              4.3s
 => [4/4] COPY . .                                 0.0s
 => exporting to image                             3.0s
 => => exporting layers                            0.8s
 => => exporting manifest sha256:100b6e679af7cfbf  0.0s
 => => exporting config sha256:523d50d71406085aad  0.0s
 => => exporting attestation manifest sha256:37a7  0.0s
 => => exporting manifest list sha256:8fa24f007cd  0.0s
 => => naming to docker.io/library/service_discov  0.0s
 => => unpacking to docker.io/library/service_dis  2.2s
 => resolving provenance for metadata file         0.0s
[+] up 14/14
 ✔ Image redis:alpine                      Pulled   5.6s
 ✔ Image multi_container_test-web-server Built   15.4s
 ✔ Network multi_container_test_default  Created  0.0s
 ✔ Container multi_container_test-web... Started  0.5s
 ✔ Container multi_container_test-red... Started  0.7s
PS C:\Users\homec\Desktop\codyssey_mission1\app\multi_container_test> curl http://localhost:5000  
어서오세요! 10번째 방문자이시군요!
PS C:\Users\homec\Desktop\codyssey_mission1\app\multi_container_test> curl http://localhost:5000
어서오세요! 11번째 방문자이시군요!
```