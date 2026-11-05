### 4.7.2 바인드 마운트(Bind Mount) 실습 로그

**1. 호스트 디렉토리 생성 및 컨테이너 연결**
- 호스트 경로: `~/moby-counter`
- 컨테이너 경로: `/app`
```bash
PS C:\Users\homec\Desktop\codyssey_mission1> mkdir -p ~/moby-counter                                  

    디렉터리: C:\Users\homec

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d----        2026-11-04  오후 7:46                moby-counter

PS C:\Users\homec\Desktop\codyssey_mission1> docker run -d -it --name bind-test-container -v ~/moby-counter:/app alpine sh
e0bb9f2a88c6a08c7692cac827e919029b752b3be6bb9b4591359f4de20bdb51

```
**2. 컨테이너 내부에서 데이터 생성**
```bash
PS C:\Users\homec\Desktop\codyssey_mission1> docker exec bind-test-container sh -c "echo 'hello from container' > /app/test.txt"

**3. 호스트 시스템에서 데이터 동기화 확인**
```bash
PS C:\Users\homec\Desktop\codyssey_mission1> cat ~/moby-counter/test.txt
hello from container
```
**4. 컨테이너 삭제 후 데이터 유지 검증**

컨테이너를 삭제해도 호스트의 절대 경로에 데이터가 남아있는지 확인합니다.
```bash
PS C:\Users\homec\Desktop\codyssey_mission1> docker rm -f bind-test-container                                   
bind-test-container
PS C:\Users\homec\Desktop\codyssey_mission1> docker run --rm -v ~/moby-counter:/app alpine cat /app/test.txt
hello from container
```

5. 바인드 마운트 특징 요약

장점: 호스트의 특정 파일이나 폴더를 직접 공유하므로, 소스 코드 수정 시 실시간 반영이 필요한 개발 환경에 유리함.
단점: 호스트의 특정 절대 경로를 지정해야 하므로, OS가 다르거나 경로 구조가 다른 환경에서는 재현성이 떨어짐.

###  도커 바인드 마운트: 절대경로 vs 상대경로 선택 기준 및 재현성

도커에서 호스트의 디렉토리를 컨테이너에 연결(바인드 마운트)할 때, 호스트 경로를 지정하는 방식에 따라 프로젝트의 **재현성(Reproducibility)**에 큰 영향을 미칩니다.

#### 1. 절대경로 (Absolute Path)
- **예시:** `/Users/myname/workspace/project/data:/app/data`
- **선택 기준:** 특정 서버나 PC의 고정된 시스템 경로(예: `/var/log`, 공용 백업 디렉토리)를 연결해야 할 때 사용합니다.
- **재현성에 미치는 영향 (낮음):** 경로가 특정 호스트의 환경(OS, 사용자 이름 등)에 강하게 종속됩니다. 다른 개발자가 이 코드를 받아 실행하면 해당 경로가 존재하지 않아 **마운트 에러가 발생하며 재현성이 깨집니다.**

#### 2. 상대경로 (Relative Path)
- **예시:** `./data:/app/data`
- **선택 기준:** 프로젝트 폴더 내부에 있는 소스 코드나 설정 파일, 프로젝트 종속 데이터를 연결할 때 사용합니다.
- **재현성에 미치는 영향 (높음):** 현재 작업 디렉토리를 기준으로 하므로, 다른 개발자가 `git clone`을 받아 어느 위치에 저장하든 동일하게 작동합니다. **팀 협업 및 CI/CD 환경에서 완벽한 재현성을 보장합니다.**

####  결론 및 Best Practice
프로젝트를 깃허브에 공유하고 팀원들과 협업하는 환경에서는 **반드시 상대경로(`./`)를 사용**하는 것이 원칙입니다. 특히 `docker-compose.yml` 파일 내에서 상대경로를 사용하면, 누구나 명령어 한 줄(`docker-compose up`)로 동일한 환경을 100% 재현할 수 있습니다.