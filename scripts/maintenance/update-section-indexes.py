#!/usr/bin/env python3
"""Append 'Topics in this section' with links to all .md files in each docs subdir.
   Marks topics that have a 'Products & Tools' (or similar) section with 🛠.
   Marks topics without real content (placeholder only) with 📝. Writes topics-needing-content.md."""
import re
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent.parent / "docs"
SECTION_DIRS = [
    "architecture", "ingestion", "storage", "databases", "patterns",
    "transformation", "modeling", "quality", "orchestration", "formats",
    "governance", "observability", "advanced", "ai-ml", "conversational-analytics",
    "analytics", "cross-cutting", "version-control",
]

# Section dir -> nav title (for "Topics needing content" page)
SECTION_TITLES = {
    "architecture": "Architecture & Design",
    "ingestion": "Data Ingestion",
    "storage": "Data Storage",
    "databases": "Databases",
    "patterns": "Integration Patterns",
    "transformation": "Data Transformation",
    "modeling": "Data Modeling",
    "quality": "Data Quality",
    "orchestration": "Data Orchestration",
    "formats": "Data Formats",
    "governance": "Data Governance",
    "observability": "Data Observability",
    "advanced": "Advanced Concepts",
    "ai-ml": "AI & Machine Learning",
    "conversational-analytics": "Conversational Analytics",
    "analytics": "Analytics & BI",
    "cross-cutting": "Cross-cutting",
    "version-control": "Version Control",
}

# Placeholder that indicates the topic has not been written yet
STUB_PLACEHOLDER = "[Brief 2-3 sentence overview of what this topic is and why it matters in data pipelines.]"

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


def is_stub(md_path: Path) -> bool:
    """True if the topic still has placeholder content (no real content written yet)."""
    try:
        text = md_path.read_text()
        return STUB_PLACEHOLDER in text
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
        # Append topic links; add 🛠 for Products & Tools, 📝 for topics needing content
        topic_lines = ["\n\n## Topics in this section\n"]
        topic_lines.append("*🛠 = includes Products & Tools · 📝 = topic needs content*\n\n")
        for f in topic_files:
            t = f.stem
            title = slug_to_title(t)
            marks = []
            if has_products_tools_section(f):
                marks.append("🛠")
            if is_stub(f):
                marks.append("📝")
            mark = " " + " ".join(marks) if marks else ""
            topic_lines.append(f"- [{title}]({t}.md){mark}\n")
        index_md.write_text(lines + "".join(topic_lines))

    _write_topics_needing_content()


def _write_topics_needing_content() -> None:
    """Write docs/topics-needing-content.md listing all stub topics by category."""
    out = [
        "# Topics needing content\n\n",
        "These topics still have placeholder content and need to be written. "
        "You can use this page to find them quickly.\n\n",
    ]
    total = 0
    for section in SECTION_DIRS:
        dirpath = DOCS / section
        if not dirpath.is_dir():
            continue
        topic_files = sorted(
            f for f in dirpath.glob("*.md") if f.name != "index.md"
        )
        stubs = [f for f in topic_files if is_stub(f)]
        if not stubs:
            continue
        title = SECTION_TITLES.get(section, slug_to_title(section))
        out.append(f"## {title}\n\n")
        for f in stubs:
            rel = f"{section}/{f.stem}.md"
            name = slug_to_title(f.stem)
            out.append(f"- [{name}]({rel})\n")
        out.append("\n")
        total += len(stubs)
    out.append(f"\n*Total: {total} topics needing content.*\n")
    (DOCS / "topics-needing-content.md").write_text("".join(out))


if __name__ == "__main__":
    main()
