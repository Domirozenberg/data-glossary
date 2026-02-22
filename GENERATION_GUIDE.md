# Topic Generation Guide

This guide helps you complete the remaining one-pager topics for the Data Pipeline Glossary.

## Current Status

✅ **Completed Categories:**
- Architecture & Design Patterns (14 files)
- Data Ingestion (14 files)
- Data Storage (15 files)
- Database Types & Technologies (46 files)

📝 **In Progress / Remaining:**
- Data Transformation (3/16 files)
- Data Modeling (1/14 files)
- Data Quality (1/14 files)
- Data Orchestration (1/14 files)
- Data Formats (1/13 files)
- Data Governance (1/15 files)
- Data Observability (1/8 files)
- Advanced Concepts (1/21 files)
- AI & ML (1/~29 files)
- Conversational Analytics (1/~14 files)
- Analytics & BI (1/~29 files)
- Cross-Cutting Topics (1/6 files)

## Checking if a Topic Exists

The status of topics is automatically tracked in `TOPICS.md` and `INDEX.md`:

### Method 1: Check TOPICS.md
The `TOPICS.md` file uses checkboxes to show completion status:
- `- [ ]` = Topic not yet created
- `- [x]` = Topic completed (automatically marked when generated)

**Example:**
```markdown
- [x] Model Training Pipelines  ← Completed
- [ ] Model Inference Pipelines ← Not yet created
```

### Method 2: Check INDEX.md
The `INDEX.md` file shows which topics have files:
- **Topics with files**: Shown as links, e.g., `[Data Pipeline Architecture](architecture/data-pipeline-architecture.md)`
- **Topics without files**: Shown as plain text, e.g., `Lambda Architecture`

**Example:**
```markdown
- [Model Training Pipelines](ai-ml/model-training-pipelines.md)  ← Has file
- Model Inference Pipelines  ← No file yet
```

### Automatic Status Updates

When you generate a topic using `generate-topic.sh`, it automatically:
1. ✅ Marks the topic as `[x]` in `TOPICS.md`
2. ✅ Adds a link in `INDEX.md`

### Sync Existing Files

If you have existing topic files that aren't marked, run the sync script:
```bash
./scripts/maintenance/sync-topic-status.sh
```

This script:
- Scans all existing topic files under docs/
- Updates `docs/TOPICS.md` to mark them as `[x]`

**Note:** The bulk generator (`generate-topics.py`) automatically skips topics that already have files, so you can safely run it without overwriting existing content.

## Generation Tools

### Structure Analysis

The glossary includes tools to analyze and understand topic file structures:

```bash
# Analyze a topic file's structure (or use fill-topic.sh which does this for you)
./scripts/maintenance/fill-topic.sh docs/<category>/<topic>.md

# Example:
./scripts/maintenance/fill-topic.sh docs/ai-ml/model-training-pipelines.md
```

This outputs JSON showing:
- Title
- Category
- All section headings
- Whether the file has placeholder content
- Last updated date

### Option 1: Individual Topic Generator (Shell Script)

Generate a single topic file:

```bash
./scripts/maintenance/generate-topic.sh <category> <topic-name> <title>
```

**Examples:**
```bash
# AI/ML topics
./scripts/maintenance/generate-topic.sh ai-ml model-training-pipelines "Model Training Pipelines"
./scripts/maintenance/generate-topic.sh ai-ml model-inference-pipelines "Model Inference Pipelines"
./scripts/maintenance/generate-topic.sh ai-ml model-serving "Model Serving"
./scripts/maintenance/generate-topic.sh ai-ml feature-stores "Feature Stores"

# Transformation topics
./scripts/maintenance/generate-topic.sh transformation data-aggregation "Data Aggregation"
./scripts/maintenance/generate-topic.sh transformation data-enrichment "Data Enrichment"
./scripts/maintenance/generate-topic.sh transformation data-deduplication "Data Deduplication"

# Modeling topics
./scripts/maintenance/generate-topic.sh modeling star-schema "Star Schema"
./scripts/maintenance/generate-topic.sh modeling snowflake-schema "Snowflake Schema"
./scripts/maintenance/generate-topic.sh modeling fact-tables "Fact Tables"

# Quality topics
./scripts/maintenance/generate-topic.sh quality data-accuracy "Data Accuracy"
./scripts/maintenance/generate-topic.sh quality data-completeness "Data Completeness"
./scripts/maintenance/generate-topic.sh quality data-consistency "Data Consistency"

# Analytics topics
./scripts/maintenance/generate-topic.sh analytics predictive-analytics "Predictive Analytics"
./scripts/maintenance/generate-topic.sh analytics self-service-analytics "Self-service Analytics"
./scripts/maintenance/generate-topic.sh analytics real-time-analytics "Real-time Analytics"
```

