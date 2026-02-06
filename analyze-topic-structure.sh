#!/bin/bash

# Data Pipeline Glossary - Topic Structure Analyzer
# Analyzes a topic file to detect its structure (sections, placeholders, etc.)
# Outputs JSON with structure information for use by AI filling scripts

FILE_PATH=$1

if [ -z "$FILE_PATH" ] || [ ! -f "$FILE_PATH" ]; then
    echo "Usage: $0 <file-path>"
    echo "Example: $0 ai-ml/model-training-pipelines.md"
    exit 1
fi

# Extract title (first # heading)
TITLE=$(grep -m 1 "^# " "$FILE_PATH" | sed 's/^# //')

# Extract all section headings (## headings)
SECTIONS=$(grep "^## " "$FILE_PATH" | sed 's/^## //')

# Check for placeholder content (content in brackets)
HAS_PLACEHOLDERS=false
if grep -q "\[.*\]" "$FILE_PATH"; then
    HAS_PLACEHOLDERS=true
fi

# Extract category and last updated from footer
CATEGORY=$(grep "^\*\*Category\*\*:" "$FILE_PATH" | sed 's/^\*\*Category\*\*: *//' | sed 's/ *$//')
LAST_UPDATED=$(grep "^\*\*Last Updated\*\*:" "$FILE_PATH" | sed 's/^\*\*Last Updated\*\*: *//' | sed 's/ *$//')

# Output structure as JSON
echo "{"
echo "  \"title\": \"$TITLE\","
echo "  \"category\": \"$CATEGORY\","
echo "  \"lastUpdated\": \"$LAST_UPDATED\","
echo "  \"hasPlaceholders\": $HAS_PLACEHOLDERS,"
echo "  \"sections\": ["

# Output sections as array
FIRST=true
while IFS= read -r section; do
    if [ "$FIRST" = true ]; then
        FIRST=false
    else
        echo ","
    fi
    echo -n "    \"$section\""
done <<< "$SECTIONS"

echo ""
echo "  ]"
echo "}"
