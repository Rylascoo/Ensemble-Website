import {spawn} from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
const [mode,widthArg,diagPath,profileArg,screenshotPath,portArg]=process.argv.slice(2);
const profile=path.resolve(profileArg);
const width=Number(widthArg),height=2400,browser=process.env.BROWSER,cdpPort=Number(portArg||9331);
if(!browser) throw new Error('BROWSER not set');
const carrierPath=path.resolve('prototypes/appui-01/phase2-current-performance-immediate-causal-context-composition-01.html');
const html=fs.readFileSync(carrierPath,'utf8');
fs.rmSync(profile,{recursive:true,force:true});fs.mkdirSync(profile,{recursive:true});
const args=['--headless=new','--no-sandbox','--disable-gpu','--disable-dev-shm-usage',`--remote-debugging-port=${cdpPort}`,`--user-data-dir=${profile}`,'about:blank'];if(mode==='forced')args.splice(args.length-1,0,'--force-high-contrast');
const cp=spawn(browser,args,{stdio:['ignore','ignore','inherit']});const sleep=ms=>new Promise(r=>setTimeout(r,ms));
async function waitPort(){for(let i=0;i<300;i++){try{const r=await fetch(`http://127.0.0.1:${cdpPort}/json/version`);if(r.ok)return}catch{}await sleep(100)}throw new Error('CDP unavailable; exit='+cp.exitCode)}
try{
 await waitPort();const r=await fetch(`http://127.0.0.1:${cdpPort}/json/new?about%3Ablank`,{method:'PUT'});const target=await r.json();const ws=new WebSocket(target.webSocketDebuggerUrl);await new Promise((res,rej)=>{ws.onopen=res;ws.onerror=rej});
 let id=0;const pending=new Map();ws.onmessage=e=>{const m=JSON.parse(e.data);if(m.id&&pending.has(m.id)){const q=pending.get(m.id);pending.delete(m.id);m.error?q.rej(new Error(JSON.stringify(m.error))):q.res(m.result)}};const send=(method,params={})=>new Promise((res,rej)=>{const n=++id;pending.set(n,{res,rej});ws.send(JSON.stringify({id:n,method,params}))});
 await send('Page.enable');await send('Runtime.enable');await send('Emulation.setDeviceMetricsOverride',{width,height,deviceScaleFactor:1,mobile:false,screenWidth:width,screenHeight:height});
 const tree=await send('Page.getFrameTree');await send('Page.setDocumentContent',{frameId:tree.frameTree.frame.id,html});await sleep(180);
 const expr=`(()=>{const all=[...document.querySelectorAll('*')];const overflowElements=all.map((e,i)=>{const r=e.getBoundingClientRect();return{i,tag:e.tagName,cls:typeof e.className==='string'?e.className:'',text:(e.textContent||'').trim().replace(/\\s+/g,' ').slice(0,90),left:r.left,right:r.right,scrollWidth:e.scrollWidth,clientWidth:e.clientWidth}}).filter(x=>x.right>innerWidth+.5||x.left<-.5||x.scrollWidth>x.clientWidth+1).slice(0,80);return{mode:${JSON.stringify(mode)},forcedColors:matchMedia('(forced-colors: active)').matches,viewport:{width:innerWidth,height:innerHeight,scrollWidth:document.documentElement.scrollWidth,scrollHeight:document.documentElement.scrollHeight},overflowElements,shellCount:document.querySelectorAll('.shell').length,stageCount:document.querySelectorAll('.stage').length,coneCount:document.querySelectorAll('.cone').length,contextCount:document.querySelectorAll('.context').length,flowStepCount:document.querySelectorAll('.step').length,blockedCount:document.querySelectorAll('.blocked .card').length,imageCount:document.images.length,externalResources:[...document.querySelectorAll('link[href],script[src],img[src]')].map(x=>x.href||x.src)};})()`;
 const ev=await send('Runtime.evaluate',{expression:expr,returnByValue:true});const diag=ev?.result?.value;if(!diag)throw new Error('diagnostic missing');fs.writeFileSync(diagPath,JSON.stringify(diag,null,2)+'\n');
 if(screenshotPath && screenshotPath !== '-'){const layout=await send('Page.getLayoutMetrics');const cs=layout.cssContentSize||layout.contentSize;const shot=await send('Page.captureScreenshot',{format:'png',captureBeyondViewport:true,clip:{x:0,y:0,width:Math.ceil(cs.width),height:Math.ceil(cs.height),scale:1}});fs.writeFileSync(screenshotPath,Buffer.from(shot.data,'base64'))}
 try{ws.send(JSON.stringify({id:++id,method:'Browser.close'}));await sleep(120)}catch{}ws.close();
}finally{if(cp.exitCode===null)cp.kill('SIGTERM');await Promise.race([new Promise(r=>cp.once('exit',r)),sleep(1500)])}

