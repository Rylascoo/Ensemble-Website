import fs from 'node:fs';
import path from 'node:path';
import { spawn } from 'node:child_process';
import { fileURLToPath, pathToFileURL } from 'node:url';
const browser=process.env.BROWSER;
if(!browser) throw new Error('BROWSER not set');
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const page=path.join(root,'prototypes','website-v2-2-temporal-interaction-accessibility-study','index.html');
const output=process.argv[2]||path.join(root,'.tmp','temporal-interaction-accessibility.json');
const profile=path.join(root,'.tmp',`temporal-interaction-accessibility-edge-${process.pid}`);
fs.mkdirSync(profile,{recursive:true});
const cp=spawn(browser,['--headless=new','--no-sandbox','--disable-gpu','--disable-dev-shm-usage','--disable-extensions','--remote-debugging-port=0',`--user-data-dir=${profile}`,'about:blank'],{stdio:['ignore','ignore','inherit']});
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
async function port(){const f=path.join(profile,'DevToolsActivePort');for(let i=0;i<300;i++){if(fs.existsSync(f)){const [p]=fs.readFileSync(f,'utf8').trim().split(/\r?\n/);if(p)return p}await sleep(100)}throw new Error('CDP port unavailable')}
let ws,id=0;const pending=new Map();
function send(method,params={}){return new Promise((res,rej)=>{const n=++id;pending.set(n,{res,rej});ws.send(JSON.stringify({id:n,method,params}))})}
async function evalv(expression){const r=await send('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true});if(r.exceptionDetails)throw new Error(JSON.stringify(r.exceptionDetails));return r.result.value}
async function waitReady(){for(let i=0;i<100;i++){const v=await evalv('!!window.__KYM_TEMPORAL__');if(v)return;await sleep(50)}throw new Error('prototype API unavailable')}
const viewports=[[2048,1199],[1235,647],[1138,1354],[1227,1422],[768,1024],[600,900],[599,900],[390,844],[320,640]];
const results={source:pathToFileURL(page).href,viewports:[],interaction:{},reducedMotion:{},accessibility:{}};
try{
 const p=await port(); const target=await (await fetch(`http://127.0.0.1:${p}/json/new?about%3Ablank`,{method:'PUT'})).json();
 ws=new WebSocket(target.webSocketDebuggerUrl); await new Promise((res,rej)=>{ws.onopen=res;ws.onerror=rej});
 ws.onmessage=e=>{const m=JSON.parse(e.data);if(m.id&&pending.has(m.id)){const q=pending.get(m.id);pending.delete(m.id);m.error?q.rej(new Error(JSON.stringify(m.error))):q.res(m.result)}};
 await send('Page.enable'); await send('Runtime.enable');
 for(const [width,height] of viewports){
   await send('Emulation.setDeviceMetricsOverride',{width,height,deviceScaleFactor:1,mobile:false,screenWidth:width,screenHeight:height});
   await send('Emulation.setEmulatedMedia',{features:[{name:'prefers-reduced-motion',value:'no-preference'}]});
   await send('Page.navigate',{url:pathToFileURL(page).href}); await waitReady(); await sleep(80);
   const metrics=await evalv(`(()=>{const b=document.querySelector('.brand-lockup').getBoundingClientRect(),w=document.querySelector('.wordmark').getBoundingClientRect();return {overflowX:document.documentElement.scrollWidth-document.documentElement.clientWidth,brandCenter:b.left+b.width/2,viewportCenter:innerWidth/2,wordmarkContained:w.left>=0&&w.right<=innerWidth,stageNatural:[document.querySelector('.scene-art').naturalWidth,document.querySelector('.scene-art').naturalHeight],state:window.__KYM_TEMPORAL__.state}})()`);
   await send('Emulation.setEmulatedMedia',{features:[{name:'prefers-reduced-motion',value:'reduce'}]});
   const geometry=await evalv(`(()=>{const brand=document.querySelector('.brand-lockup').getBoundingClientRect(),items={presence:'.a3',person:'.p2',trace:'.trace',life:'.adult'},out={};for(const [state,sel] of Object.entries(items)){window.__KYM_TEMPORAL__.set(window.__KYM_TEMPORAL__.order.indexOf(state));const r=document.querySelector(sel).getBoundingClientRect();out[state]={heightRatio:+(r.height/innerHeight).toFixed(3),withinX:r.right>0&&r.left<innerWidth,withinY:r.bottom>0&&r.top<innerHeight,overlapsBrand:!(r.right<brand.left||r.left>brand.right||r.bottom<brand.top||r.top>brand.bottom)}}return out})()`);
   results.viewports.push({width,height,...metrics,geometry});
 }
 await send('Emulation.setDeviceMetricsOverride',{width:1235,height:647,deviceScaleFactor:1,mobile:false,screenWidth:1235,screenHeight:647});
 await send('Emulation.setEmulatedMedia',{features:[{name:'prefers-reduced-motion',value:'no-preference'}]});
 await send('Page.navigate',{url:pathToFileURL(page).href}); await waitReady();
 results.interaction.initial=await evalv('window.__KYM_TEMPORAL__.snapshot()');
 await evalv(`(()=>{const e=document.getElementById('experience');e.focus();e.dispatchEvent(new KeyboardEvent('keydown',{key:'ArrowDown',bubbles:true,cancelable:true}));return true})()`); await sleep(620);
 results.interaction.keyboardForward=await evalv('window.__KYM_TEMPORAL__.snapshot()');
 await evalv(`(()=>{window.dispatchEvent(new WheelEvent('wheel',{deltaY:80,bubbles:true,cancelable:false}));return true})()`); await sleep(220);
 results.interaction.wheelForward=await evalv('window.__KYM_TEMPORAL__.snapshot()');
 await evalv(`(()=>{const e=document.getElementById('experience');e.dispatchEvent(new KeyboardEvent('keydown',{key:'ArrowUp',bubbles:true,cancelable:true}));return true})()`);
 results.interaction.keyboardReverse=await evalv('window.__KYM_TEMPORAL__.snapshot()');
 await send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:false,screenWidth:390,screenHeight:844});
 await send('Page.navigate',{url:pathToFileURL(page).href}); await waitReady();
 results.interaction.touch=await evalv(`(()=>{const e=document.getElementById('experience');const t1=new Touch({identifier:1,target:e,clientX:180,clientY:620});const t2=new Touch({identifier:1,target:e,clientX:180,clientY:500});e.dispatchEvent(new TouchEvent('touchstart',{touches:[t1],bubbles:true}));e.dispatchEvent(new TouchEvent('touchend',{changedTouches:[t2],bubbles:true}));return window.__KYM_TEMPORAL__.snapshot()})()`);
 await evalv('window.__KYM_TEMPORAL__.set(0)');
 results.interaction.rapidForward=await evalv(`(()=>{for(let n=0;n<6;n++)window.__KYM_TEMPORAL__.advance();return window.__KYM_TEMPORAL__.snapshot()})()`);
 results.interaction.rapidReverse=await evalv(`(()=>{for(let n=0;n<4;n++)window.__KYM_TEMPORAL__.reverse();return window.__KYM_TEMPORAL__.snapshot()})()`);
 results.interaction.focusAfterRetarget=await evalv(`(()=>{const e=document.getElementById('experience');e.focus();window.__KYM_TEMPORAL__.advance();window.__KYM_TEMPORAL__.reverse();return {activeId:document.activeElement.id,state:window.__KYM_TEMPORAL__.state}})()`);
 await evalv('window.__KYM_TEMPORAL__.set(1)'); await sleep(620); await evalv('window.__KYM_TEMPORAL__.advance()'); await sleep(40); await evalv('window.__KYM_TEMPORAL__.advance()'); await sleep(80);
 results.interaction.interruptedEmptyGhostCheck=await evalv('window.__KYM_TEMPORAL__.snapshot()');
 await send('Emulation.setEmulatedMedia',{features:[{name:'prefers-reduced-motion',value:'reduce'}]});
 await send('Page.navigate',{url:pathToFileURL(page).href}); await waitReady();
 results.reducedMotion.initial=await evalv(`({snapshot:window.__KYM_TEMPORAL__.snapshot(),animations:document.getAnimations().filter(a=>a.playState==='running').length})`);
 results.reducedMotion.sequence=await evalv(`(()=>{const a=[];for(let n=0;n<7;n++){window.__KYM_TEMPORAL__.advance();a.push(window.__KYM_TEMPORAL__.state)}return {states:a,snapshot:window.__KYM_TEMPORAL__.snapshot(),animations:document.getAnimations().filter(x=>x.playState==='running').length}})()`);
 await send('Emulation.setDeviceMetricsOverride',{width:320,height:640,deviceScaleFactor:1,mobile:false,screenWidth:320,screenHeight:640}); await send('Emulation.setEmulatedMedia',{features:[]}); await send('Page.navigate',{url:pathToFileURL(page).href}); await waitReady(); await send('Page.bringToFront');
 results.accessibility.text200=await evalv(`(()=>{document.documentElement.style.fontSize='32px';const w=document.querySelector('.wordmark').getBoundingClientRect();return {overflowX:document.documentElement.scrollWidth-document.documentElement.clientWidth,wordmarkContained:w.left>=0&&w.right<=innerWidth}})()`);
 await evalv(`(()=>{document.documentElement.style.fontSize='';document.getElementById('experience').focus();return true})()`); results.accessibility.focus=await evalv(`(()=>{const e=document.getElementById('experience'),s=getComputedStyle(e);return {activeId:document.activeElement.id,matchesFocus:e.matches(':focus'),boxShadow:s.boxShadow}})()`);
 await send('Emulation.setEmulatedMedia',{features:[{name:'forced-colors',value:'active'}]}); results.accessibility.forcedColors=await evalv(`(()=>({matches:matchMedia('(forced-colors: active)').matches,sceneDisplay:getComputedStyle(document.querySelector('.scene')).display,a3Display:getComputedStyle(document.querySelector('.a3')).display,wordmarkDisplay:getComputedStyle(document.querySelector('.wordmark')).display,statusDisplay:getComputedStyle(document.querySelector('.status')).display}))()`);
 fs.mkdirSync(path.dirname(output),{recursive:true});fs.writeFileSync(output,JSON.stringify(results,null,2)+'\n');console.log(JSON.stringify(results,null,2));
 ws.close();
}finally{cp.kill('SIGTERM');await Promise.race([new Promise(r=>cp.once('exit',r)),sleep(1200)])}
