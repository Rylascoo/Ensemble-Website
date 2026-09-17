import fs from 'node:fs';
import http from 'node:http';
import os from 'node:os';
import path from 'node:path';
import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const browser = process.env.BROWSER;
if (!browser) throw new Error('BROWSER not set');
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const publicRoot = path.join(root, 'site', 'public');
const output = process.argv[2] || path.join(os.tmpdir(), 'website-narrative-cadence.json');
const captureRoot = process.argv[3] || path.join(os.tmpdir(), 'website-narrative-cadence-captures');
const profile = path.join(os.tmpdir(), `website-narrative-cadence-edge-${process.pid}`);
fs.mkdirSync(profile, { recursive: true });
fs.mkdirSync(captureRoot, { recursive: true });

const types = new Map([
  ['.html', 'text/html; charset=utf-8'], ['.css', 'text/css; charset=utf-8'],
  ['.js', 'text/javascript; charset=utf-8'], ['.png', 'image/png'],
  ['.webp', 'image/webp'], ['.jpg', 'image/jpeg'], ['.svg', 'image/svg+xml']
]);
const server = http.createServer((req, res) => {
  const url = new URL(req.url, 'http://127.0.0.1');
  const rel = url.pathname === '/' ? 'index.html' : url.pathname.replace(/^\/+/, '');
  const file = path.resolve(publicRoot, rel);
  if (!file.startsWith(publicRoot) || !fs.existsSync(file) || !fs.statSync(file).isFile()) {
    res.writeHead(404); res.end('not found'); return;
  }
  res.writeHead(200, { 'content-type': types.get(path.extname(file).toLowerCase()) || 'application/octet-stream' });
  fs.createReadStream(file).pipe(res);
});

await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
const origin = `http://127.0.0.1:${server.address().port}`;
const cp = spawn(browser, [
  '--headless=new', '--no-sandbox', '--disable-gpu', '--disable-dev-shm-usage',
  '--disable-extensions', '--remote-debugging-port=0', `--user-data-dir=${profile}`, 'about:blank'
], { stdio: ['ignore', 'ignore', 'inherit'] });
const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
async function cdpPort() {
  const file = path.join(profile, 'DevToolsActivePort');
  for (let i = 0; i < 300; i++) {
    if (fs.existsSync(file)) {
      const [port] = fs.readFileSync(file, 'utf8').trim().split(/\r?\n/);
      if (port) return port;
    }
    await sleep(100);
  }
  throw new Error('CDP port unavailable');
}
let ws, id = 0;
const pending = new Map();
function send(method, params = {}) {
  return new Promise((resolve, reject) => {
    const requestId = ++id;
    pending.set(requestId, { resolve, reject });
    ws.send(JSON.stringify({ id: requestId, method, params }));
  });
}
async function evalv(expression) {
  const result = await send('Runtime.evaluate', { expression, returnByValue: true, awaitPromise: true });
  if (result.exceptionDetails) throw new Error(JSON.stringify(result.exceptionDetails));
  return result.result.value;
}
async function waitReady() {
  for (let i = 0; i < 120; i++) {
    if (await evalv('!!window.__KYM_TEMPORAL__ && document.readyState === "complete"')) return;
    await sleep(50);
  }
  throw new Error('candidate API unavailable');
}
async function capture(name) {
  const result = await send('Page.captureScreenshot', { format: 'png', captureBeyondViewport: false });
  fs.writeFileSync(path.join(captureRoot, `${name}.png`), Buffer.from(result.data, 'base64'));
}

