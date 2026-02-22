# Scripts

This folder contains scripts for maintaining the Data Pipeline Glossary. Scripts are organized into two categories:

## Maintenance scripts (for you)

Scripts in `maintenance/` are intended for ongoing project updates. Run them from the **project root**.

| Script | Purpose |
|--------|---------|
| `generate-topic.sh` | Create a new topic file with template. Updates TOPICS.md. |
| `generate-topics.py` | Bulk-generate topic files from docs/TOPICS.md. |
| `fill-topic.sh` | Prepare context for AI to fill empty/placeholder sections in a topic. |
| `sync-topic-status.sh` | Sync completion status in TOPICS.md based on existing topic files. |
| `update-section-indexes.py` | Update section index pages with topic links; writes topics-needing-content.md. (Also runs automatically before each MkDocs build.) |
| `link-related-topics.py` | Convert plain-text Related Topics entries to markdown links. (Also runs automatically before each MkDocs build.) |

### Examples

```bash
# Create a single topic
./scripts/maintenance/generate-topic.sh ai-ml model-training-pipelines "Model Training Pipelines"

# Bulk generate from TOPICS.md
python scripts/maintenance/generate-topics.py docs/TOPICS.md

# Prepare a topic for AI filling
./scripts/maintenance/fill-topic.sh docs/ai-ml/model-training-pipelines.md

# Sync status after adding/editing topics
./scripts/maintenance/sync-topic-status.sh
```

## Internal scripts (for AI / tooling)

Scripts in `internal/` are helpers used by maintenance scripts. They are not meant for direct use.

| Script | Used by | Purpose |
|--------|---------|---------|
| `analyze-topic-structure.sh` | fill-topic.sh, generate-topic.sh | Output JSON structure of a topic file. |
| `detect-empty-sections.sh` | fill-topic.sh | Output JSON of sections that need content. |
