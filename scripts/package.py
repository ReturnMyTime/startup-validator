# /// script
# requires-python = ">=3.11"
# ///
"""Package the startup-validator skill into a distributable zip file."""

import re
import zipfile
from pathlib import Path


def get_version(skill_path: Path) -> str:
    """Extract version from SKILL.md frontmatter."""
    content = skill_path.read_text()
    match = re.search(r"^version:\s*(.+)$", content, re.MULTILINE)
    if not match:
        raise ValueError("Could not find version in SKILL.md frontmatter")
    return match.group(1).strip()


def package(project_root: Path) -> Path:
    """Create a zip file with the skill contents."""
    skill_path = project_root / "SKILL.md"
    readme_path = project_root / "README.md"
    dist_dir = project_root / "dist"
    dist_dir.mkdir(exist_ok=True)

    version = get_version(skill_path)
    zip_name = f"startup-validator-v{version}.zip"
    zip_path = dist_dir / zip_name

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(skill_path, "startup-validator/SKILL.md")
        zf.write(readme_path, "startup-validator/README.md")

    print(f"Packaged: {zip_path}")
    print(f"Version:  {version}")
    print(f"Size:     {zip_path.stat().st_size:,} bytes")
    return zip_path


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    package(root)
