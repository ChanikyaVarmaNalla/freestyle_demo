# freestyle_demo
This is my Jenkins freestyle demo git

# These are the steps I followed
Step 1:	git init

Step 2:	ssh-keygen -t ed25519 -C "nchanikyavarma04@gmail.com"

Step 3:	set the ssh key in github.com

Step 4:	git clone git@github.com:ChanikyaVarmaNalla/freestyle_demo.git

Step 5:	git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        Git Steps.txt
        free_demo/
        freestyle_demo/

nothing added to commit but untracked files present (use "git add" to track)

Step 6:	git add .

Step 7:	git commit -m "First Commit"

Step 8:	git status
git status
On branch master
nothing to commit, working tree clean

Step 9:	git remote -v	empty

Step 10:	git remote add origin git@github.com:ChanikyaVarmaNalla/freestyle_demo.git		Done

Step 11:	git remote -v
origin  git@github.com:ChanikyaVarmaNalla/freestyle_demo.git (fetch)
origin  git@github.com:ChanikyaVarmaNalla/freestyle_demo.git (push)

Step 12:	git branch
* master

Step 13:	git checkout -b main		Switched to a new branch 'main'

Step 15:	git push origin main
To github.com:ChanikyaVarmaNalla/freestyle_demo.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'github.com:ChanikyaVarmaNalla/freestyle_demo.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

Step 16:	git fetch origin main
remote: Enumerating objects: 8, done.
remote: Counting objects: 100% (8/8), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 6 (delta 3), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (6/6), 2.21 KiB | 151.00 KiB/s, done.
From github.com:ChanikyaVarmaNalla/freestyle_demo
 * branch            main       -> FETCH_HEAD
   1a56163..ddb4f29  main       -> origin/main

Step 17:  git merge origin/main
Merge made by the 'ort' strategy.
 README.md | 69 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 69 insertions(+)

Step 18:	git push origin main
Enumerating objects: 52, done.
Counting objects: 100% (52/52), done.
Delta compression using up to 8 threads
Compressing objects: 100% (47/47), done.
Writing objects: 100% (51/51), 9.10 KiB | 1.14 MiB/s, done.
Total 51 (delta 20), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (20/20), done.
To github.com:ChanikyaVarmaNalla/freestyle_demo.git
   a7612bd..c9854f5  main -> main


Task 5 Processes

Step1 : docker build -t task5 .

Step2 : docker images		to check if the image is build or not
REPOSITORY                           TAG       IMAGE ID       CREATED        SIZE
chanikyavarmanalla/my-docker-image   latest    076ab9f84862   7 hours ago    1.1GB
task5                                latest    076ab9f84862   7 hours ago    1.1GB
my-build-image-2                     latest    dbe66247efdb   28 hours ago   1.1GB
my-build-image-3                     latest    dbe66247efdb   28 hours ago   1.1GB
my-build-image-1                     latest    727f7e13fc39   28 hours ago   998MB
my-build-image                       latest    99ecbb644815   29 hours ago   1.23GB

Step3 : docker tag task5 chanikyavarmanalla/task5:latest

Step4 : docker push chanikyavarmanalla/task5:latest
The push refers to repository [docker.io/chanikyavarmanalla/task5]
cfa2010ad0d1: Mounted from chanikyavarmanalla/my-docker-image
5f70bf18a086: Mounted from chanikyavarmanalla/my-docker-image
f894ad2945e1: Mounted from chanikyavarmanalla/my-docker-image
9f675dc32926: Mounted from chanikyavarmanalla/my-docker-image
efb139f3f261: Mounted from chanikyavarmanalla/my-docker-image
a85edf4c031f: Mounted from chanikyavarmanalla/my-docker-image
7788a8bbe052: Mounted from chanikyavarmanalla/my-docker-image
3440999c544b: Mounted from chanikyavarmanalla/my-docker-image
c5f1d4dd95f0: Mounted from chanikyavarmanalla/my-docker-image
6a25221bdf24: Mounted from chanikyavarmanalla/my-docker-image
b578f477cd5d: Mounted from chanikyavarmanalla/my-docker-image
b298f9991a11: Mounted from chanikyavarmanalla/my-docker-image
c94dc8fa3d89: Mounted from chanikyavarmanalla/my-docker-image
latest: digest: sha256:79bac7ebddaf2d95679bd388f8c12b04412c7856f17e170cbd6d018e3ab208e1 size: 3054

Step5 : docker rmi task5
Untagged: task5:latest

Step6 : docker images
REPOSITORY                           TAG       IMAGE ID       CREATED        SIZE
chanikyavarmanalla/my-docker-image   latest    076ab9f84862   8 hours ago    1.1GB
chanikyavarmanalla/task5             latest    076ab9f84862   8 hours ago    1.1GB
my-build-image-2                     latest    dbe66247efdb   28 hours ago   1.1GB
my-build-image-3                     latest    dbe66247efdb   28 hours ago   1.1GB
my-build-image-1                     latest    727f7e13fc39   28 hours ago   998MB
my-build-image                       latest    99ecbb644815   29 hours ago   1.23GB

Step7 : docker pull chanikyavarmanalla/task5:latest
latest: Pulling from chanikyavarmanalla/task5
Digest: sha256:79bac7ebddaf2d95679bd388f8c12b04412c7856f17e170cbd6d018e3ab208e1
Status: Image is up to date for chanikyavarmanalla/task5:latest
docker.io/chanikyavarmanalla/task5:latest

What's Next?
  View summary of image vulnerabilities and recommendations → docker scout quickview chanikyavarmanalla/task5:latest

Step8 : docker images
REPOSITORY                           TAG       IMAGE ID       CREATED        SIZE
chanikyavarmanalla/my-docker-image   latest    076ab9f84862   8 hours ago    1.1GB
chanikyavarmanalla/task5             latest    076ab9f84862   8 hours ago    1.1GB
my-build-image-2                     latest    dbe66247efdb   28 hours ago   1.1GB
my-build-image-3                     latest    dbe66247efdb   28 hours ago   1.1GB
my-build-image-1                     latest    727f7e13fc39   28 hours ago   998MB
my-build-image                       latest    99ecbb644815   29 hours ago   1.23GB

Step9 : docker run chanikyavarmanalla/task5:latest
Factorial = 120