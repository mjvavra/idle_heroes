"""Copy the knowledge-base folders into _site_src/ for MkDocs to build.

Keeps the repo layout as-is and leaves out templates, CLAUDE.md and screenshots.
Usage: python scripts/assemble_docs.py
"""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "_site_src"
REPO = "https://github.com/mjvavra/idle_heroes"
FOLDERS = ["account", "heroes", "artifacts", "systems", "game-modes", "strategies", "reference", "logs"]

# Clear old files but keep the folders: OneDrive can lock folders and block rmtree.
if OUT.exists():
    for f in OUT.rglob("*"):
        if f.is_file():
            f.unlink()
OUT.mkdir(exist_ok=True)

shutil.copy(ROOT / "README.md", OUT / "index.md")
for folder in FOLDERS:
    src = ROOT / folder
    if src.exists():
        shutil.copytree(src, OUT / folder, ignore=shutil.ignore_patterns("_TEMPLATE.md"),
                        dirs_exist_ok=True)

# MkDocs uses index.md as a folder's landing page.
for readme in OUT.rglob("README.md"):
    readme.rename(readme.with_name("index.md"))

# Fix links: README.md pages are now index.md, and templates aren't published,
# so point template links at GitHub instead.
for page in OUT.rglob("*.md"):
    folder = page.parent.relative_to(OUT).as_posix()
    text = page.read_text(encoding="utf-8")
    text = text.replace("README.md)", "index.md)")
    text = text.replace("(_TEMPLATE.md)", f"({REPO}/blob/main/{folder}/_TEMPLATE.md)")
    page.write_text(text, encoding="utf-8")

print(f"Assembled site source in {OUT}")
