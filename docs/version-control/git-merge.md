# Git Merge

## Overview
Merging combines the work from two branches into one. You typically merge a feature or fix branch into `main` (or another target) so that the target branch includes all commits from both lines. Git can do a fast-forward merge when one branch is strictly ahead, or create a merge commit when both branches have new commits.

## Definition
**Merge** is the process of integrating the history of another branch into the current branch. The result is either a **fast-forward** (the current branch pointer simply moves to the tip of the other branch, no new commit) or a **merge commit** (a new commit with two parents that ties both histories together). **Merge conflicts** occur when the same lines were changed in both branches; you must resolve them before completing the merge.

## Key Concepts

- **Fast-forward merge**: When the current branch (e.g. `main`) has no new commits since the other branch (e.g. `feature/x`) diverged, Git can "fast-forward" by moving `main` to point at the same commit as `feature/x`. No merge commit is created.
- **Merge commit**: When both branches have new commits, Git creates a new commit that has two parents—the previous tip of the current branch and the tip of the merged branch. That commit represents "branch x merged into main."
- **Merge conflict**: If the same part of a file was changed in both branches, Git can’t decide automatically. It marks the file as conflicted and inserts conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`). You edit the file to choose the correct content, then `git add` and `git commit` to finish the merge.
- **git merge**: Run from the branch that should receive the changes (e.g. `main`). Example: `git checkout main` then `git merge feature/login`. Git brings `feature/login`’s commits into `main`.

## How It Works

1. **Prepare**: Switch to the branch that should get the merge (e.g. `main`). Ensure it’s up to date (e.g. `git pull`).
2. **Merge**: Run `git merge <branch-to-merge>`. Git finds the common ancestor and applies the other branch’s commits.
3. **Fast-forward or merge commit**: If possible, Git does a fast-forward; otherwise it creates a merge commit (unless you pass `--no-ff` to force a merge commit).
4. **Conflicts**: If there are conflicts, Git stops and lists the conflicted files. Open each file, remove the markers, fix the content, then `git add` the file and run `git commit` (no message needed for a merge commit, or add one with `-m`).
5. **After merge**: The current branch now includes all work from both. You can delete the merged branch if it’s no longer needed and push the result.

## Use Cases

- **Finishing a feature**: Merge `feature/login` into `main` so the main line has the new login code.
- **Pulling updates**: When you run `git pull`, Git fetches and then merges the remote branch (e.g. `origin/main`) into your current branch; that merge can be fast-forward or a merge commit.
- **Combining parallel work**: Two people worked on different branches; merge one into the other (or both into `main`) to combine the work. Resolve any conflicts once.
- **Keeping main stable**: Merge only after review (e.g. via pull request) so main always reflects tested or approved changes.

## Considerations

- **Conflict resolution**: Take care when resolving conflicts; wrong choices can drop or duplicate code. Review the full file after fixing.
- **Merge vs rebase**: Merge preserves the exact history (including merge commits). Rebasing rewrites history to look linear; it’s powerful but can complicate shared branches. For most workflows, merging is simpler and safe.
- **Deleting the merged branch**: After merging, the branch (e.g. `feature/login`) is redundant unless you keep it for reference. Delete it locally with `git branch -d feature/login` and on the remote with `git push origin --delete feature/login` if applicable.

## Best Practices

- Merge into the target branch from the source branch (e.g. `git checkout main` then `git merge feature/x`).
- Before merging, update the target (e.g. pull on `main`) and ensure the source branch is built and tested.
- Resolve conflicts promptly; don’t leave the repo in a conflicted state. Use `git status` to see conflicted files.
- Prefer small, focused branches so merges are straightforward and conflicts are rare.

## Related Topics

- [Git Branches](git-branches.md)
- [Git Push and Pull](git-push-and-pull.md)
- [GitHub Pull Requests](github-pull-requests.md)
- [Git Repository and Workflow](git-repository-and-workflow.md)
- [Git and GitHub](git-and-github.md)

---

**Category**: Version Control & Git  
**Last Updated**: 2025
