# Git Branches

## Overview
A branch is a movable pointer to a commit. You use branches to work on features or fixes without changing the main line (e.g. `main`). Creating, switching, and merging branches is central to both solo and team workflows and keeps history organized.

## Definition
A **branch** is a named reference that points to a commit and moves forward when you make new commits on that branch. The default branch is often `main` or `master`. **Checking out** or **switching** to a branch updates your working directory to match that branch’s tip and sets HEAD to that branch so new commits extend it.

## Key Concepts

- **Branch as pointer**: A branch is just a name pointing at a commit. When you commit, the current branch moves to the new commit; other branches stay where they were.
- **HEAD**: Usually points at the current branch (which in turn points at a commit). "Detached HEAD" means HEAD points directly at a commit, not a branch—fine for looking around, but new commits won’t be on any branch unless you create one.
- **Create branch**: `git branch <name>` creates a new branch at the current commit; it doesn’t switch to it. `git checkout -b <name>` (or `git switch -c <name>`) creates and switches in one step.
- **Switch branch**: `git checkout <name>` or `git switch <name>` changes the working directory to match that branch and sets HEAD to it. You must commit or stash uncommitted changes first if they would be overwritten.
- **List branches**: `git branch` lists local branches; `git branch -a` includes remote-tracking branches (e.g. `remotes/origin/main`).
- **Default branch**: The branch you get after clone (e.g. `main`). New repos often create it on first commit; remotes expose it so pull requests and deployments target it by default.

## How It Works

1. **Start from main**: You’re on `main`. Create a branch: `git checkout -b feature/login`. You’re now on `feature/login`; HEAD and that branch point at the same commit as `main`.
2. **Work and commit**: Each commit moves `feature/login` (and HEAD) forward. `main` stays where it was.
3. **Switch back**: `git checkout main` puts you on `main`; your working directory matches the last commit on `main`. The commits on `feature/login` are still there.
4. **Merge later**: When the feature is ready, you merge `feature/login` into `main` (see Git Merge). Then you can delete the feature branch and push `main`.

## Use Cases

- **Feature work**: One branch per feature or fix so `main` stays stable and you can switch context.
- **Experiments**: Try something on a branch; if it doesn’t work out, switch back to `main` and delete the branch. No impact on main.
- **Collaboration**: Everyone pushes branches; you open a pull request to merge a branch into `main` (or another target) after review.
- **Release lines**: Some teams keep a `main` plus long-lived branches like `release/2.x` for bugfixes; the same concepts apply.

## Considerations

- **Uncommitted changes**: Git won’t switch branches if you have modified files that would be overwritten. Commit or stash first.
- **Remote branches**: When you push a new branch with `git push -u origin <branch>`, the remote gets that branch and your local one can track it. Deleting a branch locally doesn’t delete it on the remote unless you run `git push origin --delete <branch>`.
- **Branch names**: Use short, clear names (e.g. `feature/add-search`, `fix/login-redirect`). Avoid special characters and spaces.

## Best Practices

- Keep `main` (or your default branch) in a good state; merge only tested or reviewed work.
- Create a branch for each logical unit of work; delete the branch after merge to keep the list tidy.
- Use `git switch` and `git restore` (newer) or `git checkout` (older) as you prefer; the important thing is to commit or stash before switching when you have uncommitted changes.
- Push branches when you want backup or to open a pull request; set upstream with `-u` on first push.

## Related Topics

- Git Repository and Workflow
- Git Merge
- GitHub Pull Requests
- Git Push and Pull
- Git and GitHub

---

**Category**: Version Control & Git  
**Last Updated**: 2025
