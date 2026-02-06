# Git and GitHub

## Overview
Git is a distributed version control system that tracks changes in files and coordinates work across copies of a project. GitHub is a hosted service built on Git that provides remote repositories, collaboration features, and integration with tools like CI/CD and project management. Together they are the standard way to store code, collaborate, and deploy applications.

## Definition
**Git** is open-source software that maintains a history of changes (commits) in a **repository** (repo) and supports branching, merging, and syncing between local and remote copies. **GitHub** is a platform that hosts Git repositories on the internet, adds pull requests, issues, Actions, and access control, and is often used as the "source of truth" for teams and for deployment (e.g. Vercel, Netlify).

## Key Concepts

- **Repository (repo)**: A project folder whose history Git tracks. Can exist only on your machine (local) or on a server (remote, e.g. GitHub).
- **Commit**: A saved snapshot of changes with a message. The history of commits forms the project timeline.
- **Branch**: A parallel line of work. The default branch is often `main`. You create branches for features or fixes, then merge them.
- **Remote**: A reference to a repo hosted elsewhere (e.g. `origin` pointing to GitHub). You push and pull to sync.
- **Clone**: Copy a remote repo to your machine. You clone once; afterward you pull and push.
- **Push**: Send your local commits to a remote (e.g. `git push origin main`).
- **Pull**: Bring remote changes into your local repo (e.g. `git pull origin main`).
- **SSH vs HTTPS**: Two ways to authenticate with GitHub. SSH uses a key pair (no password each time); HTTPS uses a username and token or credential helper.

## How It Works

1. **Local workflow**: You edit files, then `git add` and `git commit` to record snapshots. Branches let you try changes without touching `main`.
2. **Syncing with GitHub**: You add a remote (`git remote add origin <url>`). `git push` uploads your commits; `git pull` (or `git fetch` then merge) downloads others’ changes.
3. **Multiple machines / accounts**: You can use different remotes or different SSH keys (e.g. one host for work, one for personal) so the right identity is used per repo.
4. **Deployment**: Services like Vercel connect to your GitHub repo, run a build on each push, and publish the result. The repo URL and branch (e.g. `main`) are what you configure.

## Use Cases

- **Personal projects**: Keep code on GitHub, push from your laptop, deploy from the same repo.
- **Team collaboration**: Everyone clones the same repo, works on branches, and merges via pull requests.
- **CI/CD and hosting**: Connect GitHub to Vercel, Netlify, or GitHub Actions to build and deploy on push.
- **Multiple GitHub accounts**: Use SSH config (e.g. `Host github-personal`) with different keys so work and personal repos use the correct account.

## Considerations

- **Authentication**: Use SSH keys and `~/.ssh/config` to avoid mixing work and personal credentials; clear or avoid storing HTTPS credentials for the wrong account.
- **Root directory**: For monorepos (e.g. app in an `app/` subfolder), set the build "Root Directory" in Vercel (or similar) so the correct folder is built.
- **Branch protection**: On shared repos, protect `main` so changes go through pull requests and reviews.
- **Secrets**: Never commit API keys or passwords; use environment variables or secret managers in the host (e.g. Vercel env vars).

## Best Practices

- Commit often with clear messages; push regularly so work is backed up and others can pull.
- Use branches for features or fixes; merge to `main` after review or self-review.
- Keep one remote (e.g. `origin`) pointing at the canonical repo (e.g. GitHub); use SSH with the right key per account.
- For deploy: set Root Directory when the app lives in a subfolder; use a single production branch (e.g. `main`) unless you use preview branches on purpose.
- Add a `.gitignore` for build output, dependencies, and secrets so they are never committed.

## Related Topics

- Data Pipeline Best Practices (documentation and versioning of pipeline code)
- Data Versioning (versioning datasets and models)

## Further Reading

- [Git documentation](https://git-scm.com/doc)
- [GitHub Docs](https://docs.github.com)
- [Vercel: Git integration](https://vercel.com/docs/deployments/git)

---

**Category**: Version Control & Git  
**Last Updated**: 2025
