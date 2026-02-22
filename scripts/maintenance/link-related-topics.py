#!/usr/bin/env python3
"""
Make "Related Topics" in each topic file clickable by converting plain text
topic names to markdown links. Builds a map from doc titles/slugs to paths,
then updates each file's Related Topics section.
"""
import re
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent.parent / "docs"

# Aliases for Related Topics that don't have an exact doc title match (phrase -> path under docs/)
RELATED_TOPIC_ALIASES: dict[str, str] = {
    "Publish-Subscribe Pattern": "architecture/event-driven-processing.md",
    "Data Integration": "patterns/data-synchronization.md",
    "Master Data Management": "governance/data-stewardship.md",
    "Asynchronous Processing": "architecture/event-driven-processing.md",
    "Federated Governance": "governance/data-stewardship.md",
    "Business Intelligence": "analytics/business-intelligence.md",
    "Data Warehousing": "architecture/data-lake-vs-data-warehouse.md",
    "Data Governance": "governance/data-catalog.md",
    "Data Transformation": "transformation/data-normalization.md",
    "Data Quality": "quality/data-quality-metrics.md",
    "Data Migration": "databases/database-migration.md",
    "ETL/ELT": "patterns/etl-vs-elt.md",
    "Medallion Architecture": "architecture/medallion-architecture.md",
    "Relational Database": "databases/relational-database.md",
    "AI-powered Data Discovery": "conversational-analytics/LLM-based-data-discovery.md",
    "AI-powered Data Cataloging": "governance/data-catalog.md",
    "Version Control": "version-control/git-and-github.md",
    "Data Loading": "ingestion/full-load-vs-incremental-load.md",
    "Real-time Processing": "architecture/stream-processing.md",
    "Data Historization": "modeling/slowly-changing-dimensions.md",
    "Database Normalization": "databases/normalization.md",
    "Data Validation": "quality/data-validation-rules.md",
    "MLOps": "ai-ml/mlops.md",
    "SQL": "databases/sql.md",
    "SQL (Structured Query Language)": "databases/sql.md",
    "Column-Family Stores": "databases/column-family-stores.md",
    "Change Data Capture (CDC)": "ingestion/change-data-capture.md",
    "Event Sourcing": "architecture/event-driven-processing.md",
    "Microservices": "architecture/event-driven-processing.md",
}


def slug_from_title(title: str) -> str:
    """e.g. 'Data Lake vs Data Warehouse' -> 'data-lake-vs-data-warehouse'."""
    t = title.strip()
    # Remove parenthetical like (CDC) or (RDBMS) for slug
    t = re.sub(r"\s*\([^)]*\)\s*", " ", t)
    t = re.sub(r"\s+", "-", t.lower())
    return re.sub(r"[^a-z0-9\-]", "", t)


def build_title_to_path() -> dict[str, str]:
    """Scan docs and return map: normalized title and slug -> relative path (e.g. architecture/batch-processing.md)."""
    title_to_path: dict[str, str] = {}
    for md in DOCS.rglob("*.md"):
        if md.name in ("index.md", "TOPICS.md", "full-index.md") or md == DOCS / "index.md":
            continue
        rel = md.relative_to(DOCS)
        path_str = str(rel).replace("\\", "/")
        try:
            first_line = next(iter(md.read_text().splitlines()))
        except (StopIteration, Exception):
            continue
        if not first_line.startswith("#"):
            continue
        title = first_line.lstrip("#").strip()
        if not title:
            continue
        title_to_path[title] = path_str
        title_to_path[title.lower()] = path_str
        slug = slug_from_title(title)
        if slug:
            title_to_path[slug] = path_str
        # For "A vs B" titles, also map "A" and "B" to this doc (e.g. "Incremental Load" -> full-load-vs-incremental-load.md)
        if " vs " in title:
            for part in title.split(" vs "):
                p = part.strip()
                if p:
                    title_to_path[p] = path_str
                    title_to_path[p.lower()] = path_str
                    part_slug = slug_from_title(p)
                    if part_slug:
                        title_to_path[part_slug] = path_str
    # Add aliases so common Related Topics phrases resolve to the right doc
    for phrase, path_str in RELATED_TOPIC_ALIASES.items():
        title_to_path[phrase] = path_str
        title_to_path[phrase.lower()] = path_str
    return title_to_path


