# Git Commit and Status

## Overview
Committing is how you save snapshots of your project in Git. Before committing, you stage changes with `git add`. The commands `git status` and `git diff` show what is modified, staged, or untracked so you always know what will be included in the next commit and what you might lose if you discard changes.

## Definition
A **commit** is a snapshot of the entire project at a point in time, identified by a hash, with a message and author. The **staging area** is the set of changes you have marked for the next commit. **Status** and **diff** report the state of your working directory and staging area relative to the last commit and to each other.

## Key Concepts

- **git add**: Moves changes from the working directory into the staging area. `git add <file>` stages that file; `git add .` stages all changes in the current directory (and below). You can run `git add` multiple times before one commit.
- **git commit**: Creates a new commit from whatever is currently staged. The message (e.g. `-m "Add feature X"`) is required for clarity. Commit only runs on staged content; unstaged changes are left in the working directory.
- **git status**: Shows which files are modified, staged, or untracked, and which branch you’re on. Use it often to avoid committing the wrong thing or forgetting to add files.
- **git diff**: Without arguments, shows unstaged changes (working directory vs staging area). With `--staged`, shows staged changes (staging area vs last commit). Helps you review exactly what will go into the next commit.
- **.gitignore**: A file listing patterns (e.g. `node_modules/`, `*.log`, `.env`) that Git should ignore. Ignored files never appear as “to be committed” and won’t be pushed.

## How It Works

1. **Edit files**: Changes appear as “modified” or “untracked” in `git status`.
2. **Stage**: `git add <files>` copies the current content of those files into the staging area. Status then shows them as “to be committed.”
3. **Review**: `git diff --staged` shows the exact diff that will be committed. Fix anything that shouldn’t be in this commit (e.g. unstage with `git restore --staged <file>`).
4. **Commit**: `git commit -m "message"` creates the snapshot from the staging area and moves the current branch (and HEAD) to that commit. The staging area is cleared; working directory matches the new commit unless you had unstaged changes.
5. **Repeat**: New changes show up again in status; add and commit again when you have another logical unit of work.

## Use Cases

- **Saving progress**: Small, frequent commits so work is saved and easy to describe.
- **Partial commits**: Stage only some files (or `git add -p` for partial hunks) to build one commit that does one thing.
- **Checking before commit**: `git status` and `git diff --staged` to avoid committing debug code, secrets, or unrelated changes.
- **Reverting mistakes**: Before commit: `git restore --staged <file>` to unstage; `git restore <file>` to discard working-directory changes. After commit: use `git revert` or other history commands.

## Considerations

- **Nothing to commit**: If you run `git commit` and see “nothing added to commit,” you didn’t stage anything. Run `git add` first.
- **Large or binary files**: Avoid committing build artifacts, dependencies, or huge binaries; add them to `.gitignore` and use a proper storage or dependency system.
- **Secrets**: Never commit passwords, API keys, or tokens. Use environment variables and `.gitignore` for any file that might contain secrets.

## Best Practices

- Write clear commit messages (what changed and why) in present tense (“Add login form” not “Added login form”).
- Run `git status` before and after add/commit to confirm what’s included.
- Use `.gitignore` for `node_modules/`, `dist/`, `.env`, and OS files (e.g. `.DS_Store`) so they never get staged.
- Prefer many small commits over one huge commit; they’re easier to review, revert, and bisect.

## Related Topics

- [Git Repository and Workflow](git-repository-and-workflow.md)
- [Git Push and Pull](git-push-and-pull.md)
- [Git Branches](git-branches.md)
- [Git and GitHub](git-and-github.md)

---

**Category**: Version Control & Git  
**Last Updated**: 2025
