## 실습 환경 및 이슈 해결
- **문제 발생**: Windows 환경의 Git Bash에서 `chmod` 명령어가 실제 파일 권한에 반영되지 않는 문제 확인.
- **해결 방법**: Docker를 이용해 리눅스 환경(Alpine Linux) 컨테이너를 실행하여 실습을 진행함.

## 실습 로그 (Docker Container 내부)
### 1. 파일 권한 변경 (secret.txt)
- **명령어**: `chmod 600 secret.txt`
- **결과**: 
  - 전: `-rw-r--r--`
  - 후: `-rw-------`

### 2. 디렉토리 권한 변경 (private_dir)
- **명령어**: `chmod 777 private_dir`
- **결과**:
  - 전: `drwxr-xr-x`
  - 후: `drwxrwxrwx`

```powershell
PS C:\Users\homec\Desktop\codyssey_mission1> docker run -it --rm alpine sh                                      
Unable to find image 'alpine:latest' locally
latest: Pulling from library/alpine
7b229517ed22: Pull complete 
3ec36f3670df: Download complete 
3da1513d2124: Download complete 
Digest: sha256:be2656061b536c1883c4034790e21d0a09c5aaaf51968b89368a3c0371ea2c9a
Status: Downloaded newer image for alpine:latest
/ # mkdir /practice
/ # cd /practice
/practice # touch secret.txt
/practice # mkdir private_dir
/practice # ls -l
total 4
drwxr-xr-x    2 root     root          4096 Nov  3 10:53 private_dir
-rw-r--r--    1 root     root             0 Nov  3 10:52 secret.txt
/practice # chmod 600 secret.txt
/practice # chmod 777 private_dir
/practice # ls -l
total 4
drwxrwxrwx    2 root     root          4096 Nov  3 10:53 private_dir
-rw-------    1 root     root             0 Nov  3 10:52 secret.txt
/practice # 
```