(()=>{
'use strict';
const DURATION=6800;
const MOTION_START=.13;
const MOTION_END=.87;
const stage=document.getElementById('stage');
const image=document.getElementById('stage-image');
const figure=document.getElementById('bellweather');
const head=document.getElementById('head');
const armL=document.getElementById('arm-left');
const armR=document.getElementById('arm-right');
const legL=document.getElementById('leg-left');
const legR=document.getElementById('leg-right');
const shadow=document.getElementById('passage-shadow');
const reflection=document.getElementById('passage-reflection');
const plum=document.getElementById('plum-spill');
const teal=document.getElementById('teal-spill');
const scrub=document.getElementById('scrub');
const play=document.getElementById('play');
const readout=document.getElementById('readout');
let progress=0,raf=0,startTime=0,playing=false;
const clamp=(v,a=0,b=1)=>Math.max(a,Math.min(b,v));
const smooth=t=>t*t*(3-2*t);
const mix=(a,b,t)=>a+(b-a)*t;
function travelAt(t){
  if(t<=.08) return .08*smooth(t/.08);
  if(t>=.92) return .92+.08*smooth((t-.92)/.08);
  return t;
}
function pose(p){
  progress=clamp(p);
  const mt=clamp((progress-MOTION_START)/(MOTION_END-MOTION_START));
  const travel=travelAt(mt);
  const x=mix(1080,904,travel);
  const ground=mix(724,708,travel);
  const scale=travel<.55?mix(1,.94,travel/.55):mix(.94,.68,(travel-.55)/.45);
  const stride=Math.sin(Math.PI*5.2*travel);
  const recognition=Math.exp(-Math.pow((mt-.47)/.10,2));
  const bob=-1.25*Math.sin(Math.PI*5.2*travel);
  const lean=.65*Math.sin(Math.PI*travel)-.35*recognition;
  figure.setAttribute('transform','translate('+x.toFixed(3)+' '+(ground+bob).toFixed(3)+') rotate('+lean.toFixed(3)+') scale('+scale.toFixed(4)+')');
  head.setAttribute('transform','rotate('+(-2.55*recognition).toFixed(3)+' -9 -176)');
  armL.setAttribute('transform','rotate('+(-3.3*stride).toFixed(3)+' -10 -136)');
  armR.setAttribute('transform','rotate('+(3.3*stride).toFixed(3)+' 12 -134)');
  legL.setAttribute('transform','rotate('+(2.5*stride).toFixed(3)+' -3 -82)');
  legR.setAttribute('transform','rotate('+(-2.5*stride).toFixed(3)+' 3 -82)');
  const visibleContact=smooth(clamp((mt-.03)/.10))*(1-smooth(clamp((mt-.80)/.16)));
  shadow.setAttribute('cx',x.toFixed(2));
  shadow.setAttribute('cy',(ground-4).toFixed(2));
  shadow.setAttribute('rx',mix(33,24,travel).toFixed(2));
  shadow.setAttribute('opacity',(visibleContact*.23).toFixed(4));
  const threshold=smooth(clamp((mt-.33)/.42));
  const settle=progress<=MOTION_END?1:1-smooth(clamp((progress-MOTION_END)/(1-MOTION_END)));
  reflection.setAttribute('cx',mix(x,910,.38).toFixed(2));
  reflection.setAttribute('cy',(ground-10).toFixed(2));
  reflection.setAttribute('rx',mix(36,47,threshold).toFixed(2));
  reflection.setAttribute('opacity',(threshold*settle*.105).toFixed(4));
  scrub.value=String(Math.round(progress*1000));
  readout.textContent=progress.toFixed(3);
}
function stop(){
  if(raf) cancelAnimationFrame(raf);
  raf=0;playing=false;play.textContent='Play once';
}
function tick(now){
  if(!playing)return;
  const p=clamp((now-startTime)/DURATION);
  pose(p);
  if(p<1)raf=requestAnimationFrame(tick);else stop();
}
function playOnce(){
  stop();pose(0);playing=true;play.textContent='Pause';
  startTime=performance.now();raf=requestAnimationFrame(tick);
}
play.addEventListener('click',()=>{if(playing){stop();return;}playOnce();});
scrub.addEventListener('input',()=>{stop();pose(Number(scrub.value)/1000);});
image.addEventListener('load',()=>pose(progress));
pose(0);
window.__MOTION01__={
  setProgress(p){stop();pose(Number(p));return this.diagnostic();},
  playOnce,stop,
  diagnostic(){
    const r=stage.getBoundingClientRect();
    return {
      variant:'A-prime Quiet Recognition',progress,durationMs:DURATION,motionWindow:[MOTION_START,MOTION_END],
      figureTransform:figure.getAttribute('transform'),
      headTransform:head.getAttribute('transform'),
      shadowOpacity:shadow.getAttribute('opacity'),
      reflectionOpacity:reflection.getAttribute('opacity'),
      plumOpacity:getComputedStyle(plum).opacity,
      tealOpacity:getComputedStyle(teal).opacity,
      stageRect:{x:r.x,y:r.y,width:r.width,height:r.height},
      stageNatural:[image.naturalWidth,image.naturalHeight],
      viewport:[innerWidth,innerHeight],
      horizontalOverflow:document.documentElement.scrollWidth>innerWidth+1
    };
  }
};
})();
