

### git ssh로 통신 연결 확인

```bash
PS C:\Users\homec\Desktop\codyssey_mission1> git remote -v       
origin  git@github.com:hogeol99/codyssey_mission1.git (fetch)
origin  git@github.com:hogeol99/codyssey_mission1.git (push)
```

- https : 웹 페이지 및 웹 기반 리소스 송수신, 별도 키 생성없이 바로 사용가능하나 반복 인증 필요, 개인 액세스 토큰 입력방식

- ssh : 원격 서버에 안전하게 로그인 및 제어, 한번 세팅하면 로그인 정보 입력 없이 안전하게 접속 가능, 로컬과 서버에 등록된 ssh키 쌍으로 통신