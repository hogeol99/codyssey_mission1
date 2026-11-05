
# Compose를 활용한 container 생성및 포트 연결

## compose 방식 장점

- 문서화: 파일 자체가 실행 옵션(포트, 볼륨, 환경변수 등)을 기록한 문서가 됩니다.
- 버전 관리: 이 파일을 Git에 올리면 팀원 누구나 똑같은 환경을 1초 만에 구축할 수 있습니다.
- 휴먼 에러 방지: 긴 명령어를 치다가 오타를 낼 일이 없습니다.

## yml파일을 통한 container 생성

- [yml 파일 확인](../app/compose_practice/docker-compose.yml)

- `docker compose up -d`

```bash
PS C:\Users\homec\Desktop\codyssey_mission1\app\compose_practice> docker compose up -d
[+] up 2/2
 ✔ Network compose_practice_default    Created                                                                                                                                               0.1s
 ✔ Container compose_practice-my-web-1 Started                                                                                                                                               1.1s
 ```

 ## curl로 웹페이지 확인
 ```bash
PS C:\Users\homec\Desktop\codyssey_mission1\app\compose_practice> curl http://localhost:8080
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, nginx is successfully installed and working.
Further configuration is required for the web server, reverse proxy, 
API gateway, load balancer, content cache, or other features.</p>

<p>For online documentation and support please refer to
<a href="https://nginx.org/">nginx.org</a>.<br/>
To engage with the community please visit
<a href="https://community.nginx.org/">community.nginx.org</a>.<br/>
For enterprise grade support, professional services, additional 
security features and capabilities please refer to
<a href="https://f5.com/nginx">f5.com/nginx</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```
