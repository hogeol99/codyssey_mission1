# 커스텀 이미지 제작


## 1. 선택한 베이스 이미지
- **선택 방식**: (A) 웹 서버 베이스 이미지 활용
- **베이스 이미지**: nginx:latest (공식 Docker Hub 이미지)
[확인](../app/dockerfile)

## 2. 커스텀 포인트 및 목적
- **ENV 설정**: APP_OWNER 환경 변수를 추가하여 이미지 관리자 정보를 내부에 기록함.
- **COPY (콘텐츠 교체)**: 기본 NGINX 환영 페이지 대신 내가 직접 작성한 index.html을 출력하도록 설정함.
- **LABEL 추가**: 이미지의 용도를 설명하는 메타데이터를 추가하여 가독성을 높임.
[확인](../app/dockerfile)
- **커스텀 index.html 구성**:기본 Nginx 초기 화면을 대체하기 위해 작성된 커스텀 HTML 파일의 내용입니다.
[확인](../app/index.html)

## 3. 빌드 및 실행 결과
- **빌드 명령어**: `docker build -t my-custom-web:1.0 .`
- **실행 명령어**: `docker run -d -p 8080:80 --name my-web-container my-custom-web:1.0`
- **핵심 결과**:
docker images 명령 시 my-custom-web 리스트 확인됨.
브라우저에서 localhost:8080 접속 시 커스텀 페이지 정상 출력됨.

- **웹 페이지 확인**:
[확인](../images/web%20image.png)

[curl확인]
```bash
PS C:\Users\homec\Desktop\codyssey_mission1\app> curl http://localhost:8080
<!DOCTYPE html>
<html>
<head>
    <title>나의 커스텀 도커 서버</title>
    <meta charset="utf-8">
</head>
<body>
    <h1>안녕하세요! 도커 커스텀 이미지 빌드에 성공했습니다.</h1>
    <p>이 페이지는 NGINX 베이스 이미지에 제 파일을 넣어서 만든 것입니다.</p>
</body>
</html>
```


- **로그 확인** :
```bash
PS C:\Users\homec\Desktop\codyssey_mission1\app> docker build -t my-custom-web:1.0 .      
[+] Building 2.6s (8/8) FINISHED                                     docker:desktop-linux
 => [internal] load build definition from dockerfile                                 0.0s
 => => transferring dockerfile: 646B                                                 0.0s
 => [internal] load metadata for docker.io/library/nginx:latest                      2.2s
 => [auth] library/nginx:pull token for registry-1.docker.io                         0.0s
 => [internal] load .dockerignore                                                    0.0s
 => => transferring context: 2B                                                      0.0s
 => [internal] load build context                                                    0.0s
 => => transferring context: 375B                                                    0.0s
 => CACHED [1/2] FROM docker.io/library/nginx:latest@sha256:5ab5b0b01097420873a3f33  0.0s
 => => resolve docker.io/library/nginx:latest@sha256:5ab5b0b01097420873a3f3330f4424  0.0s
 => [2/2] COPY index.html /usr/share/nginx/html/index.html                           0.0s
 => exporting to image                                                               0.2s
 => => exporting layers                                                              0.0s
 => => exporting manifest sha256:85788d62828fadcbfa5109cccba9bc7fd3c1480ac41bb6abbd  0.0s
 => => exporting config sha256:a81a901849c1e4a358eae77268977e32707e6daa0142f2bcdd2b  0.0s
 => => exporting attestation manifest sha256:d79d0b61fa10121898576eea69fa390c26538f  0.0s
 => => exporting manifest list sha256:a5584bc7ccd2208dcab206bf5f08fff90e5880e9eae0a  0.0s
 => => naming to docker.io/library/my-custom-web:1.0                                 0.0s
 => => unpacking to docker.io/library/my-custom-web:1.0                              0.0s
PS C:\Users\homec\Desktop\codyssey_mission1\app> docker run -d -p 8080:80 --name my-web-container my-custom-web:1.0
68e49859168ad11b7d6520b1d8975e6a90c43798a7dc291780b587f1a43848e2
```


## 4. 변경한 LABEL, ENV 확인

- **실행 명령어**: `docker inspect --format='{{.Config.Labels.description}}' my-custom-web:1.0` , `docker inspect --format='{{.Config.Env}}' my-custom-web:1.0`

- **결과**:
```bash
PS C:\Users\homec\Desktop\codyssey_mission1\app> docker inspect --format='{{.Config.Labels.description}}' my-custom-web:1.0
나의 첫 번째 커스텀 웹 서버 이미지
PS C:\Users\homec\Desktop\codyssey_mission1\app> docker inspect --format='{{.Config.Env}}' my-custom-web:1.0               
[PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin NGINX_VERSION=1.31.8 NJS_VERSION=1.0.2 NJS_RELEASE=1~trixie ACME_VERSION=0.4.1 PKG_RELEASE=1~trixie DYNPKG_RELEASE=1~trixie APP_OWNER=KwonJiUn]
```

### 네트워크 네임스페이스 및 포트 포워딩 원리
네트워크 네임스페이스(Network Namespace):

Docker는 리눅스의 네트워크 네임스페이스 기술을 사용하여 각 컨테이너마다 독립적인 네트워크 스택(IP, 라우팅 테이블, 포트 등)을 부여합니다. 이를 통해 컨테이너들은 서로 충돌 없이 격리된 네트워크 환경에서 동작할 수 있습니다.
포트 포워딩(Port Forwarding)의 작동 원리:

컨테이너는 격리된 네트워크 안에 있기 때문에 외부에서 직접 접근할 수 없습니다. 따라서 **호스트의 특정 포트(8080)**와 **컨테이너의 포트(80)**를 연결(Mapping)하여, 호스트로 들어온 신호를 컨테이너 내부로 전달해 주는 가교 역할을 수행합니다.
