# Git & GitHub Commands Reference Guide

---

## 1. Initial Setup (Do Once)

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
git config --list
```

---

## 2. Clone Existing Repository

```bash
git clone https://github.com/username/repository.git
cd repository
```

---

## 3. Start New Project (Local → GitHub)

```bash
git init
git add .
git commit -m "Initial commit"

git remote add origin https://github.com/username/repository.git
git branch -M main
git push -u origin main
```

---

## 4. Check Status & History

```bash
git status
git log
git log --oneline --graph --all
```

---

# Branching Workflow

## Create and Switch to New Branch

```bash
git checkout -b feature-branch
```

## Switch Between Branches

```bash
git checkout main
git checkout feature-branch
```

## List Branches

```bash
git branch
```

## Delete Branch

```bash
git branch -d feature-branch
git branch -D feature-branch
```

---

## 5. Add & Commit Changes

```bash
git add filename.txt
git add .
git commit -m "Meaningful commit message"
git commit --amend
```

---

## 6. Push Branch to GitHub

```bash
git push -u origin feature-branch
```

---

## 7. Pull Latest Changes

```bash
git pull origin main
git pull
```

---

# Merge Branch into Main

```bash
git checkout main
git pull origin main
git merge feature-branch
git push origin main
```

---

## 8. Handle Merge Conflicts

After resolving conflicts manually:

```bash
git add .
git commit -m "Resolved merge conflicts"
```

---

## 9. Fetch vs Pull

```bash
git fetch origin
git diff main origin/main
```

---

## 10. Stash (Temporary Save Work)

```bash
git stash
git stash list
git stash apply
git stash pop
```

---

## 11. Reset & Revert

```bash
git reset filename.txt
git reset --soft HEAD~1
git reset --hard HEAD~1
git revert <commit_hash>
```

---

## 12. Remote Commands

```bash
git remote -v
git remote set-url origin new_url
```

---

## 13. Clean Workspace

```bash
git clean -f
git clean -fd
```

---

# Recommended Daily Feature Branch Workflow

```bash
git checkout main
git pull origin main
git checkout -b feature-name

# Make changes

git add .
git commit -m "Add feature"
git push -u origin feature-name

# Create Pull Request on GitHub

# After merge:
git checkout main
git pull origin main
git branch -d feature-name
```
