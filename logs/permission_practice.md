
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

```bash
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

### 리눅스 권한 숫자 표기법 (rwx) 설명
리눅스에서 권한은 읽기(r), 쓰기(w), 실행(x) 세 가지 비트의 조합으로 결정되며, 각 비트는 다음과 같은 숫자로 계산됩니다.

권한별 숫자 값:

r (read): 4
w (write): 2
x (execute): 1
- (none): 0
3자리 숫자의 의미:

첫 번째 자리: 소유자 (Owner) 권한
두 번째 자리: 그룹 (Group) 권한
세 번째 자리: 기타 사용자 (Others) 권한
주요 예시 설명:

600 (rw-------): 소유자만 읽기/쓰기 가능 (4+2=6), 나머지는 아무 권한 없음 (0). 실습에서 사용한 설정
755 (rwxr-xr-x): 소유자는 모든 권한(4+2+1=7), 그룹과 타인은 읽기 및 실행만 가능(4+1=5). 보통 실행 파일에 사용.
644 (rw-r--r--): 소유자는 읽기/쓰기(4+2=6), 그룹과 타인은 읽기만 가능(4). 보통 일반 문서 파일에 사용.