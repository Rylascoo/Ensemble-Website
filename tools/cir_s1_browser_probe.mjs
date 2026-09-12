import { spawn } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
const [mode,widthArg,diagPath,profile,screenshotPath] = process.argv.slice(2);
const width=Number(widthArg), height=1400, browser=process.env.BROWSER;
if(!browser) throw new Error('BROWSER not set');
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const harness=path.join(root,'prototypes','cir-s1','harness.html');
fs.rmSync(profile,{recursive:true,force:true}); fs.mkdirSync(profile,{recursive:true});
const args=['--headless=new','--no-sandbox','--disable-gpu','--disable-dev-shm-usage','--allow-file-access-from-files','--remote-debugging-port=0',`--user-data-dir=${profile}`,'about:blank'];
if(mode==='forced') args.splice(args.length-1,0,'--force-high-contrast');
const cp=spawn(browser,args,{stdio:['ignore','ignore','inherit']});
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
async function port(){
  const active=path.join(profile,'DevToolsActivePort');
  for(let i=0;i<400;i++){
    if(fs.existsSync(active)){try{const [p]=fs.readFileSync(active,'utf8').trim().split(/\r?\n/); if(p) return p;}catch{}}
    await sleep(100);
  }
  throw new Error('DevToolsActivePort unavailable; launcher exit='+cp.exitCode);
}
try {
  const p=await port(); let target=null;
  for(let i=0;i<100;i++){
    try{const r=await fetch(`http://127.0.0.1:${p}/json/new?about%3Ablank`,{method:'PUT'});if(r.ok){target=await r.json();break;}}catch{}
    await sleep(100);
  }
  if(!target?.webSocketDebuggerUrl) throw new Error('page target unavailable');
  const ws=new WebSocket(target.webSocketDebuggerUrl);
  await new Promise((res,rej)=>{ws.onopen=res;ws.onerror=rej});
  let id=0; const pending=new Map();
  ws.onmessage=e=>{const m=JSON.parse(e.data);if(m.id&&pending.has(m.id)){const q=pending.get(m.id);pending.delete(m.id);m.error?q.rej(new Error(JSON.stringify(m.error))):q.res(m.result)}};
  const send=(method,params={})=>new Promise((res,rej)=>{const n=++id;pending.set(n,{res,rej});ws.send(JSON.stringify({id:n,method,params}))});
  await send('Page.enable'); await send('Runtime.enable');
  await send('Emulation.setDeviceMetricsOverride',{width,height,deviceScaleFactor:1,mobile:false,screenWidth:width,screenHeight:height});
  const nav=await send('Page.navigate',{url:pathToFileURL(harness).href});
  if(nav?.errorText) throw new Error('navigate: '+nav.errorText);
  let diag=null,last=null;
  for(let i=0;i<150;i++){
    const ev=await send('Runtime.evaluate',{expression:'window.__CIR_S1_DIAGNOSTIC__||null',returnByValue:true});
    last=ev?.result?.value||null;if(last){diag=last;break;}await sleep(100);
  }
  if(!diag) throw new Error('CIR-S1 diagnostic missing: '+JSON.stringify(last));
  const overflowEval=await send('Runtime.evaluate',{expression:`(()=>[...document.querySelectorAll('*')].map((e,i)=>{const r=e.getBoundingClientRect();return {i,tag:e.tagName,id:e.id||'',cls:typeof e.className==='string'?e.className:'',left:r.left,right:r.right,width:r.width,scrollWidth:e.scrollWidth,clientWidth:e.clientWidth}}).filter(x=>x.right>innerWidth+0.5||x.left<-0.5||x.scrollWidth>x.clientWidth+1).slice(0,80))()`,returnByValue:true});
  diag.overflowElements=overflowEval?.result?.value||[];
  const cueEval=await send('Runtime.evaluate',{expression:`(()=>[...document.querySelectorAll('.cue')].map(e=>({family:e.dataset.family,character:e.dataset.character,geometry:e.dataset.geometry,color:getComputedStyle(e).color,width:e.getBoundingClientRect().width,height:e.getBoundingClientRect().height})))()`,returnByValue:true});
  diag.cues=cueEval?.result?.value||[];
  fs.writeFileSync(diagPath,JSON.stringify(diag,null,2)+'\n');
  if(screenshotPath){
    const layout=await send('Page.getLayoutMetrics');
    const cs=layout.cssContentSize||layout.contentSize;
    const shot=await send('Page.captureScreenshot',{format:'png',captureBeyondViewport:true,clip:{x:0,y:0,width:Math.ceil(cs.width),height:Math.ceil(cs.height),scale:1}});
    fs.writeFileSync(screenshotPath,Buffer.from(shot.data,'base64'));
  }
  ws.close();
} finally {
  cp.kill('SIGTERM');
  await Promise.race([new Promise(r=>cp.once('exit',r)),sleep(1500)]);
}