**Command Format:**
```bash
./scripts/maintenance/generate-topic.sh <category> <topic-name> <title>
```

Where:
- `<category>`: Directory name (e.g., `ai-ml`, `transformation`, `quality`)
- `<topic-name>`: Filename slug in lowercase with hyphens (e.g., `model-training-pipelines`)
- `<title>`: Display title with proper capitalization (e.g., `"Model Training Pipelines"`)

The script will:
- Create the category directory if needed
- Generate a template file with all sections
- Prompt before overwriting existing files
- Create the file: `<category>/<topic-name>.md`
- **Automatically update TOPICS.md** (mark as `[x]`)
- **Automatically update INDEX.md** (add link)
- Provide instructions for filling in content

### Filling in Content

After generating a template, you can fill it with content in three ways:

**Option 1: Use AI Assistant** (Recommended)
```bash
# After generating, ask the AI:
"Fill in the content for @<category>/<topic-name>.md based on the structure"
```

The AI will automatically:
- Read the file to detect its structure (all `##` sections)
- Identify which sections are empty or have placeholders (content in brackets)
- Fill only those sections that need content
- Preserve all existing filled content
- Maintain the existing structure and formatting

**Adding New Sections to Existing Topics:**

You can add new sections to any existing topic file, and the AI will fill them:

1. **Add a new section** to your topic file (e.g., `## Examples`, `## Common Pitfalls`, `## Real-world Scenarios`)
2. **Add a placeholder** in that section (e.g., `[Examples of this concept in practice]`)
3. **Ask the AI** to fill it: "Fill in the content for @<file-path> based on the structure"
4. The AI will detect the new section and fill only that section, preserving all other content

Example:
```markdown
## Examples

[Examples of LLM-based data discovery in practice]
```

Then ask: "Fill in the content for @conversational-analytics/LLM-based-data-discovery.md"

**Option 2: Use Fill Helper Script**
```bash
./scripts/maintenance/fill-topic.sh docs/<category>/<topic-name>.md
# This analyzes the structure and shows you the exact prompt to use
```

**Option 2b: Check Which Sections Need Filling**
```bash
./scripts/maintenance/fill-topic.sh docs/<category>/<topic-name>.md
# This shows structure and which sections are empty or have placeholders
```

**Option 3: Manual Editing**
Edit the file directly following the template structure and writing guidelines.

### Customizing Topic Structure

You can customize the structure of any topic file by:
- Adding new sections (e.g., `## Examples`, `## Common Pitfalls`)
- Removing sections you don't need
- Renaming sections to better fit the topic
- Reordering sections

When you ask the AI to fill content, it will automatically detect and respect your custom structure. The `scripts/maintenance/generate-topic.sh` script will also show the file structure when creating or overwriting files.

### Option 2: Bulk Generator (Python Script)

Generate all remaining topics from TOPICS.md:

```bash
python3 scripts/maintenance/generate-topics.py docs/TOPICS.md
```

Or specify a different topics file:
```bash
python3 scripts/maintenance/generate-topics.py docs/TOPICS.md
```

The script will:
- Read TOPICS.md
- Skip topics that already have files
- Generate template files for all unchecked topics
- Show summary of generated vs skipped files

**Note:** The bulk generator creates template files that you'll need to fill in with content.

## Writing Guidelines

### Template Structure

Each one-pager follows this structure:

1. **Overview** (2-3 sentences)
   - What it is and why it matters
   - Keep it concise and accessible

2. **Definition**
   - Clear, precise definition
   - Avoid jargon when possible

3. **Key Concepts** (3-7 bullet points)
   - Core concepts with brief explanations
   - Use bold for concept names

