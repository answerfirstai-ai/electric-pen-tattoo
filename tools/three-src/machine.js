import {WebGLRenderer,Scene,PerspectiveCamera,PMREMGenerator,MeshPhysicalMaterial,Mesh,Group,BoxGeometry,CylinderGeometry,TorusGeometry,SphereGeometry,ConeGeometry,DirectionalLight,SpotLight,ACESFilmicToneMapping,SRGBColorSpace,Color,PointLight,Box3,Vector3} from 'three';
import {RoomEnvironment} from '/workspace/tools/node_modules/three/examples/jsm/environments/RoomEnvironment.js';
export function mount(el,{dpr=1.5,frames=false}={}){
  const r=new WebGLRenderer({antialias:true,alpha:true,preserveDrawingBuffer:frames});
  r.setPixelRatio(Math.min(devicePixelRatio,dpr)); r.toneMapping=ACESFilmicToneMapping; r.toneMappingExposure=1.05; r.outputColorSpace=SRGBColorSpace;
  el.appendChild(r.domElement);
  const s=new Scene(); const pm=new PMREMGenerator(r); s.environment=pm.fromScene(new RoomEnvironment(),.04).texture;
  const cam=new PerspectiveCamera(30,1,.1,100); cam.position.set(0,0.2,9);
  const chrome=new MeshPhysicalMaterial({color:0xdfe3ea,metalness:1,roughness:.08});
  const brass=new MeshPhysicalMaterial({color:0xB8893B,metalness:1,roughness:.25});
  const copper=new MeshPhysicalMaterial({color:0xB06A3E,metalness:1,roughness:.32});
  const grip=new MeshPhysicalMaterial({color:0x111111,metalness:.2,roughness:.45,clearcoat:.6,clearcoatRoughness:.2});
  const m=new Group(); const add=(g,mat,p,rz=0,rx=0)=>{const o=new Mesh(g,mat);o.position.set(...p);o.rotation.z=rz;o.rotation.x=rx;m.add(o);return o};
  // frame: back upright + lower rail + top arm
  add(new BoxGeometry(.32,3.2,.5),chrome,[-1.5,.2,0]);
  add(new BoxGeometry(3.2,.34,.5),chrome,[0,-1.2,0]);
  add(new BoxGeometry(2.4,.22,.36),chrome,[-.4,1.75,0],-.08);
  // coils
  for(const x of [-.5,.45]){add(new CylinderGeometry(.42,.42,1.5,48),copper,[x,-.25,0]);
    for(const y of [.55,-1.03]) add(new CylinderGeometry(.5,.5,.12,48),brass,[x,y,0]);
    for(let i=0;i<9;i++) add(new TorusGeometry(.425,.012,8,48),copper,[x,-.85+i*.17,0],0,Math.PI/2);}
  // armature bar + spring
  add(new BoxGeometry(1.8,.1,.42),new MeshPhysicalMaterial({color:0x222222,metalness:.9,roughness:.35}),[0,.75,0]);
  // binding posts
  for(const p of [[-1.5,1.95,0],[.9,1.62,0],[-1.5,-.95,.3]]){add(new CylinderGeometry(.16,.16,.36,32),brass,p);add(new SphereGeometry(.17,24,16),brass,[p[0],p[1]+.2,p[2]])}
  // tube + grip + tip
  add(new CylinderGeometry(.13,.13,1.4,32),chrome,[1.7,-1.2,0],Math.PI/2);
  const g=add(new CylinderGeometry(.42,.38,1.9,48),grip,[2.9,-1.2,0],Math.PI/2);
  add(new TorusGeometry(.4,.04,12,48),chrome,[1.95,-1.2,0],0,0).rotation.y=Math.PI/2;
  add(new ConeGeometry(.12,.7,32),chrome,[4.15,-1.2,0],-Math.PI/2);
  m.rotation.z=-.5; m.scale.setScalar(.8); const bb=new Box3().setFromObject(m),c=bb.getCenter(new Vector3()); m.position.sub(c); s.add(m);
  const key=new DirectionalLight(0xffffff,2.2);key.position.set(-5,4,6);s.add(key);
  const rim=new DirectionalLight(0xffffff,3);rim.position.set(4,3,-5);s.add(rim);
  const neon=new PointLight(0xC42021,30,14);neon.position.set(3,-2,3);s.add(neon);
  const sweep=new SpotLight(0xFFB86B,0,20,.25,.6);sweep.position.set(-6,2,6);s.add(sweep);s.add(sweep.target);
  let D=15;const size=()=>{const w=el.clientWidth,h=el.clientHeight;r.setSize(w,h,false);cam.aspect=w/h;D=w>h?15.5:15;cam.updateProjectionMatrix()};size();
  let t=0,px=0,tpx=0;
  const set=(p)=>{t=p};
  const render=()=>{px+=(tpx-px)*.06; const a=-.6+t*1.05; cam.position.set(Math.sin(a+px)*D*(1-t*.1),0.5+px*.5,Math.cos(a+px)*D*(1-t*.1)); cam.lookAt(0,0,0);
    sweep.intensity=60*Math.sin(Math.PI*t); sweep.target.position.set(-3+t*6,0,0); r.render(s,cam)};
  return {set,render,size,renderer:r,pointer:(x)=>{tpx=x*.1},canvas:r.domElement};
}