def relative_path(from_file: Path, to_path: str) -> str:
    """Path from from_file's directory to to_path (to_path is under docs/)."""
    from_dir = from_file.parent
    to_full = DOCS / to_path
    try:
        rel = to_full.relative_to(from_dir)
    except ValueError:
        # Cross-directory: go up from from_dir to docs, then down to to_path
        try:
            up = from_dir.relative_to(DOCS)
            depth = len(up.parts)
            rel = Path("/".join([".."] * depth) + "/" + to_path)
        except ValueError:
            rel = Path(to_path)
    return str(rel).replace("\\", "/")


def link_line(line: str, title_to_path: dict[str, str], from_file: Path) -> str:
    """Convert one Related Topics bullet to a link if we have a match."""
    stripped = line.strip()
    if not stripped.startswith("- "):
        return line
    rest = stripped[2:].strip()
    if rest.startswith("[") and "](" in rest:
        # Already a link - fix path if it's docs-relative (missing ../) when cross-directory
        m = re.match(r"^\[([^\]]+)\]\(([^)]+)\)\s*(.*)$", rest)
        if m:
            label, path, trail = m.group(1), m.group(2), m.group(3)
            if not path.startswith(("http", "#", "../")) and "/" in path and path.count("/") >= 1:
                correct = relative_path(from_file, path)
                if correct != path:
                    if trail and not trail.startswith(" "):
                        trail = " " + trail
                    return f"- [{label}]({correct}){trail}"
        return line
    # Try full string first (e.g. "Change Data Capture (CDC)" must match as-is, not stripped)
    path = title_to_path.get(rest) or title_to_path.get(rest.lower()) or title_to_path.get(slug_from_title(rest))
    topic_name = rest
    suffix = ""
    if not path:
        # Fallback: "Topic Name (long description)" -> link "Topic Name", keep " (description)" (ignore short parens like (CDC))
        match = re.match(r"^(.+?)\s*\((?!https?://)[^)]{15,}\)\s*$", rest)
        if match:
            topic_name = match.group(1).strip()
            suffix = " " + rest[match.end(1) :].strip()
            path = title_to_path.get(topic_name) or title_to_path.get(topic_name.lower()) or title_to_path.get(slug_from_title(topic_name))
    if path:
        rel = relative_path(from_file, path)
        if suffix and not suffix.startswith(" "):
            suffix = " " + suffix
        return f"- [{topic_name}]({rel}){suffix}"
    return line


def process_file(md_path: Path, title_to_path: dict[str, str]) -> bool:
    """Replace Related Topics section bullets with links. Returns True if changed."""
    text = md_path.read_text()
    if "## Related Topics" not in text:
        return False
    before, rest = text.split("## Related Topics", 1)
    # Section ends at next ## or ---
    if "## " in rest:
        section, after = rest.split("## ", 1)
        section = "## Related Topics" + section
        after = "## " + after
    elif "---" in rest:
        section, after = rest.split("---", 1)
        section = "## Related Topics" + section
        after = "---" + after
    else:
        section = "## Related Topics" + rest
        after = ""
    lines = section.splitlines()
    new_lines = []
    in_bullets = False
    changed = False
    for i, line in enumerate(lines):
        if line.strip().startswith("- "):
            new_line = link_line(line, title_to_path, md_path)
            if new_line != line:
                changed = True
            new_lines.append(new_line)
        else:
            new_lines.append(line)
    if not changed:
        return False
    new_text = before + "\n".join(new_lines) + "\n" + after
    md_path.write_text(new_text)
    return True


def main():
    title_to_path = build_title_to_path()
    count = 0
    for md in DOCS.rglob("*.md"):
        if md.name in ("index.md", "TOPICS.md", "full-index.md") or md == DOCS / "index.md":
            continue
        if process_file(md, title_to_path):
            count += 1
            print(md.relative_to(DOCS))
    print(f"Updated {count} files.")


if __name__ == "__main__":
    main()
