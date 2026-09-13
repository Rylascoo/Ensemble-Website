import {spawn} from 'node:child_process';
import fs from 'node:fs';
const [forcedArg,widthArg,fontArg,diagPath,profile,screenshotPath]=process.argv.slice(2);
const width=Number(widthArg),height=12000,fontPercent=Number(fontArg),forced=forcedArg==='forced';
const browser=process.env.BROWSER,pageUrl=process.env.IMG01_URL||'http://127.0.0.1:8766/prototypes/img-01/reference-board.html',cdpPort=Number(process.env.IMG01_CDP_PORT||9231);
if(!browser)throw new Error('BROWSER not set');fs.rmSync(profile,{recursive:true,force:true});fs.mkdirSync(profile,{recursive:true});
const args=['--headless=new','--no-sandbox','--disable-gpu','--disable-dev-shm-usage',`--remote-debugging-port=${cdpPort}`,`--user-data-dir=${profile}`,'about:blank'];if(forced)args.splice(args.length-1,0,'--force-high-contrast');
const cp=spawn(browser,args,{stdio:['ignore','ignore','inherit']});const sleep=ms=>new Promise(r=>setTimeout(r,ms));
async function port(){for(let i=0;i<300;i++){try{const r=await fetch(`http://127.0.0.1:${cdpPort}/json/version`);if(r.ok)return String(cdpPort)}catch{}await sleep(100)}throw new Error('CDP unavailable')}
try{
 const p=await port();let target=null;for(let i=0;i<80;i++){try{const r=await fetch(`http://127.0.0.1:${p}/json/new?about%3Ablank`,{method:'PUT'});if(r.ok){target=await r.json();break}}catch{}await sleep(100)}if(!target?.webSocketDebuggerUrl)throw new Error('page target unavailable');
 const ws=new WebSocket(target.webSocketDebuggerUrl);await new Promise((res,rej)=>{ws.onopen=res;ws.onerror=rej});let id=0;const pending=new Map();ws.onmessage=e=>{const m=JSON.parse(e.data);if(m.id&&pending.has(m.id)){const q=pending.get(m.id);pending.delete(m.id);m.error?q.rej(new Error(JSON.stringify(m.error))):q.res(m.result)}};const send=(method,params={})=>new Promise((res,rej)=>{const n=++id;pending.set(n,{res,rej});ws.send(JSON.stringify({id:n,method,params}))});
 await send('Page.enable');await send('Runtime.enable');await send('Emulation.setDeviceMetricsOverride',{width,height,deviceScaleFactor:1,mobile:false,screenWidth:width,screenHeight:height});
 const nav=await send('Page.navigate',{url:pageUrl});if(nav?.errorText)throw new Error(nav.errorText);for(let i=0;i<120;i++){const ev=await send('Runtime.evaluate',{expression:'!!window.__IMG01_API__',returnByValue:true});if(ev?.result?.value)break;if(i===119)throw new Error('IMG01 API missing');await sleep(100)}
 for(let i=0;i<120;i++){const iv=await send('Runtime.evaluate',{expression:`[...document.querySelectorAll('.source img')].every(x=>x.complete&&x.naturalWidth>0)`,returnByValue:true});if(iv?.result?.value)break;if(i===119)throw new Error('source images not loaded');await sleep(50)}
 await send('Runtime.evaluate',{expression:`document.documentElement.style.fontSize='${fontPercent}%';true`,returnByValue:true});await sleep(120);const ev=await send('Runtime.evaluate',{expression:'window.__IMG01_API__.diagnostic()',returnByValue:true});const diag=ev?.result?.value;if(!diag)throw new Error('diagnostic missing');diag.requested={width,forced,fontPercent};fs.writeFileSync(diagPath,JSON.stringify(diag,null,2)+'\n');
 if(screenshotPath){const layout=await send('Page.getLayoutMetrics');const cs=layout.cssContentSize||layout.contentSize;const shot=await send('Page.captureScreenshot',{format:'png',captureBeyondViewport:true,clip:{x:0,y:0,width:Math.ceil(cs.width),height:Math.ceil(cs.height),scale:1}});fs.writeFileSync(screenshotPath,Buffer.from(shot.data,'base64'))}
 try{ws.send(JSON.stringify({id:++id,method:'Browser.close'}));await sleep(120)}catch{}ws.close();
}finally{cp.kill('SIGTERM');await Promise.race([new Promise(r=>cp.once('exit',r)),sleep(1200)])}
