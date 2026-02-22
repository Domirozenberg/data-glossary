"""MkDocs plugin: run section index update and related-topics linking before each build.
   Also expands nav so each category includes index + all topic pages (same order as
   section indexes), enabling prev/next navigation within categories."""
from pathlib import Path
import subprocess
import sys

from mkdocs.plugins import BasePlugin, get_plugin_logger

log = get_plugin_logger(__name__)


def _expand_section_nav(nav, docs_dir: Path):
    """Replace each 'Section': 'category/index.md' with Section: [ index, topic1, ... ] (sorted)."""
    out = []
    for item in nav:
        if isinstance(item, dict):
            for title, value in item.items():
                if isinstance(value, str) and value.endswith("/index.md"):
                    section_dir = docs_dir / value[: -len("/index.md")]
                    if section_dir.is_dir():
                        topic_files = sorted(
                            f for f in section_dir.glob("*.md") if f.name != "index.md"
                        )
                        rel_paths = [value]
                        for f in topic_files:
                            rel_paths.append(
                                str(f.relative_to(docs_dir)).replace("\\", "/")
                            )
                        out.append({title: rel_paths})
                        log.debug("Expanded nav for %s: %d pages", title, len(rel_paths))
                    else:
                        out.append(item)
                else:
                    out.append(item)
        else:
            out.append(item)
    return out


def _run_script(project_root: Path, name: str, script_path: Path) -> None:
    if not script_path.exists():
        log.warning("Script not found: %s", script_path)
        return
    try:
        subprocess.run(
            [sys.executable, str(script_path)],
            cwd=str(project_root),
            check=True,
            capture_output=True,
            text=True,
        )
        log.info("%s completed", name)
    except subprocess.CalledProcessError as e:
        log.warning("%s failed: %s", name, e.stderr or e)
    except Exception as e:
        log.warning("%s error: %s", name, e)


class SectionIndexUpdaterPlugin(BasePlugin):
    """Runs scripts before each build: section indexes (🛠 marks) and related-topics linking.
       Expands nav so prev/next (navigation.footer) works within each category."""

    def on_config(self, config, **kwargs):
        """Expand nav: each category index becomes index + all topic pages (alphabetical)."""
        project_root = Path(__file__).resolve().parent.parent
        docs_dir = project_root / config["docs_dir"]
        nav = config.get("nav", [])
        config["nav"] = _expand_section_nav(nav, docs_dir)
        return config

    def on_pre_build(self, config, **kwargs):
        project_root = Path(__file__).resolve().parent.parent
        maintenance_dir = project_root / "scripts" / "maintenance"
        _run_script(
            project_root,
            "Section indexes (Products & Tools marks)",
            maintenance_dir / "update-section-indexes.py",
        )
        _run_script(
            project_root,
            "Related topics linking",
            maintenance_dir / "link-related-topics.py",
        )
