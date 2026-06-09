#!/usr/bin/env python3
"""Validate repository skill documentation consistency."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"

LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
REF_RE = re.compile(r"`?(references/[A-Za-z0-9_.\-/]+\.(?:md|csx))`?")
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
FENCED_CODE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")
PINNED_NUGET_RE = re.compile(r'#r\s+"nuget:\s*[^",]+,\s*[^"]+"')


def is_external_link(target: str) -> bool:
    return (
        "://" in target
        or target.startswith("#")
        or target.startswith("mailto:")
        or target.startswith("tel:")
    )


def strip_anchor(target: str) -> str:
    return target.split("#", 1)[0]


def strip_code(text: str) -> str:
    text = FENCED_CODE_RE.sub("", text)
    return INLINE_CODE_RE.sub("", text)


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}

    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def validate_markdown_links(path: Path) -> list[str]:
    errors: list[str] = []
    text = strip_code(path.read_text(encoding="utf-8"))
    for target in LINK_RE.findall(text):
        target = target.strip()
        if is_external_link(target):
            continue
        target = strip_anchor(target)
        if not target:
            continue
        if not (path.parent / target).resolve().exists():
            errors.append(f"{path.relative_to(ROOT)}: broken relative link: {target}")
    return errors


def validate_reference_mentions(path: Path) -> list[str]:
    errors: list[str] = []
    text = strip_code(path.read_text(encoding="utf-8"))
    for target in REF_RE.findall(text):
        if not (path.parent / target).exists():
            errors.append(f"{path.relative_to(ROOT)}: missing referenced file: {target}")
    return errors


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    readme = skill_dir / "README.md"
    references = skill_dir / "references"
    scripts = skill_dir / "scripts"
    template_csx = references / "template.csx"

    for required in (skill_md, readme, references):
        if not required.exists():
            errors.append(f"{skill_dir.relative_to(ROOT)}: missing {required.name}")

    if skill_md.exists():
        frontmatter = parse_frontmatter(skill_md)
        if frontmatter.get("name") != skill_dir.name:
            errors.append(
                f"{skill_md.relative_to(ROOT)}: frontmatter name must match folder name"
            )
        if not frontmatter.get("description"):
            errors.append(f"{skill_md.relative_to(ROOT)}: missing description")

    markdown_text = ""
    for path in (skill_md, readme):
        if path.exists():
            markdown_text += "\n" + strip_code(path.read_text(encoding="utf-8"))

    supports_csx_mode = "Mode 2" in markdown_text and (
        "CSX" in markdown_text or "dotnet script" in markdown_text
    )
    if supports_csx_mode:
        if not scripts.exists():
            errors.append(
                f"{skill_dir.relative_to(ROOT)}: CSX Mode 2 skills must include scripts/"
            )
        if not template_csx.exists():
            errors.append(
                f"{skill_dir.relative_to(ROOT)}: CSX Mode 2 skills must include references/template.csx"
            )

    return errors


def validate_template(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    if PINNED_NUGET_RE.search(text):
        errors.append(
            f"{path.relative_to(ROOT)}: avoid pinned versions in dotnet-script #r nuget references"
        )
    if 'Syncfusion.Licensing' not in text:
        errors.append(
            f"{path.relative_to(ROOT)}: template should reference Syncfusion.Licensing"
        )
    return errors


def main() -> int:
    errors: list[str] = []

    if not SKILLS_DIR.exists():
        print("Missing skills directory", file=sys.stderr)
        return 1

    for skill_dir in sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir()):
        errors.extend(validate_skill(skill_dir))

    for markdown in sorted(ROOT.rglob("*.md")):
        errors.extend(validate_markdown_links(markdown))
        errors.extend(validate_reference_mentions(markdown))
        text = markdown.read_text(encoding="utf-8")
        if "^xx.x.xx" in text:
            errors.append(
                f"{markdown.relative_to(ROOT)}: replace placeholder package version ^xx.x.xx"
            )

    for template in sorted(SKILLS_DIR.glob("*/references/template.csx")):
        errors.extend(validate_template(template))

    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Skill validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
