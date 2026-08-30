# 🐙 Step-by-Step: Upload & Collaborate on GitHub (3 Members)

This guide walks all 3 team members through creating the repo, adding
collaborators, and contributing via branches + pull requests, so the
final commit history clearly shows each person's work.

---

## Step 1 — One member creates the repository

(Let's call this person **Member 1**, the "repo owner".)

1. Go to https://github.com and click **New repository**.
2. Repository name: `digital-queue-management-system`
3. Description: "Digital Queue Management System for Government Services — Python, OOP, File Handling"
4. Set to **Public** (or Private if your college requires it).
5. Check **Add a README file** → uncheck it if you already have the one from this project (avoid conflicts) — or check it and we'll merge later.
6. Add `.gitignore` template: choose **Python**, or skip it since we already have one.
7. Click **Create repository**.

## Step 2 — Add the other 2 members as collaborators

1. In the new repo, go to **Settings → Collaborators**.
2. Click **Add people**, and enter each teammate's GitHub username or email.
3. Both teammates will get an email invite — they must click **Accept**.

*(If your class requires an "Organization", create one instead under
github.com/organizations/new, add all 3 as members, and create the repo
inside the org — same steps otherwise.)*

## Step 3 — Everyone clones the repo locally

Each member runs this once:

```bash
git clone https://github.com/<owner-username>/digital-queue-management-system.git
cd digital-queue-management-system
```

## Step 4 — Add the project files (Member 1 only, first push)

Copy all the files from this project (`src/`, `tests/`, `README.md`,
`requirements.txt`, `.gitignore`, `GITHUB_SETUP_GUIDE.md`) into the
cloned folder, then:

```bash
git add .
git commit -m "Initial project scaffold: folder structure, README, gitignore"
git push origin main
```

The other two members now run `git pull origin main` to get this base.

## Step 5 — Each member works on their own branch

This is what makes the contribution graph show 3 distinct authors.

**Member 1 (OOP Module):**
```bash
git checkout -b feature/oop-models
# edit src/exceptions.py and src/models.py
git add src/exceptions.py src/models.py
git commit -m "Add Citizen, ServiceCounter, GovernmentQueueSystem classes and custom exceptions"
git push origin feature/oop-models
```

**Member 2 (File Handling Module):**
```bash
git checkout -b feature/file-handling
# edit src/file_manager.py
git add src/file_manager.py
git commit -m "Add FileManager: save/load citizens, activity logging, report export"
git push origin feature/file-handling
```

**Member 3 (Functions & Integration Module):**
```bash
git checkout -b feature/functions-integration
# edit src/utils.py, src/main.py, tests/test_queue.py
git add src/utils.py src/main.py tests/test_queue.py
git commit -m "Add input validation functions, CLI menu integration, and unit tests"
git push origin feature/functions-integration
```

## Step 6 — Open Pull Requests

For each branch:

1. Go to the repo on GitHub → you'll see a **"Compare & pull request"** banner for the just-pushed branch. Click it.
2. Base: `main` ← Compare: `feature/your-branch`
3. Add a short description of what the module does.
4. Tag a teammate as **Reviewer** (Settings gear icon on the right side of the PR page).
5. Click **Create pull request**.

## Step 7 — Review and merge

1. The reviewer opens the **Files changed** tab, reads the code, and leaves comments or approves.
2. Once approved, click **Merge pull request** → **Confirm merge**.
3. Click **Delete branch** (cleans up the branch list on GitHub).
4. Everyone runs `git checkout main && git pull origin main` to sync.

Repeat Steps 5–7 for any later changes/bug fixes — always branch → commit → PR → merge, never push directly to `main` once the base is set up.

## Step 8 — Final touches before submission

```bash
git checkout main
git pull origin main
git tag -a v1.0 -m "Final submission version"
git push origin v1.0
```

- Confirm all 3 usernames appear in **Insights → Contributors** on GitHub (this is what most instructors check).
- Make sure `README.md` is up to date and the repo link is ready to submit.

## Quick command reference

| Action | Command |
|---|---|
| Check current branch | `git status` |
| Switch to main | `git checkout main` |
| Create + switch to new branch | `git checkout -b feature/name` |
| Stage changes | `git add <file>` or `git add .` |
| Commit | `git commit -m "message"` |
| Push new branch | `git push origin feature/name` |
| Pull latest main | `git pull origin main` |
| See commit history | `git log --oneline --graph --all` |
