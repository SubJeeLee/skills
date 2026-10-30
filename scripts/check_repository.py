#!/usr/bin/env python3
"""Check repository-local Markdown targets and minimal skill metadata. No network."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    errors = []
    markdown_files = sorted(ROOT.rglob('*.md'))
    for path in markdown_files:
        if '.git' in path.relative_to(ROOT).parts:
            continue
        content = path.read_text(encoding='utf-8')
        for match in re.finditer(r'\]\(([^)]+)\)', content):
            target = match.group(1).split('#', 1)[0]
            if not target or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.is_relative_to(ROOT):
                errors.append(f'{path.relative_to(ROOT)}: target escapes repository: {target}')
            elif not resolved.exists():
                errors.append(f'{path.relative_to(ROOT)}: missing target: {target}')

    skills = sorted((ROOT / 'skills').glob('*/SKILL.md'))
    if not skills:
        errors.append('No SKILL.md files found')
    for path in skills:
        text = path.read_text(encoding='utf-8')
        header = re.match(r'\A---\n(.*?)\n---(?:\n|$)', text, re.S)
        if not header:
            errors.append(f'{path.relative_to(ROOT)}: missing YAML frontmatter')
            continue
        values = dict(re.findall(r'^(name|description):[ \t]*(.+)$', header.group(1), re.M))
        name = values.get('name', '')
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64:
            errors.append(f'{path.relative_to(ROOT)}: invalid name')
        if name != path.parent.name:
            errors.append(f'{path.relative_to(ROOT)}: folder/name mismatch')
        if not values.get('description', '').strip():
            errors.append(f'{path.relative_to(ROOT)}: missing description')

    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'PASS: checked local Markdown targets and metadata for {len(skills)} skill(s).')
    print('Not checked: remote links, runtime compatibility, behavior, or exam permissions.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
