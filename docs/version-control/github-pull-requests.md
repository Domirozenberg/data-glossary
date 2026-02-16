# GitHub Pull Requests

## Overview
A pull request (PR) is GitHub’s way to propose merging one branch into another. You push a branch, open a PR against the target branch (e.g. `main`), add a description and optionally request reviewers. After discussion and approval, the PR is merged on GitHub, and the target branch is updated. PRs are the standard workflow for code review and controlled integration.

## Definition
A **pull request** is a GitHub (or GitLab/Bitbucket) feature that represents "please merge branch A into branch B." It shows the diff, allows comments on lines of code, supports review approvals and status checks, and performs the merge on the server when you click "Merge." The underlying Git operations (merge, or sometimes squash/rebase) are done by the platform; you don’t have to run `git merge` locally for the target branch unless you prefer to.

## Key Concepts

- **Branch-based**: You work on a branch (e.g. `feature/add-search`), push it to GitHub, then open a PR that targets `main` (or another branch). The PR compares the two branches and shows what would change.
- **Review**: Reviewers can comment on the whole PR or on specific lines. They can approve, request changes, or leave comments. Status checks (e.g. CI) can be required before merge.
- **Merge options**: When merging, GitHub can create a merge commit, squash all commits into one, or rebase. Squash is common for keeping `main` history simple; the PR’s commits become one commit on the target.
- **Closing**: Merging the PR closes it and updates the target branch. You can also close without merging (e.g. abandon the feature). Deleting the source branch after merge keeps the repo tidy.
- **Draft PR**: You can open a PR as "draft" to get early feedback without implying it’s ready to merge.

## How It Works

1. **Create branch and push**: Locally you run `git checkout -b feature/my-feature`, make commits, then `git push -u origin feature/my-feature`.
2. **Open PR**: On GitHub, you’ll see a prompt to "Compare & pull request" for the branch you just pushed. Click it, choose the base branch (e.g. `main`), add a title and description, optionally assign reviewers, and create the PR.
3. **Review and CI**: Reviewers comment; CI runs if configured. You push more commits to the same branch to address feedback; the PR updates automatically.
4. **Merge**: When satisfied, a reviewer (or you, if allowed) clicks "Merge," chooses the merge type (merge commit, squash, rebase), and confirms. The target branch is updated on GitHub.
5. **Sync locally**: Others (and you) run `git checkout main` and `git pull` to get the merged changes. You can delete the feature branch locally and on the remote.

## Use Cases

- **Code review**: Every change goes through a PR so someone else can review before it lands on `main`.
- **Documentation**: The PR description and comments document why a change was made and how it was reviewed.
- **CI/CD**: Require that tests (or other checks) pass before merge; the PR shows the status.
- **Open source**: Contributors fork the repo, push a branch, and open a PR against the upstream repo. Maintainers review and merge.
- **Deployment**: Many teams deploy only from `main`. Merging a PR triggers the deployment pipeline (e.g. Vercel) for the updated `main`.

## Considerations

- **Permissions**: Repo settings control who can open PRs, who can merge, and whether review or status checks are required. Branch protection on `main` often requires at least one approval and passing checks.
- **Conflicts**: If `main` has changed since you branched, the PR may show "merge conflicts." You resolve them by updating your branch (e.g. merge `main` into your branch or rebase), then push. The PR updates.
- **Size**: Keep PRs small and focused so they’re easier to review and merge. Split large features into several PRs.

## Best Practices

- Write a clear PR title and description: what changed, why, and how to test. Link issues if applicable.
- Request review from the right people; address feedback with new commits or comments.
- Keep the branch up to date with the target (merge or rebase `main` into your branch) to avoid last-minute conflicts.
- Delete the branch after merge unless you have a reason to keep it. Use "Delete branch" on the PR page or `git push origin --delete <branch>`.

## Related Topics

- [Git and GitHub](git-and-github.md)
- [Git Branches](git-branches.md)
- [Git Merge](git-merge.md)
- [Git Push and Pull](git-push-and-pull.md)
- [Git Clone and Remotes](git-clone-and-remotes.md)

---

**Category**: Version Control & Git  
**Last Updated**: 2025
