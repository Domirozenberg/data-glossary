#!/bin/bash

# Data Pipeline Glossary - Empty Section Detector
# Detects which sections in a topic file are empty or have placeholders
# Outputs JSON with sections that need to be filled

FILE_PATH=$1

if [ -z "$FILE_PATH" ] || [ ! -f "$FILE_PATH" ]; then
    echo "Usage: $0 <file-path>"
    echo "Example: $0 ai-ml/model-training-pipelines.md"
    exit 1
fi

# Extract title
TITLE=$(grep -m 1 "^# " "$FILE_PATH" | sed 's/^# //')

# Get all section headings
SECTIONS=$(grep "^## " "$FILE_PATH" | sed 's/^## //')

# Output JSON with sections that need filling
echo "{"
echo "  \"title\": \"$TITLE\","
echo "  \"filePath\": \"$FILE_PATH\","
echo "  \"sectionsToFill\": ["

FIRST=true
while IFS= read -r section; do
    # Find the section content (from this heading to next heading or end of file)
    # Check if section has placeholder content or is empty
    SECTION_LINE=$(grep -n "^## $section$" "$FILE_PATH" | cut -d: -f1)
    
    if [ -n "$SECTION_LINE" ]; then
        # Get content from this section to next section or end
        NEXT_SECTION_LINE=$(awk "NR > $SECTION_LINE && /^## / {print NR; exit}" "$FILE_PATH")
        
        if [ -z "$NEXT_SECTION_LINE" ]; then
            # Last section, get to end of file
            SECTION_CONTENT=$(sed -n "$((SECTION_LINE+1)),\$p" "$FILE_PATH")
        else
            # Get content until next section
            SECTION_CONTENT=$(sed -n "$((SECTION_LINE+1)),$((NEXT_SECTION_LINE-1))p" "$FILE_PATH")
        fi
        
        # Check if section is empty or has placeholders
        IS_EMPTY=false
        HAS_PLACEHOLDER=false
        
        # Remove empty lines and check
        CLEANED=$(echo "$SECTION_CONTENT" | sed '/^[[:space:]]*$/d' | sed '/^---$/d' | sed '/^\*\*Category\*\*:/d' | sed '/^\*\*Last Updated\*\*:/d')
        
        if [ -z "$CLEANED" ]; then
            IS_EMPTY=true
        fi
        
        # Check for placeholder patterns
        if echo "$SECTION_CONTENT" | grep -q "\[.*\]"; then
            HAS_PLACEHOLDER=true
        fi
        
        # If empty or has placeholder, mark for filling
        if [ "$IS_EMPTY" = true ] || [ "$HAS_PLACEHOLDER" = true ]; then
            if [ "$FIRST" = true ]; then
                FIRST=false
            else
                echo ","
            fi
            echo -n "    {"
            echo -n "\"name\": \"$section\","
            echo -n "\"isEmpty\": $IS_EMPTY,"
            echo -n "\"hasPlaceholder\": $HAS_PLACEHOLDER"
            echo -n "}"
        fi
    fi
done <<< "$SECTIONS"

echo ""
echo "  ]"
echo "}"
