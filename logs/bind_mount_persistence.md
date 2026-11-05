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