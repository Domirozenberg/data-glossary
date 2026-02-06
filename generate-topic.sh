#!/bin/bash

# Data Pipeline Glossary - Topic Generator Script
# This script helps generate one-pager markdown files for topics
# and automatically updates TOPICS.md and INDEX.md

# Usage: ./generate-topic.sh <category> <topic-name> <title>
# Example: ./generate-topic.sh transformation data-aggregation "Data Aggregation"

CATEGORY=$1
TOPIC_NAME=$2
TITLE=$3

if [ -z "$CATEGORY" ] || [ -z "$TOPIC_NAME" ] || [ -z "$TITLE" ]; then
    echo "Usage: $0 <category> <topic-name> <title>"
    echo "Example: $0 transformation data-aggregation 'Data Aggregation'"
    exit 1
fi

# Create category directory if it doesn't exist
mkdir -p "$CATEGORY"

# File path
FILE_PATH="$CATEGORY/$TOPIC_NAME.md"

# Check if file already exists and analyze its structure
if [ -f "$FILE_PATH" ]; then
    echo "File $FILE_PATH already exists."
    echo ""
    echo "Current file structure:"
    ./analyze-topic-structure.sh "$FILE_PATH" 2>/dev/null || echo "  (Could not analyze structure)"
    echo ""
    echo "Overwrite? (y/n)"
    read -r response
    if [ "$response" != "y" ]; then
        echo "Aborted."
        exit 1
    fi
    echo ""
    echo "⚠️  Note: If the existing file has a custom structure, the AI will preserve it when filling content."
    echo ""
fi

# Generate file content
cat > "$FILE_PATH" << EOF
# $TITLE

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

**Category**: $(echo "$CATEGORY" | sed 's/\b\(.\)/\u\1/g')  
**Last Updated**: $(date +%Y)
EOF

echo "Created $FILE_PATH"
echo ""
echo "📋 File structure:"
./analyze-topic-structure.sh "$FILE_PATH" 2>/dev/null || echo "  (Could not analyze structure)"
echo ""
echo "🤖 Ready for AI to fill content. The file contains a template."
echo "   When you see this message, ask the AI assistant:"
echo "   'Fill in the content for @$FILE_PATH based on the structure'"
echo ""
echo "   The AI will automatically detect and respect the structure shown above."
echo ""

# Update TOPICS.md - mark as completed
if [ -f "TOPICS.md" ]; then
    # Escape special characters for sed
    ESCAPED_TITLE=$(echo "$TITLE" | sed 's/[[\.*^$()+?{|]/\\&/g')
    
    # Try exact match first
    if grep -q "^- \[ \] $ESCAPED_TITLE" TOPICS.md; then
        sed -i '' "s/^- \[ \] $ESCAPED_TITLE/- [x] $ESCAPED_TITLE/" TOPICS.md
        echo "✓ Updated TOPICS.md: marked '$TITLE' as completed"
    # Try with flexible matching (topic may have extra text)
    elif grep -q "^- \[ \] .*$ESCAPED_TITLE" TOPICS.md; then
        sed -i '' "s|^- \[ \] \(.*$ESCAPED_TITLE.*\)|- [x] \1|" TOPICS.md
        echo "✓ Updated TOPICS.md: marked topic containing '$TITLE' as completed"
    else
        echo "⚠️  Could not find '$TITLE' in TOPICS.md to mark as completed"
    fi
fi

# Update INDEX.md - add link if not present
if [ -f "INDEX.md" ]; then
    # Check if link already exists
    if ! grep -q "\[$TITLE\]($FILE_PATH)" INDEX.md; then
        # Escape special characters for sed
        ESCAPED_TITLE=$(echo "$TITLE" | sed 's/[[\.*^$()+?{|]/\\&/g')
        
        # Try exact match first
        if grep -q "^-\s*$ESCAPED_TITLE" INDEX.md && ! grep -q "^-\s*\[$ESCAPED_TITLE\]" INDEX.md; then
            sed -i '' "s|^- \($ESCAPED_TITLE\)|- [$TITLE]($FILE_PATH)|" INDEX.md
            echo "✓ Updated INDEX.md: added link for '$TITLE'"
        # Try flexible matching
        elif grep -q "^-\s.*$ESCAPED_TITLE" INDEX.md && ! grep -q "^-\s.*\[.*$ESCAPED_TITLE.*\]" INDEX.md; then
            sed -i '' "s|^- \(.*$ESCAPED_TITLE.*\)|- [\1]($FILE_PATH)|" INDEX.md
            echo "✓ Updated INDEX.md: added link for topic containing '$TITLE'"
        else
            echo "⚠️  Could not find '$TITLE' in INDEX.md to add link (may already have link)"
        fi
    else
        echo "✓ Link already exists in INDEX.md for '$TITLE'"
    fi
fi

echo "Edit the file to fill in the content."
