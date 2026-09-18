import {spawn} from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const here=path.dirname(fileURLToPath(import.meta.url));
const browser=process.env.BROWSER;
const pageUrl=process.env.MOTION01_URL||'http://127.0.0.1:8765/prototypes/website-concealed-production-motion-choreography-01/index.html';
if(!browser) throw new Error('BROWSER not set');
const profile=path.join(here,'.edge-profile-'+process.pid);
const width=Number(process.env.MOTION01_WIDTH||1000);
const height=Number(process.env.MOTION01_HEIGHT||700);
const label=(process.env.MOTION01_LABEL||'wide').replace(/[^a-z0-9_-]/gi,'-');
const framesDir=path.join(here,'frames-'+label);
const diagPath=path.join(here,'motion-diagnostics-'+label+'.json');
fs.rmSync(profile,{recursive:true,force:true});
fs.rmSync(framesDir,{recursive:true,force:true});
fs.mkdirSync(profile,{recursive:true});
fs.mkdirSync(framesDir,{recursive:true});
const cp=spawn(browser,['--headless=new','--no-sandbox','--disable-gpu','--remote-debugging-port=0',`--user-data-dir=${profile}`,'about:blank'],{stdio:['ignore','ignore','inherit']});
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
async function port(){
  const f=path.join(profile,'DevToolsActivePort');
  for(let i=0;i<300;i++){if(fs.existsSync(f)){const [p]=fs.readFileSync(f,'utf8').trim().split(/\r?\n/);if(p)return p;}await sleep(50);}
  throw new Error('DevToolsActivePort unavailable');
}

try{
  const p=await port();
  const r=await fetch(`http://127.0.0.1:${p}/json/new?about%3Ablank`,{method:'PUT'});
  const target=await r.json();
  const ws=new WebSocket(target.webSocketDebuggerUrl);
  await new Promise((res,rej)=>{ws.onopen=res;ws.onerror=rej});
  let id=0;const pending=new Map();
  ws.onmessage=e=>{const m=JSON.parse(e.data);if(m.id&&pending.has(m.id)){const q=pending.get(m.id);pending.delete(m.id);m.error?q.rej(new Error(JSON.stringify(m.error))):q.res(m.result)}};
  const send=(method,params={})=>new Promise((res,rej)=>{const n=++id;pending.set(n,{res,rej});ws.send(JSON.stringify({id:n,method,params}))});
  await send('Page.enable');await send('Runtime.enable');
  await send('Emulation.setDeviceMetricsOverride',{width,height,deviceScaleFactor:1,mobile:width<600,screenWidth:width,screenHeight:height});
  await send('Page.navigate',{url:pageUrl});
  for(let i=0;i<120;i++){
    const ev=await send('Runtime.evaluate',{expression:'!!window.__MOTION01__ && document.getElementById("stage-image")?.complete',returnByValue:true});
    if(ev?.result?.value)break;
    if(i===119)throw new Error('motion API unavailable');
    await sleep(50);
  }
  const samples=[];
  const frameCount=49;
  for(let i=0;i<frameCount;i++){
    const progress=i/(frameCount-1);
    const ev=await send('Runtime.evaluate',{expression:`window.__MOTION01__.setProgress(${progress})`,returnByValue:true});
    const diag=ev?.result?.value;
    samples.push(diag);
    const rect=diag.stageRect;
    const shot=await send('Page.captureScreenshot',{format:'png',clip:{x:rect.x,y:rect.y,width:rect.width,height:rect.height,scale:1}});
    fs.writeFileSync(path.join(framesDir,`frame-${String(i).padStart(3,'0')}.png`),Buffer.from(shot.data,'base64'));
  }

  const latentConstant=samples.every(s=>s.plumOpacity===samples[0].plumOpacity&&s.tealOpacity===samples[0].tealOpacity);
  const summary={
    pageUrl,
    frameCount,
    requestedViewport:[width,height],
    stageNatural:samples[0].stageNatural,
    stageRect:samples[0].stageRect,
    motionWindow:samples[0].motionWindow,
    durationMs:samples[0].durationMs,
    horizontalOverflow:samples.some(s=>s.horizontalOverflow),
    latentLightComputedOpacityConstant:latentConstant,
    latentOpacity:[samples[0].plumOpacity,samples[0].tealOpacity],
    keySamples:[samples[0],samples[7],samples[14],samples[24],samples[34],samples[41],samples[48]]
  };
  fs.writeFileSync(diagPath,JSON.stringify(summary,null,2)+'\n');
  ws.close();
}finally{
  cp.kill('SIGTERM');
  await Promise.race([new Promise(r=>cp.once('exit',r)),sleep(1200)]);
  try{fs.rmSync(profile,{recursive:true,force:true});}catch{}
}
