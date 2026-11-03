#!/usr/bin/env node
// Local COFA adapter; upstream MIT renderer and resources remain unchanged.
import { lstatSync, readFileSync, realpathSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';
import { prepareRenderedHtml, renderPage, reportLine } from './render.mjs';

const CSP = "default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; img-src data:; font-src data:; connect-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'";

export function renderCofaHtml(source, root = process.cwd()) {
  const result = renderPage(source, { root, models: false });
  if (result.errors.length) throw new Error(result.errors.join('\n'));
  if (!result.kit) throw new Error('Expected a kit page with a data-ve-kit stylesheet marker');
  let html = prepareRenderedHtml(result.html);
  html = html.replace(/<link\b[^>]*\bhref=["']https:\/\/fonts\.(?:googleapis|gstatic)\.com[^>]*>/gi, '');
  html = html.replace(/<head\b[^>]*>/i, head => `${head}\n<meta http-equiv="Content-Security-Policy" content="${CSP}">`);
  return { html, warnings: result.warnings, report: result.report };
}

function main() {
  const args = process.argv.slice(2);
  let input, output, root = process.cwd(), force = false;
  for (let i = 0; i < args.length; i++) {
    if (args[i] === '--force') force = true;
    else if (args[i] === '-o' || args[i] === '--root') {
      const flag = args[i], value = args[++i];
      if (!value || value.startsWith('-')) throw new Error(`Missing value for ${flag}`);
      if (flag === '-o') output = value; else root = value;
    } else if (args[i].startsWith('-') || input) throw new Error(`Unexpected argument: ${args[i]}`);
    else input = args[i];
  }
  if (!input) throw new Error('Usage: node render-cofa.mjs page.src.html [-o page.html] [--root project] [--force]');
  output ??= input.endsWith('.src.html') ? input.slice(0, -9) + '.html' : undefined;
  if (!output) throw new Error('Name the input *.src.html or specify -o output.html');
  if (resolve(input) === resolve(output)) throw new Error('Output must not replace the source');
  if (lstatSync(output, { throwIfNoEntry: false })?.isSymbolicLink()) throw new Error('Output must not be a symlink');
  const result = renderCofaHtml(readFileSync(input, 'utf8'), root);
  writeFileSync(output, result.html, { flag: force ? 'w' : 'wx' });
  console.log(`Wrote ${resolve(output)}`);
  console.log(reportLine(result.report));
  for (const warning of result.warnings) console.log(`Warning: ${warning}`);
  console.log('No browser launched or inspected. App behavior and diagram claims were not verified by this renderer.');
}

if (process.argv[1] && import.meta.url === pathToFileURL(realpathSync(process.argv[1])).href) {
  try { main(); } catch (error) { console.error(`ERROR: ${error.message}`); process.exitCode = 1; }
}
