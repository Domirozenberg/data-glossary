#!/bin/bash

# Data Pipeline Glossary - Topic Filler Helper
# Prepares information for AI to fill topic content.
# Run from project root: ./scripts/maintenance/fill-topic.sh docs/ai-ml/model-training-pipelines.md

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
INTERNAL="$SCRIPT_DIR/../internal"

FILE_PATH=$1

if [ -z "$FILE_PATH" ]; then
    echo "Usage: $0 <file-path>"
    echo "Example: $0 docs/ai-ml/model-training-pipelines.md"
    exit 1
fi

# Resolve path relative to project root
if [[ "$FILE_PATH" != /* ]]; then
    FILE_PATH="$PROJECT_ROOT/$FILE_PATH"
fi

if [ ! -f "$FILE_PATH" ]; then
    echo "Error: File not found: $FILE_PATH"
    exit 1
fi

echo "📋 Analyzing structure of: $FILE_PATH"
echo ""
"$INTERNAL/analyze-topic-structure.sh" "$FILE_PATH"
echo ""
echo "📝 Sections that need filling:"
"$INTERNAL/detect-empty-sections.sh" "$FILE_PATH"
echo ""
echo "🤖 To fill this file, ask the AI assistant:"
echo "   'Fill in the content for @$FILE_PATH based on the structure'"
echo ""
echo "   The AI will:"
echo "   - Read the file to understand its structure"
echo "   - Fill only sections that are empty or have placeholders"
echo "   - Preserve all existing filled content"
echo "   - Maintain the existing structure and formatting"
echo ""
echo "   💡 Tip: You can add new sections to existing topics, and the AI will fill them!"
echo ""
