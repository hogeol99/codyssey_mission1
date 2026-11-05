# docker compose 운영 명령어 실습 

## 1. 컨테이너 실행

`docker compose up -d`

```bash
PS C:\Users\homec\Desktop\codyssey_mission1\app\multi_container_test> docker compose up -d                        
[+] Building 2.2s (12/12) FINISHED                                                                                                                                                               
 => [internal] load local bake definitions                                                                                                                                                  0.0s
 => => reading from stdin 637B                                                                                                                                                              0.0s
 => [internal] load build definition from Dockerfile                                                                                                                                        0.0s
 => => transferring dockerfile: 175B                                                                                                                                                        0.0s
 => [internal] load metadata for docker.io/library/python:3.9-slim                                                                                                                          1.4s
 => [auth] library/python:pull token for registry-1.docker.io                                                                                                                               0.0s
 => [internal] load .dockerignore                                                                                                                                                           0.0s
 => => transferring context: 2B                                                                                                                                                             0.0s
 => [1/4] FROM docker.io/library/python:3.9-slim@sha256:2d97f6910b16bd338d3060f261f53f144965f755599aab1acda1e13cf1731b1b                                                                    0.1s
 => => resolve docker.io/library/python:3.9-slim@sha256:2d97f6910b16bd338d3060f261f53f144965f755599aab1acda1e13cf1731b1b                                                                    0.0s
 => [internal] load build context                                                                                                                                                           0.1s
 => => transferring context: 1.05kB                                                                                                                                                         0.0s
 => CACHED [2/4] WORKDIR /code                                                                                                                                                              0.0s
 => CACHED [3/4] RUN pip install flask redis                                                                                                                                                0.0s
 => CACHED [4/4] COPY . .                                                                                                                                                                   0.0s
 => exporting to image                                                                                                                                                                      0.2s
 => => exporting layers                                                                                                                                                                     0.0s
 => => exporting manifest sha256:ddfe366509a3dfc736e0faa6ab7a14479f5c482d065872d1fc620904fea7b399                                                                                           0.0s
 => => exporting config sha256:74aa22fb224cf4d3e0dc9b662518314d7539b777acf98336b67970e39da0ba41                                                                                             0.1s
 => => exporting attestation manifest sha256:68c789bb4fd8fc18f307a0506964a616db5fa3ea5d2ef1995be945865f80d5b8                                                                               0.0s
 => => exporting manifest list sha256:c72ab7a798f3eee280ad07d872c82b3d76c958fb63da79fe2e43c56280e0d7d9                                                                                      0.0s
 => => naming to docker.io/library/multi_container_test-web-server:latest                                                                                                                   0.0s
 => => unpacking to docker.io/library/multi_container_test-web-server:latest                                                                                                                0.0s
 => resolving provenance for metadata file                                                                                                                                                  0.0s
[+] up 4/4
 ✔ Image multi_container_test-web-server       Built                                                                                                                                         2.8s
 ✔ Network multi_container_test_default        Created                                                                                                                                       0.1s
 ✔ Container multi_container_test-web-server-1 Started                                                                                                                                       0.7s
 ✔ Container multi_container_test-redis-db-1   Started                    
 ```

 ## 2. 컨테이너 목록 및 상태 확인

 - 명령어 : `docker compose ps`

 현재 프로젝트로 실행된 컨테이너들의 이름, 상태(Status), 포트 맵핑 정보를 한눈에 보여줍니다. Exit 상태라면 설정에 문제가 있다는 뜻입니다.

 ```bash
 PS C:\Users\homec\Desktop\codyssey_mission1\app\multi_container_test> docker compose ps   
NAME                                IMAGE                             COMMAND                   SERVICE      CREATED          STATUS          PORTS
multi_container_test-redis-db-1     redis:alpine                      "docker-entrypoint.s…"   redis-db     14 seconds ago   Up 13 seconds   6379/tcp
multi_container_test-web-server-1   multi_container_test-web-server   "python app.py"           web-server   14 seconds ago   Up 13 seconds   0.0.0.0:5000->5000/tcp, [::]:5000->5000/tcp
```

