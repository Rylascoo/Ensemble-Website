import { spawn } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
const [mode,widthArg,diagPath,profile,screenshotPath,portArg] = process.argv.slice(2);
const debugPort=Number(portArg||process.env.CDP_PORT||9237);
const width=Number(widthArg),height=1500,browser=process.env.BROWSER;
if(!browser) throw new Error('BROWSER not set');
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const harness=path.join(root,'prototypes','perf-s1','harness.html');
fs.rmSync(profile,{recursive:true,force:true});
fs.mkdirSync(profile,{recursive:true});
const args=['--headless=new','--no-sandbox','--disable-gpu','--disable-dev-shm-usage','--allow-file-access-from-files','--disable-extensions',`--remote-debugging-port=${debugPort}`,`--user-data-dir=${profile}`,'about:blank'];
if(mode==='forced')args.splice(args.length-1,0,'--force-high-contrast');
const cp=spawn(browser,args,{stdio:['ignore','ignore','inherit']});
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
async function waitForCDP(){
  for(let i=0;i<400;i++){
    try{const r=await fetch(`http://127.0.0.1:${debugPort}/json/version`);if(r.ok)return String(debugPort)}catch{}
    await sleep(100);
  }
  throw new Error('CDP endpoint unavailable on explicit port '+debugPort+'; launcher exit='+cp.exitCode);
}
try{
  const p=await waitForCDP();let target=null;
  for(let i=0;i<100;i++){
    try{const r=await fetch(`http://127.0.0.1:${p}/json/new?about%3Ablank`,{method:'PUT'});if(r.ok){target=await r.json();break}}catch{}
    await sleep(100);
  }
  if(!target?.webSocketDebuggerUrl)throw new Error('page target unavailable');
  const ws=new WebSocket(target.webSocketDebuggerUrl);
  await new Promise((res,rej)=>{ws.onopen=res;ws.onerror=rej});
  let id=0;const pending=new Map();
  ws.onmessage=e=>{const m=JSON.parse(e.data);if(m.id&&pending.has(m.id)){const q=pending.get(m.id);pending.delete(m.id);m.error?q.rej(new Error(JSON.stringify(m.error))):q.res(m.result)}};
  const send=(method,params={})=>new Promise((res,rej)=>{const n=++id;pending.set(n,{res,rej});ws.send(JSON.stringify({id:n,method,params}))});
  await send('Page.enable');await send('Runtime.enable');
  await send('Emulation.setDeviceMetricsOverride',{width,height,deviceScaleFactor:1,mobile:false,screenWidth:width,screenHeight:height});
  const nav=await send('Page.navigate',{url:pathToFileURL(harness).href});
  if(nav?.errorText)throw new Error('navigate: '+nav.errorText);
  for(let i=0;i<100;i++){
    const ready=await send('Runtime.evaluate',{expression:'document.readyState',returnByValue:true});
    if(ready?.result?.value==='complete')break;
    await sleep(100);
  }
  const expression=`(()=>{
    const visible=el=>{if(!el)return false;const r=el.getBoundingClientRect(),s=getComputedStyle(el);return r.width>0&&r.height>0&&s.display!=='none'&&s.visibility!=='hidden'};
    const centerX=el=>{const r=el.getBoundingClientRect();return (r.left+r.right)/2};
    const boards=[...document.querySelectorAll('.board')];
    const missingSourceFlags=[],sourceHeaderMismatch=[],geometryFailures=[],sourceAlignmentFailures=[],labelVisibilityFailures=[],boardOverflowFailures=[];
    for(const b of boards){
      const family=b.dataset.family,stage=b.querySelector('.stage'),panel=b.querySelector('.perf-panel');
      const sources=[...b.querySelectorAll('.char[data-source="true"]')],header=b.querySelector('.source-header');
      const label=b.querySelector('.history-label'),copy=b.querySelector('.perf-copy');
      if(sources.length!==1||!visible(sources[0].querySelector('.source-flag')))missingSourceFlags.push(family+':'+b.dataset.kind+':'+b.dataset.count);
      if(!header||header.textContent.trim()!==b.dataset.source)sourceHeaderMismatch.push(family+':'+b.dataset.kind+':'+b.dataset.count);
      if(!visible(header)||!visible(copy)||!visible(label)||!visible(sources[0]?.querySelector('.char-name')))labelVisibilityFailures.push(family+':'+b.dataset.kind+':'+b.dataset.count);
      const ratio=panel.getBoundingClientRect().width/stage.getBoundingClientRect().width;
      const target=family==='F1'?0.62:0.86;if(Math.abs(ratio-target)>0.015)geometryFailures.push(family+':width:'+ratio.toFixed(3));
      if(family==='F1'&&sources.length===1){const x=centerX(sources[0]),r=panel.getBoundingClientRect();if(x<r.left-1||x>r.right+1)sourceAlignmentFailures.push(family+':source-outside-dock');}
      if(family==='F2'&&sources.length===1&&Math.abs(centerX(header)-centerX(sources[0]))>12)sourceAlignmentFailures.push(family+':header:'+Math.abs(centerX(header)-centerX(sources[0])).toFixed(1));
      if(family==='F3'&&sources.length===1){const w=b.querySelector('.witness');if(!w||Math.abs(centerX(w)-centerX(sources[0]))>2)sourceAlignmentFailures.push(family+':witness');}
      if(family==='F4'&&sources.length===1){const a=b.querySelector('.aperture-mask');if(!a||Math.abs(centerX(a)-centerX(sources[0]))>2)sourceAlignmentFailures.push(family+':aperture');}
      if(b.scrollWidth>b.clientWidth+1)boardOverflowFailures.push(family+':'+b.dataset.kind+':'+b.dataset.count);
    }
    const exactQuote='These fibers match the raft’s mooring line.';
    return {schema:'kymaean.perf-s1.browser-diagnostic.v1',forcedColors:matchMedia('(forced-colors: active)').matches,viewport:{innerWidth,scrollWidth:document.documentElement.scrollWidth},families:new Set(boards.map(b=>b.dataset.family)).size,boards:boards.length,stressBoards:boards.filter(b=>b.dataset.kind==='stress').length,exactBoards:boards.filter(b=>b.dataset.kind==='exact').length,characterLoci:document.querySelectorAll('.char').length,sourceFlags:document.querySelectorAll('.char[data-source="true"] .source-flag').length,sourceHeaders:document.querySelectorAll('.source-header').length,panels:document.querySelectorAll('.perf-panel').length,historyRows:document.querySelectorAll('.history-row').length,exactCopyBoards:boards.filter(b=>b.dataset.kind==='exact'&&b.querySelector('.perf-copy')?.textContent.includes(exactQuote)).length,witnessCount:document.querySelectorAll('.witness').length,apertureCount:document.querySelectorAll('.aperture-mask').length,missingSourceFlags,sourceHeaderMismatch,geometryFailures,sourceAlignmentFailures,labelVisibilityFailures,boardOverflowFailures};
  })()`;
  const ev=await send('Runtime.evaluate',{expression,returnByValue:true});
  const diag=ev?.result?.value;
  if(!diag)throw new Error('PERF-S1 diagnostic missing');
  fs.writeFileSync(diagPath,JSON.stringify(diag,null,2)+'\n');
  if(screenshotPath){
    const layout=await send('Page.getLayoutMetrics');
    const cs=layout.cssContentSize||layout.contentSize;
    const shot=await send('Page.captureScreenshot',{format:'png',captureBeyondViewport:true,clip:{x:0,y:0,width:Math.ceil(cs.width),height:Math.ceil(cs.height),scale:1}});
    fs.writeFileSync(screenshotPath,Buffer.from(shot.data,'base64'));
  }
  ws.send(JSON.stringify({id:++id,method:'Browser.close'}));
  await sleep(300);
  try{ws.close()}catch{}
}finally{
  cp.kill('SIGTERM');
  await Promise.race([new Promise(r=>cp.once('exit',r)),sleep(1500)]);
}
