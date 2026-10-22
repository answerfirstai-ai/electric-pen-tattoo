(()=>{
const RM=matchMedia('(prefers-reduced-motion: reduce)').matches;
const $=(s,c=document)=>c.querySelector(s),$$=(s,c=document)=>[...c.querySelectorAll(s)];
if(!window.gsap){return}
gsap.registerPlugin(ScrollTrigger);
const hero=$('#hero');
if(hero&&!RM){
  const sheet=$('#sheet'),inner=$('.sheet-in',sheet),svg=$('.lettering',sheet);
  const lines=$$('.ln',svg);
  lines.forEach(p=>{const L=Math.ceil(p.getTotalLength());p.style.strokeDasharray=L;p.style.strokeDashoffset=L;p._L=L});
  const tip=$('.tip',svg);
  /* --- 1. Hero entrance: the needle --- */
  const tl=gsap.timeline({defaults:{ease:'power1.inOut'}});
  tl.from(inner,{y:-40,rotate:-3,duration:.6,ease:'back.out(1.4)'},0)
    .from($$('.tape',inner),{scale:0,duration:.25,stagger:.05,ease:'back.out(3)'},.25);
  const W=.55,N=lines.length,D=1.4,state={p:0};
  const buzz=gsap.to(tip,{x:'+=2',y:'-=2',duration:.03,repeat:-1,yoyo:true,ease:'none',paused:true});
  tl.set(tip,{opacity:1},.45).add(()=>buzz.play(),.45)
    .to(state,{p:1,duration:D,ease:'none',onUpdate(){
      const span=1-W, p=state.p; let act=null;
      for(let i=0;i<N;i++){const s=i/(N-1)*span, f=Math.min(1,Math.max(0,(p-s)/W));
        lines[i].style.strokeDashoffset=lines[i]._L*(1-f); if(f>0&&f<1)act=[lines[i],f]}
      if(act){const pt=act[0].getPointAtLength(act[0]._L*act[1]);const m=act[0].getCTM(),sm=svg.getCTM();
        const x=pt.x,y=pt.y,t=act[0].transform.baseVal.consolidate();const tx=t?t.matrix.e:0,ty=t?t.matrix.f:0;
        tip.setAttribute('cx',x+tx);tip.setAttribute('cy',y+ty)}
    }},.45)
    .add(()=>{buzz.pause();gsap.to(tip,{opacity:0,duration:.2})},.45+D);
  const cx=tip.getAttribute('cx');
  ['.fill-r','.fill-g','.fill-y'].forEach((c,i)=>{
    tl.fromTo($(c,svg),{opacity:1,clipPath:'circle(0% at 50% 55%)'},{clipPath:'circle(150% at 50% 55%)',duration:.35,ease:'power2.out'},1.85+i*.12)});
  tl.to($('.shadow',svg),{opacity:1,duration:.3},2.2).to($('.halftone',svg),{opacity:1,duration:.3},2.4)
    .from('.hero-copy .ctas .btn',{y:16,opacity:0,duration:.4,stagger:.08,ease:'power3.out'},2.55)
    .from('.hero .lede',{y:12,duration:.4,ease:'power3.out'},2.5)
    .from('.sticker',{scale:1.4,rotate:12,opacity:0,duration:.3,ease:'back.out(2.5)'},2.8);
  /* --- 2. Ch.1 The wall: pull back --- */
  const mm=gsap.matchMedia();
  mm.add({d:'(min-width:901px)',m:'(max-width:900px)'},ctx=>{
    const ws=$$('.ws');ws.forEach(w=>w.classList.remove('slot'));
    const slot=ws[ctx.conditions.d?7:4];slot.classList.add('slot');
    const others=ws.filter(w=>w!==slot&&getComputedStyle(w).display!=='none');
    const geo=()=>{const a=sheet.getBoundingClientRect(),b=slot.getBoundingClientRect();
      gsap.set(sheet,{x:0,y:0,xPercent:-50,yPercent:-50,scale:1});const a2=sheet.getBoundingClientRect();
      return {s:Math.min(b.width/a2.width,b.height/a2.height),x:(b.left+b.width/2)-(a2.left+a2.width/2),y:(b.top+b.height/2)-(a2.top+a2.height/2)}};
    let g=geo();
    const st=gsap.timeline({scrollTrigger:{trigger:hero,start:'top top',end:'+=150%',pin:true,scrub:.8,invalidateOnRefresh:true,onRefreshInit:()=>{g=geo()}}});
    st.to(sheet,{scale:()=>g.s,x:()=>g.x,y:()=>g.y,ease:'power2.inOut',duration:1},0)
      .to('.hero-copy,.scrollcue',{opacity:0,y:30,duration:.3},0)
      .fromTo(others,{autoAlpha:0,x:()=>gsap.utils.random(-600,600),y:()=>gsap.utils.random(-500,500),rotate:()=>gsap.utils.random(-40,40),scale:1.3},
        {autoAlpha:1,x:0,y:0,rotate:(i,el)=>el.style.getPropertyValue('--r')||0,scale:1,ease:'power3.out',duration:.75,stagger:{each:.03,from:'center'}},.15);
    return ()=>{};
  });
}
if(!RM){
  /* artist sheets tilt in; flash pieces drop; booking steps draw */
  $$('.acard,.fl,.scard,.vcard').forEach(el=>gsap.from(el,{y:40,rotate:-4,opacity:0,duration:.5,ease:'back.out(1.2)',scrollTrigger:{trigger:el,start:'top 88%',once:true}}));
  $$('.step').forEach(el=>{const p=$('.sp',el),L=p.getTotalLength();gsap.set(p,{strokeDasharray:L,strokeDashoffset:L});
    gsap.timeline({scrollTrigger:{trigger:el,start:'top 80%',end:'top 40%',scrub:true}}).to(p,{strokeDashoffset:0,ease:'none'}).from(el,{opacity:.3,x:30,ease:'none'},0)});
  $$('.about h2,.banner-h').forEach(el=>gsap.from(el,{y:30,opacity:0,duration:.6,ease:'power3.out',scrollTrigger:{trigger:el,start:'top 90%'}}));
  /* magnetic sticker / buttons on fine pointer */
  if(matchMedia('(pointer:fine)').matches){
    $$('.btn-y').forEach(b=>{b.addEventListener('pointermove',e=>{const r=b.getBoundingClientRect();gsap.to(b,{x:(e.clientX-r.left-r.width/2)*.18,y:(e.clientY-r.top-r.height/2)*.25,duration:.3})});
      b.addEventListener('pointerleave',()=>gsap.to(b,{x:0,y:0,duration:.5,ease:'elastic.out(1,.4)'}))});
  }
}
})();
