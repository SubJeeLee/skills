#!/usr/bin/env python3
"""Render an agent-authored architecture model as an offline HTML code tour."""

import argparse
import html
import json
from pathlib import Path
import re
import sys


STATES = {'planned', 'implemented', 'verified', 'unknown'}


def text(value, where):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f'{where}: expected a non-empty string')


def strings(value, where):
    if not isinstance(value, list) or any(not isinstance(x, str) for x in value):
        raise ValueError(f'{where}: expected an array of strings')


def evidence(item, where):
    state = item.get('status')
    if state not in STATES:
        raise ValueError(f'{where}: status must be one of {sorted(STATES)}')
    for key in ('sources', 'evidence'):
        strings(item.get(key, []), f'{where}.{key}')
    if state in {'implemented', 'verified'} and not any(s.strip() for s in item.get('sources', [])):
        raise ValueError(f'{where}: implemented/verified needs source references')
    if state == 'verified' and not any(s.strip() for s in item.get('evidence', [])):
        raise ValueError(f'{where}: verified needs actual execution evidence')


def validate(model):
    if not isinstance(model, dict) or model.get('version') != 1:
        raise ValueError('Expected an object with version: 1')
    for key in ('title', 'scope', 'snapshot'):
        text(model.get(key), key)
    diagrams = model.get('diagrams')
    if not isinstance(diagrams, list) or not diagrams:
        raise ValueError('diagrams: expected a non-empty array')
    diagram_ids = set()
    for di, diagram in enumerate(diagrams):
        where = f'diagrams[{di}]'
        if not isinstance(diagram, dict):
            raise ValueError(f'{where}: expected an object')
        for key in ('id', 'title', 'description'):
            text(diagram.get(key), f'{where}.{key}')
        if diagram['id'] in diagram_ids:
            raise ValueError(f'{where}: duplicate diagram id')
        diagram_ids.add(diagram['id'])
        nodes, edges = diagram.get('nodes'), diagram.get('edges')
        if not isinstance(nodes, list) or not nodes or not isinstance(edges, list):
            raise ValueError(f'{where}: expected non-empty nodes and an edges array')
        node_ids, positions = set(), set()
        for ni, node in enumerate(nodes):
            loc = f'{where}.nodes[{ni}]'
            if not isinstance(node, dict):
                raise ValueError(f'{loc}: expected an object')
            for key in ('id', 'label', 'summary'):
                text(node.get(key), f'{loc}.{key}')
            if node['id'] in node_ids:
                raise ValueError(f'{loc}: duplicate node id')
            node_ids.add(node['id'])
            for key, limit in (('column', 8), ('row', 12)):
                value = node.get(key)
                if type(value) is not int or not 0 <= value <= limit:
                    raise ValueError(f'{loc}.{key}: expected an integer between 0 and {limit}')
            position = (node['column'], node['row'])
            if position in positions:
                raise ValueError(f'{loc}: overlapping node position')
            positions.add(position)
            for key in ('inputs', 'outputs', 'conditions', 'failures'):
                strings(node.get(key, []), f'{loc}.{key}')
            evidence(node, loc)
        for ei, edge in enumerate(edges):
            loc = f'{where}.edges[{ei}]'
            if not isinstance(edge, dict):
                raise ValueError(f'{loc}: expected an object')
            for key in ('from', 'to', 'label'):
                text(edge.get(key), f'{loc}.{key}')
            if edge['from'] not in node_ids or edge['to'] not in node_ids:
                raise ValueError(f'{loc}: edge points to an unknown node')
            if edge['from'] == edge['to']:
                raise ValueError(f'{loc}: self-loops should be described in node conditions')
            evidence(edge, loc)
    for key in ('docker', 'decisions', 'questions'):
        if not isinstance(model.get(key, []), list):
            raise ValueError(f'{key}: expected an array')
    strings(model.get('questions', []), 'questions')
    for i, check in enumerate(model.get('docker', [])):
        if not isinstance(check, dict):
            raise ValueError(f'docker[{i}]: expected an object')
        for key in ('item', 'detail'):
            text(check.get(key), f'docker[{i}].{key}')
        evidence(check, f'docker[{i}]')
    for i, decision in enumerate(model.get('decisions', [])):
        if not isinstance(decision, dict):
            raise ValueError(f'decisions[{i}]: expected an object')
        for key in ('choice', 'reason', 'alternatives'):
            text(decision.get(key), f'decisions[{i}].{key}')
        strings(decision.get('evidence', []), f'decisions[{i}].evidence')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('model', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--force', action='store_true', help='Replace this existing output intentionally')
    args = parser.parse_args()
    try:
        model = json.loads(args.model.read_text(encoding='utf-8'))
        validate(model)
        if args.output.resolve() == args.model.resolve():
            raise ValueError('Output must not replace the input model')
        template = Path(__file__).resolve().parents[1] / 'assets' / 'viewer.html'
        if args.output.resolve() == template.resolve():
            raise ValueError('Output must not replace the viewer template')
        payload = json.dumps(model, ensure_ascii=False).replace('&', '\\u0026').replace('<', '\\u003c').replace('>', '\\u003e').replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')
        replacements = {'__MODEL_JSON__': payload, '__PAGE_TITLE__': html.escape(model['title'])}
        page = re.sub(r'__MODEL_JSON__|__PAGE_TITLE__', lambda match: replacements[match.group()], template.read_text(encoding='utf-8'))
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open('w' if args.force else 'x', encoding='utf-8') as stream:
            stream.write(page)
        print(f'Wrote {args.output.resolve()}')
        print('Checked model structure and evidence fields; did not inspect source files or execute the described app/Docker commands.')
        return 0
    except (OSError, ValueError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
