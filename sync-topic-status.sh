#!/bin/bash

# Sync topic status in TOPICS.md and INDEX.md based on existing files
# This script scans all topic files and updates the status marks

echo "Syncing topic status in TOPICS.md and INDEX.md..."
echo ""

# Find all topic markdown files
find . -name "*.md" -type f \
    -not -path "./README.md" \
    -not -path "./INDEX.md" \
    -not -path "./TOPICS.md" \
    -not -path "./TEMPLATE.md" \
    -not -path "./GENERATION_GUIDE.md" \
    -not -path "./*.sh" \
    -not -path "./*.py" \
    | while read -r filepath; do
    
    # Get category and topic name
    category=$(dirname "$filepath" | sed 's|^\./||')
    filename=$(basename "$filepath" .md)
    
    # Extract title from first line of file (remove # and trim)
    title=$(head -n 1 "$filepath" | sed 's/^# *//' | sed 's/ *$//')
    
    if [ -z "$title" ]; then
        # Fallback: convert filename to title
        title=$(echo "$filename" | sed 's/-/ /g' | sed 's/\b\(.\)/\u\1/g')
    fi
    
    # Update TOPICS.md - mark as completed
    if [ -f "TOPICS.md" ]; then
        # Try exact match first
        if grep -q "^- \[ \] $title" TOPICS.md; then
            sed -i '' "s/^- \[ \] $title/- [x] $title/" TOPICS.md
            echo "✓ Marked '$title' as completed in TOPICS.md"
        # Try with parentheses/extra text
        elif grep -q "^- \[ \] .*$title" TOPICS.md; then
            # Match line and mark it
            sed -i '' "s|^- \[ \] \(.*$title.*\)|- [x] \1|" TOPICS.md
            echo "✓ Marked topic containing '$title' as completed in TOPICS.md"
        fi
    fi
    
    # Update INDEX.md - add link if not present
    if [ -f "INDEX.md" ]; then
        # Check if already has link
        if ! grep -q "\[$title\]($filepath)" INDEX.md; then
            # Find topic without link and add it
            if grep -q "^-\s*$title" INDEX.md; then
                # Escape special chars for sed
                escaped_title=$(echo "$title" | sed 's/[[\.*^$()+?{|]/\\&/g')
                sed -i '' "s|^- \($escaped_title\)|- [$title]($filepath)|" INDEX.md
                echo "✓ Added link for '$title' in INDEX.md"
            elif grep -q "^-\s.*$title" INDEX.md; then
                # More flexible matching
                escaped_title=$(echo "$title" | sed 's/[[\.*^$()+?{|]/\\&/g')
                sed -i '' "s|^- \(.*$escaped_title.*\)|- [\1]($filepath)|" INDEX.md
                echo "✓ Added link for topic containing '$title' in INDEX.md"
            fi
        fi
    fi
done

echo ""
echo "Sync complete! Review TOPICS.md and INDEX.md for changes."
