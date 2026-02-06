# Git Push and Pull

## Overview
Push sends your local commits to a remote repository (e.g. GitHub); pull brings remote changes into your local repo and updates your current branch. Together they keep your machine and the server in sync. Understanding fetch, upstream tracking, and when to pull before push avoids "rejected" updates and lost work.

## Definition
**Push** uploads commits from your local branch to a remote branch. **Pull** is shorthand for "fetch from the remote, then merge the tracked remote branch into the current branch." **Fetch** only downloads new commits and updates remote-tracking refs (e.g. `origin/main`); it does not change your working files until you merge or pull.

## Key Concepts

- **git push**: `git push <remote> <branch>` (e.g. `git push origin main`) sends your local commits for that branch to the remote. The remote must accept the update; if someone else pushed first, you’ll be rejected until you pull (or fetch and merge) and try again.
- **git pull**: `git pull <remote> <branch>` (or just `git pull` if tracking is set) runs `git fetch` then merges the remote branch into your current branch. It can create a merge commit if histories have diverged.
- **git fetch**: Downloads new commits and refs from the remote but does not change your current branch or working directory. You can then inspect with `git log origin/main` and merge when ready.
- **Upstream (tracking)**: A local branch can "track" a remote branch (e.g. `main` tracks `origin/main`). Then `git push` and `git pull` without arguments use that remote and branch. Set with `git push -u origin main` the first time you push.
- **Rejected push**: If the remote has commits you don’t have, push is rejected. Pull (or fetch and merge) to integrate those commits, then push again.

## How It Works

1. **After you commit locally**: Your branch is ahead of the remote. `git push origin main` uploads your new commits; the remote’s `main` now matches yours (assuming no one else pushed).
2. **When others have pushed**: The remote is ahead of you. `git pull` (or `git fetch` then `git merge origin/main`) brings their commits into your branch. Resolve any merge conflicts, then push.
3. **Divergent history**: If you and someone else both committed on the same branch, pull will merge, often creating a merge commit. Then push. Alternatively you can rebase (advanced) to keep a linear history.
4. **First push of a new branch**: Use `git push -u origin <branch-name>` so the local branch tracks the new remote branch; later you can just `git push` and `git pull`.

## Use Cases

- **Backing up work**: Push regularly so your commits are on GitHub (or another server) and safe from local loss.
- **Collaboration**: Pull before starting work to get teammates’ changes; push when your feature is ready so others can pull.
- **Deployment**: Services like Vercel watch a branch (e.g. `main`); every push to that branch triggers a new build and deploy.
- **Safer update**: Use `git fetch` then `git log origin/main` to see what’s new before merging; then `git merge origin/main` (or pull) when you’re ready.

## Considerations

- **Pull before push**: Get into the habit of pulling (or at least fetching) before you push so you don’t get rejected and so you integrate others’ work early.
- **Merge commits**: Pull can create a merge commit if both you and the remote have new commits. That’s normal; you can push the result. If you prefer a linear history, use rebase (advanced).
- **Force push**: `git push --force` overwrites the remote branch with your local one. Use only on branches you own (e.g. a feature branch); never force-push shared branches like `main` unless you’re sure.

## Best Practices

- Set upstream on first push: `git push -u origin main` so later you can use `git push` and `git pull` without typing the remote and branch.
- Pull (or fetch and merge) before starting work and before pushing to avoid rejections and merge surprises.
- Push often so your work is backed up and visible to CI/CD or teammates.
- If push is rejected, don’t force push without understanding why; pull, resolve any conflicts, then push.

## Related Topics

- Git Clone and Remotes
- Git Commit and Status
- Git Branches
- Git Merge
- Git and GitHub

---

**Category**: Version Control & Git  
**Last Updated**: 2025
