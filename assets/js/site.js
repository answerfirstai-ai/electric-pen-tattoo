(()=>{
const RM=matchMedia('(prefers-reduced-motion: reduce)').matches;
const $=(s,c=document)=>c.querySelector(s),$$=(s,c=document)=>[...c.querySelectorAll(s)];
const BASE='/electric-pen-tattoo/';
// close mobile menu after picking a link / on Escape
$$('.mnav a').forEach(a=>a.addEventListener('click',()=>a.closest('details').open=false));
addEventListener('keydown',e=>{if(e.key==='Escape')$$('.mnav[open]').forEach(d=>d.open=false)});
if(RM||!window.gsap)return;
gsap.registerPlugin(ScrollTrigger);
if(document.querySelector('.hero .h-sweep')&&matchMedia('(min-width:901px)').matches)gsap.fromTo('.hero .h-sweep',{backgroundPosition:'-40% 0'},{backgroundPosition:'130% 0',ease:'none',scrollTrigger:{trigger:'.hero',start:'top top',end:'bottom top',scrub:.8}});
const desk=matchMedia('(min-width:901px)').matches, fine=matchMedia('(pointer:fine)').matches;
/* 1. Hero "lights up": only the photo + light move; text is visible and clickable from frame 0 */
const himg=null;
if(himg){
  const tl=gsap.timeline({defaults:{ease:'power2.out'}});
  tl.fromTo(himg,{filter:'brightness(.35) blur(6px)',scale:1.1},{filter:'brightness(1) blur(0px)',scale:1,duration:2.2},0)
  const skip=()=>{tl.progress(1);off()};const ev=['wheel','touchstart','keydown','pointerdown'];
  const off=()=>ev.forEach(e=>removeEventListener(e,skip));ev.forEach(e=>addEventListener(e,skip,{passive:true,once:true}));
  // scroll: slow push-in + parallax (no pin)
  gsap.to(himg,{yPercent:6,scale:1.05,ease:'none',scrollTrigger:{trigger:'.hero',start:'top top',end:'bottom top',scrub:true}});
  if(desk&&fine){const m=$('.hero');m.addEventListener('pointermove',e=>{const x=e.clientX/innerWidth-.5,y=e.clientY/innerHeight-.5;gsap.to(himg,{x:x*-14,y:y*-8,duration:1.2,ease:'power2.out'})})}
}
/* parallax layers */
$$('.par').forEach(el=>gsap.fromTo(el,{yPercent:6},{yPercent:-6,ease:'none',scrollTrigger:{trigger:el,start:'top bottom',end:'bottom top',scrub:true}}));
/* rack-focus reveals on images (content stays readable) */
$$('.bk-media img').forEach(img=>gsap.fromTo(img,{scale:1.08,filter:'blur(6px)'},{scale:1,filter:'blur(0px)',duration:1.4,ease:'power2.out',scrollTrigger:{trigger:img,start:'top 85%',once:true}}));
/* 2. Machine: desktop live 3D (pin ≤ 1 viewport), mobile image sequence (no pin) */
/* machine: static render only (Rev4 QA) */
})();
