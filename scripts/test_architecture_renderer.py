#!/usr/bin/env python3
"""Exercise model integrity, safe HTML embedding, and overwrite behavior."""

from copy import deepcopy
from html.parser import HTMLParser
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'cofa-architecture-tour'
RENDER = SKILL / 'scripts' / 'render.py'
EXAMPLE = json.loads((SKILL / 'assets' / 'example.json').read_text(encoding='utf-8'))


class EmbeddedModel(HTMLParser):
    def __init__(self):
        super().__init__()
        self.inside = False
        self.data = ''
        self.script_count = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'script':
            self.script_count += 1
            self.inside = dict(attrs).get('id') == 'model'

    def handle_endtag(self, tag):
        if tag == 'script':
            self.inside = False

    def handle_data(self, data):
        if self.inside:
            self.data += data


class RendererTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name)
        self.model_path = self.path / 'model.json'
        self.output = self.path / 'tour.html'

    def run_renderer(self, model, *extra):
        self.model_path.write_text(json.dumps(model, ensure_ascii=False), encoding='utf-8')
        return subprocess.run([sys.executable, str(RENDER), str(self.model_path), '--output', str(self.output), *extra], capture_output=True, text=True)

    def test_example_round_trips_without_extra_scripts(self):
        result = self.run_renderer(EXAMPLE)
        self.assertEqual(result.returncode, 0, result.stderr)
        parser = EmbeddedModel()
        parser.feed(self.output.read_text(encoding='utf-8'))
        self.assertEqual(json.loads(parser.data), EXAMPLE)
        self.assertEqual(parser.script_count, 2)

    def test_script_delimiters_and_template_tokens_remain_data(self):
        model = deepcopy(EXAMPLE)
        model['title'] = '__MODEL_JSON__ </script><script>globalThis.injected=true</script> & "'
        model['diagrams'][0]['nodes'][0]['summary'] = '__PAGE_TITLE__ </script><img src=x onerror=alert(1)>'
        result = self.run_renderer(model)
        self.assertEqual(result.returncode, 0, result.stderr)
        parser = EmbeddedModel()
        parser.feed(self.output.read_text(encoding='utf-8'))
        self.assertEqual(json.loads(parser.data), model)
        self.assertEqual(parser.script_count, 2)
        self.assertNotIn('<img ', self.output.read_text(encoding='utf-8'))

    def test_rejects_verified_without_execution_evidence(self):
        model = deepcopy(EXAMPLE)
        model['diagrams'][0]['nodes'][0].update(status='verified', sources=['synthetic-fixture.py:1'])
        result = self.run_renderer(model)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('execution evidence', result.stderr)
        self.assertFalse(self.output.exists())

    def test_rejects_implemented_without_code_sources(self):
        model = deepcopy(EXAMPLE)
        model['diagrams'][0]['edges'][0]['status'] = 'implemented'
        result = self.run_renderer(model)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('source references', result.stderr)

    def test_rejects_dangling_connection_and_overlapping_positions(self):
        for field in ('connection', 'position'):
            with self.subTest(field=field):
                model = deepcopy(EXAMPLE)
                if field == 'connection':
                    model['diagrams'][0]['edges'][0]['to'] = 'missing'
                else:
                    model['diagrams'][0]['nodes'][1]['column'] = 0
                result = self.run_renderer(model)
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse(self.output.exists())

    def test_preserves_existing_output_unless_force_requested(self):
        self.output.write_text('existing user document', encoding='utf-8')
        result = self.run_renderer(EXAMPLE)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.output.read_text(encoding='utf-8'), 'existing user document')
        result = self.run_renderer(EXAMPLE, '--force')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('<!doctype html>', self.output.read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main()
