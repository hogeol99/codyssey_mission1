## git config --list 로그

```bash
PS C:\Users\homec\Desktop\codyssey_mission1> git config --list                            
diff.astextplain.textconv=astextplain
filter.lfs.clean=git-lfs clean -- %f
filter.lfs.smudge=git-lfs smudge -- %f
filter.lfs.process=git-lfs filter-process
filter.lfs.required=true
http.sslbackend=schannel
core.autocrlf=true
core.fscache=true
core.symlinks=false
pull.rebase=false
credential.helper=manager
credential.https://dev.azure.com.usehttppath=true
init.defaultbranch=master
user.name=hogeol99
user.email=home*********@gmail.com
core.repositoryformatversion=0
core.filemode=false
core.bare=false
core.logallrefupdates=true
core.symlinks=false
core.ignorecase=true
remote.origin.url=https://github.com/hogeol99/codyssey_mission1
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.main.remote=origin
branch.main.merge=refs/heads/main
(END)
```


## github 연동 증거 로그
```bash
PS C:\Users\homec\Desktop\codyssey_mission1> git remote -v    
origin  https://github.com/hogeol99/codyssey_mission1 (fetch)
origin  https://github.com/hogeol99/codyssey_mission1 (push)
PS C:\Users\homec\Desktop\codyssey_mission1> 
```

## github vscode 연동
[확인](../images/vscodetogit.png)

## git add, commit, push 과정 및 결과

```bash

PS C:\Users\homec\Desktop\codyssey_mission1> git add .           
PS C:\Users\homec\Desktop\codyssey_mission1> git commit -m "readme update"                  
[main 944e251] readme update
 1 file changed, 0 insertions(+), 0 deletions(-)
PS C:\Users\homec\Desktop\codyssey_mission1> git push origin main         
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 583 bytes | 194.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/hogeol99/codyssey_mission1
   efa96a7..944e251  main -> main
```