import assert from 'node:assert/strict';
import { mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { renderCofaHtml } from '../skills/visual-explainer/kit/render-cofa.mjs';

const source = `<!doctype html><html lang="ko" data-register="blueprint"><head><title>가상 코드 흐름</title><link rel="stylesheet" href="kit.css" data-ve-kit></head><body><main><figure class="ve-steps"><ve-flow label="입력 검증 후 응답 생성"><ve-node id="validate" at="1 1" data-s="1">검증 함수</ve-node><ve-node id="reply" at="2 1" data-s="2">응답 함수</ve-node><ve-edge from="validate" to="reply" label="valid input" data-s="2"/></ve-flow><div class="ve-player"><ol class="ve-cap"><li data-n="1/2">입력을 검증합니다.</li><li data-n="2/2">응답을 생성합니다.</li></ol><button data-go="-1">이전</button><button data-play>재생</button><input type="range" aria-label="단계"><button data-go="1">다음</button></div><figcaption>합성 설명 모델이며 실제 앱 실행 기록은 아닙니다.</figcaption></figure></main></body></html>`;

const rendered = renderCofaHtml(source);
assert.equal(rendered.report.figures, 1);
assert.equal(rendered.report.uncaptioned, 0);
assert.match(rendered.html, /<svg\b/);
assert.doesNotMatch(rendered.html, /<ve-node\b/);
assert.match(rendered.html, /Content-Security-Policy/);
assert.match(rendered.html, /connect-src 'none'/);
assert.doesNotMatch(rendered.html, /<link\b[^>]*href=["']https:\/\/fonts\./);
assert.throws(() => renderCofaHtml('<html><body>No kit marker</body></html>'), /kit page/);

const dir = mkdtempSync(join(tmpdir(), 'visual-explainer-check-'));
try {
  const input = join(dir, 'flow.src.html'), output = join(dir, 'flow.html');
  writeFileSync(input, source);
  const command = fileURLToPath(new URL('../skills/visual-explainer/kit/render-cofa.mjs', import.meta.url));
  const run = extra => spawnSync(process.execPath, [command, input, '-o', output, ...extra], { encoding: 'utf8' });
  let result = run([]);
  assert.equal(result.status, 0, result.stderr);
  assert.match(result.stdout, /No browser launched or inspected/);
  const before = readFileSync(output, 'utf8');
  result = run([]);
  assert.notEqual(result.status, 0);
  assert.equal(readFileSync(output, 'utf8'), before);
  result = run(['--force']);
  assert.equal(result.status, 0, result.stderr);
  assert.equal(readFileSync(input, 'utf8'), source);
  console.log('PASS: bundled kit renders HTML; COFA resource policy, validation errors, CLI output and overwrite behavior checked.');
  console.log('Not checked: model comprehension, COFA registration, browser behavior or app execution.');
} finally { rmSync(dir, { recursive: true, force: true }); }
