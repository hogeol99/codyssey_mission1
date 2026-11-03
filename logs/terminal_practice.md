# 터미널 조작 실습 로그 (Terminal Operations)

이 문서는 과제 수행 중 진행한 기본적인 터미널 명령어 실습 기록입니다.

```powershell
PS C:\Users\homec\Desktop\codyssey_mission1> pwd

Path
----
C:\Users\homec\Desktop\codyssey_mission1

PS C:\Users\homec\Desktop\codyssey_mission1> ls -Force

    디렉터리: C:\Users\homec\Desktop\codyssey_mission1

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d--h-        2026-11-03  오후 4:42                .git
d----        2026-11-03  오후 4:39                app
d----        2026-11-03  오후 4:39                docs
d----        2026-11-03  오후 4:39                logs
-a---        2026-11-03  오후 4:40             60 READM
                                                  E.md

PS C:\Users\homec\Desktop\codyssey_mission1> New-Item test.txt -Type File                       

    디렉터리: C:\Users\homec\Desktop\codyssey_mission1

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---        2026-11-03  오후 5:09              0 test.
                                                  txt

PS C:\Users\homec\Desktop\codyssey_mission1> Set-Content test.txt -Value "Hello World"
PS C:\Users\homec\Desktop\codyssey_mission1> cat test.txt       
Hello World
PS C:\Users\homec\Desktop\codyssey_mission1> cp test.txt test_copy.txt
PS C:\Users\homec\Desktop\codyssey_mission1> mv test_copy.txt renamed.txt
PS C:\Users\homec\Desktop\codyssey_mission1> ls

    디렉터리: C:\Users\homec\Desktop\codyssey_mission1

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d----        2026-11-03  오후 4:39                app
d----        2026-11-03  오후 4:39                docs
d----        2026-11-03  오후 4:39                logs
-a---        2026-11-03  오후 4:40             60 READM
                                                  E.md
-a---        2026-11-03  오후 5:09             13 renam
                                                  ed.tx
                                                  t
-a---        2026-11-03  오후 5:09             13 test.
                                                  txt

PS C:\Users\homec\Desktop\codyssey_mission1> rm renamed.txt                         
PS C:\Users\homec\Desktop\codyssey_mission1> ls

    디렉터리: C:\Users\homec\Desktop\codyssey_mission1

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d----        2026-11-03  오후 4:39                app
d----        2026-11-03  오후 4:39                docs
d----        2026-11-03  오후 4:39                logs
-a---        2026-11-03  오후 4:40             60 READM
                                                  E.md
-a---        2026-11-03  오후 5:09             13 test.
                                                  txt

PS C:\Users\homec\Desktop\codyssey_mission1> mkdir practice              

    디렉터리: C:\Users\homec\Desktop\codyssey_mission1

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d----        2026-11-03  오후 5:29                pract
                                                  ice

PS C:\Users\homec\Desktop\codyssey_mission1> mv test.txt practice/       
PS C:\Users\homec\Desktop\codyssey_mission1> 
```