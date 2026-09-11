import { spawn } from 'node:child_process';
import fs from 'node:fs';
const [mode,widthArg,diagPath,profile,screenshotPath] = process.argv.slice(2);
const width=Number(widthArg), height=3000, browser=process.env.BROWSER;
if(!browser) throw new Error('BROWSER not set');
fs.rmSync(profile,{recursive:true,force:true}); fs.mkdirSync(profile,{recursive:true});
const args=['--headless=new','--no-sandbox','--disable-gpu','--disable-dev-shm-usage','--remote-debugging-port=0',`--user-data-dir=${profile}`,'about:blank'];
if(mode==='forced') args.splice(args.length-1,0,'--force-high-contrast');
const cp=spawn(browser,args,{stdio:['ignore','ignore','inherit']});
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
async function port(){
  const active=profile+'/DevToolsActivePort';
  for(let i=0;i<400;i++){
    if(fs.existsSync(active)){const [p]=fs.readFileSync(active,'utf8').trim().split(/\r?\n/); if(p) return p;}
    await sleep(100);
  }
  throw new Error('DevToolsActivePort unavailable; launcher exit='+cp.exitCode);
}
try {
  const p=await port(); let target=null;
  for(let i=0;i<100;i++){
    try{const r=await fetch(`http://127.0.0.1:${p}/json/new?about%3Ablank`,{method:'PUT'}); if(r.ok){target=await r.json();break;}}catch{}
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
  const nav=await send('Page.navigate',{url:'http://127.0.0.1:8765/prototypes/sym-02/harness.html'});
  if(nav?.errorText) throw new Error('navigate: '+nav.errorText);
  let diag=null,last=null;
  for(let i=0;i<150;i++){
    const ev=await send('Runtime.evaluate',{expression:'window.__SYM02_DIAGNOSTIC__||null',returnByValue:true});
    last=ev?.result?.value||null; if(last){diag=last;break;} await sleep(100);
  }
  if(!diag) throw new Error('SYM-02 diagnostic missing: '+JSON.stringify(last));
  const rasterEval=await send('Runtime.evaluate',{expression:`(async()=>{
    async function measure(markup,vb){const blob=new Blob([markup],{type:'image/svg+xml'}),url=URL.createObjectURL(blob),img=new Image();await new Promise((res,rej)=>{img.onload=res;img.onerror=rej;img.src=url});const scale=8,c=document.createElement('canvas');c.width=Math.round(vb.width*scale);c.height=Math.round(vb.height*scale);const x=c.getContext('2d',{willReadFrequently:true});x.drawImage(img,0,0,c.width,c.height);URL.revokeObjectURL(url);const d=x.getImageData(0,0,c.width,c.height).data;let a=0,sx=0,sy=0,minx=c.width,miny=c.height,maxx=-1,maxy=-1;for(let py=0,i=3;py<c.height;py++){for(let px=0;px<c.width;px++,i+=4){const w=d[i]/255;if(!w)continue;a+=w;sx+=px*w;sy+=py*w;minx=Math.min(minx,px);miny=Math.min(miny,py);maxx=Math.max(maxx,px);maxy=Math.max(maxy,py)}}return {filledArea:a/(scale*scale),centroidX:vb.x+sx/a/scale,centroidY:vb.y+sy/a/scale,bbox:{x:vb.x+minx/scale,y:vb.y+miny/scale,width:(maxx-minx+1)/scale,height:(maxy-miny+1)/scale}}}
    const out={};for(const f of [...document.querySelectorAll('.family')]){const id=f.dataset.family,src=f.dataset.src,text=await (await fetch(src)).text(),doc=new DOMParser().parseFromString(text,'image/svg+xml'),svg=doc.documentElement,v=svg.viewBox.baseVal,vb={x:v.x,y:v.y,width:v.width,height:v.height};const all=await measure(text,vb),paths=[];for(const p of [...svg.querySelectorAll('path')]){const shell='<svg xmlns="http://www.w3.org/2000/svg" viewBox="'+[vb.x,vb.y,vb.width,vb.height].join(' ')+'">'+p.outerHTML+'</svg>';paths.push(await measure(shell,vb))}out[id]={...all,paths}}return out})()`,awaitPromise:true,returnByValue:true});
  diag.rasterMetrics=rasterEval?.result?.value||{};
  const overflowEval=await send('Runtime.evaluate',{expression:`(()=>[...document.querySelectorAll('*')].map((e,i)=>{const r=e.getBoundingClientRect();return {i,tag:e.tagName,id:e.id||'',cls:typeof e.className==='string'?e.className:'',text:(e.textContent||'').trim().replace(/\s+/g,' ').slice(0,120),left:r.left,right:r.right,width:r.width,scrollWidth:e.scrollWidth,clientWidth:e.clientWidth}}).filter(x=>x.right>innerWidth+0.5||x.left<-0.5||x.scrollWidth>x.clientWidth+1).slice(0,80))()`,returnByValue:true});
  diag.overflowElements=overflowEval?.result?.value||[];
  fs.writeFileSync(diagPath,JSON.stringify(diag)+'\n');
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
