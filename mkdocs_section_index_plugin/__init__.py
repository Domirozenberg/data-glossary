"""MkDocs plugin: run section index update and related-topics linking before each build."""
from pathlib import Path
import subprocess
import sys

from mkdocs.plugins import BasePlugin, get_plugin_logger

log = get_plugin_logger(__name__)


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
    """Runs scripts before each build: section indexes (🛠 marks) and related-topics linking."""

    def on_pre_build(self, config, **kwargs):
        project_root = Path(__file__).resolve().parent.parent
        scripts_dir = project_root / "scripts"
        _run_script(
            project_root,
            "Section indexes (Products & Tools marks)",
            scripts_dir / "update-section-indexes.py",
        )
        _run_script(
            project_root,
            "Related topics linking",
            scripts_dir / "link-related-topics.py",
        )
