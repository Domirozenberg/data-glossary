#!/bin/bash

# Sync topic status in docs/TOPICS.md based on existing topic files
# Scans all topic files under docs/ and updates the status marks
# Run from project root: ./scripts/maintenance/sync-topic-status.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
DOCS="$PROJECT_ROOT/docs"
TOPICS_FILE="$DOCS/TOPICS.md"

echo "Syncing topic status in TOPICS.md..."
echo ""

if [ ! -f "$TOPICS_FILE" ]; then
    echo "Error: TOPICS.md not found at $TOPICS_FILE"
    exit 1
fi

# Find all topic markdown files under docs (exclude index.md, TOPICS.md, etc.)
find "$DOCS" -name "*.md" -type f \
    ! -path "$DOCS/index.md" \
    ! -path "$DOCS/TOPICS.md" \
    ! -path "$DOCS/topics-needing-content.md" \
    ! -path "$DOCS/full-index.md" \
    ! -name "index.md" \
    | while read -r filepath; do

    # Get category and topic name (relative to docs)
    rel_path="${filepath#$DOCS/}"
    category=$(dirname "$rel_path" | sed 's|^\./||')
    filename=$(basename "$filepath" .md)

    # Extract title from first line of file (remove # and trim)
    title=$(head -n 1 "$filepath" | sed 's/^# *//' | sed 's/ *$//')

    if [ -z "$title" ]; then
        title=$(echo "$filename" | sed 's/-/ /g' | sed 's/\b\(.\)/\u\1/g')
    fi

    # Update TOPICS.md - mark as completed
    if grep -q "^- \[ \] $title" "$TOPICS_FILE"; then
        sed -i '' "s/^- \[ \] $title/- [x] $title/" "$TOPICS_FILE"
        echo "✓ Marked '$title' as completed in TOPICS.md"
    elif grep -q "^- \[ \] .*$title" "$TOPICS_FILE"; then
        escaped_title=$(echo "$title" | sed 's/[[\.*^$()+?{|]/\\&/g')
        sed -i '' "s|^- \[ \] \(.*$escaped_title.*\)|- [x] \1|" "$TOPICS_FILE"
        echo "✓ Marked topic containing '$title' as completed in TOPICS.md"
    fi
done

echo ""
echo "Sync complete! Review TOPICS.md for changes."
