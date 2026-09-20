import { spawn } from 'node:child_process';
import fs from 'node:fs';

const [variant, widthArg, heightArg, screenshotPath, profile] = process.argv.slice(2);
const width = Number(widthArg), height = Number(heightArg);
const browser = process.env.BROWSER;
if (!browser) throw new Error('BROWSER not set');
const url = `http://127.0.0.1:8877/prototypes/website-v2-2-mascot-placement-study/index.html?variant=${variant}`;
fs.rmSync(profile, {recursive:true, force:true});
fs.mkdirSync(profile, {recursive:true});
const args = ['--headless=new','--no-sandbox','--disable-gpu','--disable-dev-shm-usage','--remote-debugging-port=0',`--user-data-dir=${profile}`,'about:blank'];
const cp = spawn(browser, args, {stdio:['ignore','ignore','inherit']});
const sleep = ms => new Promise(r => setTimeout(r, ms));
async function devtoolsPort(){
  const f = profile + '/DevToolsActivePort';
  for(let i=0;i<400;i++){ if(fs.existsSync(f)){ const [p]=fs.readFileSync(f,'utf8').trim().split(/\r?\n/); if(p) return p; } await sleep(50); }
  throw new Error('DevToolsActivePort unavailable');
}
try {
  const port = await devtoolsPort();
  let target;
  for(let i=0;i<100;i++){
    try { const r = await fetch(`http://127.0.0.1:${port}/json/new?about%3Ablank`, {method:'PUT'}); if(r.ok){target=await r.json(); break;} } catch {}
    await sleep(50);
  }
  if(!target?.webSocketDebuggerUrl) throw new Error('page target unavailable');
  const ws = new WebSocket(target.webSocketDebuggerUrl);
  await new Promise((res,rej)=>{ws.onopen=res; ws.onerror=rej;});
  let id=0; const pending=new Map();
  ws.onmessage=e=>{const m=JSON.parse(e.data); if(m.id&&pending.has(m.id)){const q=pending.get(m.id); pending.delete(m.id); m.error?q.rej(new Error(JSON.stringify(m.error))):q.res(m.result);}};
  const send=(method,params={})=>new Promise((res,rej)=>{const n=++id; pending.set(n,{res,rej}); ws.send(JSON.stringify({id:n,method,params}));});
  await send('Page.enable'); await send('Runtime.enable');
  await send('Emulation.setDeviceMetricsOverride',{width,height,deviceScaleFactor:1,mobile:false,screenWidth:width,screenHeight:height});
  const nav=await send('Page.navigate',{url}); if(nav?.errorText) throw new Error(nav.errorText);
  for(let i=0;i<120;i++){
    const ev=await send('Runtime.evaluate',{expression:'document.readyState',returnByValue:true});
    if(ev?.result?.value==='complete') break;
    await sleep(50);
  }
  await send('Runtime.evaluate',{expression:'Promise.all([...document.images].map(i=>i.decode().catch(()=>{})))',awaitPromise:true,returnByValue:true});
  await sleep(variant==='a4' ? 4700 : 1500);
  const info=await send('Runtime.evaluate',{expression:`(()=>{const b=document.querySelector('.brand-lockup')?.getBoundingClientRect();const m=document.querySelector('.bellweather-study')?.getBoundingClientRect();return{variant:document.body.dataset.variant,viewport:[innerWidth,innerHeight],scroll:[document.documentElement.scrollWidth,document.documentElement.scrollHeight],brand:b&&{left:b.left,right:b.right,top:b.top,bottom:b.bottom,width:b.width,height:b.height},mascot:m&&{left:m.left,right:m.right,top:m.top,bottom:m.bottom,width:m.width,height:m.height,opacity:getComputedStyle(document.querySelector('.bellweather-study')).opacity}}})()`,returnByValue:true});
  const shot=await send('Page.captureScreenshot',{format:'png',captureBeyondViewport:false});
  fs.writeFileSync(screenshotPath,Buffer.from(shot.data,'base64'));
  fs.writeFileSync(screenshotPath.replace(/\.png$/i,'.json'),JSON.stringify(info?.result?.value,null,2)+'\n');
  ws.close();
} finally {
  cp.kill('SIGTERM');
  await Promise.race([new Promise(r=>cp.once('exit',r)),sleep(1200)]);
}


