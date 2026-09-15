import { spawn } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
const [mode,widthArg,diagPath,profile,screenshotPath] = process.argv.slice(2);
const carrierUrl=pathToFileURL(path.resolve('prototypes/appui-01/empty-unavailable-transitional-workspace-functional-study-01.html')).href;
const width=Number(widthArg),height=2400,browser=process.env.BROWSER;
if(!browser) throw new Error('BROWSER not set');
fs.rmSync(profile,{recursive:true,force:true});fs.mkdirSync(profile,{recursive:true});
const args=['--headless=new','--no-sandbox','--disable-gpu','--disable-dev-shm-usage','--remote-debugging-port=0',`--user-data-dir=${profile}`,'about:blank'];
if(mode==='forced') args.splice(args.length-1,0,'--force-high-contrast');
const cp=spawn(browser,args,{stdio:['ignore','ignore','inherit']});
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
async function port(){const active=profile+'/DevToolsActivePort';for(let i=0;i<400;i++){if(fs.existsSync(active)){try{const [p]=fs.readFileSync(active,'utf8').trim().split(/\r?\n/);if(p)return p}catch(e){if(e?.code!=='EBUSY'&&e?.code!=='EACCES')throw e}}await sleep(100)}throw new Error('DevToolsActivePort unavailable; exit='+cp.exitCode)}
try{
 const p=await port();let target=null;
 for(let i=0;i<100;i++){try{const r=await fetch(`http://127.0.0.1:${p}/json/new?about%3Ablank`,{method:'PUT'});if(r.ok){target=await r.json();break}}catch{}await sleep(100)}
 if(!target?.webSocketDebuggerUrl) throw new Error('page target unavailable');
 const ws=new WebSocket(target.webSocketDebuggerUrl);await new Promise((res,rej)=>{ws.onopen=res;ws.onerror=rej});
 let id=0;const pending=new Map();
 ws.onmessage=e=>{const m=JSON.parse(e.data);if(m.id&&pending.has(m.id)){const q=pending.get(m.id);pending.delete(m.id);m.error?q.rej(new Error(JSON.stringify(m.error))):q.res(m.result)}};
 const send=(method,params={})=>new Promise((res,rej)=>{const n=++id;pending.set(n,{res,rej});ws.send(JSON.stringify({id:n,method,params}))});
 await send('Page.enable');await send('Runtime.enable');await send('Emulation.setDeviceMetricsOverride',{width,height,deviceScaleFactor:1,mobile:false,screenWidth:width,screenHeight:height});
 const nav=await send('Page.navigate',{url:carrierUrl});if(nav?.errorText)throw new Error('navigate: '+nav.errorText);
 for(let i=0;i<100;i++){const q=await send('Runtime.evaluate',{expression:'document.readyState',returnByValue:true});if(q?.result?.value==='complete')break;await sleep(50)}
 await sleep(120);
 const expr=`(()=>{const all=[...document.querySelectorAll('*')];const overflowElements=all.map((e,i)=>{const r=e.getBoundingClientRect();return {i,tag:e.tagName,cls:typeof e.className==='string'?e.className:'',text:(e.textContent||'').trim().replace(/\\s+/g,' ').slice(0,90),left:r.left,right:r.right,scrollWidth:e.scrollWidth,clientWidth:e.clientWidth}}).filter(x=>x.right>innerWidth+.5||x.left<-.5||x.scrollWidth>x.clientWidth+1).slice(0,60);return {mode:${JSON.stringify(mode)},forcedColors:matchMedia('(forced-colors: active)').matches,viewport:{width:innerWidth,height:innerHeight,scrollWidth:document.documentElement.scrollWidth,scrollHeight:document.documentElement.scrollHeight},overflowElements,appCount:document.querySelectorAll('.app').length,stateCount:document.querySelectorAll('.state').length,primaryCount:document.querySelectorAll('.primary').length,scenicImageCount:document.images.length,externalResources:[...document.querySelectorAll('link[href],script[src],img[src]')].map(x=>x.href||x.src)};})()`;
 const ev=await send('Runtime.evaluate',{expression:expr,returnByValue:true});const diag=ev?.result?.value;if(!diag)throw new Error('APPUI character-bounded diagnostic missing');
 fs.writeFileSync(diagPath,JSON.stringify(diag,null,2)+'\n');
 if(screenshotPath){const layout=await send('Page.getLayoutMetrics');const cs=layout.cssContentSize||layout.contentSize;const shot=await send('Page.captureScreenshot',{format:'png',captureBeyondViewport:true,clip:{x:0,y:0,width:Math.ceil(cs.width),height:Math.ceil(cs.height),scale:1}});fs.writeFileSync(screenshotPath,Buffer.from(shot.data,'base64'))}
 await send('Browser.close').catch(()=>{});ws.close();
}finally{if(cp.exitCode===null)cp.kill('SIGTERM');await Promise.race([new Promise(r=>cp.once('exit',r)),sleep(1500)])}


