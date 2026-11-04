# 컨테이너 실행 실습 상세 로그

## 1. hello-world 실행 결과
- **명령어**: `docker run hello-world`
- **결과**: "Hello from Docker!" 메시지 출력 확인 (성공)
```bash
PS C:\Users\homec\Desktop\codyssey_mission1> docker run hello-world           
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
4f55086f7dd0: Pull complete 
d5e71e642bf5: Download complete 
Digest: sha256:c567b231f65614688711a75f31518a064258a51d442117a3e771a3a8fdba78ef
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

```

## 2. ubuntu 컨테이너 내부 조작
- **명령어**: `docker run -it --name my-ubuntu ubuntu /bin/bash`
- **수행 내용**:
  - `ls`: 컨테이너 내부 루트 디렉토리 파일 확인
  - `echo`: 텍스트 출력 확인
- **결과**: 
```bash
PS C:\Users\homec\Desktop\codyssey_mission1> docker run -it --name my-ubuntu ubuntu /bin/bash
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
f3f25b84a7d7: Pull complete 
edafa32f5d9e: Pull complete 
21594acc2d8b: Download complete 
Digest: sha256:6a06111c3b0a8600feadb270aec771dc239bf407b25625f93f44ab00e11f4d3c
Status: Downloaded newer image for ubuntu:latest
root@629faa9de5d0:/# ls
bin   dev  home  lib64  mnt  proc  run   srv  tmp  var
boot  etc  lib   media  opt  root  sbin  sys  usr
root@629faa9de5d0:/# echo "Hello Ubuntu"
Hello Ubuntu
root@629faa9de5d0:/# exit
exit
```

## 3. exec , attach 실습
- **명령어**: `docker exec -it real-test /bin/bash`, `docker attach real-test`
- **수행 내용**:
  - `exec`: 실행 중인 컨테이너에 새 프로세스 실행 exec + exit: 컨테이너는 계속 실행됨. (기존 프로세스에 영향을 주지 않는 별도의 세션이기 때문)
  - `attach`: 실행 중인 메인 프로세스에 연결 attach + exit: 컨테이너가 함께 종료됨. (컨테이너를 실행시킨 메인 프로세스 자체를 종료시키기 때문)
- **결과**: 

```bash
PS C:\Users\homec\Desktop\codyssey_mission1> docker run -dit --name real-test ubuntu /bin/bash
fa2f83e9f770a37083e5a4c0d64e3ec48ef643f6b4b695246b8d8fa07f28ca2e
PS C:\Users\homec\Desktop\codyssey_mission1> docker ps -a                                     
CONTAINER ID   IMAGE     COMMAND       CREATED         STATUS         PORTS     NAMES
fa2f83e9f770   ubuntu    "/bin/bash"   8 seconds ago   Up 7 seconds             real-test
PS C:\Users\homec\Desktop\codyssey_mission1> docker exec -it real-test /bin/bash
root@fa2f83e9f770:/# exit
exit

PS C:\Users\homec\Desktop\codyssey_mission1> docker ps
CONTAINER ID   IMAGE     COMMAND       CREATED              STATUS              PORTS     NAMES
fa2f83e9f770   ubuntu    "/bin/bash"   About a minute ago   Up About a minute             real-test
PS C:\Users\homec\Desktop\codyssey_mission1> docker attach real-test     
root@fa2f83e9f770:/# exit
exit
PS C:\Users\homec\Desktop\codyssey_mission1> docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
PS C:\Users\homec\Desktop\codyssey_mission1> docker ps -a
CONTAINER ID   IMAGE     COMMAND       CREATED         STATUS                      PORTS     NAMES
fa2f83e9f770   ubuntu    "/bin/bash"   2 minutes ago   Exited (0) 10 seconds ago             real-test
```


