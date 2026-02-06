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
├── app/                         # Web app (browse, print, download)
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

## Web App

A web application in the `app/` folder lets you browse the glossary in a browser, with navigation by category, print/PDF, and download-as-Markdown. See [app/README.md](app/README.md) for setup and deployment (e.g. to Vercel).

## Generation Tools

Two tools are provided to help generate topic files:

### Individual Topic Generator
Generate a single topic file with template:
```bash
./generate-topic.sh <category> <topic-name> <title>
```

Example:
```bash
./generate-topic.sh transformation data-aggregation "Data Aggregation"
```

**Automatically updates:**
- ✅ Marks topic as `[x]` in `TOPICS.md`
- ✅ Adds link in `INDEX.md`

### Bulk Topic Generator
Generate all remaining topics from TOPICS.md:
```bash
python3 generate-topics.py TOPICS.md
```

This will create template files for all unchecked topics in TOPICS.md and automatically update status.

### Sync Existing Files
If you have existing files that aren't marked, sync their status:
```bash
./sync-topic-status.sh
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
