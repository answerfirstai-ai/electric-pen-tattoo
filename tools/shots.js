const {chromium}=require('/workspace/tools/node_modules/playwright');
const base=process.argv[2], out=process.argv[3], tag=process.argv[4]||'';
(async()=>{const b=await chromium.launch();const errs=[];
for(const [name,vp,mob] of [['desktop',{width:1440,height:900},false],['mobile',{width:390,height:844},true]]){
 const c=await b.newContext({viewport:vp,isMobile:mob,hasTouch:mob,deviceScaleFactor:mob?2:1});const p=await c.newPage();
 p.on('console',m=>{if(m.type()==='error')errs.push(name+': '+m.text())});p.on('pageerror',e=>errs.push(name+' pageerror: '+e.message));
 for(const path of ['','artists/','flash/','visit/','nope/']){
  const r=await p.goto(base+path,{waitUntil:'networkidle'});await p.waitForTimeout(path?600:3400);
  const slug=(path.replace(/\/$/,'')||'home');
  if(!path){await p.screenshot({path:`${out}/${tag}${slug}_${name}_hero.png`});
    await p.mouse.wheel(0,vp.height*0.7);await p.waitForTimeout(1200);await p.screenshot({path:`${out}/${tag}${slug}_${name}_pullback.png`});
    await p.mouse.wheel(0,vp.height*1.2);await p.waitForTimeout(1500);await p.screenshot({path:`${out}/${tag}${slug}_${name}_wall.png`});
    await p.evaluate(()=>window.scrollTo(0,0));await p.waitForTimeout(500);}
  await p.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=300){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,60))}});await p.waitForTimeout(800);
  await p.screenshot({path:`${out}/${tag}${slug}_${name}_full.png`,fullPage:true});
 } await c.close();}
console.log(JSON.stringify(errs));await b.close();})();
