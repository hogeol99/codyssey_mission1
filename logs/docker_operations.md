# Docker 기본 운영 실습 로그

## 1. 이미지(Image) 조작
- **명령어**: `docker pull nginx` / `docker images`
- **결과**:
```bash
# 이미지 목록 확인 결과
PS C:\Users\homec\Desktop\codyssey_mission1> docker pull nginx
Using default tag: latest
latest: Pulling from library/nginx
Digest: sha256:5ab5b0b01097420873a3f3330f44248e34a3c2a3e8d5ee30658aeae8cb7435da
Status: Downloaded newer image for nginx:latest
docker.io/library/nginx:latest
PS C:\Users\homec\Desktop\codyssey_mission1> docker images    
                                                                                                                                                                            i Info →   U  In Use
IMAGE          ID             DISK USAGE   CONTENT SIZE   EXTRA
nginx:latest   5ab5b0b01097        243MB         66.8MB        
PS C:\Users\homec\Desktop\codyssey_mission1> 
```

## 2. 컨테이너(Container) 실행 및 조회
- **명령어**: `docker run -d --name my-web nginx` / `docker ps`
- **결과**:
```bash
PS C:\Users\homec\Desktop\codyssey_mission1> docker run -d --name my-web nginx
f1041a6f1459b90dfbbf01cb24868cf2ba3482c7a5a2cf0003fe44347b2487a3
# 실행 중인 컨테이너 확인
PS C:\Users\homec\Desktop\codyssey_mission1> docker ps
CONTAINER ID   IMAGE     COMMAND                   CREATED         STATUS         PORTS     NAMES
f1041a6f1459   nginx     "/docker-entrypoint.…"   5 seconds ago   Up 4 seconds   80/tcp    my-web
PS C:\Users\homec\Desktop\codyssey_mission1> 
```
## 3. 운영(Operations) 및 모니터링
- **로그 확인** (`docker logs my-web`):
```bash
PS C:\Users\homec\Desktop\codyssey_mission1> docker logs my-web
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2026/11/03 12:00:50 [notice] 1#1: using the "epoll" event method
```
- **리소스 확인** (`docker stats`):
```bash
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O         BLOCK I/O         PIDS
f1041a6f1459   my-web    0.00%     10.9MiB / 7.65GiB   0.14%     1.17kB / 126B   16.5MB / 12.3kB   9
# 종료시 ctrl + c 혹은 docker stats --no-stream 사용시 실행 후 바로 종료됨 
```
## 4. 컨테이너 중지 및 종료 확인
- **명령어** : `docker stop my-web` / `docker ps -a`
결과:
```bash
PS C:\Users\homec\Desktop\codyssey_mission1> docker stop my-web
my-web
PS C:\Users\homec\Desktop\codyssey_mission1> docker ps -a      
CONTAINER ID   IMAGE     COMMAND                   CREATED         STATUS                     PORTS     NAMES
f1041a6f1459   nginx     "/docker-entrypoint.…"   7 minutes ago   Exited (0) 6 seconds ago             my-web
```