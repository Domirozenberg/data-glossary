#!/usr/bin/env python3
"""Append 'Topics in this section' with links to all .md files in each docs subdir.
   Marks topics that have a 'Products & Tools' (or similar) section with 🛠."""
import re
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs"
SECTION_DIRS = [
    "architecture", "ingestion", "storage", "databases", "patterns",
    "transformation", "modeling", "quality", "orchestration", "formats",
    "governance", "observability", "advanced", "ai-ml", "conversational-analytics",
    "analytics", "cross-cutting", "version-control",
]

# Heading that indicates the topic has a Products & Tools section (case-insensitive)
PRODUCTS_TOOLS_HEADING = re.compile(
    r"^#+\s+(?:.*(?:products?\s*[&and]?\s*tools?|tools?\s*[&and]?\s*products?).*|tools?\s*)$",
    re.IGNORECASE | re.MULTILINE,
)

def slug_to_title(slug: str) -> str:
    """e.g. data-pipeline-architecture -> Data Pipeline Architecture"""
    return slug.replace("-", " ").title()

def has_products_tools_section(md_path: Path) -> bool:
    """True if the file contains a ## Products & Tools (or similar) heading."""
    try:
        text = md_path.read_text()
        return bool(PRODUCTS_TOOLS_HEADING.search(text))
    except Exception:
        return False

def main():
    for section in SECTION_DIRS:
        dirpath = DOCS / section
        if not dirpath.is_dir():
            continue
        index_md = dirpath / "index.md"
        if not index_md.exists():
            continue
        # Collect topic files (exclude index.md)
        topic_files = sorted(
            f for f in dirpath.glob("*.md") if f.name != "index.md"
        )
        if not topic_files:
            continue
        lines = index_md.read_text().rstrip()
        # Remove existing "## Topics" block if present
        lines = re.sub(r"\n## Topics in this section.*(?=\n\n|\Z)", "", lines, flags=re.DOTALL)
        lines = lines.rstrip()
        # Append topic links; add 🛠 for topics with Products & Tools
        topic_lines = ["\n\n## Topics in this section\n"]
        topic_lines.append("*🛠 = includes Products & Tools*\n\n")
        for f in topic_files:
            t = f.stem
            title = slug_to_title(t)
            mark = " 🛠" if has_products_tools_section(f) else ""
            topic_lines.append(f"- [{title}]({t}.md){mark}\n")
        index_md.write_text(lines + "".join(topic_lines))

if __name__ == "__main__":
    main()
