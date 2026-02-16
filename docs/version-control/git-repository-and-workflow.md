# Git Repository and Workflow

## Overview
A Git repository is a project folder that Git tracks, containing your files plus a hidden `.git` directory that stores history and metadata. Understanding the three main areas—working directory, staging area, and commit history—makes daily Git actions (add, commit, push) clear and predictable.

## Definition
A **repository** (repo) is any directory that has been initialized with `git init` or obtained by cloning. Inside it, the **working directory** is the files you see and edit; the **staging area** (index) is what you have marked to include in the next commit; and the **commit history** is the immutable chain of snapshots you have already saved. Git commands move changes between these three areas.

## Key Concepts

- **Working directory**: The current state of your project files as you edit them. Not yet saved to history. `git status` shows which files are modified, new, or deleted here.
- **Staging area (index)**: A temporary holding area for changes that will go into the next commit. You add files with `git add`; only staged changes are committed.
- **Commit history**: The sequence of commits (snapshots) stored in `.git`. Each commit has a unique ID, a message, author, and parent(s). History is append-only; you don’t change past commits in normal workflow.
- **.git directory**: Hidden folder at the repo root. It holds objects (blobs, trees, commits), refs (branches, tags), and config. Never edit it by hand; use Git commands.
- **HEAD**: A reference to the current commit (and usually the current branch). When you commit, HEAD moves to the new commit.

## How It Works

1. **Edit**: You change files in the working directory. Git sees them as “modified” or “untracked.”
2. **Stage**: `git add <file>` (or `git add .`) copies the current state of those files into the staging area. You can add in several steps before committing.
3. **Commit**: `git commit -m "message"` takes everything in the staging area, creates a new snapshot, and moves HEAD (and the current branch) to that snapshot. The working directory and staging area are then clean for that commit.
4. **Repeat**: You keep editing, staging, and committing. Branches and remotes add more steps (push, pull, merge) on top of this loop.

## Use Cases

- **Understanding why nothing happens**: If you run `git commit` without having run `git add`, nothing is committed because the staging area is empty.
- **Partial commits**: Stage only some files or some hunks (`git add -p`) to build one commit that does one logical thing.
- **Inspecting state**: `git status` and `git diff` show the difference between working directory, staging area, and last commit.
- **Recovering**: You can undo a bad add with `git restore --staged <file>` and discard working changes with `git restore <file>` (before committing).

## Considerations

- **What gets committed**: Only tracked files that are staged. New files are untracked until you `git add` them. Ignored files (`.gitignore`) never appear as “to be committed.”
- **Commit size**: Small, logical commits are easier to review, revert, and bisect. One commit per “unit of work” is a good default.
- **No automatic save**: Until you commit, changes exist only in your working directory (and staging area). A crash or mistaken `git restore` can lose unstaged or uncommitted work.

## Best Practices

- Run `git status` often to see what’s modified, staged, or untracked.
- Stage and commit in small steps; use clear commit messages (what and why).
- Use `.gitignore` for build output, dependencies, and secrets so they never get staged.
- Before big changes, commit or stash so you have a clean state to return to.

## Related Topics

- [Git and GitHub](git-and-github.md)
- [Git Commit and Status](git-commit-and-status.md)
- [Git Clone and Remotes](git-clone-and-remotes.md)
- [Git Branches](git-branches.md)

---

**Category**: Version Control & Git  
**Last Updated**: 2025
