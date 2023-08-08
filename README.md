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

Step 16:	git rebase origin/main
warning: unable to rmdir 'freestyle_demo': Directory not empty
Successfully rebased and updated refs/heads/main.

Step 17:	git push origin main
Enumerating objects: 52, done.
Counting objects: 100% (52/52), done.
Delta compression using up to 8 threads
Compressing objects: 100% (47/47), done.
Writing objects: 100% (51/51), 9.10 KiB | 1.14 MiB/s, done.
Total 51 (delta 20), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (20/20), done.
To github.com:ChanikyaVarmaNalla/freestyle_demo.git
   a7612bd..c9854f5  main -> main