## 3. 실시간 로그 모니터링

- 명령어 : `docker compose logs -f --tail 10`

컨테이너 내부에서 어떤 일이 일어나는지 들여다봅니다. (가장 중요한 디버깅 단계)
-f (Follow): 로그를 실시간으로 계속 출력합니다.
--tail 10: 너무 많은 로그 대신 마지막 10줄만 먼저 보여줍니다.
확인: 브라우저에서 새로고침을 누를 때마다 로그가 찍히는지 확인해 보세요! (중단하려면 Ctrl + C)

```bash
PS C:\Users\homec\Desktop\codyssey_mission1\app\multi_container_test> docker compose logs -f --tail 10 
redis-db-1    | 1:M 05 Nov 2026 12:54:28.744 * <ReJSON> Exported RedisJSON_V6 API
web-server-1  |  * Serving Flask app 'app'
web-server-1  |  * Debug mode: off
redis-db-1    | 1:M 05 Nov 2026 12:54:28.744 * <ReJSON> Exported RedisJSON_V7 API
web-server-1  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
web-server-1  |  * Running on all addresses (0.0.0.0)
web-server-1  |  * Running on http://127.0.0.1:5000
web-server-1  |  * Running on http://172.20.0.3:5000
web-server-1  | Press CTRL+C to quit
redis-db-1    | 1:M 05 Nov 2026 12:54:28.744 * <ReJSON> Exported RedisJSON_V8 API
redis-db-1    | 1:M 05 Nov 2026 12:54:28.744 * <ReJSON> Enabled diskless replication
redis-db-1    | 1:M 05 Nov 2026 12:54:28.744 * <ReJSON> Initialized shared string cache, thread safe: true.
redis-db-1    | 1:M 05 Nov 2026 12:54:28.744 * Module 'ReJSON' loaded from /usr/local/lib/redis/modules//rejson.so
redis-db-1    | 1:M 05 Nov 2026 12:54:28.744 * <search> Acquired RedisJSON_V8 API
redis-db-1    | 1:M 05 Nov 2026 12:54:28.745 * Server initialized
redis-db-1    | 1:M 05 Nov 2026 12:54:28.746 * Ready to accept connections tcp
redis-db-1    | 1:M 05 Nov 2026 12:54:28.746 # WARNING: Redis does not require authentication and is not protected by network restrictions. Redis will accept connections from any IP address on any network interface.
web-server-1  | 172.20.0.1 - - [05/Nov/2026 12:55:38] "GET / HTTP/1.1" 200 -
web-server-1  | 172.20.0.1 - - [05/Nov/2026 12:55:46] "GET / HTTP/1.1" 200 -
web-server-1  | 172.20.0.1 - - [05/Nov/2026 12:55:49] "GET / HTTP/1.1" 200 -
web-server-1  | 172.20.0.1 - - [05/Nov/2026 12:55:50] "GET / HTTP/1.1" 200 -
web-server-1  | 172.20.0.1 - - [05/Nov/2026 12:55:51] "GET / HTTP/1.1" 200 -
```

## 4. 컨테이너 정리

- 명령어 :`docker compose down`

컨테이너를 정지(Stop)시키는 것뿐만 아니라, 생성된 컨테이너와 네트워크를 모두 삭제하여 호스트 PC를 깨끗하게 유지합니다.

```bash
PS C:\Users\homec\Desktop\codyssey_mission1\app\multi_container_test> docker compose down             
[+] down 3/3
 ✔ Container multi_container_test-redis-db-1   Removed                                                                                                                                       0.2s
 ✔ Container multi_container_test-web-server-1 Removed                                                                                                                                       3.3s
 ✔ Network multi_container_test_default        Removed                                                                                                                                       0.2s
PS C:\Users\homec\Desktop\codyssey_mission1\app\multi_container_test> docker ps -a       
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
PS C:\Users\homec\Desktop\codyssey_mission1\app\multi_container_test> 
```

