import { spawn } from 'node:child_process';
import fs from 'node:fs';
const [forcedArg,widthArg,fontArg,spacingArg,diagPath,profile,screenshotPath]=process.argv.slice(2);
const width=Number(widthArg),height=7200,fontPercent=Number(fontArg),browser=process.env.BROWSER;
if(!browser) throw new Error('BROWSER not set');
const forced=forcedArg==='forced', spacing=spacingArg==='spacing';
fs.rmSync(profile,{recursive:true,force:true});fs.mkdirSync(profile,{recursive:true});
const args=['--headless=new','--no-sandbox','--disable-gpu','--disable-dev-shm-usage','--remote-debugging-port=0',`--user-data-dir=${profile}`,'about:blank'];
if(forced) args.splice(args.length-1,0,'--force-high-contrast');
const cp=spawn(browser,args,{stdio:['ignore','ignore','inherit']});
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
async function port(){const active=profile+'/DevToolsActivePort';for(let i=0;i<400;i++){if(fs.existsSync(active)){const [p]=fs.readFileSync(active,'utf8').trim().split(/\r?\n/);if(p)return p;}await sleep(100);}throw new Error('DevToolsActivePort unavailable; launcher exit='+cp.exitCode);}
try{
 const p=await port();let target=null;
 for(let i=0;i<100;i++){try{const r=await fetch(`http://127.0.0.1:${p}/json/new?about%3Ablank`,{method:'PUT'});if(r.ok){target=await r.json();break;}}catch{}await sleep(100);}
 if(!target?.webSocketDebuggerUrl)throw new Error('page target unavailable');
 const ws=new WebSocket(target.webSocketDebuggerUrl);await new Promise((res,rej)=>{ws.onopen=res;ws.onerror=rej});
 let id=0;const pending=new Map();ws.onmessage=e=>{const m=JSON.parse(e.data);if(m.id&&pending.has(m.id)){const q=pending.get(m.id);pending.delete(m.id);m.error?q.rej(new Error(JSON.stringify(m.error))):q.res(m.result)}};
 const send=(method,params={})=>new Promise((res,rej)=>{const n=++id;pending.set(n,{res,rej});ws.send(JSON.stringify({id:n,method,params}))});
 await send('Page.enable');await send('Runtime.enable');
 await send('Emulation.setDeviceMetricsOverride',{width,height,deviceScaleFactor:1,mobile:false,screenWidth:width,screenHeight:height});
 const nav=await send('Page.navigate',{url:'http://127.0.0.1:8765/prototypes/typ-02/harness.html'});if(nav?.errorText)throw new Error('navigate: '+nav.errorText);
 for(let i=0;i<150;i++){const ev=await send('Runtime.evaluate',{expression:'!!window.__TYP02_API__',returnByValue:true});if(ev?.result?.value)break;if(i===149)throw new Error('TYP-02 API missing');await sleep(100);}
 await send('Runtime.evaluate',{expression:`(()=>{document.documentElement.style.fontSize='${fontPercent}%';document.documentElement.classList.toggle('spacing-stress',${spacing});return true})()`,returnByValue:true});
 await sleep(60);
 const ev=await send('Runtime.evaluate',{expression:'window.__TYP02_API__.diagnostic()',returnByValue:true});
 const diag=ev?.result?.value;if(!diag)throw new Error('TYP-02 diagnostic missing');
 diag.requested={width,forced,fontPercent,spacing};
 await send('Runtime.evaluate',{expression:'document.activeElement?.blur();document.body.tabIndex=-1;document.body.focus()',returnByValue:true});
 const keyboardFocus=[];
 for(let i=0;i<36;i++){
  await send('Input.dispatchKeyEvent',{type:'keyDown',key:'Tab',code:'Tab',windowsVirtualKeyCode:9,nativeVirtualKeyCode:9});
  await send('Input.dispatchKeyEvent',{type:'keyUp',key:'Tab',code:'Tab',windowsVirtualKeyCode:9,nativeVirtualKeyCode:9});
  await sleep(12);
  const f=await send('Runtime.evaluate',{expression:`(()=>{const e=document.activeElement;if(!e)return null;const s=e.closest('.surface');const cs=getComputedStyle(e);const w=e.classList?.contains('selected')?getComputedStyle(e,'::before'):null;return{surface:s?.id||null,text:(e.textContent||'').trim(),selected:!!e.classList?.contains('selected'),focusVisible:e.matches?.(':focus-visible')||false,outlineWidth:cs.outlineWidth,outlineStyle:cs.outlineStyle,witnessWidth:w?.width||null,witnessHeight:w?.height||null}})()`,returnByValue:true});
  keyboardFocus.push(f?.result?.value||null);
 }
 diag.keyboardFocus=keyboardFocus;
 const overflowEval=await send('Runtime.evaluate',{expression:`(()=>[...document.querySelectorAll('*')].map((e,i)=>{const r=e.getBoundingClientRect();return{i,tag:e.tagName,id:e.id||'',cls:typeof e.className==='string'?e.className:'',left:r.left,right:r.right,width:r.width,scrollWidth:e.scrollWidth,clientWidth:e.clientWidth}}).filter(x=>x.right>innerWidth+.5||x.left<-.5||x.scrollWidth>x.clientWidth+1).slice(0,100))()`,returnByValue:true});
 diag.overflowElements=overflowEval?.result?.value||[];
 fs.writeFileSync(diagPath,JSON.stringify(diag)+'\n');
 if(screenshotPath){const layout=await send('Page.getLayoutMetrics');const cs=layout.cssContentSize||layout.contentSize;const shot=await send('Page.captureScreenshot',{format:'png',captureBeyondViewport:true,clip:{x:0,y:0,width:Math.ceil(cs.width),height:Math.ceil(cs.height),scale:1}});fs.writeFileSync(screenshotPath,Buffer.from(shot.data,'base64'));}
 ws.close();
}finally{cp.kill('SIGTERM');await Promise.race([new Promise(r=>cp.once('exit',r)),sleep(1500)]);}