4. **How It Works**
   - Mechanism, process, or approach
   - Can include numbered steps
   - Describe, don't reference specific tools

5. **Use Cases**
   - When to use this approach
   - Common scenarios
   - Benefits in specific contexts

6. **Considerations**
   - Important factors
   - Trade-offs
   - Challenges or limitations

7. **Best Practices**
   - Recommended approaches
   - Common patterns
   - Things to avoid

8. **Related Topics**
   - Links to related concepts
   - How it connects to other components

9. **Further Reading** (optional)
   - Authoritative sources
   - Related industry concepts

### Writing Tips

- **Keep it conceptual**: Focus on concepts, not specific tools
- **One page**: Aim for 300-500 words
- **Be clear**: Write for data architects, not just experts
- **Use examples**: Include examples when helpful (but keep them tool-agnostic)
- **Cross-reference**: Link to related topics
- **Stay current**: Focus on modern approaches

### Category-Specific Notes

**Data Transformation:**
- Focus on transformation techniques and patterns
- Explain when to use each approach
- Include performance considerations

**Data Modeling:**
- Explain modeling concepts clearly
- Include examples of model structures
- Connect to use cases

**Data Quality:**
- Explain quality dimensions
- Focus on techniques, not tools
- Include measurement approaches

**Data Orchestration:**
- Focus on orchestration patterns
- Explain dependency management
- Include error handling approaches

**Data Formats:**
- Explain format characteristics
- Compare formats when relevant
- Include use case guidance

**Data Governance:**
- Focus on governance concepts
- Explain compliance aspects
- Include best practices

**Data Observability:**
- Explain observability pillars
- Focus on what to monitor
- Include alerting strategies

**Advanced Concepts:**
- Cover advanced techniques
- Explain optimization approaches
- Include scalability patterns

**AI & ML:**
- Focus on ML pipeline concepts
- Explain feature engineering
- Include MLOps practices

**Conversational Analytics:**
- Explain NLP concepts
- Focus on query understanding
- Include implementation considerations

**Analytics & BI:**
- Explain analytical concepts
- Focus on OLAP and reporting
- Include visualization approaches

**Cross-Cutting Topics:**
- Provide general guidance
- Include best practices
- Cover common patterns

## Quality Checklist

Before considering a topic complete:

- [ ] Overview is clear and concise
- [ ] Definition is accurate
- [ ] Key concepts are explained
- [ ] "How It Works" section is complete
- [ ] Use cases are relevant
- [ ] Considerations are realistic
- [ ] Best practices are actionable
- [ ] Related topics are linked
- [ ] No tool-specific references
- [ ] Length is appropriate (300-500 words)
- [ ] Category is correct
- [ ] Year is current

## Workflow Suggestions

1. **Start with high-priority topics** from each category
2. **Use the template** - don't start from scratch
3. **Reference existing files** for style consistency
4. **Review related topics** to ensure consistency
5. **Test links** to related topics
6. **Update INDEX.md** as you complete topics

## Getting Help

- Review existing files for style and structure
- Check TEMPLATE.md for the standard format
- Look at completed categories for examples
- Use the generation tools to create templates

## Next Steps

1. **Sync existing files** (if you have files that aren't marked):
   ```bash
   ./scripts/maintenance/sync-topic-status.sh
   ```
   This will update TOPICS.md and INDEX.md for all existing files.

2. **Generate new topics** using either method:
   
   **Option A: Individual topics**
   ```bash
   # Example: Generate an AI/ML topic
   ./scripts/maintenance/generate-topic.sh ai-ml model-inference-pipelines "Model Inference Pipelines"
   
   # This automatically:
   # - Creates: ai-ml/model-inference-pipelines.md
   # - Marks it as [x] in TOPICS.md
   # - Adds link in INDEX.md
   ```
   
   **Option B: Bulk generation**
   ```bash
   python3 scripts/maintenance/generate-topics.py docs/TOPICS.md
   ```
   This creates templates for all unchecked topics and updates status.

3. **Fill in the templates** with content using the writing guidelines

4. **Review and refine** completed topics

**Note:** Status is automatically tracked in TOPICS.md (`[x]` = completed) and INDEX.md (links = files exist). No manual updates needed!

Good luck completing the glossary! 🚀
