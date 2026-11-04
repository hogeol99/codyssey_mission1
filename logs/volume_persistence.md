# Docker 볼륨 영속성 검증 실습

## 1. 실습 목적
컨테이너 삭제 후에도 데이터가 유지되는지 Docker Volume 기능을 통해 검증한다.

## 2. 검증 절차 및 명령어
1) **볼륨 생성**
   - `docker volume create my-db-data`
```bash
PS C:\Users\homec\Desktop\codyssey_mission1> docker volume create my-db-data
my-db-data
PS C:\Users\homec\Desktop\codyssey_mission1> docker volume ls               
DRIVER    VOLUME NAME
local     my-db-data
```
2) **데이터 생성 (Container 1)**
   - 명령어: `docker run -it --name container-1 -v my-db-data:/data alpine sh`
   - 작업: `/data/persistence.txt` 파일 생성 및 내용 작성
```bash
PS C:\Users\homec\Desktop\codyssey_mission1> docker run -it --name container-1 -v my-db-data:/data alpine sh   
Unable to find image 'alpine:latest' locally
latest: Pulling from library/alpine
7b229517ed22: Pull complete 
3da1513d2124: Download complete 
3ec36f3670df: Download complete 
Digest: sha256:be2656061b536c1883c4034790e21d0a09c5aaaf51968b89368a3c0371ea2c9a
Status: Downloaded newer image for alpine:latest
/ # cd /data
/data # echo "Volume Persistence Test - Success!" > persistence.txt
/data # ls
persistence.txt
/data # exit
```
3) **컨테이너 삭제**
   - 명령어: `docker rm -f container-1`
```bash
PS C:\Users\homec\Desktop\codyssey_mission1> docker rm -f container-1                     
container-1     
PS C:\Users\homec\Desktop\codyssey_mission1> docker ps -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```
4) **데이터 유지 확인 (Container 2)**
   - 명령어: `docker run -it --name container-2 -v my-db-data:/data alpine sh`
   - 결과: `cat /data/persistence.txt` 실행 시 이전 데이터가 동일하게 출력됨
```bash
PS C:\Users\homec\Desktop\codyssey_mission1> docker ps -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
PS C:\Users\homec\Desktop\codyssey_mission1> docker run -it --name container-2 -v my-db-data:/data alpine sh
/ # cat /data/persistence.txt
Volume Persistence Test - Success!
/ # exit
```

## 3. 최종 결과
- 컨테이너의 생명주기와 상관없이 볼륨에 저장된 데이터는 영구적으로 보존됨을 확인함.