#!/usr/bin/env python3
"""
Data Pipeline Glossary - Bulk Topic Generator
Generates one-pager markdown files from a list of topics
"""

import os
import sys
from datetime import datetime
from pathlib import Path

TEMPLATE = """# {title}

## Overview
[Brief 2-3 sentence overview of what this topic is and why it matters in data pipelines.]

## Definition
[Clear, concise definition of the concept.]

## Key Concepts

- **Concept 1**: [Explanation]
- **Concept 2**: [Explanation]
- **Concept 3**: [Explanation]

## How It Works
[Explanation of the mechanism, process, or approach. Include diagrams or examples if helpful (described, not tool-specific).]

## Use Cases
- [When to use this approach/technique]
- [Common scenarios]
- [Benefits in specific contexts]

## Considerations
- [Important factors to consider]
- [Trade-offs]
- [Challenges or limitations]

## Best Practices
- [Recommended approaches]
- [Common patterns]
- [Things to avoid]

## Related Topics
- [Link to related concepts in the glossary]
- [How this connects to other pipeline components]

## Further Reading
- [Optional: Links to authoritative sources or standards]
- [Related industry concepts]

---

**Category**: {category}  
**Last Updated**: {year}
"""

# Map TOPICS.md section headers to category folder names
SECTION_TO_FOLDER = {
    'architecture-&-design-patterns': 'architecture',
    'data-ingestion': 'ingestion',
    'data-storage': 'storage',
    'database-types-&-technologies': 'databases',
    'data-transformation': 'transformation',
    'data-modeling': 'modeling',
    'data-quality-&-validation': 'quality',
    'data-orchestration': 'orchestration',
    'data-formats-&-serialization': 'formats',
    'data-governance': 'governance',
    'data-observability': 'observability',
    'advanced-concepts': 'advanced',
    'ai-&-machine-learning': 'ai-ml',
    'conversational-analytics': 'conversational-analytics',
    'analytics-&-business-intelligence': 'analytics',
    'cross-cutting-topics': 'cross-cutting',
    'version-control-&-git': 'version-control',
}

def slugify(text):
    """Convert text to URL-friendly slug"""
    return text.lower().replace(' ', '-').replace('(', '').replace(')', '').replace(',', '').replace('/', '-').replace('&', '')

def update_topics_md(topic_title):
    """Update TOPICS.md to mark topic as completed"""
    topics_file = Path('TOPICS.md')
    if not topics_file.exists():
        return
    
    content = topics_file.read_text()
    # Try exact match first
    pattern1 = f"- [ ] {topic_title}"
    replacement1 = f"- [x] {topic_title}"
    if pattern1 in content:
        content = content.replace(pattern1, replacement1)
        topics_file.write_text(content)
        return True
    
    # Try with flexible matching
    import re
    pattern2 = re.compile(rf"^- \[ \] (.*{re.escape(topic_title)}.*)$", re.MULTILINE)
    if pattern2.search(content):
        content = pattern2.sub(rf"- [x] \1", content)
        topics_file.write_text(content)
        return True
    
    return False

def update_index_md(topic_title, filepath):
    """Update INDEX.md to add link for topic"""
    index_file = Path('INDEX.md')
    if not index_file.exists():
        return
    
    content = index_file.read_text()
    # Check if link already exists
    if f"[{topic_title}]({filepath})" in content:
        return False
    
    # Try to find topic without link and add it
    import re
    # Match lines starting with "- " followed by topic title (not already a link)
    pattern = re.compile(rf"^- ({re.escape(topic_title)})(?!.*\]\()", re.MULTILINE)
    if pattern.search(content):
        content = pattern.sub(rf"- [{topic_title}]({filepath})", content)
        index_file.write_text(content)
        return True
    
    # Try flexible matching
    pattern2 = re.compile(rf"^- (.*{re.escape(topic_title)}.*)(?!.*\]\()", re.MULTILINE)
    if pattern2.search(content):
        match = pattern2.search(content)
        if match:
            full_title = match.group(1)
            content = pattern2.sub(rf"- [{full_title}]({filepath})", content)
            index_file.write_text(content)
            return True
    
    return False

def generate_file(category, topic_title, overwrite=False):
    """Generate a markdown file for a topic"""
    category_dir = Path(category)
    category_dir.mkdir(exist_ok=True)
    
    filename = slugify(topic_title) + '.md'
    filepath = category_dir / filename
    
    if filepath.exists() and not overwrite:
        print(f"  ⚠️  Skipping {filepath} (already exists)")
        return False
    
    # Format category name for display
    category_display = category.replace('-', ' ').title()
    
    content = TEMPLATE.format(
        title=topic_title,
        category=category_display,
        year=datetime.now().year
    )
    
    filepath.write_text(content)
    print(f"  ✅ Created {filepath}")
    
    # Update TOPICS.md and INDEX.md
    if update_topics_md(topic_title):
        print(f"  ✓ Marked '{topic_title}' as completed in TOPICS.md")
    if update_index_md(topic_title, str(filepath)):
        print(f"  ✓ Added link for '{topic_title}' in INDEX.md")
    
    return True

def generate_from_list(topics_file):
    """Generate files from a topics list file"""
    if not os.path.exists(topics_file):
        print(f"Error: {topics_file} not found")
        return
    
    current_category = None
    generated = 0
    skipped = 0
    
    with open(topics_file, 'r') as f:
        for line in f:
            line = line.strip()
            
            # Skip empty lines and markdown headers
            if not line or line.startswith('#'):
                # Check if it's a category header
                if line.startswith('## '):
                    raw = line.replace('## ', '').lower().replace(' ', '-')
                    if '/' in raw:
                        raw = raw.split('/')[0]
                    current_category = SECTION_TO_FOLDER.get(raw, raw.replace('&', ''))
                continue
            
            # Skip list markers and completed items
            if line.startswith('- [x]') or line.startswith('- [X]'):
                continue  # Skip completed items
            
            # Extract topic from list item
            if line.startswith('- [ ]'):
                topic = line.replace('- [ ]', '').strip()
            elif line.startswith('-'):
                topic = line.replace('-', '').strip()
            else:
                continue
            
            if not topic or not current_category:
                continue
            
            # Clean up topic title (remove markdown links if present)
            if '[' in topic and ']' in topic:
                # Extract text from markdown link [text](url)
                topic = topic.split(']')[0].replace('[', '').strip()
            
            if generate_file(current_category, topic):
                generated += 1
            else:
                skipped += 1
    
    print(f"\n📊 Summary: Generated {generated} files, Skipped {skipped} files")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        topics_file = sys.argv[1]
    else:
        topics_file = 'TOPICS.md'
    
    print(f"Generating topics from {topics_file}...\n")
    generate_from_list(topics_file)
