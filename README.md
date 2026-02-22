# Data Pipeline Glossary

A comprehensive glossary of data pipeline concepts, technologies, and techniques for data architects.

## Project Overview

This glossary provides one-page explanations of key components, steps, and concepts in modern data pipelines. Each topic is explained at a conceptual level, focusing on **what** and **why** rather than specific tool implementations.

## Structure

```
├── README.md                    # This file
├── TOPICS.md                    # Complete list of topics
├── INDEX.md                     # Quick navigation index
├── TEMPLATE.md                  # Template for one-pagers
├── architecture/                # High-level architecture concepts
├── ingestion/                   # Data ingestion patterns
├── storage/                     # Data storage concepts
├── databases/                   # Database types and technologies
├── transformation/              # Data transformation techniques
├── orchestration/               # Pipeline orchestration
├── quality/                     # Data quality and validation
├── governance/                  # Data governance concepts
├── patterns/                    # Common patterns and paradigms
├── formats/                     # Data formats and serialization
├── ai-ml/                       # AI & Machine Learning concepts
├── conversational-analytics/    # Conversational analytics & AI interfaces
└── analytics/                   # Analytics & Business Intelligence
```

## How to Use

1. Browse topics by category in the directory structure
2. Each topic is a standalone one-pager in Markdown format
3. Topics are cross-referenced where relevant
4. Focus is on concepts, not specific tools

## Pushing changes to the repo

To save and push your work to GitHub (or your Git remote):

1. **Check what changed**
   ```bash
   git status
   ```

2. **Stage changes** (all files, or list specific paths)
   ```bash
   git add .
   # or: git add path/to/file1 path/to/file2
   ```

3. **Commit with a message**
   ```bash
   git commit -m "Short description of what you did"
   ```

4. **Push to the remote**
   ```bash
   git push
   ```
   If your branch is new and not yet on the remote: `git push -u origin <branch-name>` (e.g. `git push -u origin main`).

## Generation Tools

Two tools are provided to help generate topic files:

### Individual Topic Generator
Generate a single topic file with template:
```bash
./scripts/maintenance/generate-topic.sh <category> <topic-name> <title>
```

Example:
```bash
./scripts/maintenance/generate-topic.sh transformation data-aggregation "Data Aggregation"
```

**Automatically updates:**
- ✅ Marks topic as `[x]` in `docs/TOPICS.md`

### Bulk Topic Generator
Generate all remaining topics from docs/TOPICS.md:
```bash
python3 scripts/maintenance/generate-topics.py docs/TOPICS.md
```

This will create template files for all unchecked topics in TOPICS.md and automatically update status.

### Sync Existing Files
If you have existing files that aren't marked, sync their status:
```bash
./scripts/maintenance/sync-topic-status.sh
```

See `GENERATION_GUIDE.md` for detailed instructions and writing guidelines.

## Contributing

When adding a new topic:
1. Use the template in `TEMPLATE.md` or the generation tools
2. Keep it to one page (aim for 300-500 words)
3. Focus on concepts and principles
4. Include cross-references to related topics
5. Avoid tool-specific examples

For detailed guidelines, see `GENERATION_GUIDE.md`.
