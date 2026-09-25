#!/usr/bin/env node
// Kymaean website tool. Zero dependencies (Node 20+).
//
//   node tools/site.mjs stamp   rewrite ?v= content hashes and the CSP inline-script hashes
//   node tools/site.mjs check   verify the site is consistent; exits 1 on any failure
//
// Asset URLs carry ?v=<first 8 hex of sha256(file)> so /assets/* can be cached forever.
// The CSP in site/public/_headers allows inline scripts only by exact sha256 hash.

import { readFileSync, writeFileSync, readdirSync, statSync, existsSync } from "node:fs";
import { join, relative, extname, dirname, resolve } from "node:path";
import { createHash } from "node:crypto";
import { fileURLToPath } from "node:url";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const PUB = join(ROOT, "site", "public");
const HEADERS = join(PUB, "_headers");
const ORIGIN = "https://www.kymaean.com";
const BUDGET_KIB = 400; // everything a first visit can download
const FORBIDDEN = [/bellweather/i, /\bbelle\b/i]; // retired character names

const walk = (dir) => readdirSync(dir).flatMap((n) => {
  const p = join(dir, n);
  if (n === ".git" || n === "node_modules" || n === ".wrangler") return [];
  return statSync(p).isDirectory() ? walk(p) : [p];
});
const sha = (buf, enc = "hex") => createHash("sha256").update(buf).digest(enc);
const short = (file) => sha(readFileSync(file)).slice(0, 8);
const REF = /(["'(]|https:\/\/www\.kymaean\.com)(\/[^"'()\s?#]+)\?v=([0-9a-f]{8})/g;
const inlineScripts = (html) => [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map((m) => m[1]);

function stamp() {
  const files = walk(PUB);
  // CSS first: HTML hashes depend on the stamped CSS bytes.
  for (const ext of [".css", ".html"]) {
    for (const f of files.filter((f) => extname(f) === ext)) {
      const before = readFileSync(f, "utf8");
      const after = before.replace(REF, (m, q, p) => {
        const target = join(PUB, p);
        if (!existsSync(target)) throw new Error(`${relative(ROOT, f)}: missing ${p}`);
        return `${q}${p}?v=${short(target)}`;
      });
      if (after !== before) { writeFileSync(f, after); console.log("stamped", relative(ROOT, f)); }
    }
  }
  const hashes = [...new Set(files.filter((f) => extname(f) === ".html")
    .flatMap((f) => inlineScripts(readFileSync(f, "utf8")))
    .map((s) => `'sha256-${sha(s, "base64")}'`))].sort();
  const h = readFileSync(HEADERS, "utf8");
  const next = h.replace(/^(\s*Content-Security-Policy:[^\n]*?script-src )[^;\n]*;/m, `$1${hashes.join(" ") || "'none'"};`);
  if (next !== h) { writeFileSync(HEADERS, next); console.log("stamped site/public/_headers (CSP)"); }
}

function check() {
  const problems = [];
  const bad = (msg) => problems.push(msg);
  const files = walk(PUB);
  const headers = readFileSync(HEADERS, "utf8");
  const csp = (headers.match(/^\s*Content-Security-Policy:([^\n]*)$/m) || [])[1] || "";
  if (!/^\/\*\s*$/m.test(headers)) bad("_headers: missing the /* rule");
  for (const d of ["default-src 'none'", "script-src ", "frame-ancestors 'none'", "base-uri 'none'"]) {
    if (!csp.includes(d)) bad(`_headers: CSP is missing ${d.trim()}`);
  }

  for (const f of files.filter((f) => [".html", ".css"].includes(extname(f)))) {
    const rel = relative(ROOT, f);
    const text = readFileSync(f, "utf8");
    for (const [, , p, v] of text.matchAll(REF)) {
      const target = join(PUB, p);
      if (!existsSync(target)) bad(`${rel}: ${p} does not exist`);
      else if (short(target) !== v) bad(`${rel}: ${p}?v=${v} is stale (run: node tools/site.mjs stamp)`);
    }
    for (const [, url] of text.matchAll(/(?:src|href)="(\/[^"?#]*)/g)) {
      if (!existsSync(join(PUB, url === "/" ? "index.html" : url))) bad(`${rel}: ${url} does not exist`);
    }
    for (const [, url] of text.matchAll(/(https?:\/\/[^"'\s)<]+)/g)) {
      if (!url.startsWith(ORIGIN) && !url.startsWith("http://www.w3.org/")) bad(`${rel}: external URL ${url}`);
    }
    if (extname(f) === ".html") {
      for (const need of ['<html lang="', "<title>", 'name="viewport"', 'name="description"', "<main"]) {
        if (!text.includes(need)) bad(`${rel}: missing ${need}`);
      }
      for (const s of inlineScripts(text)) {
        if (!csp.includes(`'sha256-${sha(s, "base64")}'`)) bad(`${rel}: inline script hash not in CSP (run stamp)`);
      }
    }
  }
  if (!existsSync(join(PUB, "404.html"))) bad("site/public/404.html is missing");

  const kib = files.reduce((n, f) => n + statSync(f).size, 0) / 1024;
  if (kib > BUDGET_KIB) bad(`site/public is ${kib.toFixed(1)} KiB; budget is ${BUDGET_KIB} KiB`);

  const textExt = new Set([".html", ".css", ".js", ".mjs", ".md", ".json", ".jsonc", ".txt", ".yml", ".svg", ".xml", ""]);
  for (const f of walk(ROOT).filter((f) => textExt.has(extname(f)) && !f.endsWith("site.mjs"))) {
    const text = readFileSync(f, "utf8");
    for (const re of FORBIDDEN) if (re.test(text)) bad(`${relative(ROOT, f)}: contains retired term ${re}`);
  }

  if (problems.length) { console.error(problems.map((p) => "FAIL " + p).join("\n")); process.exit(1); }
  console.log(`PASS  ${files.length} files, ${kib.toFixed(1)} KiB published`);
}

const cmd = process.argv[2];
if (cmd === "stamp") stamp();
else if (cmd === "check") check();
else { console.error("usage: node tools/site.mjs stamp|check"); process.exit(2); }
