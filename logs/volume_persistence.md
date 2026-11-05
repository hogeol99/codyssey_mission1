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

## 4.데이터 백업 및 관리 전략

### 1. docker cp 사용

가장 직관적인 방법으로, 컨테이너 내부의 데이터를 호스트 컴퓨터로 직접 복사하는 방식

```bash
# 컨테이너의 /app/logs 데이터를 현재 폴더의 backup 폴더로 복사
docker cp my_container:/app/logs ./backup_logs
```

- 장점: 별도의 설정 없이 즉시 실행 가능합니다.
- 단점: 매번 수동으로 실행해야 하므로 자동화가 어렵습니다.

### 2. 임시 컨테이너를 이용한 압축

Docker 볼륨 전체를 압축 파일로 만들어 보관하는 가장 권장되는 방식

```bash
docker run --rm --volumes-from [대상_컨테이너] -v $(pwd):/backup ubuntu tar cvf /backup/backup.tar [데이터_경로]
```
--volumes-from: 백업할 볼륨을 가진 컨테이너에 연결합니다.
-v $(pwd):/backup: 현재 호스트 경로를 컨테이너의 /backup에 마운트합니다.
tar cvf: 데이터를 하나로 묶어 압축 파일을 생성합니다.
--rm: 작업이 끝나면 임시로 쓴 컨테이너를 자동으로 삭제합니다.