const viewports = [[2048,1199],[1235,647],[1138,1354],[1227,1422],[768,1024],[600,900],[599,900],[390,844],[320,640]];
const results = { source: origin, viewports: [], interaction: {}, reducedMotion: {}, accessibility: {}, assets: {} };
try {
  const port = await cdpPort();
  const target = await (await fetch(`http://127.0.0.1:${port}/json/new?about%3Ablank`, { method: 'PUT' })).json();
  ws = new WebSocket(target.webSocketDebuggerUrl);
  await new Promise((resolve, reject) => { ws.onopen = resolve; ws.onerror = reject; });
  ws.onmessage = event => {
    const message = JSON.parse(event.data);
    if (!message.id || !pending.has(message.id)) return;
    const request = pending.get(message.id); pending.delete(message.id);
    message.error ? request.reject(new Error(JSON.stringify(message.error))) : request.resolve(message.result);
  };
  await send('Page.enable'); await send('Runtime.enable');
  for (const [width, height] of viewports) {
    await send('Emulation.setDeviceMetricsOverride', { width, height, deviceScaleFactor: 1, mobile: false, screenWidth: width, screenHeight: height });
    await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'no-preference' }] });
    await send('Page.navigate', { url: `${origin}/` });
    await waitReady(); await sleep(100);
    const metrics = await evalv(`(()=>{const b=document.querySelector('.brand-lockup').getBoundingClientRect(),w=document.querySelector('.wordmark').getBoundingClientRect(),scene=document.querySelector('.scene-art'),p=document.querySelector('.presence-carrier'),q=document.querySelector('.person-carrier');return {overflowX:document.documentElement.scrollWidth-document.documentElement.clientWidth,brandCenter:b.left+b.width/2,viewportCenter:innerWidth/2,wordmarkContained:w.left>=0&&w.right<=innerWidth,stageNatural:[scene.naturalWidth,scene.naturalHeight],presenceNatural:[p.naturalWidth,p.naturalHeight],personNatural:[q.naturalWidth,q.naturalHeight],state:window.__KYM_TEMPORAL__.state}})()`);
    await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] });
    const geometry = await evalv(`(()=>{const brand=document.querySelector('.brand-lockup').getBoundingClientRect(),items={presence:'.presence-carrier',person:'.person-carrier',trace:'.trace-evidence',life:'.life-evidence'},out={};for(const [state,sel] of Object.entries(items)){window.__KYM_TEMPORAL__.set(window.__KYM_TEMPORAL__.order.indexOf(state));const r=document.querySelector(sel).getBoundingClientRect();out[state]={heightRatio:+(r.height/innerHeight).toFixed(3),withinX:r.right>0&&r.left<innerWidth,withinY:r.bottom>0&&r.top<innerHeight,overlapsBrand:!(r.right<brand.left||r.left>brand.right||r.bottom<brand.top||r.top>brand.bottom)}}return out})()`);
    results.viewports.push({ width, height, ...metrics, geometry });
  }

  await send('Emulation.setDeviceMetricsOverride', { width: 1235, height: 647, deviceScaleFactor: 1, mobile: false, screenWidth: 1235, screenHeight: 647 });
  await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'no-preference' }] });
  await send('Page.navigate', { url: `${origin}/` }); await waitReady();
  results.interaction.initial = await evalv('window.__KYM_TEMPORAL__.snapshot()');
  results.interaction.timing = await evalv('window.__KYM_TEMPORAL__.timing');

  await evalv(`(()=>{const e=document.getElementById('main');e.focus();e.dispatchEvent(new KeyboardEvent('keydown',{key:'ArrowDown',bubbles:true,cancelable:true}));return true})()`);
  await sleep(340);
  results.interaction.keyboardPresence = await evalv('window.__KYM_TEMPORAL__.snapshot()');

  await evalv(`(()=>{window.dispatchEvent(new WheelEvent('wheel',{deltaY:80,bubbles:true}));return true})()`);
  await sleep(330);
  results.interaction.wheelPersonDuringEmpty = await evalv('window.__KYM_TEMPORAL__.snapshot()');
  await sleep(360);
  results.interaction.wheelPersonRevealed = await evalv('window.__KYM_TEMPORAL__.snapshot()');

  await evalv(`(()=>{const e=document.getElementById('main');e.dispatchEvent(new KeyboardEvent('keydown',{key:'ArrowUp',bubbles:true,cancelable:true}));return true})()`);
  await sleep(330);
  results.interaction.keyboardReverseDuringEmpty = await evalv('window.__KYM_TEMPORAL__.snapshot()');
  await sleep(360);
  results.interaction.keyboardReverseRevealed = await evalv('window.__KYM_TEMPORAL__.snapshot()');

  await send('Page.navigate', { url: `${origin}/` }); await waitReady();
  results.interaction.wheelBurstSingleStep = await evalv(`(()=>{for(let i=0;i<6;i++)window.dispatchEvent(new WheelEvent('wheel',{deltaY:80,bubbles:true}));return window.__KYM_TEMPORAL__.snapshot()})()`);
  await sleep(260);
  results.interaction.wheelSecondGesture = await evalv(`(()=>{window.dispatchEvent(new WheelEvent('wheel',{deltaY:80,bubbles:true}));return window.__KYM_TEMPORAL__.snapshot()})()`);
  await sleep(690);
  results.interaction.wheelSecondGestureRevealed = await evalv('window.__KYM_TEMPORAL__.snapshot()');

  await send('Page.navigate', { url: `${origin}/` }); await waitReady();
  results.interaction.wheelChapterSequence = [];
  for (let n = 0; n < 4; n++) {
    await evalv(`(()=>{window.dispatchEvent(new WheelEvent('wheel',{deltaY:80,bubbles:true}));return true})()`);
    await sleep(900);
    results.interaction.wheelChapterSequence.push(await evalv('window.__KYM_TEMPORAL__.snapshot()'));
  }
  results.interaction.wheelReverseSequence = [];
  for (let n = 0; n < 4; n++) {
    await evalv(`(()=>{window.dispatchEvent(new WheelEvent('wheel',{deltaY:-80,bubbles:true}));return true})()`);
    await sleep(900);
    results.interaction.wheelReverseSequence.push(await evalv('window.__KYM_TEMPORAL__.snapshot()'));
  }

  await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 1, mobile: false, screenWidth: 390, screenHeight: 844 });
  await send('Page.navigate', { url: `${origin}/` }); await waitReady();
  results.interaction.touch = await evalv(`(()=>{const e=document.getElementById('main');const a=new Touch({identifier:1,target:e,clientX:180,clientY:620});const b=new Touch({identifier:1,target:e,clientX:180,clientY:500});e.dispatchEvent(new TouchEvent('touchstart',{touches:[a],bubbles:true}));e.dispatchEvent(new TouchEvent('touchend',{changedTouches:[b],bubbles:true}));return window.__KYM_TEMPORAL__.snapshot()})()`);

  await evalv('window.__KYM_TEMPORAL__.set(0)');
  results.interaction.rapidForwardStart = await evalv(`(()=>{for(let n=0;n<4;n++)window.__KYM_TEMPORAL__.advance();return window.__KYM_TEMPORAL__.snapshot()})()`);
  await sleep(690);
  results.interaction.rapidForwardSettled = await evalv('window.__KYM_TEMPORAL__.snapshot()');
  results.interaction.rapidReverseStart = await evalv(`(()=>{for(let n=0;n<3;n++)window.__KYM_TEMPORAL__.reverse();return window.__KYM_TEMPORAL__.snapshot()})()`);
  await sleep(690);
  results.interaction.rapidReverseSettled = await evalv('window.__KYM_TEMPORAL__.snapshot()');
  results.interaction.focusAfterRetarget = await evalv(`(()=>{const e=document.getElementById('main');e.focus();window.__KYM_TEMPORAL__.advance();window.__KYM_TEMPORAL__.reverse();return {activeId:document.activeElement.id,state:window.__KYM_TEMPORAL__.state,renderState:window.__KYM_TEMPORAL__.renderState}})()`);

  await send('Page.navigate', { url: `${origin}/` }); await waitReady();
  await evalv('window.__KYM_TEMPORAL__.set(1)'); await sleep(340);
  await evalv('window.__KYM_TEMPORAL__.advance()'); await sleep(330);
  results.interaction.automaticEmptyProof = await evalv('window.__KYM_TEMPORAL__.snapshot()');
  await sleep(360);
  results.interaction.automaticRevealProof = await evalv('window.__KYM_TEMPORAL__.snapshot()');
  await evalv('window.__KYM_TEMPORAL__.advance()'); await sleep(120);
  await evalv('window.__KYM_TEMPORAL__.advance()'); await sleep(250);
  results.interaction.interruptedEmptyRetarget = await evalv('window.__KYM_TEMPORAL__.snapshot()');
  await sleep(350);
  results.interaction.interruptedRetargetSettled = await evalv('window.__KYM_TEMPORAL__.snapshot()');

  await send('Page.navigate', { url: `${origin}/` }); await waitReady();
  await evalv(`(()=>{const e=document.getElementById('main');e.focus();e.dispatchEvent(new KeyboardEvent('keydown',{key:'End',bubbles:true,cancelable:true}));return true})()`);
  await sleep(900);
  results.interaction.endKey = await evalv('window.__KYM_TEMPORAL__.snapshot()');
  await evalv(`(()=>{const e=document.getElementById('main');e.dispatchEvent(new KeyboardEvent('keydown',{key:'Home',bubbles:true,cancelable:true}));return true})()`);
  await sleep(340);
  results.interaction.homeKey = await evalv('window.__KYM_TEMPORAL__.snapshot()');

  await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] });
  await send('Page.navigate', { url: `${origin}/` }); await waitReady();
  results.reducedMotion.initial = await evalv(`({snapshot:window.__KYM_TEMPORAL__.snapshot(),animations:document.getAnimations().filter(a=>a.playState==='running').length})`);
  results.reducedMotion.sequence = await evalv(`(()=>{const states=[];for(let n=0;n<4;n++){window.__KYM_TEMPORAL__.advance();states.push(window.__KYM_TEMPORAL__.state)}return {states,snapshot:window.__KYM_TEMPORAL__.snapshot(),animations:document.getAnimations().filter(a=>a.playState==='running').length}})()`);

  await send('Emulation.setDeviceMetricsOverride', { width: 320, height: 640, deviceScaleFactor: 1, mobile: false, screenWidth: 320, screenHeight: 640 });
  await send('Emulation.setEmulatedMedia', { features: [] });
  await send('Page.navigate', { url: `${origin}/` }); await waitReady();
  results.accessibility.text200 = await evalv(`(()=>{document.documentElement.style.fontSize='32px';const w=document.querySelector('.wordmark').getBoundingClientRect();return {overflowX:document.documentElement.scrollWidth-document.documentElement.clientWidth,wordmarkContained:w.left>=0&&w.right<=innerWidth}})()`);
  await evalv(`document.documentElement.style.fontSize=''`);
  for (let n = 0; n < 2; n++) {
    await send('Input.dispatchKeyEvent', { type: 'keyDown', key: 'Tab', code: 'Tab', windowsVirtualKeyCode: 9 });
    await send('Input.dispatchKeyEvent', { type: 'keyUp', key: 'Tab', code: 'Tab', windowsVirtualKeyCode: 9 });
  }
  results.accessibility.focus = await evalv(`(()=>{const e=document.getElementById('main'),s=getComputedStyle(e);return {activeId:document.activeElement.id,matchesFocus:e.matches(':focus'),matchesFocusVisible:e.matches(':focus-visible'),boxShadow:s.boxShadow}})()`);
  await send('Emulation.setEmulatedMedia', { features: [{ name: 'forced-colors', value: 'active' }] });
  results.accessibility.forcedColors = await evalv(`(()=>({matches:matchMedia('(forced-colors: active)').matches,sceneDisplay:getComputedStyle(document.querySelector('.scene')).display,presenceDisplay:getComputedStyle(document.querySelector('.presence-carrier')).display,wordmarkDisplay:getComputedStyle(document.querySelector('.wordmark')).display,statusDisplay:getComputedStyle(document.querySelector('.status')).display}))()`);

  results.assets = await evalv(`(()=>({stage:[document.querySelector('.scene-art').naturalWidth,document.querySelector('.scene-art').naturalHeight],presence:[document.querySelector('.presence-carrier').naturalWidth,document.querySelector('.presence-carrier').naturalHeight],person:[document.querySelector('.person-carrier').naturalWidth,document.querySelector('.person-carrier').naturalHeight]}))()`);

  await send('Emulation.setDeviceMetricsOverride', { width: 2048, height: 1199, deviceScaleFactor: 1, mobile: false, screenWidth: 2048, screenHeight: 1199 });
  await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] });
  await send('Page.navigate', { url: `${origin}/` }); await waitReady();
  await capture('wide-place');
  await evalv('window.__KYM_TEMPORAL__.set(2)'); await capture('wide-person');
  await evalv('window.__KYM_TEMPORAL__.set(3)'); await capture('wide-trace');
  await evalv('window.__KYM_TEMPORAL__.set(4)'); await capture('wide-life');

  await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 1, mobile: false, screenWidth: 390, screenHeight: 844 });
  await send('Page.navigate', { url: `${origin}/` }); await waitReady();
  await evalv('window.__KYM_TEMPORAL__.set(2)'); await capture('mobile-person');
  await evalv('window.__KYM_TEMPORAL__.set(4)'); await capture('mobile-life');

  fs.mkdirSync(path.dirname(output), { recursive: true });
  fs.writeFileSync(output, JSON.stringify(results, null, 2) + '\n');
  console.log(JSON.stringify(results, null, 2));
  ws.close();
} finally {
  server.closeAllConnections?.();
  await new Promise(resolve => server.close(resolve));
  if (process.platform === 'win32' && cp.pid) {
    const killer = spawn('taskkill', ['/PID', String(cp.pid), '/T', '/F'], { stdio: 'ignore' });
    await new Promise(resolve => killer.once('exit', resolve));
    const escapedProfile = profile.replaceAll("'", "''");
    const reaper = spawn('powershell.exe', ['-NoProfile', '-Command', `$p='${escapedProfile}'; Get-CimInstance Win32_Process | Where-Object { $_.Name -eq 'msedge.exe' -and $_.CommandLine -like ('*' + $p + '*') } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }`], { stdio: 'ignore' });
    await Promise.race([new Promise(resolve => reaper.once('exit', resolve)), sleep(2000)]);
    await sleep(250);
  } else {
    cp.kill('SIGTERM');
    await Promise.race([new Promise(resolve => cp.once('exit', resolve)), sleep(1200)]);
  }
  for (let attempt = 0; attempt < 8 && fs.existsSync(profile); attempt += 1) {
    try { fs.rmSync(profile, { recursive: true, force: true }); } catch {}
    if (fs.existsSync(profile)) await sleep(250);
  }
}
