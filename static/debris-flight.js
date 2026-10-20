// DEBRIS FIELDS · STAGE 1 — the flight space (prototype; true scale since 2026-10-11).
// Spec: quavara-docs/quavara-debris-field-game-stage1-spec.md. Why it is built this way:
//  • TRUE DISTANCES (Eric 10-11): 1 game unit = 1 metre and the Sun, the rings and the gas giants sit at their real
//    distances. Positions are kept in full precision on the CPU; only small local offsets go to the GPU (each field's
//    rocks are stored relative to the field's centre), so nothing shakes even a billion kilometres out. Bodies far
//    beyond the camera's range (the Sun, Jupiter, Saturn) are drawn at a fixed distance in their true direction and at
//    their true apparent size.
//  • The Sun is the only light; its brightness falls with the square of the distance, so the Mercury ring is bright,
//    the Mars ring dimmer, and the Starship out by Jupiter sits in deep twilight under its own floodlights.
//  • WARP (Eric 10-11) crosses the system in seconds: to any of the four rings, the Starship, the wormhole, Jupiter or
//    Saturn. Pick a ring and you arrive on its line at your current longitude.
//  • The debris lies in a band around each ring's line. Fields are laid out in 3 km cells around the pilot from the
//    session's random seed, so every session is a new layout and the rings never run dry. Inara warns you when you
//    drift out of the ring you're working.
//  • The Starship parks by the wormhole on the far side of Jupiter (STORY-BIBLE), far from every debris field.
'use strict';
let SEED=(function(){try{return crypto.getRandomValues(new Uint32Array(1))[0];}catch(e){return (Math.random()*4294967296)>>>0;}})();
function rng(seed){let a=seed>>>0;return function(){a=(a+0x6D2B79F5)>>>0;let t=a;t=Math.imul(t^(t>>>15),t|1);
 t^=t+Math.imul(t^(t>>>7),t|61);return((t^(t>>>14))>>>0)/4294967296;};}
const R=rng(SEED);

// ── SCALE: true distances. 1 unit = 1 metre.
const AU=1.495978707e11;                 // metres
const SUN_R=6.957e8;                     // the Sun's true radius, metres
const SUN_POS=new THREE.Vector3();
const Y_AXIS=new THREE.Vector3(0,1,0);
const RINGS=[ // where the four destroyed inner planets orbited: their true mean distances from the Sun (STORY-BIBLE.md)
 {key:'mercury',planet:'Mercury',au:0.387},
 {key:'venus',  planet:'Venus',  au:0.723},
 {key:'earth',  planet:'Earth',  au:1.000},
 {key:'mars',   planet:'Mars',   au:1.524}];
RINGS.forEach(r=>{r.r=r.au*AU;r.name=r.planet+' ring';});
// The band the debris is spread through around each ring's line (tunable): 25 km either side, 6 km above and below.
// Narrow enough that a pilot can drift out of it and Inara notices; far wider than any scanner can reach.
const BAND={half:25000,thick:6000};
const CELL=3000;                         // fields are laid out in 3 km cells around the pilot (about one per cell)
const FIELD_GAP=260;
// Field types (Eric 10-11): a field's size and its pieces' sizes are separate. Every field is a MIX of piece sizes, with
// far more small fragments than big ones (as broken rock really is), so even a huge field has plenty a beginner's hold
// can take, while its big chunks wait for whoever has a mining laser. Bigger fields are easier to see and hear.
//   n = how many pieces (range) · sc = piece scale range in metres (smallest..largest) · share = how often it occurs
const SIZES={
 large: {n:[400,1200],sc:[0.05,4.0], sight:1100,share:.25},   // huge fields: every size, from pebbles to big chunks
 medium:{n:[60,250],  sc:[0.06,2.0], sight:600, share:.35},
 small: {n:[10,20],   sc:[0.12,1.2], sight:260, share:.25},   // small fields: small and medium pieces
 tiny:  {n:[8,20],    sc:[0.04,0.35],sight:160, share:.15}};  // tiny clusters: very small and small pieces, the faintest
const SIZE_BIAS=2.4;                     // >1 = many more small pieces than large ones
function fieldRad(n,sc){return Math.round(3*Math.cbrt(n)+2.5*sc[1]);}   // a field spreads out with its piece count
const GIANTS=[ // true mean distances and radii; the angles just set where they are in this session's sky
 {name:'Jupiter',au:5.204,ang:2.1,rad:6.9911e7,color:0xd2b08a},
 {name:'Saturn', au:9.583,ang:4.4,rad:5.8232e7,color:0xe0cc9c,ring:true}];
GIANTS.forEach(g=>g.pos=new THREE.Vector3(Math.cos(g.ang),0,Math.sin(g.ang)).multiplyScalar(g.au*AU));
// The wormhole opened near the far side of Jupiter (STORY-BIBLE): here, 3 million km beyond Jupiter, away from the Sun.
const WORMHOLE_POS=GIANTS[0].pos.clone().add(GIANTS[0].pos.clone().normalize().multiplyScalar(3.0e9));
const WORMHOLE_R=1500;
// The Starship parks 30 km off the wormhole so its research teams can keep studying it, far from every debris field.
const STARSHIP_POS=(function(){const out=WORMHOLE_POS.clone().normalize(),side=new THREE.Vector3(-out.z,0,out.x);
 return WORMHOLE_POS.clone().addScaledVector(side,30000).addScaledVector(out,-12000).add(new THREE.Vector3(0,2500,0));})();

// ── RENDERER / SCENE
const cv=document.getElementById('c');
const renderer=new THREE.WebGLRenderer({canvas:cv,antialias:true,logarithmicDepthBuffer:true});
renderer.setPixelRatio(Math.min(devicePixelRatio,2));
renderer.physicallyCorrectLights=true;
renderer.toneMapping=THREE.ACESFilmicToneMapping;renderer.toneMappingExposure=1.15;
renderer.outputEncoding=THREE.sRGBEncoding;
const scene=new THREE.Scene();scene.background=new THREE.Color(0x000000);
scene.fog=new THREE.FogExp2(0x000000,0.0009);   // how far YOU can see; landmarks and lights ignore it
const cam=new THREE.PerspectiveCamera(62,innerWidth/innerHeight,0.3,400000);
function resize(){cam.aspect=innerWidth/innerHeight;cam.updateProjectionMatrix();renderer.setSize(innerWidth,innerHeight);}
addEventListener('resize',resize);resize();


// ── THE SUN: the one light. A directional light from the Sun's true direction, as bright as the inverse-square law says
//    at the pilot's distance (1.6 at 1 AU, the brightness tuned for the Earth ring earlier).
const sunLight=new THREE.DirectionalLight(0xfff1dc,1.6);scene.add(sunLight);scene.add(sunLight.target);
scene.add(new THREE.AmbientLight(0x0a0d14,0.02));   // a whisper, so the dark side is black-blue, not a hole
function glowTex(stops){const c=document.createElement('canvas');c.width=c.height=256;const g=c.getContext('2d');
 const gr=g.createRadialGradient(128,128,0,128,128,128);stops.forEach(s=>gr.addColorStop(s[0],s[1]));g.fillStyle=gr;
 g.fillRect(0,0,256,256);const t=new THREE.CanvasTexture(c);t.encoding=THREE.sRGBEncoding;return t;}
const sun=new THREE.Mesh(new THREE.SphereGeometry(1,48,32),new THREE.MeshBasicMaterial({color:0xfff3d0,fog:false}));
scene.add(sun);
const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex([[0,'rgba(255,240,200,1)'],[.18,'rgba(255,214,140,.55)'],
 [.45,'rgba(255,170,80,.12)'],[1,'rgba(255,140,40,0)']]),fog:false,depthWrite:false,blending:THREE.AdditiveBlending,transparent:true}));
scene.add(glow);

// Far bodies are drawn IMP_D metres away in their true direction, scaled to their true apparent size (the camera can't
// reach a billion kilometres, and doesn't need to).
const IMP_D=200000,tv=new THREE.Vector3();
function placeFar(obj,truePos,trueR){tv.copy(truePos).sub(cam.position);const d=tv.length();
 if(d<IMP_D){obj.position.copy(truePos);obj.scale.setScalar(trueR);return trueR;}
 obj.position.copy(cam.position).addScaledVector(tv,IMP_D/d);const s=trueR*IMP_D/d;obj.scale.setScalar(s);return s;}

// ── STARFIELD (rides with the camera: the stars are too far for anything you do to move them)
const stars=(function(){const n=6000,P=new Float32Array(n*3),C=new Float32Array(n*3);
 for(let i=0;i<n;i++){const u=R()*2-1,th=R()*Math.PI*2,s=Math.sqrt(1-u*u),d=300000;
  P[i*3]=s*Math.cos(th)*d;P[i*3+1]=u*d;P[i*3+2]=s*Math.sin(th)*d;const b=0.25+Math.pow(R(),3)*0.75,w=R()<0.1;
  C[i*3]=b;C[i*3+1]=b*(w?0.85:0.95);C[i*3+2]=b*(w?0.7:1);}
 const g=new THREE.BufferGeometry();g.setAttribute('position',new THREE.BufferAttribute(P,3));g.setAttribute('color',new THREE.BufferAttribute(C,3));
 const p=new THREE.Points(g,new THREE.PointsMaterial({size:1.6,sizeAttenuation:false,vertexColors:true,fog:false,depthWrite:false}));
 scene.add(p);return p;})();

// ── GAS GIANTS (landmarks): lit by the Sun, never fogged, with a faint glow of their own so they read as discs.
const LANDMARKS=[];
GIANTS.forEach(g=>{
 const m=new THREE.Mesh(new THREE.SphereGeometry(1,64,40),new THREE.MeshStandardMaterial({color:g.color,roughness:1,metalness:0,fog:false,emissive:g.color,emissiveIntensity:0.07}));
 if(g.ring){const rg=new THREE.Mesh(new THREE.RingGeometry(1.35,2.3,96),new THREE.MeshStandardMaterial({color:0xcdb892,
  roughness:1,side:THREE.DoubleSide,transparent:true,opacity:.75,fog:false}));rg.rotation.x=Math.PI/2.4;m.add(rg);}
 scene.add(m);LANDMARKS.push({name:g.name,pos:g.pos,draw:m,rad:g.rad,far:true});});
LANDMARKS.push({name:'Sun',pos:SUN_POS,draw:sun,rad:SUN_R,far:true});

// ── THE WORMHOLE (STORY-BIBLE): a dark throat ringed with light, slowly turning. Its research is why the Starship is here.
const wormhole=new THREE.Group();
(function(){const core=new THREE.Mesh(new THREE.SphereGeometry(1,48,32),new THREE.MeshBasicMaterial({color:0x000000,fog:false}));
 wormhole.add(core);
 const ringTex=glowTex([[0,'rgba(0,0,0,0)'],[.42,'rgba(0,0,0,0)'],[.5,'rgba(150,200,255,.95)'],[.6,'rgba(120,90,255,.45)'],[1,'rgba(40,20,120,0)']]);
 [[3.2,0.9],[4.6,0.45]].forEach(([s,o],i)=>{const sp=new THREE.Sprite(new THREE.SpriteMaterial({map:ringTex,fog:false,depthWrite:false,
  blending:THREE.AdditiveBlending,transparent:true,opacity:o}));sp.scale.set(s,s,1);sp.userData.spin=i?-0.05:0.08;wormhole.add(sp);});})();
wormhole.position.copy(WORMHOLE_POS);wormhole.scale.setScalar(WORMHOLE_R);scene.add(wormhole);
LANDMARKS.push({name:'Wormhole',pos:WORMHOLE_POS,draw:wormhole,rad:WORMHOLE_R});

// ── THE STARSHIP: Humboldt-Horizon class, Eric's design (10-10, finished 10-11). True scale: 263 m hull (266 m to the wingtips), 244 m wingtip to wingtip.
//    Model axes: bow toward +Z (the group is turned to face the Sun), Y up.
//    Ships come home from the front, pass UNDER the long bow, and fly aft into the opening (the "mouth") between the
//    bow and the lower rear fins. The command deck is the band of lit windows on the underside of the bow, looking
//    down on that approach: it is the Tower, where Inara watches you come in.
const ship=new THREE.Group();
const DOCK={approach:new THREE.Vector3(0,-34,215),mouth:new THREE.Vector3(0,-30,-35)};   // ship-local waypoints
const guideLights=[];
(function(){
 const hullMat=new THREE.MeshStandardMaterial({color:0x5a606b,roughness:.5,metalness:.35,fog:false});   // dark gunmetal (high metalness reads black with no reflections to show)
 const finMat=new THREE.MeshStandardMaterial({color:0x4a4f58,roughness:.55,metalness:.35,side:THREE.DoubleSide,fog:false});
 // hull sections: a top-view profile lofted with an OVAL cross-section (Eric, 10-11: the body matches the oval exhaust),
 // squeezed thin toward the bow tip. section() gives the half-width and half-height at any z, so parts sit on the skin.
 const SKIN=2.2;
 function section(pts,height,taperFrom,taperTo){const zTip=pts[0][1],zLast=pts[pts.length-1][1];
  return z=>{let w=pts[pts.length-1][0]+SKIN;
   if(z>zLast)for(let i=1;i<pts.length;i++){const a=pts[i-1],b=pts[i];if(z<=a[1]&&z>=b[1]){const t=(a[1]-z)/(a[1]-b[1]);
    w=a[0]+(b[0]-a[0])*t+SKIN*Math.min(1,(zTip-z)/10);break;}}
   const t=Math.min(1,Math.max(0,(z-taperFrom)/(taperTo-taperFrom)));return {w:Math.max(0,w),h:height*0.85*(1-0.85*t)};};}
 // ring point: the oval, plus an optional blade edge drawn out along each side (Eric, 10-11: sharp port and starboard edges)
 const EDGE_K=3;
 // wo = the un-rounded half-width: the blade edge is measured from it, so rounding the stern never moves the blades
 function ring(a,w,h,flare,wo=w){const c=Math.cos(a),s=Math.sin(a);
  return [c*w+Math.sign(c)*(flare*wo+(wo-w))*Math.pow(1-Math.abs(s),EDGE_K),s*h];}
 // stern rounding (Eric, 10-11): over the last ROUND_L metres the body curves in by up to ROUND_D, a quarter-round
 // fillet, so the rear end has soft edges. The blade edges keep their full reach.
 const ROUND_L=6;
 function dagger(pts,height,taperFrom,taperTo,flare=0,hole=null){
  const sec=section(pts,height,taperFrom,taperTo),N=64,S=80,zTip=pts[0][1],zEnd=pts[pts.length-1][1]-SKIN;
  const pos=[],idx=[];
  const zs=[];for(let j=0;j<=S;j++){const z=zTip-(zTip-zEnd)*j/S;if(z>zEnd+ROUND_L)zs.push(z);}
  for(let j=0;j<=10;j++)zs.push(zEnd+ROUND_L*(1-j/10));                          // fine steps through the fillet
  const D=Math.min(3,0.35*sec(zEnd).h);
  const round=z=>{const u=Math.max(0,1-(z-zEnd)/ROUND_L);return D*(1-Math.sqrt(1-u*u));};
  for(const z of zs){const {w,h}=sec(z),d=round(z);
   for(let i=0;i<N;i++){const r=ring(i/N*Math.PI*2,w-d,h-d,flare,w);pos.push(r[0],r[1],z);}}
  for(let j=0;j<zs.length-1;j++)for(let i=0;i<N;i++){const a=j*N+i,b=j*N+(i+1)%N,c=a+N,d=b+N;idx.push(a,c,b,b,c,d);}
  const ci=pos.length/3,{w,h}=sec(zEnd);                                          // flat stern cap; with a hole it is a ring
  for(let i=0;i<N;i++){const r=ring(i/N*Math.PI*2,w-D,h-D,flare,w);pos.push(r[0],r[1],zEnd);}  // around the exhaust opening
  if(hole){for(let i=0;i<N;i++){const a=i/N*Math.PI*2;pos.push(Math.cos(a)*hole.rx,Math.sin(a)*hole.ry,zEnd);}
   for(let i=0;i<N;i++){const o=ci+i,o1=ci+(i+1)%N,n=ci+N+i,n1=ci+N+(i+1)%N;idx.push(n,o1,o,n,n1,o1);}}
  else{const c=pos.length/3;pos.push(0,0,zEnd);for(let i=0;i<N;i++)idx.push(c,ci+(i+1)%N,ci+i);}
  const g=new THREE.BufferGeometry();g.setAttribute('position',new THREE.Float32BufferAttribute(pos,3));g.setIndex(idx);
  g.computeVertexNormals();return g;}
 // main hull: needle bow at z=+130, widest at the wings, stern at z=-130
 const MAIN=[[0,130],[7,90],[15,30],[19,-40],[20,-100],[14,-130]],MAIN_FLARE=1.2,mainSec=section(MAIN,14,20,130);
 const EXH={rx:12,ry:12*0.42},ZS=MAIN[MAIN.length-1][1]-SKIN;          // exhaust opening in the stern face, and that face's z
 const main=new THREE.Mesh(dagger(MAIN,14,20,130,MAIN_FLARE,EXH),hullMat);ship.add(main);
 // upper deck ridge
 const RIDGE=[[0,70],[6,30],[10,-40],[11,-110],[8,-126]],RIDGE_Y=12,ridgeSec=section(RIDGE,8,0,70);
 const ridge=new THREE.Mesh(dagger(RIDGE,8,0,70),hullMat);ridge.position.y=RIDGE_Y;ship.add(ridge);
 // fin from a 2-D triangle-ish outline (x = along the ship, y = out from the hull), thin
 function fin(outline,thick){const sh=new THREE.Shape();outline.forEach((p,i)=>i?sh.lineTo(p[0],p[1]):sh.moveTo(p[0],p[1]));
  const g=new THREE.ExtrudeGeometry(sh,{depth:thick,bevelEnabled:false});g.translate(0,0,-thick/2);return new THREE.Mesh(g,finMat);}
 // dorsal shark fin
 const DORSAL=[[-120,0],[-40,0],[-95,34],[-118,30]];
 const dorsal=fin(DORSAL,1.6);dorsal.rotation.y=-Math.PI/2;dorsal.position.y=16;ship.add(dorsal);
 // swept side wings (Eric's top-view illustration, 10-11): flat blades in the plane of the hull's side edges, rooted
 // inside the body and swept back to sharp tips beside the stern. Outline in ship coordinates (x out, z along).
 const WING=[[18,15],[122,-136],[106,-128],[18,-92]];
 [-1,1].forEach(s=>{const sh=new THREE.Shape();WING.forEach((p,i)=>i?sh.lineTo(s*p[0],p[1]):sh.moveTo(s*p[0],p[1]));
  const g=new THREE.ExtrudeGeometry(sh,{depth:1.4,bevelEnabled:false});g.translate(0,0,-0.7);g.rotateX(Math.PI/2);
  const w=new THREE.Mesh(g,finMat);w.position.y=-0.3;ship.add(w);});
 // lower rear fins: blades rooted in the underside of the stern, splayed out and down at 45° (Eric's illustrations, 10-11);
 // the mouth is the gap between them, under the hull
 [-1,1].forEach(s=>{const b=fin([[-124,4],[-60,4],[-10,-46],[-40,-44],[-120,-12]],2.0);
  b.rotation.y=-Math.PI/2;const g=new THREE.Group();g.add(b);g.position.set(s*10,-5,0);g.rotation.z=s*Math.PI/4;ship.add(g);});
 // engine: an oval exhaust set into the stern (Eric's illustration, 10-11), no tail pipe. A dark well sunk flush into the stern,
 // and the heat source glowing from deep inside it: a long hot core between two round burners.
 const OV=0.42;                                                       // oval height / width
 const well=new THREE.Mesh(new THREE.CylinderGeometry(12,12,6,64,1,true),new THREE.MeshStandardMaterial({color:0x23272d,
  roughness:.6,metalness:.4,side:THREE.DoubleSide,fog:false}));well.rotation.x=Math.PI/2;well.scale.set(1,1,OV);well.position.z=ZS+3;ship.add(well);   // sunk into the hull, flush with the stern
 const rim=new THREE.Mesh(new THREE.TorusGeometry(12,0.6,8,64),hullMat);rim.scale.set(1,OV,1);rim.position.z=ZS;ship.add(rim);   // thin lip on the opening
 const heat=(()=>{const c=document.createElement('canvas');c.width=512;c.height=216;const g=c.getContext('2d');
  g.save();g.beginPath();g.ellipse(256,108,252,104,0,0,Math.PI*2);g.clip();
  g.fillStyle='#3a1a06';g.fillRect(0,0,512,216);
  const blob=(x,y,rx,ry,stops)=>{g.save();g.translate(x,y);g.scale(rx/ry,1);const gr=g.createRadialGradient(0,0,0,0,0,ry);
   stops.forEach(t=>gr.addColorStop(t[0],t[1]));g.fillStyle=gr;g.beginPath();g.arc(0,0,ry,0,Math.PI*2);g.fill();g.restore();};
  blob(256,108,250,104,[[0,'rgba(255,150,60,.55)'],[1,'rgba(120,50,10,0)']]);            // warm wash across the well
  blob(256,108,120,46,[[0,'#fff6dc'],[.35,'#ffd28a'],[.75,'rgba(255,150,60,.6)'],[1,'rgba(255,120,40,0)']]);   // long core
  [118,394].forEach(x=>blob(x,108,48,48,[[0,'#fffbea'],[.4,'#ffd58f'],[.8,'rgba(255,150,60,.5)'],[1,'rgba(255,120,40,0)']]));
  g.restore();const t=new THREE.CanvasTexture(c);t.encoding=THREE.sRGBEncoding;return t;})();
 const core=new THREE.Mesh(new THREE.PlaneGeometry(24,24*OV),new THREE.MeshBasicMaterial({map:heat,transparent:true,fog:false,toneMapped:false}));
 core.position.z=ZS+5.8;core.rotation.y=Math.PI;ship.add(core);
 const eglow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex([[0,'rgba(255,190,110,.9)'],[.3,'rgba(255,150,60,.35)'],[1,'rgba(255,120,40,0)']]),
  fog:false,depthWrite:false,blending:THREE.AdditiveBlending,transparent:true}));eglow.scale.set(40,17,1);eglow.position.z=-140;ship.add(eglow);
 const el=new THREE.PointLight(0xff9c4a,500,0,2);el.position.z=-160;ship.add(el);   // dim: lights what is behind the ship, keeps the stern dark
 // THE TOWER (command deck): a long pod hanging under the bow (Eric, 10-11). Inara is stationed here, watching every craft
 // that leaves and comes home; the docking path runs beneath it. A wraparound band of tall lit windows looks out on all
 // sides, with a second row angled down over the approach. The pod's top is sunk into the hull so it reads as one piece.
 const TOWER={zc:45,L:11.3,W:3.7,H:2,yc:-10.5,p:2.5,gap:1.5};   // 1/3 of the first draft (Eric, 10-11)                       // centre z, half-length, half-width, half-height
 // the pod's centre line follows the hull's underside and sweeps up toward its nose, so the front blends into the hull
 const towerY=z=>-mainSec(z).h+(TOWER.yc+mainSec(TOWER.zc).h)+1.5*Math.max(0,(z-TOWER.zc)/TOWER.L)**2;
 const towerHalfW=z=>{const u=Math.min(1,Math.abs(z-TOWER.zc)/TOWER.L);return TOWER.W*Math.pow(1-Math.pow(u,TOWER.p),1/TOWER.p);};
 {const N=40,zs=[];for(let j=0;j<=48;j++){const t=-1+2*j/48;zs.push(TOWER.zc+TOWER.L*Math.sign(t)*Math.pow(Math.abs(t),0.8));}
  const pos=[],idx=[];
  for(const z of zs){const w=towerHalfW(z),h=TOWER.H*w/TOWER.W;
   for(let i=0;i<N;i++){const a=i/N*Math.PI*2;pos.push(Math.cos(a)*w,towerY(z)+Math.sin(a)*h,z);}}
  for(let j=0;j<zs.length-1;j++)for(let i=0;i<N;i++){const a=j*N+i,b=j*N+(i+1)%N,c=a+N,d=b+N;idx.push(a,b,c,b,d,c);}
  const g=new THREE.BufferGeometry();g.setAttribute('position',new THREE.Float32BufferAttribute(pos,3));g.setIndex(idx);
  g.computeVertexNormals();ship.add(new THREE.Mesh(g,hullMat));}
 // windows: walk the pod's outline at window height and set a pane every TOWER.gap metres (facing outward), all the way round except the aft end
 {const deckMat=new THREE.MeshBasicMaterial({color:0xffd9a0,fog:false,side:THREE.DoubleSide});
  const rows=[{dy:-0.2,pw:1.0,ph:1.2,tilt:0},{dy:-1.15,pw:0.9,ph:0.7,tilt:0.55}];  // main band; lower row tilted to look down
  const outline=[];for(let i=0;i<=720;i++){const th=i/720*Math.PI*2,c=Math.cos(th),sn=Math.sin(th);
   outline.push([TOWER.W*Math.sign(c)*Math.pow(Math.abs(c),2/TOWER.p),TOWER.zc+TOWER.L*Math.sign(sn)*Math.pow(Math.abs(sn),2/TOWER.p)]);}
  const m4=new THREE.Matrix4(),q=new THREE.Quaternion(),e=new THREE.Euler(0,0,0,'YXZ'),one=new THREE.Vector3(1,1,1),v=new THREE.Vector3();
  for(const r of rows){const k=Math.sqrt(Math.max(0,1-(r.dy/TOWER.H)**2)),spots=[];let run=0;
   for(let i=1;i<outline.length;i++){const p0=outline[i-1],p1=outline[i];run+=Math.hypot(p1[0]-p0[0],p1[1]-p0[1]);
    if(run<TOWER.gap)continue;run=0;if(p1[1]<TOWER.zc-TOWER.L*0.55)continue;                 // no windows on the aft end
    const yaw=Math.atan2(p1[0]-p0[0],p1[1]-p0[1])+Math.PI/2;spots.push([p1[0]*k,p1[1],yaw]);}
   const im=new THREE.InstancedMesh(new THREE.PlaneGeometry(r.pw,r.ph),deckMat,spots.length);
   spots.forEach((sp,n)=>{const nx=Math.sin(sp[2]),nz=Math.cos(sp[2]);
    v.set(sp[0]+nx*0.12,towerY(sp[1])+r.dy,sp[1]+nz*0.12);e.set(r.tilt,sp[2],0);q.setFromEuler(e);m4.compose(v,q,one);im.setMatrixAt(n,m4);});
   ship.add(im);}}
 // THE NAME (Eric, 10-11): "WSC ALEXANDER VON HUMBOLDT" on both sides of the raised section on top, clear of the
 // windows. It lines up with the tall rear fin: on the starboard side the first letter starts under the fin's leading
 // edge, and on the port side the last letter ends under it; from there the name runs aft. The lettering is a strip
 // laid onto the curved skin so it sits flush along its whole length.
 {const NAME='WSC  ALEXANDER  VON  HUMBOLDT',TH=3.4,YC=RIDGE_Y+2;
  const c=document.createElement('canvas'),g=c.getContext('2d');g.font='600 180px Georgia, "Times New Roman", serif';
  const tw=Math.ceil(g.measureText(NAME).width)+40;c.width=tw;c.height=256;
  g.font='600 180px Georgia, "Times New Roman", serif';g.fillStyle='#eef1f5';g.textBaseline='middle';g.fillText(NAME,20,136);
  const tex=new THREE.CanvasTexture(c);tex.encoding=THREE.sRGBEncoding;tex.anisotropy=8;
  const mat=new THREE.MeshBasicMaterial({map:tex,transparent:true,fog:false,toneMapped:false,side:THREE.DoubleSide,
   polygonOffset:true,polygonOffsetFactor:-2});                                         // lit lettering, readable on the dark hull
  const L=TH*tw/256,zFront=DORSAL[1][0],SEG=40;                                          // fin's leading edge on the hull
  const skinX=(y,z)=>{const k=ridgeSec(z),sn=Math.max(-1,Math.min(1,(y-RIDGE_Y)/k.h));return k.w*Math.sqrt(1-sn*sn);};
  [-1,1].forEach(sd=>{const pos=[],uv=[],idx=[];
   const ROWS=8;                                                                         // rows across the height follow the curve
   for(let i=0;i<=SEG;i++)for(let j=0;j<=ROWS;j++){const u=i/SEG,v=j/ROWS,y=YC+(v-0.5)*TH;
    const z=sd>0?zFront-u*L:zFront-L+u*L;                                               // reads bow→stern on starboard, stern→bow on port
    pos.push(sd*(skinX(y,z)+0.15),y,z);uv.push(u,v);}
   for(let i=0;i<SEG;i++)for(let j=0;j<ROWS;j++){const a=i*(ROWS+1)+j,b=a+ROWS+1;idx.push(a,b,a+1,a+1,b,b+1);}
   const geo=new THREE.BufferGeometry();geo.setAttribute('position',new THREE.Float32BufferAttribute(pos,3));
   geo.setAttribute('uv',new THREE.Float32BufferAttribute(uv,2));geo.setIndex(idx);ship.add(new THREE.Mesh(geo,mat));});}
 // THE BAY DOOR (Eric, 10-11): a large hatch in the belly behind the Tower, shown only closed. Players infer it is where
 // their craft dock and undock; it sits over the docking mouth. Panels follow the curved belly: a framed door split
 // down the middle into two leaves, with cross ribs and amber marker lights at the corners.
 {const BAY={x:11,z0:-58,z1:-8};
  const belly=(x,z)=>{const k=mainSec(z);return -k.h*Math.sqrt(Math.max(0,1-(x/k.w)**2));};
  const patch=(x0,x1,z0,z1,off,mat)=>{const nx=12,nz=20,pos=[],idx=[];
   for(let j=0;j<=nz;j++)for(let i=0;i<=nx;i++){const x=x0+(x1-x0)*i/nx,z=z0+(z1-z0)*j/nz;pos.push(x,belly(x,z)-off,z);}
   for(let j=0;j<nz;j++)for(let i=0;i<nx;i++){const a=j*(nx+1)+i,b=a+1,c=a+nx+1,d=c+1;idx.push(a,b,c,b,d,c);}
   const g=new THREE.BufferGeometry();g.setAttribute('position',new THREE.Float32BufferAttribute(pos,3));g.setIndex(idx);
   g.computeVertexNormals();ship.add(new THREE.Mesh(g,mat));};
  const doorMat=new THREE.MeshStandardMaterial({color:0x40454e,roughness:.6,metalness:.4,side:THREE.DoubleSide,fog:false});
  const frameMat=new THREE.MeshStandardMaterial({color:0x7a808b,roughness:.4,metalness:.5,side:THREE.DoubleSide,fog:false});
  const seamMat=new THREE.MeshBasicMaterial({color:0x0b0d10,side:THREE.DoubleSide,fog:false});
  patch(-BAY.x,BAY.x,BAY.z0,BAY.z1,0.12,doorMat);                                  // the door
  const F=1.4;                                                                      // frame width
  patch(-BAY.x-F,BAY.x+F,BAY.z0-F,BAY.z0,0.3,frameMat);patch(-BAY.x-F,BAY.x+F,BAY.z1,BAY.z1+F,0.3,frameMat);
  patch(-BAY.x-F,-BAY.x,BAY.z0,BAY.z1,0.3,frameMat);patch(BAY.x,BAY.x+F,BAY.z0,BAY.z1,0.3,frameMat);
  patch(-0.25,0.25,BAY.z0,BAY.z1,0.2,seamMat);                                     // centre seam: two leaves
  for(let z=BAY.z0+10;z<BAY.z1-1;z+=10){patch(-BAY.x,-0.25,z-0.15,z+0.15,0.18,seamMat);patch(0.25,BAY.x,z-0.15,z+0.15,0.18,seamMat);}
  const lamp=new THREE.MeshBasicMaterial({color:0xffb347,fog:false}),lg=new THREE.SphereGeometry(0.6,10,8);
  [[-1,BAY.z0-F/2],[1,BAY.z0-F/2],[-1,BAY.z1+F/2],[1,BAY.z1+F/2]].forEach(c=>{const x=c[0]*(BAY.x+F/2);
   const m=new THREE.Mesh(lg,lamp);m.position.set(x,belly(x,c[1])-0.5,c[1]);ship.add(m);});}
 // scattered lit portholes along the flanks
 const pm=new THREE.InstancedMesh(new THREE.PlaneGeometry(1.1,0.55),new THREE.MeshBasicMaterial({color:0xffcf8a,fog:false,side:THREE.DoubleSide}),420);
 const m4=new THREE.Matrix4(),q4=new THREE.Quaternion(),s4=new THREE.Vector3(1,1,1),p4=new THREE.Vector3();
 for(let i=0;i<420;i++){const z=-125+Math.random()*215;const side=Math.random()<.5?-1:1;
  const y=-3+Math.random()*8*(z>60?0.4:1),k=mainSec(z);
  p4.set(side*(ring(Math.asin(Math.max(-1,Math.min(1,y/k.h))),k.w,k.h,MAIN_FLARE)[0]+0.15),y,z);   // on the flank skin
 q4.setFromAxisAngle(Y_AXIS,side*Math.PI/2);m4.compose(p4,q4,s4);pm.setMatrixAt(i,m4);}
 ship.add(pm);
 // hull floodlights, so the ship reads as a shape even on the side away from the Sun
 [[0,45,-20,4500,0xc8d4ff],[0,-75,60,2200,0xffe0b0],[60,0,-60,3000,0xc8d4ff],[-60,0,-60,3000,0xc8d4ff]].forEach(f=>{
  const l=new THREE.PointLight(f[4],f[3],0,2);l.position.set(f[0],f[1],f[2]);ship.add(l);});
 // the mouth: a faint blue work-light inside the opening
 const ml=new THREE.PointLight(0x7fb0ff,1800,0,2);ml.position.set(0,-22,-40);ship.add(ml);
 // guide lights: a lane from in front of the bow, under it, into the mouth (they pulse in sequence toward the ship)
 const gm=new THREE.SphereGeometry(0.9,10,8);
 for(let i=0;i<16;i++){const t=i/15;const p=DOCK.approach.clone().lerp(DOCK.mouth,t);
  [-1,1].forEach(s=>{const m=new THREE.Mesh(gm,new THREE.MeshBasicMaterial({color:0x7fe0a8,fog:false}));m.position.set(s*9,p.y-4,p.z);ship.add(m);guideLights.push({m,t});});}
})();
ship.position.copy(STARSHIP_POS);ship.lookAt(0,0,0);scene.add(ship);
ship.updateMatrixWorld(true);
const DOCK_W={approach:ship.localToWorld(DOCK.approach.clone()),mouth:ship.localToWorld(DOCK.mouth.clone())};
function pulseGuides(t){for(const g of guideLights){const ph=((t*0.6-g.t)%1+1)%1;const k=Math.pow(1-ph,6);g.m.material.color.setRGB(0.25+0.25*k,0.45+0.5*k,0.35+0.4*k);}}
LANDMARKS.unshift({name:'Starship',pos:ship.position,draw:ship,home:true,rad:140});

// ── MATERIALS, HOLD AND COLLECTING (Eric 10-10: cubic space, true shapes).
//  • 1 game unit = 1 metre. Every rock IS a piece of material at its true size and shape (its mesh scale), with a real
//    volume and a real mass (volume × the material's real density).
//  • The hold has real interior dimensions. A piece goes in only if (1) its shape fits through and inside the hold
//    (its three dimensions, turned any way, against the hold's) and (2) there is room left for its BULK: the box it
//    occupies, not just its own volume. Irregular rocks waste space, so two pieces whose volumes would fit can still
//    fail to fit together; they must be cut smaller first (mining laser, later).
//  • Collecting takes time per piece (bigger pieces longer). Nothing is instant.
const MATERIALS={ // kg per cubic metre (real densities). Fields hold ORES and minerals as found (Eric 10-11, rule 25);
 // every piece is pure mineral (rule 27). The ONE list is minerals.py on the server (Eric 10-19: about thirty real
 // minerals in three tiers); test_server.py checks this copy against it. 1 diamond in 100,000 is near-flawless: the
 // server rolls it (rule 26). Lonsdaleite gets its own alert when collected.
 "basalt"         :{name:"Basalt",density:2900,band:'common'},
 "iron-nickel"    :{name:"Iron-nickel metal",density:7900,band:'common'},
 "water-ice"      :{name:"Water ice",density:917,band:'common'},
 "iron"           :{name:"Iron ore (hematite)",density:5300,band:'plentiful'},
 "magnetite"      :{name:"Iron ore (magnetite)",density:5150,band:'plentiful'},
 "bauxite"        :{name:"Aluminium ore (bauxite)",density:2400,band:'plentiful'},
 "olivine"        :{name:"Magnesium ore (olivine)",density:3270,band:'plentiful'},
 "quartz"         :{name:"Quartz",density:2650,band:'plentiful'},
 "copper"         :{name:"Copper ore (chalcopyrite)",density:4190,band:'ore'},
 "ilmenite"       :{name:"Titanium ore (ilmenite)",density:4720,band:'ore'},
 "pentlandite"    :{name:"Nickel ore (pentlandite)",density:4800,band:'ore'},
 "sphalerite"     :{name:"Zinc ore (sphalerite)",density:4050,band:'ore'},
 "galena"         :{name:"Lead ore (galena)",density:7600,band:'ore'},
 "chromite"       :{name:"Chromium ore (chromite)",density:4790,band:'ore'},
 "pyrolusite"     :{name:"Manganese ore (pyrolusite)",density:5060,band:'ore'},
 "apatite"        :{name:"Phosphate (apatite)",density:3190,band:'ore'},
 "graphite"       :{name:"Graphite",density:2250,band:'ore'},
 "sulfur"         :{name:"Native sulfur",density:2070,band:'ore'},
 "spodumene"      :{name:"Lithium ore (spodumene)",density:3150,band:'ore'},
 "silver"         :{name:"Silver ore (acanthite)",density:7300,band:'scarce'},
 "cobaltite"      :{name:"Cobalt ore (cobaltite)",density:6300,band:'scarce'},
 "cassiterite"    :{name:"Tin ore (cassiterite)",density:6990,band:'scarce'},
 "wolframite"     :{name:"Tungsten ore (wolframite)",density:7300,band:'scarce'},
 "molybdenite"    :{name:"Molybdenum ore (molybdenite)",density:4730,band:'scarce'},
 "monazite"       :{name:"Rare-earth ore (monazite)",density:5150,band:'scarce'},
 "uraninite"      :{name:"Uranium ore (uraninite)",density:10950,band:'scarce'},
 "gold"           :{name:"Native gold",density:19300,band:'scarce'},
 "diamond"        :{name:"Industrial diamond",density:3510,band:'scarce'},
 "platinum"       :{name:"Native platinum",density:21450,band:'rare'},
 "palladium"      :{name:"Native palladium",density:12020,band:'rare'},
 "iridium"        :{name:"Native iridium",density:22560,band:'rare'},
 "shocked-quartz" :{name:"Shocked quartz",density:2650,band:'shock'},
 "impact-glass"   :{name:"Impact glass",density:2200,band:'shock'},
 "maskelynite"    :{name:"Maskelynite",density:2550,band:'shock'},
 "coesite"        :{name:"Coesite",density:2920,band:'shock'},
 "stishovite"     :{name:"Stishovite",density:4290,band:'shock-rare'},
 "ringwoodite"    :{name:"Ringwoodite",density:3900,band:'shock-rare'},
 "lonsdaleite"    :{name:"Lonsdaleite",density:3520,band:'lonsdaleite'},
 "brownleeite"    :{name:"Brownleeite",density:5820,band:'brownleeite'}};
// Rarity bands (roughly real abundance, kept simple), and each band's share of pieces per field type: common rock,
// metal and ice everywhere; the rare finds are scarce, and scarcest of all in the big easy fields (small and tiny
// fields hide them). The shock minerals are spread through all four rings alike.
const MIX={
 large: {common:.5515, plentiful:.25, ore:.14, scarce:.03, rare:.002, shock:.02,  'shock-rare':.006, lonsdaleite:.0005},
 medium:{common:.4815, plentiful:.24, ore:.18, scarce:.06, rare:.005, shock:.025, 'shock-rare':.008, lonsdaleite:.0005},
 small: {common:.402, plentiful:.22, ore:.22, scarce:.11, rare:.01,  shock:.028, 'shock-rare':.009, lonsdaleite:.001},
 tiny:  {common:.3624, plentiful:.22, ore:.22, scarce:.14, rare:.016, shock:.03,  'shock-rare':.01,  lonsdaleite:.0015, brownleeite:.0001}};   // brownleeite: tiny fields only (Eric 10-19)
const BAND_MATS={};for(const m in MATERIALS)(BAND_MATS[MATERIALS[m].band]=BAND_MATS[MATERIALS[m].band]||[]).push(m);
const ICO_VOL=2.536,ICO_HALF=0.851;          // IcosahedronGeometry(1): volume, and half-extent of its box per axis
const HOLD={name:'Starter hold',dims:[1.6,1.2,1.0]};   // interior, metres → 1.92 m³
HOLD.cap=HOLD.dims[0]*HOLD.dims[1]*HOLD.dims[2];HOLD.sorted=HOLD.dims.slice().sort((a,b)=>b-a);
const cargo=[];                                // pieces aboard
function cargoBulk(){return cargo.reduce((a,p)=>a+p.box,0);}
// WHAT EACH PIECE IS (security fix 10-19): the SERVER decides, from its session seed, the field id and the piece index
// (minerals.py: field_facts, piece_mineral). This is the same roll, only to SHOW the prediction; when signed in, what is
// recorded, alerted and stored is the server's answer, and the hold shows that.
function fnv1a(t){let h=0x811C9DC5;for(let i=0;i<t.length;i++){h=Math.imul(h^t.charCodeAt(i),0x01000193)>>>0;}return h>>>0;}
function fieldFacts(seed,id){const r=rng(fnv1a(seed+'|'+id+'|size'));let v=r(),size='tiny';
 for(const k in SIZES){if(v<SIZES[k].share){size=k;break;}v-=SIZES[k].share;}
 const S=SIZES[size];return [size,S.n[0]+Math.floor(r()*(S.n[1]-S.n[0]+1))];}
function pieceMineral(seed,id,i,size){const r=rng(fnv1a(seed+'|'+id+'|'+i));let u=r(),acc=0,band='common';
 for(const b in MIX[size]){acc+=MIX[size][b];if(u<acc){band=b;break;}}
 const ms=BAND_MATS[band];return ms[Math.floor(r()*ms.length)];}   // a band, then one of its minerals alike
function makePiece(mat,sx,sy,sz){const dims=[sx,sy,sz].map(v=>2*ICO_HALF*v).sort((a,b)=>b-a);
 const vol=ICO_VOL*sx*sy*sz;return{mat,dims,vol,box:dims[0]*dims[1]*dims[2],mass:vol*MATERIALS[mat].density,taken:false};}
function shapeFits(p){return p.dims.every((d,i)=>d<=HOLD.sorted[i]);}
function roomFor(p){return cargoBulk()+p.box<=HOLD.cap+1e-9;}
function fmtKg(kg){return kg>=1000?(kg/1000).toFixed(kg>=10000?1:2)+' t':Math.round(kg)+' kg';}

let collecting=null;                           // {field, piece index, t, dur, from:Vector3}
const collectBtn=document.getElementById('collect'),holdEl=document.getElementById('holdbtn');
function nextPiece(f){let best=-1,bd=1e9;for(let i=0;i<f.pieces.length;i++){const p=f.pieces[i];if(p.taken||!shapeFits(p)||!roomFor(p))continue;
  f.mats[i].decompose(tmpP,tmpQ,tmpS);tmpP.add(f.center);const d=tmpP.distanceTo(cam.position);if(d<bd){bd=d;best=i;}}return best;}
function startCollect(){const f=lock&&lock.parked&&lock.field;if(!f)return;
 const left=f.pieces.filter(p=>!p.taken);
 if(!left.some(shapeFits)){VOICE.say('toobig');toast('TOO BIG TO TAKE','These pieces won\'t fit in your hold. Keep searching for a field of smaller debris.');return;}
 const i=nextPiece(f);if(i<0){VOICE.say('full');toast('HOLD FULL','No room left for these pieces. Return to the Starship to unload.');return;}
 const p=f.pieces[i];f.mats[i].decompose(tmpP,tmpQ,tmpS);
 collecting={f,i,t:0,dur:2+Math.min(10,p.box*12),from:tmpP.clone(),q:tmpQ.clone(),s:tmpS.clone()};}
function collectTick(dt){
 const f=lock&&lock.parked&&lock.field;
 collectBtn.hidden=!f||!!collecting;
 document.getElementById('cwrap').hidden=!collecting;
 if(!collecting)return;
 if(!f||f!==collecting.f){   // flew off (or lost the lock): stop, and put the half-drawn piece back where it was
 collecting.f.mesh.setMatrixAt(collecting.i,collecting.f.mats[collecting.i]);collecting.f.mesh.instanceMatrix.needsUpdate=true;collecting=null;return;}
 const c=collecting;c.t+=dt;const k=Math.min(1,c.t/c.dur),e=k*k*(3-2*k);
 // the piece drifts in toward the ship (field-local space), shrinking as it comes aboard
 const shipLocal=tgtV.copy(cam.position).sub(f.center);
 tmpP.copy(c.from).lerp(shipLocal,e);tmpS.copy(c.s).multiplyScalar(1-0.8*e);
 f.mesh.setMatrixAt(c.i,new THREE.Matrix4().compose(tmpP,c.q,tmpS));f.mesh.instanceMatrix.needsUpdate=true;
 document.getElementById('cbar').style.width=(k*100).toFixed(0)+'%';
 if(k<1)return;
 const p=f.pieces[c.i];p.taken=true;cargo.push(p);if(NET.on)netCollect(p);f.mesh.setMatrixAt(c.i,ZERO);f.mesh.instanceMatrix.needsUpdate=true;
 if(!voiced.piece){voiced.piece=1;VOICE.say('firstpiece');if(NET.on)VOICE.story('piece');}
 snd.ping(520);toast('+ '+fmtKg(p.mass)+' '+MATERIALS[p.mat].name.toUpperCase(),
  p.dims.map(d=>d.toFixed(2)).join(' × ')+' m · takes '+p.box.toFixed(3)+' m³ of hold space');
 collecting=null;renderHold();
 if(f.pieces.every(q=>q.taken)){lock=null;f.cleared=true;VOICE.say('cleared');toast('FIELD CLEARED','Nothing left here. There\'s more debris all through the ring.');return;}
 startCollect();}                            // keep going until full or nothing else fits
function renderHold(){const used=cargoBulk();holdEl.textContent='HOLD '+used.toFixed(2)+' / '+HOLD.cap.toFixed(2)+' m³';
 const rows={};cargo.forEach(p=>{const k=p.flawless?'flawless':p.mat;const r=rows[k]||(rows[k]={n:0,kg:0,box:0});r.n++;r.kg+=p.mass;r.box+=p.box;});
 const tb=document.getElementById('manifest');tb.textContent='';
 [...Object.keys(MATERIALS),'flawless'].forEach(m=>{if(!rows[m])return;const tr=document.createElement('tr');   // the near-flawless diamond is never mixed in (rule 26)
  [m==='flawless'?'💎 Near-flawless diamond':MATERIALS[m].name,rows[m].n,fmtKg(rows[m].kg),rows[m].box.toFixed(3)+' m³'].forEach(v=>{const td=document.createElement('td');td.textContent=v;tr.appendChild(td);});tb.appendChild(tr);});
 document.getElementById('holdempty').hidden=cargo.length>0;
 document.getElementById('holdspec').textContent=HOLD.name+': '+HOLD.dims.map(d=>d.toFixed(1)).join(' × ')+' m inside ('+HOLD.cap.toFixed(2)+' m³). Used '+used.toFixed(2)+' m³ · '+fmtKg(cargo.reduce((a,p)=>a+p.mass,0))+' aboard.';
 const sb=document.getElementById('storemanifest');sb.textContent='';let any=false;
 Object.keys(MATERIALS).forEach(m=>{const kg=STORE.kg[m];if(!kg)return;any=true;const tr=document.createElement('tr');
  [MATERIALS[m].name,fmtKg(kg),(kg/MATERIALS[m].density).toFixed(3)+' m³'].forEach(v=>{const td=document.createElement('td');td.textContent=v;tr.appendChild(td);});sb.appendChild(tr);});
 document.getElementById('storeempty').hidden=any;

 renderShipHold('sAllF',(u,left)=>{document.getElementById('sAllU').textContent=fmtM3(u)+' used ('+(100*u/SHIP_HOLD.cap).toFixed(1)+'%)';
  document.getElementById('sAllA').textContent=fmtM3(left)+' available';},'sAllN');
 document.getElementById('storespec').textContent='Your allotment in the Starship\'s cargo hold: '+STORE.cap.toFixed(2)+' m³. Used '+storeUsed().toFixed(3)+' m³.';}


// ── UNLOADING AT THE STARSHIP (Eric 10-11): docked, tap UNLOAD. Pieces move one at a time, oldest first, from the ship's
//    hold into the player's own space in the Starship's cargo hold, while two bars show the hold draining and that space
//    filling; then TRANSFER COMPLETE with what moved. Same rules as the server's unload (dfg/store.py): each piece becomes
//    its material's mass, stored by its material volume (mass ÷ density); when the space is full the rest stays aboard.
//    Nothing is unlimited: the space is SAMPLE 12 m³ (dfg settings cargo_m3_start). Prototype only: kept in this browser,
//    not yet on the game server, so the market can't see it.
const STORE={cap:12,kg:{}};
// The whole Starship cargo hold (Eric 10-11: show how full it is and what's left). ~34,000 m³ is the spec's estimate
// (about a fifth of the hull's ~170,000 m³; an assumption, §7a). Everyone shares it. Until the game server is online
// there are no other crews, so their cargo is a SAMPLE figure, labelled as such on screen.
const SHIP_HOLD={cap:34000,othersSample:21480};
function shipHoldUsed(){return SHIP_HOLD.othersSample+storeUsed();}
function fmtM3(v){return Math.round(v).toLocaleString('en-US')+' m³';}
function renderShipHold(fill,txt,note){const u=shipHoldUsed(),left=SHIP_HOLD.cap-u;
 document.getElementById(fill).style.width=(100*u/SHIP_HOLD.cap).toFixed(1)+'%';
 txt(u,left);document.getElementById(note).textContent='Total about '+fmtM3(SHIP_HOLD.cap)+' (an estimate from the ship\'s design). Other crews\' cargo is sample data until the game server is online.';}
try{const s=JSON.parse(localStorage.getItem('stardust.storage')||'null');if(s&&s.kg)STORE.kg=s.kg;}catch(e){}
function storeSave(){try{localStorage.setItem('stardust.storage',JSON.stringify({kg:STORE.kg}));}catch(e){}}
// Receipts (Eric 10-11): what you own is in the Starship's hands, so every unload gives you a receipt with a code.
// On the game server the code is issued and checkable there (stardust-server, /api/dfg/receipt/{code}). Here, before
// the game is connected, the code is made in the browser and is labelled as a prototype that can't be checked.
const RCPT_CHARS='23456789ABCDEFGHJKMNPQRSTVWXYZ';
let RECEIPTS=[];try{RECEIPTS=JSON.parse(localStorage.getItem('stardust.receipts')||'[]')||[];}catch(e){}
function receiptCode(){const a=new Uint32Array(8);crypto.getRandomValues(a);let c='';for(const v of a)c+=RCPT_CHARS[v%RCPT_CHARS.length];
 return 'WSC-'+c.slice(0,4)+'-'+c.slice(4);}
function saveReceipts(){try{localStorage.setItem('stardust.receipts',JSON.stringify(RECEIPTS.slice(0,200)));}catch(e){}}
// Saving a receipt to the player's device (Eric 10-11: "Save, and let the player choose where"). In order:
//  1. inside a claude.ai preview, the viewer's own save (it asks the player to confirm; the browser decides the folder);
//  2. browsers that can ask where to save (desktop Chrome/Edge): the system "Save as" window, so the player picks it;
//  3. everywhere else, a normal download (phones offer their share/save sheet).
let dlNS=null;try{if(window.claude&&typeof window.claude.use==='function')window.claude.use('downloads').then(n=>{dlNS=n;}).catch(()=>{});}catch(e){}
function receiptText(rc){const L=['WORLD SPACE CONSORTIUM','WSC Alexander von Humboldt · Cargo office','','RECEIPT '+rc.code,
  'Issued: '+new Date(rc.at).toString(),'Transfer: '+rc.pieces+(rc.pieces===1?' piece':' pieces')+" from your ship's hold to your space in the Starship's cargo hold"];
 if(rc.left)L.push('Left aboard your ship: '+rc.left+(rc.left===1?' piece':' pieces'));
 L.push('','Material                 Weight');
 Object.keys(rc.kg).forEach(m=>L.push(((MATERIALS[m]?MATERIALS[m].name:m)+'                         ').slice(0,25)+fmtKg(rc.kg[m])));
 L.push('','Your space after: '+rc.used.toFixed(3)+' of '+rc.total.toFixed(2)+' m³ used','',
  ...(rc.server?['Issued by the game server. Anyone can check this code at:',location.origin+'/api/dfg/receipt/'+rc.code,'']
   :['PROTOTYPE RECEIPT: made in the flight test, so this code cannot be checked yet. Once the game is connected to its',
     'server, the server issues each code and anyone can check it.','']));return L.join('\n');}
async function saveReceipt(rc){const name='stardust-receipt-'+rc.code+'.txt',text=receiptText(rc);
 try{
  if(dlNS){await dlNS.save({filename:name,data:text});return true;}
  if(window.showSaveFilePicker){const fh=await window.showSaveFilePicker({suggestedName:name,types:[{description:'Receipt',accept:{'text/plain':['.txt']}}]});
   const w=await fh.createWritable();await w.write(text);await w.close();return true;}
  const url=URL.createObjectURL(new Blob([text],{type:'text/plain'}));const a=document.createElement('a');a.href=url;a.download=name;
  document.body.appendChild(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),4000);return true;
 }catch(e){if(e&&(e.name==='AbortError'||e.code==='declined'))return false;   // the player cancelled: nothing to report
  toast('COULDN\'T SAVE','Your receipt is still in the receipts log in your quarters. Try again from there.');return false;}}
function fmtWhen(t){return new Date(t).toLocaleString([], {dateStyle:'medium',timeStyle:'short'});}
function storeUsed(){let v=0;for(const m in STORE.kg)v+=STORE.kg[m]/MATERIALS[m].density;return v;}
const unloadBtn=document.getElementById('unload'),xferEl=document.getElementById('xfer');
let xfer=null;                                 // {t, per, moved:{mat:kg}, n, full}
function startUnload(){if(!docked||!cargo.length||xfer)return;
 xfer={t:0,per:Math.max(0.6,Math.min(1.6,3.5/cargo.length)),moved:{},n:0,full:false,start:cargo.length};   // a few seconds in all
 document.getElementById('xTitle').textContent='TRANSFERRING TO THE STARSHIP';document.getElementById('xTitle').className='';
 document.getElementById('xSumB').textContent='';document.getElementById('xDone').hidden=true;xferEl.hidden=false;
 if(NET.on){   // signed in: the cargo office (the server) does the transfer and issues the receipt; the bars then show it
  const x=xfer;x.wait=true;document.getElementById('xNow').textContent='Contacting the cargo office…';renderXfer();
  netUnload().then(r=>{if(xfer!==x){netRefresh();return;}x.server=r;x.wait=false;
    if(!r.unloaded_pieces){x.full=r.storage_full;finishXfer(false);return;}xferNow(cargo[0]);})
   .catch(e=>{if(xfer!==x)return;x.wait=false;x.error=e.message;finishXfer(false);});
  return;}
 xferNow(cargo[0]);renderXfer();}
function xferMove(){const p=cargo.shift();
 if(p.flawless)xfer.gems=(xfer.gems||0)+1;   // kept apart: to the lockbox, not the cargo-hold storage
 else{STORE.kg[p.mat]=(STORE.kg[p.mat]||0)+p.mass;xfer.moved[p.mat]=(xfer.moved[p.mat]||0)+p.mass;}xfer.n++;
 storeSave();renderHold();return p;}
function xferNow(p){document.getElementById('xNow').textContent=p?'Moving '+fmtKg(p.mass)+' of '+MATERIALS[p.mat].name.toLowerCase()+'…':'';}
function renderXfer(sub){const used=Math.max(0,cargoBulk()-(sub||0)),su=storeUsed();
 document.getElementById('xHoldT').textContent=used.toFixed(2)+' / '+HOLD.cap.toFixed(2)+' m³';
 document.getElementById('xHoldF').style.width=(100*used/HOLD.cap).toFixed(1)+'%';
 document.getElementById('xShipT').textContent=su.toFixed(3)+' / '+STORE.cap.toFixed(2)+' m³';
 document.getElementById('xShipF').style.width=Math.max(su>0?1.5:0,100*su/STORE.cap).toFixed(1)+'%';
 renderShipHold('xAllF',(u,left)=>{document.getElementById('xAllT').textContent=(100*u/SHIP_HOLD.cap).toFixed(1)+'% full · '+fmtM3(left)+' free';},'xAllN');}
function unloadTick(dt){
 unloadBtn.hidden=!docked||!cargo.length||!!xfer;
 quartersBtn.hidden=!docked||!!xfer;if(!docked&&!quartersEl.hidden)quartersEl.hidden=true;   // quarters are aboard: launching leaves them
 if(!xfer)return;
 if(!docked){                                                   // launching leaves a clean view (Eric 10-11)
  if(!xfer.done&&xfer.server){   // the cargo office already moved them: finish at once
   while(xfer.n<xfer.server.unloaded_pieces&&cargo.length)xferMove();xfer.full=xfer.server.left_aboard>0;finishXfer(false);
   toast('TRANSFER COMPLETE',xfer.n+(xfer.n===1?' piece':' pieces')+' moved to the Starship. Your receipt is in your quarters.');}
  else if(!xfer.done&&!xfer.wait){finishXfer(true);const x=xfer;toast('TRANSFER STOPPED',x.n+' of '+x.start+' pieces moved before you launched; the rest are still in your hold.'+(x.n?' Your receipt is in your quarters.':''));}
  closeXfer();return;}
 if(xfer.done||xfer.wait)return;
 xfer.t+=dt;const p=cargo[0];
 renderXfer(p?p.box*Math.min(1,xfer.t/xfer.per):0);             // the piece leaving drains the hold smoothly
 if(xfer.t<xfer.per)return;
 xfer.t=0;
 if(xfer.server){if(xfer.n>=xfer.server.unloaded_pieces){xfer.full=xfer.server.left_aboard>0;finishXfer(false);return;}}
 else if(storeUsed()+p.mass/MATERIALS[p.mat].density>STORE.cap+1e-9){xfer.full=true;finishXfer(false);return;}
 xferMove();snd.ping(440);
 if(!cargo.length||(xfer.server&&xfer.n>=xfer.server.unloaded_pieces)){xfer.full=!!(xfer.server&&xfer.server.left_aboard>0);finishXfer(false);return;}
 xferNow(cargo[0]);}
function finishXfer(stopped){const x=xfer;x.done=true;renderXfer();xferNow(null);
 const t=document.getElementById('xTitle'),now=document.getElementById('xNow');
 if(x.error){t.textContent='TRANSFER NOT MADE';now.textContent=x.error+' Your cargo is still in your hold.';}
 else if(stopped){t.textContent='TRANSFER STOPPED';now.textContent='You launched. '+x.n+' of '+x.start+' pieces moved; the rest are still in your hold.';}
 else if(x.full){t.textContent='STARSHIP SPACE FULL';now.textContent=x.n+' of '+x.start+' pieces moved. Your space aboard is full, so '+cargo.length+(cargo.length===1?' piece stays':' pieces stay')+' in your hold.';}
 else{t.textContent='TRANSFER COMPLETE';t.className='done';VOICE.say('unloaded');if(x.server)VOICE.story('unload');now.textContent='All '+x.n+(x.n===1?' piece is':' pieces are')+' aboard the Starship. Your hold is empty.';snd.chime();}
 const tb=document.getElementById('xSumB');tb.textContent='';
 Object.keys(MATERIALS).forEach(m=>{if(!x.moved[m])return;const tr=document.createElement('tr');
  [MATERIALS[m].name,'+ '+fmtKg(x.moved[m])].forEach(v=>{const td=document.createElement('td');td.textContent=v;tr.appendChild(td);});tb.appendChild(tr);});
 if(x.gems){const tr=document.createElement('tr');['💎 Near-flawless diamond','+ '+x.gems+' to your lockbox'].forEach(v=>{const td=document.createElement('td');td.textContent=v;tr.appendChild(td);});tb.appendChild(tr);}
 const rb=document.getElementById('xRcpt');rb.hidden=!x.n;
 if(x.server)netApplyInventory(x.server.inventory);   // the server's figures are the truth
 const sr=x.server&&x.server.receipt;
 if(x.n){const rc=sr?{code:sr.code,at:Date.parse(sr.issued_at),pieces:sr.pieces,left:sr.left_aboard,kg:sr.kg,used:sr.space_used_m3,total:sr.space_total_m3,server:true}
  :{code:receiptCode(),at:Date.now(),pieces:x.n,left:cargo.length,kg:x.moved,used:storeUsed(),total:STORE.cap};
  RECEIPTS.unshift(rc);saveReceipts();x.receipt=rc;
  if(rc.server)document.getElementById('xRProto').textContent='Issued by the Starship\'s cargo office (the game server). Anyone can check this code. A copy is in your quarters, in the filing cabinet.';
  document.getElementById('xRCode').textContent=rc.code;document.getElementById('xRAt').textContent=fmtWhen(rc.at);
  document.getElementById('xRBody').textContent=rc.pieces+(rc.pieces===1?' piece':' pieces')+' from your ship\'s hold to your space in the Starship\'s cargo hold'+
   (rc.left?' ('+rc.left+' left aboard)':'')+'. Your space after: '+rc.used.toFixed(3)+' of '+rc.total.toFixed(2)+' m³ used.';}
 const done=document.getElementById('xDone');done.hidden=false;done.textContent=x.n?'SAVE RECEIPT':'DONE';
 document.getElementById('xClose').hidden=!x.n;if(stopped&&!x.n)setTimeout(closeXfer,4000);}
// ── THE GAME SERVER (step 2, Eric 10-11): signed in, the server is the judge of what you own. It checks every piece
//    you collect (real density, the shape fits, room left, collecting takes time), keeps what's in your hold between
//    sessions, does each unload and issues the receipt anyone can check. Without a sign-in (the private preview), the
//    flight keeps everything in this browser as before.
const NET={api:window.STARDUST_API||null,token:null,session:null,on:false,last:0,queue:Promise.resolve()};
async function netCall(path,body){
 const r=await fetch(NET.api+path,{method:body?'POST':'GET',headers:{'Content-Type':'application/json','Authorization':'Bearer '+NET.token},
   body:body?JSON.stringify(body):undefined});
 const j=await r.json().catch(()=>({}));
 if(r.status===401){NET.on=false;toast('SIGNED OUT','Sign in again so what you collect is kept.');}
 if(!r.ok)throw new Error(j.error||'The Starship didn\'t answer. Try again in a moment.');
 return j;}
function netApplyShip(j){   // rebuild the hold and storage exactly as the server has them
 if(j.ship&&j.ship.hold_dims_m){HOLD.dims=j.ship.hold_dims_m.slice();HOLD.cap=HOLD.dims[0]*HOLD.dims[1]*HOLD.dims[2];HOLD.sorted=HOLD.dims.slice().sort((a,b)=>b-a);}
 if(j.pieces){cargo.length=0;j.pieces.forEach(p=>cargo.push({id:p.id,mat:p.material,dims:p.dims_m.slice().sort((a,b)=>b-a),vol:p.volume_m3,box:p.box_m3,mass:p.kg,taken:true,flawless:!!p.flawless}));}
 if(j.storage){STORE.cap=j.storage.capacity_m3;STORE.kg=Object.assign({},j.storage.kg);storeSave();}
 renderHold();}
function netApplyInventory(inv){const st=inv&&inv.places&&inv.places.find(p=>p.kind==='starship_cargo');if(!st)return;
 STORE.cap=st.capacity_m3;STORE.kg={};(st.goods||[]).forEach(g=>{if(g.kg!=null)STORE.kg[g.item]=g.kg+(g.kg_set_aside||0);});storeSave();renderHold();}
async function netStart(){
 try{NET.token=localStorage.getItem('stardust.token');}catch(e){NET.token=null;}
 if(!NET.api||!NET.token){NET.on=false;return false;}
 try{const j=await netCall('/session',{});NET.session=j.session_id;NET.on=true;
  // the universe now comes from the server's seed, so the server can tell what every piece is: lay it out afresh
  SEED=j.seed>>>0;collecting=null;lock=null;for(const key of [...cells.keys()])unloadCell(key);fieldMemory.clear();
  netApplyShip(j);netCall('/me').then(m=>{VOICE.set(m.voice_set);VOICE.rank(m.rank);}).catch(()=>{});return true;}
 catch(e){NET.on=false;return false;}}
function netRefresh(){if(NET.on)netCall('/ship').then(netApplyShip).catch(()=>{});}
// One collect at a time, in order, never closer together than the server allows (it refuses collects under 2 s apart).
function netCollect(p){
 NET.queue=NET.queue.then(async()=>{
  const wait=NET.last+2200-Date.now();if(wait>0)await new Promise(r=>setTimeout(r,wait));NET.last=Date.now();
  try{const j=await netCall('/collect',{session_id:NET.session,field:p.fid,index:p.idx,dims:p.dims,volume_m3:p.vol});
   if(j.aboard&&j.aboard.material&&j.aboard.material!==p.mat){p.mat=j.aboard.material;p.mass=j.aboard.kg;renderHold();}   // the server's word
   if(j.aboard&&j.aboard.flawless){p.flawless=true;renderHold();   // rule 26: keep the excitement with the miner
    snd.chime();setTimeout(()=>snd.chime(),350);VOICE.say('diamond');VOICE.story('diamond');
    toast('💎 NEAR-FLAWLESS DIAMOND','One in a hundred thousand. It stays apart from industrial diamond, and goes to your lockbox when you unload.');}
   else if(j.aboard&&j.aboard.noticed){snd.chime();   // lonsdaleite: noticed when collected (it is not the near-flawless diamond)
    if(p.mat==='brownleeite'){setTimeout(()=>snd.chime(),350);toast('✦ BROWNLEEITE','Manganese silicide, known from comet dust and never found naturally on Earth. Ultra rare. Read about it in the Starship Library.');}
    else toast('✦ LONSDALEITE','Hexagonal diamond: very rare. It is not ordinary diamond. Read about it in the Starship Library.');}}
  catch(e){const i=cargo.indexOf(p);if(i>=0)cargo.splice(i,1);renderHold();
   toast('NOT COLLECTED',e.message);}});}
async function netUnload(){await NET.queue;return netCall('/unload',{docked:true});}
window.addEventListener('stardust:signedin',()=>{netStart();});
window.addEventListener('stardust:signedout',()=>{NET.on=false;NET.token=null;NET.session=null;});

// PRIVATE QUARTERS (Eric 10-11): the receipts log is viewed in your own quarters while docked aboard the Starship.
const quartersBtn=document.getElementById('quartersbtn'),quartersEl=document.getElementById('quarters');
function renderQuarters(){
 const rl=document.getElementById('rcptlist');rl.textContent='';
 RECEIPTS.forEach(rc=>{const tr=document.createElement('tr');
  const kg=Object.keys(rc.kg).map(m=>MATERIALS[m].name+' '+fmtKg(rc.kg[m])).join(', ');
  const c1=document.createElement('td'),code=document.createElement('div');code.textContent=rc.code;code.style.fontFamily='ui-monospace,Menlo,monospace';
  const when=document.createElement('div');when.className='sub';when.textContent=fmtWhen(rc.at);c1.append(code,when);
  const c2=document.createElement('td');c2.textContent=rc.pieces+(rc.pieces===1?' piece: ':' pieces: ')+kg;tr.append(c1,c2);
  const td=document.createElement('td'),b=document.createElement('button');b.className='s';b.textContent='Save';
  b.addEventListener('click',async()=>{if(await saveReceipt(rc))toast('RECEIPT SAVED',rc.code+' is on your device.');});td.appendChild(b);tr.appendChild(td);rl.appendChild(tr);});
 document.getElementById('rcptempty').hidden=RECEIPTS.length>0;document.getElementById('rcptproto').hidden=!RECEIPTS.length;}
function openQuarters(){if(!docked)return;renderQuarters();quartersEl.hidden=false;}
quartersBtn.addEventListener('click',openQuarters);
document.getElementById('qclose').addEventListener('click',()=>{quartersEl.hidden=true;});
function closeXfer(){xferEl.hidden=true;xfer=null;}
document.getElementById('xDone').addEventListener('click',async()=>{const rc=xfer&&xfer.receipt;
 if(!rc){closeXfer();return;}
 if(await saveReceipt(rc)){closeXfer();toast('RECEIPT SAVED',rc.code+' is on your device, and in the receipts log in your quarters.');}});
document.getElementById('xClose').addEventListener('click',closeXfer);
unloadBtn.addEventListener('click',startUnload);

// ── DEBRIS: fields are laid out in 3 km cells around the pilot, only inside a ring's band. Each cell's fields come from
//    the session seed and the cell's coordinates, so a cell is the same if you fly away and come back. Rocks are stored
//    relative to their field's centre (small numbers for the GPU). What you've taken is remembered.
const rockGeo=new THREE.IcosahedronGeometry(1,0);
const rockMat=new THREE.MeshStandardMaterial({color:0xffffff,roughness:.95,metalness:.08,flatShading:true});
const ZERO=new THREE.Matrix4().makeScale(0,0,0);
const tmpM=new THREE.Matrix4(),tmpQ=new THREE.Quaternion(),tmpE=new THREE.Euler(),tmpS=new THREE.Vector3(),tmpP=new THREE.Vector3(),tmpC=new THREE.Color();
const ROCK_TONES=[0x8a817a,0x6f6a66,0x9c8f80,0x7a6a5c,0x5d5a58,0x8b7765];
const FIELDS=[];                          // fields in the cells around the pilot right now
const cells=new Map(),fieldMemory=new Map();
const dot=glowTex([[0,'rgba(255,255,255,1)'],[.5,'rgba(255,255,255,.6)'],[1,'rgba(255,255,255,0)']]);
const dustMat=new THREE.PointsMaterial({size:1.4,sizeAttenuation:false,map:dot,color:0x9a8f84,transparent:true,opacity:.6,depthWrite:false});
function ringOf(p){const rxy=Math.hypot(p.x,p.z);for(const rg of RINGS)if(Math.abs(rxy-rg.r)<BAND.half&&Math.abs(p.y)<BAND.thick)return rg;return null;}
function outside(p,rg){return Math.max(Math.abs(Math.hypot(p.x,p.z)-rg.r)-BAND.half,Math.abs(p.y)-BAND.thick,0);}   // metres outside a ring's band
function cellSeed(i,j,k){return (SEED^Math.imul(i|0,73856093)^Math.imul(j|0,19349663)^Math.imul(k|0,83492791))>>>0;}
function makeField(id,ring,center,size,n,r){
 const S=SIZES[size],rad=fieldRad(n,S.sc),mem=fieldMemory.get(id);
 const im=new THREE.InstancedMesh(rockGeo,rockMat,n);
 im.position.copy(center);im.frustumCulled=false;im.visible=false;
 const fld={id,ring,size,center,rad,sight:S.sight,mesh:im,count:n,mats:[],pieces:[],shown:false,known:!!(mem&&mem.known),cleared:!!(mem&&mem.cleared)};
 for(let i=0;i<n;i++){
  const d=Math.pow(r(),0.6)*rad;const v=new THREE.Vector3(r()-.5,(r()-.5)*0.6,r()-.5).normalize().multiplyScalar(d);
  tmpE.set(r()*6.3,r()*6.3,r()*6.3);tmpQ.setFromEuler(tmpE);
  const s=S.sc[0]*Math.pow(S.sc[1]/S.sc[0],Math.pow(r(),SIZE_BIAS));   // log-spread sizes, weighted toward small fragments
  tmpS.set(s*(0.7+r()*0.6),s*(0.7+r()*0.6),s*(0.7+r()*0.6));
  const m=new THREE.Matrix4().compose(v,tmpQ,tmpS);fld.mats.push(m);
  const p=makePiece(pieceMineral(SEED,id,i,size),tmpS.x,tmpS.y,tmpS.z);p.fid=id;p.idx=i;if(mem&&mem.taken[i])p.taken=true;fld.pieces.push(p);
  im.setMatrixAt(i,p.taken?ZERO:m);tmpC.setHex(ROCK_TONES[(r()*ROCK_TONES.length)|0]);im.setColorAt(i,tmpC);}
 scene.add(im);return fld;}
function loadCell(i,j,k){
 const key=i+','+j+','+k;if(cells.has(key))return;
 const cell={fields:[],dust:null};cells.set(key,cell);
 const o=new THREE.Vector3(i*CELL,j*CELL,k*CELL),mid=o.clone().addScalar(CELL/2);
 const ring=ringOf(mid);if(!ring)return;
 const r=rng(cellSeed(i,j,k));
 // beginners first (Eric 10-11): plenty of large, easy-to-hear fields of common material
 const u=r(),n=u<0.3?0:u<0.8?1:2;
 for(let f=0;f<n;f++){
  r();const [size,nPieces]=fieldFacts(SEED,key+'#'+f);           // size and piece count: the server's roll
  const S=SIZES[size],m=fieldRad(S.n[1],S.sc);                         // room for the biggest it could be
  const c=o.clone().add(new THREE.Vector3(m+r()*(CELL-2*m),m+r()*(CELL-2*m),m+r()*(CELL-2*m)));
  if(!ringOf(c)||cell.fields.some(g=>g.center.distanceTo(c)<g.rad+m+FIELD_GAP))continue;
  const fld=makeField(key+'#'+f,ring,c,size,nPieces,r);cell.fields.push(fld);FIELDS.push(fld);}
 // a thin haze of dust, so the band reads as a place even between fields (fogged like the rocks)
 const nd=140,P=new Float32Array(nd*3);for(let d=0;d<nd*3;d++)P[d]=r()*CELL;
 const g=new THREE.BufferGeometry();g.setAttribute('position',new THREE.BufferAttribute(P,3));
 cell.dust=new THREE.Points(g,dustMat);cell.dust.position.copy(o);scene.add(cell.dust);}
function unloadCell(key){const cell=cells.get(key);cells.delete(key);
 for(const f of cell.fields){fieldMemory.set(f.id,{taken:f.pieces.map(p=>p.taken),known:f.known,cleared:f.cleared});
  scene.remove(f.mesh);f.mesh.dispose();FIELDS.splice(FIELDS.indexOf(f),1);if(lock&&lock.field===f)lock=null;bearings.delete(f);}
 if(cell.dust){scene.remove(cell.dust);cell.dust.geometry.dispose();}}
function updateCells(){
 const ci=Math.floor(cam.position.x/CELL),cj=Math.floor(cam.position.y/CELL),ck=Math.floor(cam.position.z/CELL);
 for(const key of [...cells.keys()]){const [i,j,k]=key.split(',').map(Number);
  if(Math.abs(i-ci)>2||Math.abs(j-cj)>2||Math.abs(k-ck)>2)unloadCell(key);}
 for(let a=-1;a<=1;a++)for(let b=-1;b<=1;b++)for(let c=-1;c<=1;c++)loadCell(ci+a,cj+b,ck+c);}
function updateSight(){ // per-field visibility by its size class; fog then fades what is shown with distance
 for(const f of FIELDS){const show=!f.cleared&&cam.position.distanceTo(f.center)-f.rad<f.sight;if(show!==f.shown){f.shown=show;f.mesh.visible=show;}
  if(show)f.mesh.instanceMatrix.needsUpdate=true;}}

// ── FLIGHT (Eric 2026-10-10): the WHOLE SCREEN is a joystick, the same on a phone and with a mouse.
//  • Press and hold (finger, or left mouse button) anywhere: that point becomes the stick's centre; it steers.
//  • THROTTLE (Eric 10-17), right side: ▲/▼ step it 10% at a time, 0% (stopped) to 100%. Speed follows the throttle.
//    No automatic slow-down: the player throttles down by hand on approach. The autopilot still flies itself.
//  • SIDE THRUSTERS (Eric 10-17), bottom left: ◀/▶ pivot left/right in place, to line up on a target without drifting.
//  • Drag DOWN (pull back) = nose up · drag UP (push forward) = nose down · drag RIGHT/LEFT = bank right/left (roll + turn).
//  • Let go: turning and speed slowly drift to a stop.
//  • Double-tap: if the scanner has LOCKED a field, the autopilot flies you to it. Otherwise it locks the field or
//    landmark you can see nearest the tap and flies you there. Holding the stick again takes the controls back
//    (the lock stays; double-tap again to resume).
//  Keyboard still works on desktop: W/S or PageUp/PageDown throttle, ←/→ pivot, A/D R/F Q/E, Shift boost, Space brake.
const vel=new THREE.Vector3(),rot=new THREE.Vector3();   // rot = pitch, yaw, roll rates (rad/s) in the ship's own frame
const keys={};
const MAXV=60,BOOSTV=450,ACC=40,AUTOV=900;   // autopilot cruises fast on long trips and slows as it arrives (WARP crosses the system)
// Docked in the bay under the bow, looking out past the bow (Eric 10-11): the view you get when you dock, and the view
// you launch from, including at the very start of a session.
function settleDocked(){cam.position.copy(DOCK_W.mouth);vel.set(0,0,0);rot.set(0,0,0);docked=true;
 cam.up.copy(new THREE.Vector3(0,1,0).transformDirection(ship.matrixWorld));cam.lookAt(ship.localToWorld(new THREE.Vector3(0,-30,400)));}
let throttle=0;                           // 0..10 steps of 10%
const thrEl=document.getElementById('thrtxt');
function setThrottle(n){if(lock){if(lock.parked)lock=null;else lock.auto=false;}   // like the stick: touching the throttle takes the controls back
 throttle=Math.max(0,Math.min(10,n));thrEl.textContent='Throttle '+throttle*10+'%';}
addEventListener('keydown',e=>{keys[e.code]=true;if(e.code==='KeyH')toggleHelp();
 if(running&&(e.code==='KeyW'||e.code==='PageUp')){setThrottle(throttle+1);e.preventDefault();}
 if(running&&(e.code==='KeyS'||e.code==='PageDown')){setThrottle(throttle-1);e.preventDefault();}});
addEventListener('keyup',e=>{keys[e.code]=false;});

const STICK_R=90;                          // px of drag for full deflection
const stickRing=document.getElementById('stick'),knob=document.getElementById('knob');
let stk=null;                              // {id,x0,y0,x,y}
let lastTap={t:0,x:0,y:0};
cv.addEventListener('pointerdown',e=>{
 if(!running)return;
 const now=performance.now();
 if(now-lastTap.t<320&&Math.hypot(e.clientX-lastTap.x,e.clientY-lastTap.y)<40){lockAt(e.clientX,e.clientY);lastTap.t=0;return;}
 lastTap={t:now,x:e.clientX,y:e.clientY};
 if(stk)return;
 stk={id:e.pointerId,x0:e.clientX,y0:e.clientY,x:e.clientX,y:e.clientY};cv.setPointerCapture(e.pointerId);
 stickRing.style.left=(e.clientX-65)+'px';stickRing.style.top=(e.clientY-65)+'px';stickRing.hidden=false;knob.style.transform='';});
cv.addEventListener('pointermove',e=>{if(!stk||stk.id!==e.pointerId)return;stk.x=e.clientX;stk.y=e.clientY;
 let dx=stk.x-stk.x0,dy=stk.y-stk.y0;const l=Math.hypot(dx,dy);if(l>STICK_R){dx*=STICK_R/l;dy*=STICK_R/l;}
 knob.style.transform=`translate(${dx*39/STICK_R}px,${dy*39/STICK_R}px)`;});
function endStick(e){if(stk&&stk.id===e.pointerId){stk=null;stickRing.hidden=true;}}
cv.addEventListener('pointerup',endStick);cv.addEventListener('pointercancel',endStick);
cv.addEventListener('contextmenu',e=>e.preventDefault());
const hold={boost:false};
const pivot={l:false,r:false};
document.getElementById('thrUp').addEventListener('click',()=>setThrottle(throttle+1));
document.getElementById('thrDn').addEventListener('click',()=>setThrottle(throttle-1));
[['pivL','l'],['pivR','r']].forEach(([id,k])=>{const b=document.getElementById(id);   // held: keeps pivoting
 b.addEventListener('pointerdown',e=>{pivot[k]=true;b.setPointerCapture(e.pointerId);});
 ['pointerup','pointercancel'].forEach(t=>b.addEventListener(t,()=>pivot[k]=false));});
(function(){const b=document.getElementById('bBoost');
 b.addEventListener('pointerdown',e=>{hold.boost=true;b.setPointerCapture(e.pointerId);});
 ['pointerup','pointercancel'].forEach(t=>b.addEventListener(t,()=>hold.boost=false));})();
function stickXY(){if(!stk)return[0,0];let x=(stk.x-stk.x0)/STICK_R,y=(stk.y-stk.y0)/STICK_R;const l=Math.hypot(x,y);
 if(l>1){x/=l;y/=l;}const dz=0.08;const f=v=>Math.abs(v)<dz?0:Math.sign(v)*(Math.abs(v)-dz)/(1-dz);return[f(x),f(y)];}

// LOCK + AUTOPILOT
let lock=null,docked=false;                              // {name,pos:Vector3,stopAt,auto,field?}  auto = autopilot engaged
settleDocked();                                          // every session starts docked in the bay, ready to launch
const FAR_FLY=200000;                                    // beyond 200 km, flying would take too long: use WARP
const lockEl=document.getElementById('lock');
const rayV=new THREE.Vector3(),tgtV=new THREE.Vector3();
function lockAt(px,py){
 rayV.set(px/innerWidth*2-1,-(py/innerHeight)*2+1,0.5).unproject(cam).sub(cam.position).normalize();
 let best=null,bestAng=0.2;               // within ~11° of the tap
 const cands=FIELDS.filter(f=>f.shown).map(f=>({name:FIELD_LABEL(f),pos:f.center,stopAt:standOff(f),field:f}))
  .concat(LANDMARKS.map(l=>l.home?{name:'Starship',pos:DOCK_W.approach,aim:ship.position,stopAt:14,dock:1}:
   ({name:l.name,pos:l.pos,aim:l.draw.position,stopAt:l.rad*1.6,far:true})));
 // (c.aim: tap the ship itself; the autopilot heads for its approach point)
 for(const c of cands){tgtV.copy(c.aim||c.pos).sub(cam.position);const a=tgtV.angleTo(rayV);if(a<bestAng){bestAng=a;best=c;}}
 // Nothing visible under the tap: resume the current lock (e.g. a scanner lock you can't see yet), if there is one.
 if(!best){if(lock&&!lock.auto){lock.auto=true;stk=null;stickRing.hidden=true;return;}
  warn('Nothing to lock there. Double-tap a field or landmark you can see.');return;}
 if(cam.position.distanceTo(best.pos)>FAR_FLY){warn(best.name+' is too far to fly. Use WARP.');return;}
 if(lock&&lock.pos===best.pos){lock.auto=true;stk=null;stickRing.hidden=true;return;}   // tapped what's already locked: go
 lock=Object.assign({auto:true},best);stk=null;stickRing.hidden=true;if(best.dock)VOICE.say('home');}
// Where the autopilot parks: in front of the field, outside it, so the whole field stays in view while you work it.
function standOff(f){return f.rad*1.4+({tiny:5,small:6,medium:15,large:30})[f.size];}
function FIELD_LABEL(f){return {large:'Large field',medium:'Field',small:'Small field',tiny:'Tiny field'}[f.size];}

const fwd=new THREE.Vector3(),right=new THREE.Vector3(),up=new THREE.Vector3(),q=new THREE.Quaternion(),axis=new THREE.Vector3(),want=new THREE.Vector3();
function fly(dt){
 const [sx,sy]=stickXY();
 const holding=!!stk;
 if(holding&&lock){if(lock.parked)lock=null;else lock.auto=false;}   // leaving a field you parked at releases it; otherwise the lock stays
 if((holding||throttle)&&docked){docked=false;VOICE.say('launch');VOICE.story('launch');}   // taking the stick back stops the autopilot (the lock stays)
 fwd.set(0,0,-1).applyQuaternion(cam.quaternion);right.set(1,0,0).applyQuaternion(cam.quaternion);up.set(0,1,0).applyQuaternion(cam.quaternion);
 // target turn rates
 let tp=0,ty=0,tr=0;
 if(holding){tp=sy*1.1;tr=-sx*1.5;ty=-sx*0.55;}   // pull back (down) = nose up; right = roll right + turn right
 tp+=((keys.ArrowDown?1:0)-(keys.ArrowUp?1:0))*1.0;tr+=((keys.KeyQ?1:0)-(keys.KeyE?1:0))*1.4;
 ty+=((keys.ArrowLeft||pivot.l?1:0)-(keys.ArrowRight||pivot.r?1:0))*0.8;   // side thrusters: pivot in place
 if(lock&&(lock.auto||lock.parked)){         // autopilot (and parked): keep the nose on the target
  want.copy(lock.pos).sub(cam.position).normalize();
  const lx=want.dot(right),ly=want.dot(up);ty=-lx*2.2;tp=ly*2.2;tr=0;
 }
 if(lock&&lock.dock===1&&lock.auto&&cam.position.distanceTo(lock.pos)<lock.stopAt){lock.dock=2;lock.pos=DOCK_W.mouth;lock.stopAt=22;lock.name='Starship · docking';VOICE.say('approach');warn('Cleared to dock. Bring it in under the bow.');}
 else if(lock&&lock.dock===2&&cam.position.distanceTo(lock.pos)<lock.stopAt){lock=null;settleDocked();   // settle facing out past the bow, the view from the bay
  VOICE.say('docked');toast('DOCKED','Welcome home. Your Market terminal is at the Desk in your quarters.');}
 if(lock&&lock.auto&&!lock.dock&&cam.position.distanceTo(lock.pos)<lock.stopAt){lock.auto=false;lock.parked=true;if(lock.field)VOICE.say('parked');warn('Holding position: '+lock.name);if(lock.field)lock.field.known=true;}
 if(lock&&!lock.auto&&!lock.parked&&lock.field&&lock.field.known&&cam.position.distanceTo(lock.pos)>lock.stopAt*4)lock=null;   // flew away from a visited field
 const k=1-Math.exp(-(holding||(lock&&lock.auto)||tp||ty||tr?5:2.6)*dt);  // quick to respond; on release the turn eases out in about a second (speed drifts longer)
 rot.x+=(tp-rot.x)*k;rot.y+=(ty-rot.y)*k;rot.z+=(tr-rot.z)*k;
 q.setFromAxisAngle(axis.set(1,0,0),rot.x*dt);cam.quaternion.multiply(q);
 q.setFromAxisAngle(axis.set(0,1,0),rot.y*dt);cam.quaternion.multiply(q);
 q.setFromAxisAngle(axis.set(0,0,1),rot.z*dt);cam.quaternion.multiply(q);cam.quaternion.normalize();
 fwd.set(0,0,-1).applyQuaternion(cam.quaternion);
 // thrust: the throttle sets the speed (0% = stopped)
 const boost=keys.ShiftLeft||keys.ShiftRight||hold.boost;
 let tf=throttle&&!(lock&&lock.parked)?1:0;
 const ts=(keys.KeyD?1:0)-(keys.KeyA?1:0),tu=(keys.KeyR?1:0)-(keys.KeyF?1:0);
 let cap=(boost?BOOSTV:MAXV)*throttle/10+(ts||tu?MAXV*0.3:0);
 if(lock&&lock.auto){const dist=Math.max(0,cam.position.distanceTo(lock.pos)-lock.stopAt);const aligned=Math.max(0,want.dot(fwd));
  cap=Math.min(AUTOV,Math.max(6,dist*0.6))*aligned;tf=1;}
 if(vel.length()>cap)tf=0;   // throttled down: coast down to the new speed
 const a=ACC*(boost||(lock&&lock.auto)?3.2:1);
 vel.addScaledVector(fwd,tf*a*dt).addScaledVector(right,ts*a*0.6*dt).addScaledVector(up,tu*a*0.6*dt);
 const idle=!tf&&!ts&&!tu;
 vel.multiplyScalar(Math.exp(-(keys.Space||(lock&&lock.parked)?2.6:idle?(throttle?0.35:1.2):0.12)*dt));   // parked = station-keeping brake   // released: drifts to a stop over a few seconds
 if(vel.length()>cap)vel.setLength(Math.max(cap,vel.length()*Math.exp(-1.5*dt)));
 if(!(lock&&lock.auto)&&tf){const sp=vel.length();vel.lerp(want.copy(fwd).multiplyScalar(sp),1-Math.exp(-3*dt));}   // under power the ship flies where it points
 cam.position.addScaledVector(vel,dt);
 if(lock&&lock.parked){if(lock.last)cam.position.add(tgtV.copy(lock.pos).sub(lock.last));lock.last=(lock.last||new THREE.Vector3()).copy(lock.pos);}   // station-keeping: ride along as the field drifts
 if(cam.position.length()<SUN_R*30){cam.position.setLength(SUN_R*30);vel.multiplyScalar(0.2);if(lock)lock.auto=false;warn('Too close to the Sun. Hull temperature critical.');}
}
// Approach distance (Eric 10-17): big, faint numbers top centre, to whatever the scanner is tracking.
const apprEl=document.getElementById('appr');
function approachHud(){
 const p=docked?null:lock?(lock.aim||lock.pos):scanBest&&scanStrength>0.25?scanBest.center:null;
 apprEl.hidden=!p;if(p)apprEl.textContent=fmtDist(cam.position.distanceTo(p));}
function lockHud(){
 if(!lock){lockEl.hidden=true;return;}
 pv.copy(lock.aim||lock.pos).project(cam);const on=pv.z<1&&Math.abs(pv.x)<1&&Math.abs(pv.y)<1;
 lockEl.hidden=!on;if(!on)return;
 lockEl.style.left=((pv.x+1)/2*innerWidth)+'px';lockEl.style.top=((1-pv.y)/2*innerHeight)+'px';
 lockEl.lastChild.textContent=(lock.auto?'AUTOPILOT · ':lock.parked?'HOLDING · ':'LOCKED · ')+lock.name+' · '+fmtDist(cam.position.distanceTo(lock.pos));}

// ── SCANNER (spec §5). Sweeps a cone ahead of the ship. A field's return weakens with distance, is fainter for smaller
//    fields, and is strongest dead centre; random static rides on top, so faint returns flicker. One sweep gives a
//    DIRECTION only: take a bearing, move, take another from somewhere else; where they cross, the field is FIXED and
//    the scanner LOCKS it automatically and goes quiet (Eric 10-10). Close, strong fields fix from one bearing.
const SCAN={cone:30*Math.PI/180,range:{large:1800,medium:900,small:300,tiny:200},sig:{large:1,medium:0.7,small:0.4,tiny:0.3}};   // bigger fields are louder and heard farther
const scanEl=document.getElementById('scanbar'),scanTxt=document.getElementById('scantxt');
let scanStrength=0,scanBest=null,staticV=0;
const bearings=new Map();                  // field → where you were when you took its first bearing (kept per field,
                                           // so sweeping past a neighbour doesn't wipe the one you were working on)
const sv=new THREE.Vector3();
function scanReturn(f){
 if(f.known)return 0;
 sv.copy(f.center).sub(cam.position);const d=Math.max(0,sv.length()-f.rad),R=SCAN.range[f.size];if(d>R)return 0;
 const ang=sv.angleTo(fwd);if(ang>SCAN.cone)return 0;
 const aim=Math.pow((Math.cos(ang)-Math.cos(SCAN.cone))/(1-Math.cos(SCAN.cone)),2);
 return SCAN.sig[f.size]*Math.pow(1-d/R,1.4)*aim;}
// ── FIELD CUE (Eric 10-11): finding a first field was too hard. While the stick is held, a faint glow on its rim shows
//    which way the nearest uncleared field lies (as seen on screen), even out of sight and out of scanner range. When it
//    is dead ahead, the whole rim glows. Faint far off, brighter as you close in. It points; the scanner still finds it.
const cueEl=document.getElementById('cue'),cueQ=new THREE.Quaternion(),CUE_RANGE=4500,CUE_AHEAD=8*Math.PI/180;
function fieldCue(){
 let best=null,bd=CUE_RANGE;
 if(stk&&!docked&&!(lock&&(lock.field||lock.dock)))for(const f of FIELDS){if(f.cleared)continue;
  const d=Math.max(0,cam.position.distanceTo(f.center)-f.rad);if(d<bd){bd=d;best=f;}}
 if(!best){cueEl.style.opacity=0;return;}
 sv.copy(best.center).sub(cam.position).applyQuaternion(cueQ.copy(cam.quaternion).invert());   // into the camera's view
 const ahead=sv.z<0&&Math.atan2(Math.hypot(sv.x,sv.y),-sv.z)<CUE_AHEAD;
 cueEl.classList.toggle('ahead',ahead);
 if(!ahead)cueEl.style.transform='rotate('+Math.atan2(sv.x,sv.y)+'rad)';                       // 0 = top, clockwise
 cueEl.style.opacity=(0.25+0.5*(1-bd/CUE_RANGE)).toFixed(2);}
function scan(dt){
 fieldCue();
 fwd.set(0,0,-1).applyQuaternion(cam.quaternion);
 let best=null,bv=0;
 if(!(lock&&(lock.field||lock.dock))&&!docked) for(const f of FIELDS)   // quiet while docking or docked
{const r=scanReturn(f);if(r>bv){bv=r;best=f;}}
 staticV+=((Math.random()-.5)*0.9-staticV*1.5)*dt*6;               // wandering static
 const raw=Math.max(0,Math.min(1,bv+staticV*0.18*(1-bv)));
 scanStrength+=(raw-scanStrength)*(1-Math.exp(-9*dt));scanBest=best;
 // bearings → fix → lock
 if(best&&bv>0.28){if(!voiced.ret){voiced.ret=1;VOICE.say('ret');}                          // strong enough to take a bearing on
  sv.copy(best.center).sub(cam.position);const centred=sv.angleTo(fwd)<7*Math.PI/180,dist=sv.length();
  if(centred){
   if(dist<170&&bv>0.75){fixField(best);}
   else if(!bearings.has(best)){bearings.set(best,cam.position.clone());snd.ping(660);if(!voiced.bearing){voiced.bearing=1;VOICE.say('bearing');}
    toast('BEARING TAKEN','Move off to one side, then sweep this return again to fix its position.');}
   else{const from=bearings.get(best),moved=cam.position.distanceTo(from);
    const a1=sv.copy(best.center).sub(from).normalize();const a2=tgtV.copy(best.center).sub(cam.position).normalize();
    if(moved>Math.max(35,dist*0.12)&&a1.angleTo(a2)>2.5*Math.PI/180)fixField(best);}
  }}
 scanEl.style.width=(scanStrength*100).toFixed(0)+'%';
 scanTxt.textContent=docked?'DOCKED · throttle up to launch':lock&&lock.dock?'DOCKING · under the bow':lock&&lock.parked?'HOLDING POSITION · in front of the field':lock&&lock.auto?'AUTOPILOT · hold to take the controls':lock&&lock.field?'LOCKED · double-tap to fly there':scanBest&&bearings.has(scanBest)&&scanStrength>0.2?'BEARING 1 OF 2 · move and sweep again':scanStrength>0.25?'RETURN':'SWEEPING';
 snd.scanner(lock&&(lock.field||lock.dock)||docked?-1:scanStrength);
}
function fixField(f){bearings.delete(f);lock={name:FIELD_LABEL(f),pos:f.center,stopAt:standOff(f),auto:false,field:f};snd.chime();VOICE.say('locked');
 toast('FIELD LOCKED','Scanner quiet. Double-tap to fly there.');}

// ── SOUND (spec §5): a soft hiss while nothing is in the sweep; a calm tone rises out of it, higher and clearer as you
//    aim closer and get nearer; dead centre the static falls away. Silent once locked. Gentle sine/triangle, low volume.
const snd=(function(){let ac=null,master,hissG,toneG,o1,o2,muted=false;
 function init(){if(ac)return;try{ac=new (window.AudioContext||window.webkitAudioContext)();}catch(e){return;}
  master=ac.createGain();master.gain.value=0.55;master.connect(ac.destination);
  const n=ac.sampleRate*2,buf=ac.createBuffer(1,n,ac.sampleRate),d=buf.getChannelData(0);let b0=0,b1=0,b2=0;
  for(let i=0;i<n;i++){const w=Math.random()*2-1;b0=.99765*b0+w*.099;b1=.963*b1+w*.2965;b2=.57*b2+w*1.0526;d[i]=(b0+b1+b2+w*.1848)*.12;}
  const src=ac.createBufferSource();src.buffer=buf;src.loop=true;const bp=ac.createBiquadFilter();bp.type='bandpass';bp.frequency.value=1400;bp.Q.value=0.6;
  hissG=ac.createGain();hissG.gain.value=0;src.connect(bp);bp.connect(hissG);hissG.connect(master);src.start();
  o1=ac.createOscillator();o1.type='sine';o2=ac.createOscillator();o2.type='triangle';const lp=ac.createBiquadFilter();lp.type='lowpass';lp.frequency.value=1600;
  const g2=ac.createGain();g2.gain.value=0.25;toneG=ac.createGain();toneG.gain.value=0;
  o1.connect(lp);o2.connect(g2);g2.connect(lp);lp.connect(toneG);toneG.connect(master);o1.start();o2.start();}
 function blip(f,dur,vol){if(!ac||muted)return;const t=ac.currentTime,o=ac.createOscillator(),g=ac.createGain();o.type='sine';o.frequency.value=f;
  g.gain.setValueAtTime(0.0001,t);g.gain.exponentialRampToValueAtTime(vol,t+0.01);g.gain.exponentialRampToValueAtTime(0.0001,t+dur);
  o.connect(g);g.connect(master);o.start(t);o.stop(t+dur+0.05);}
 return{
  resume(){init();if(ac&&ac.state==='suspended')ac.resume();},
  scanner(s){if(!ac)return;const t=ac.currentTime;
   if(s<0||muted){hissG.gain.setTargetAtTime(0,t,0.15);toneG.gain.setTargetAtTime(0,t,0.15);return;}
   hissG.gain.setTargetAtTime(0.05*(1-Math.min(1,s*1.25)),t,0.08);
   const f=200+620*s;o1.frequency.setTargetAtTime(f,t,0.05);o2.frequency.setTargetAtTime(f*2,t,0.05);
   toneG.gain.setTargetAtTime(s<0.06?0:0.11*Math.pow(s,1.2),t,0.06);},
  ping(f){blip(f||660,0.25,0.12);},
  chime(){blip(660,0.35,0.12);setTimeout(()=>blip(990,0.5,0.1),140);},
  warp(){if(!ac||muted)return;const t=ac.currentTime,o=ac.createOscillator(),g=ac.createGain();o.type='sawtooth';   // a rising hum as the drive spools
   o.frequency.setValueAtTime(70,t);o.frequency.exponentialRampToValueAtTime(420,t+1.4);o.frequency.exponentialRampToValueAtTime(90,t+5);
   const lp=ac.createBiquadFilter();lp.type='lowpass';lp.frequency.value=900;
   g.gain.setValueAtTime(0.0001,t);g.gain.exponentialRampToValueAtTime(0.07,t+1.2);g.gain.exponentialRampToValueAtTime(0.0001,t+5);
   o.connect(lp);lp.connect(g);g.connect(master);o.start(t);o.stop(t+5.1);},
  toggle(){muted=!muted;return muted;},get muted(){return muted;}};})();
let toastT=0;
function toast(k,w){const el=document.getElementById('toast');el.firstChild.textContent=k;el.lastChild.textContent=w;el.hidden=false;toastT=performance.now()+3200;}


// ── HUD + off-screen markers
const $=id=>document.getElementById(id);let warnT=0;
function warn(t){$('warn').textContent=t;$('warn').style.opacity=1;warnT=performance.now()+1800;}
function fmtDist(m){if(m<1000)return Math.round(m)+' m';if(m<1e6)return (m/1000).toFixed(m<1e5?1:0)+' km';
 if(m<0.05*AU)return Math.round(m/1000).toLocaleString('en-US')+' km';return (m/AU).toFixed(2)+' AU';}
const marksEl=$('marks');const MK=LANDMARKS.map(l=>{const d=document.createElement('div');d.className='mk';
 d.style.color=l.home?'#7fb0ff':l.name==='Wormhole'?'#b49cff':'#d9a441';d.innerHTML='<i></i><span></span>';marksEl.appendChild(d);return d;});
const pv=new THREE.Vector3();
function hud(){
 $('spd').textContent=vel.length().toFixed(1)+' m/s';
 $('dsun').textContent=(cam.position.length()/AU).toFixed(3)+' AU';
 $('dhome').textContent=fmtDist(cam.position.distanceTo(ship.position));
 const here=ringOf(cam.position);
 $('zone').textContent=warp?'WARP · '+warp.label:here?here.name:workRing?'Outside the '+workRing.name+' · '+fmtDist(outside(cam.position,workRing)):'';
 const placed=[];
 LANDMARKS.forEach((l,i)=>{const el=MK[i];pv.copy(l.home?ship.position:l.draw.position).project(cam);
  const behind=pv.z>1;let x=pv.x,y=pv.y;const on=!behind&&Math.abs(x)<0.95&&Math.abs(y)<0.92;
  if(!on){if(behind){x=-x;y=-y;}const m=Math.max(Math.abs(x)/0.92,Math.abs(y)/0.86,1e-6);x/=m;y/=m;}
  let px=(x+1)/2*innerWidth,py=(1-y)/2*innerHeight;
  for(let n=0;n<6&&placed.some(q=>Math.abs(q[0]-px)<70&&Math.abs(q[1]-py)<15);n++)py+=15;   // things in the same direction stack instead of overlapping
  placed.push([px,py]);
  el.className='mk'+(on?'':' edge');el.style.left=px+'px';el.style.top=py+'px';
  el.lastChild.textContent=l.name+' · '+fmtDist(cam.position.distanceTo(l.home?ship.position:l.pos));});
 if(warnT&&performance.now()>warnT){$('warn').style.opacity=0;warnT=0;}
}

// ── INARA keeps an eye on you (Eric 10-11): she tells you when you drift out of the ring you're working.
let workRing=null,inaraT=0;
function inara(text){toast('INARA',text);}
// ── INARA'S VOICE (Eric 10-20): her RECORDED lines, never live speech (rules 14, 15: no live ElevenLabs, ever).
//    Files come from the game server's volume at /voice/<set>/<ID>.mp3, in the voice set for the player's language
//    (voice_set from /api/dfg/me). A moment has several takes: one is picked at random, never the same as last time.
//    One line at a time: a moment that comes while she's talking is skipped; story beats wait their turn. The sound
//    toggle silences her too, and a missing file is simply not heard. Moments and IDs: docs/inara-tower-dialog.md, Part C.
const VOICE=(function(){
 const T=n=>'INARA-TWR-'+String(n).padStart(3,'0'),TW=(a,b)=>{const o=[];for(let n=a;n<=b;n++)o.push(T(n));return o;};
 const MOMENTS={bay:TW(1,3),launch:['INARA-TOWER-001'].concat(TW(4,6)),
  ring0:['INARA-RING-001',T(7)],ring1:['INARA-RING-002',T(8)],ring2:['INARA-RING-003',T(9)],ring3:['INARA-RING-004',T(10)],
  warp0:['INARA-RING-005'],warp1:['INARA-RING-006'],warp2:['INARA-RING-007'],warp3:['INARA-RING-008'],
  drift0:['INARA-RING-013'],drift1:['INARA-RING-014'],drift2:['INARA-RING-015'],drift3:['INARA-RING-016'],
  ret:['INARA-TOWER-002',T(11),T(12)],bearing:TW(13,14),locked:['INARA-TOWER-003'].concat(TW(15,17)),parked:TW(18,20),
  toobig:['INARA-TOWER-004',T(21)],firstpiece:TW(22,23),cleared:TW(24,25),diamond:TW(26,27),full:['INARA-TOWER-005'].concat(TW(28,29)),
  home:TW(30,31),arrived:[T(32)],approach:['INARA-TOWER-006'],docked:['INARA-TOWER-007'].concat(TW(33,34)),unloaded:[T(35)],
  // TWR-036 and 039 are SOURCE lines whose voice use Eric has not approved yet: left out of the takes
  low65:TW(37,38),low50:TW(40,41),wake:TW(42,43),sleep:TW(44,45),pass:[T(49)],fail:[T(50)],order:[T(51)],submitted:[T(53)]};
 const S=n=>'INARA-STORY-'+String(n).padStart(3,'0');
 const BEATS={welcome:['INARA-WELCOME-001','INARA-WELCOME-002',S(1),S(2),'INARA-WELCOME-003'],library:[S(3),S(4)],test:[S(5),S(6)],
  blueprint:[S(7)],launch:[S(8),S(9)],ring:[S(10),S(11)],piece:[S(12)],unload:[S(13)],diamond:[S(16)]};
 const base=(window.STARDUST_API||'').replace(/\/api\/dfg\/?$/,'');
 let set=null,cur=null,queue=[];const last={};
 function pick(m){const ids=MOMENTS[m];if(!ids)return null;const c=ids.length>1?ids.filter(i=>i!==last[m]):ids;
  const id=c[Math.floor(Math.random()*c.length)];last[m]=id;return id;}
 // Shipboard call chime (Eric 10-20): our own three-note rising bell, made here in the browser, so no one else's sound
 // is used. It plays once before Inara speaks aboard the ship; flight lines come over the radio and get no chime.
 let ac=null,chimed=false;
 function chime(){try{ac=ac||new (window.AudioContext||window.webkitAudioContext)();}catch(e){return 0;}
  const t=ac.currentTime+0.02;[[659.25,0],[987.77,0.14],[1318.5,0.28]].forEach(([f,d])=>{
   const o=ac.createOscillator(),g=ac.createGain();o.type='sine';o.frequency.value=f;
   g.gain.setValueAtTime(0,t+d);g.gain.linearRampToValueAtTime(0.18,t+d+0.01);g.gain.exponentialRampToValueAtTime(0.0005,t+d+0.6);
   o.connect(g).connect(ac.destination);o.start(t+d);o.stop(t+d+0.65);});return 800;}
 const ABOARD=['042','043','044','045','049','050','051','053'].map(n=>'INARA-TWR-'+n);   // Tower lines heard aboard: chime, no radio
 const aboard=id=>ABOARD.includes(id)||!/^INARA-(TWR|RING|TOWER)-/.test(id);
 function next(){cur=null;if(!queue.length||snd.muted||!set){queue=[];chimed=false;if(after){const f=after;after=null;f();}return;}
  if(!chimed&&aboard(queue[0])){chimed=true;const w=chime();if(w){cur={pause(){}};const mark=cur;setTimeout(()=>{if(cur===mark)next();},w);return;}}
  const id=queue.shift(),a=new Audio(base+'/voice/'+encodeURIComponent(set)+'/'+id+'.mp3');a.volume=0.85;cur=a;
  a.onended=a.onerror=()=>{if(cur===a){if(!queue.length&&!after)chimed=false;next();}};
  const p=a.play();if(p&&p.catch)p.catch(()=>{if(cur===a)next();});}   // blocked or missing: carry on silently
 function ready(){return set&&!snd.muted;}
 // Polite openers (Eric 10-20): aboard the ship Inara never just starts talking. Chime, one opener ("Is this a good
 // moment?"; the Captain set only for a Captain), then Go ahead / Not now. Go ahead plays the beat and only then marks it
 // heard; Not now (or no answer in 20 s, silently) leaves it unheard, offered again at the next beat or in 10 minutes.
 // Flight radio lines (TWR, RING, TOWER) never get an opener.
 const C=n=>'INARA-CALL-'+String(n).padStart(3,'0');
 const OPEN=[1,2,3,4,5].map(C),OPEN_CPT=[6,7,8,9,10].map(C),LATER=[C(11),C(12)];
 let rank=null,after=null,asking=false,retryT=null;const later=new Set();
 const any=a=>a[Math.floor(Math.random()*a.length)];
 function tok(){try{return localStorage.getItem('stardust.token');}catch(e){return null;}}
 async function post(beat,accepted){const t=tok();if(!t||!window.STARDUST_API)return false;
  try{const r=await fetch(window.STARDUST_API+'/voice/heard',{method:'POST',headers:{'Content-Type':'application/json',Authorization:'Bearer '+t},
   body:JSON.stringify(accepted?{beat,accepted:true}:{beat})});return !!(await r.json()).play;}catch(e){return false;}}
 function ask(done){const b=document.createElement('div');
  b.style.cssText='position:fixed;left:50%;top:24%;transform:translateX(-50%);z-index:60;display:flex;gap:8px;align-items:center;padding:8px 12px;'+
   'border-radius:10px;background:rgba(8,14,24,.92);border:1px solid #2c4a66;color:#cfe3f5;font:13px system-ui,sans-serif';
  const lab=document.createElement('b');lab.textContent='INARA';lab.style.cssText='color:#7fe0a8;font-size:11px;letter-spacing:.1em';b.appendChild(lab);
  let over=false;const end=v=>{if(over)return;over=true;clearTimeout(t);b.remove();done(v);};
  [['Go ahead','yes'],['Not now','no']].forEach(([txt,v])=>{const x=document.createElement('button');x.textContent=txt;
   x.style.cssText='font:inherit;font-size:12px;padding:5px 10px;border-radius:8px;border:1px solid #2c4a66;cursor:pointer;'+
    (v==='yes'?'background:#1f6f4a;color:#fff':'background:transparent;color:#cfe3f5');x.addEventListener('click',e=>{e.stopPropagation();end(v);});b.appendChild(x);});
  const t=setTimeout(()=>end('quiet'),20000);document.body.appendChild(b);}
 function retryLater(){clearTimeout(retryT);retryT=setTimeout(()=>{retryT=null;offerNext();},10*60*1000);}
 function offerNext(){if(asking||!later.size||!ready())return;const beat=later.values().next().value;later.delete(beat);offer(beat);}
 async function offer(beat){if(asking){later.add(beat);return;}if(!ready())return;asking=true;
  if(!await post(beat,false)||!ready()){asking=false;offerNext();return;}
  after=()=>ask(async v=>{
   if(v==='yes'&&ready()&&await post(beat,true)){chimed=true;after=()=>{asking=false;chimed=false;offerNext();};queue.push(...BEATS[beat]);if(!cur)next();return;}
   if(v!=='yes')later.add(beat);
   if(v==='no'&&ready()){chimed=true;after=()=>{asking=false;chimed=false;retryLater();};queue.push(any(LATER));if(!cur)next();return;}
   asking=false;chimed=false;retryLater();});
  queue.push(any(rank==='Captain'?OPEN_CPT:OPEN));if(!cur)next();}   // waits for the line before it, then the chime
 return {
  set(s){set=s||null;},
  rank(r){rank=r||null;},
  say(m){if(!ready()||cur||queue.length||asking)return;const id=pick(m);if(id){queue.push(id);next();}},   // busy: skip
  story(beat){if(!BEATS[beat]||!ready()||!tok()||!window.STARDUST_API)return;later.delete(beat);
   if(asking){later.add(beat);return;}offer(beat);},
  stop(){queue=[];chimed=false;after=null;asking=false;if(cur){const a=cur;cur=null;try{a.pause();}catch(e){}}},
  get busy(){return !!cur;},MOMENTS,BEATS};})();
window.STARDUST_VOICE=VOICE;
const voiced={};   // this session's once-only moments (first strong return, first bearing, first piece)
function watchRing(now){
 if(warp)return;
 const here=ringOf(cam.position);
 if(here){if(here!==workRing){const first=!workRing;workRing=here;VOICE.say('ring'+RINGS.indexOf(here));if(first)VOICE.story('ring');inara('You\'re in the '+here.name+'. Debris all around you. Start sweeping.');}inaraT=0;return;}
 if(!workRing)return;
 const out=outside(cam.position,workRing);
 if(out>2e6){workRing=null;return;}                                      // well clear: you've left on purpose
 if(now>inaraT){if(!inaraT)VOICE.say('drift'+RINGS.indexOf(workRing));inaraT=now+15000;inara('You\'re drifting out of the '+workRing.name+', '+fmtDist(out)+' outside it. Turn back toward the debris.');}}

// ── WARP (Eric 10-11): pick a destination and you're there in seconds. Rings: you arrive on the ring's line at your
//    current longitude. The route bends around the Sun if a straight line would pass too close.
let warp=null;
const DEST=[
 {key:'starship',label:'Starship',note:'home · by the wormhole'},
 ...RINGS.map(rg=>({key:rg.key,label:rg.name,ring:rg,note:rg.au.toFixed(3)+' AU from the Sun'})),
 {key:'wormhole',label:'Wormhole',note:'3,000,000 km beyond Jupiter'},
 {key:'jupiter',label:'Jupiter',note:GIANTS[0].au.toFixed(3)+' AU from the Sun'},
 {key:'saturn',label:'Saturn',note:GIANTS[1].au.toFixed(3)+' AU from the Sun'}];
function lonDeg(p){return ((Math.atan2(p.z,p.x)*180/Math.PI)+360)%360;}
function destPoint(d){
 if(d.ring){const lon=Math.atan2(cam.position.z,cam.position.x);return new THREE.Vector3(Math.cos(lon),0,Math.sin(lon)).multiplyScalar(d.ring.r).add(new THREE.Vector3(0,(R()-.5)*2000,0));}
 if(d.key==='starship')return ship.localToWorld(new THREE.Vector3(0,-34,1100));
 if(d.key==='wormhole'){const out=WORMHOLE_POS.clone().normalize();return WORMHOLE_POS.clone().addScaledVector(out,-15000).add(new THREE.Vector3(0,3000,0));}
 const g=GIANTS.find(x=>x.name.toLowerCase()===d.key);return g.pos.clone().multiplyScalar(1-12*g.rad/g.pos.length());}
function renderWarpMenu(){
 $('warplist').innerHTML='';
 DEST.forEach(d=>{const b=document.createElement('button');b.className='wdest';const p=destPoint(d);
  const coords=d.ring?'arrive at longitude '+lonDeg(p).toFixed(1)+'°':'longitude '+lonDeg(p).toFixed(1)+'°';
  b.innerHTML='<b></b><span></span><em></em>';b.children[0].textContent=d.label;b.children[1].textContent=d.note+' · '+coords;
  b.children[2].textContent=fmtDist(cam.position.distanceTo(p));
  b.addEventListener('click',()=>{$('warppanel').hidden=true;startWarp(d);});$('warplist').appendChild(b);});}
function startWarp(d){
 const to=destPoint(d),from=cam.position.clone(),dist=from.distanceTo(to);
 if(dist<20000){warn('You\'re already there.');return;}
 // bend the route around the Sun if the straight line passes within 0.25 AU of it
 let via=null;const ab=tv.copy(to).sub(from),t=Math.max(0,Math.min(1,-from.dot(ab)/ab.lengthSq()));
 if(from.clone().addScaledVector(ab,t).length()<0.25*AU){const mid=from.clone().add(to).multiplyScalar(0.5);
  const dir=mid.length()>0.05*AU?mid.normalize():new THREE.Vector3(-from.z,0,from.x).normalize();via=dir.multiplyScalar(Math.max(0.6*AU,(from.length()+to.length())/2));}
 if(collecting){collecting.f.mesh.setMatrixAt(collecting.i,collecting.f.mats[collecting.i]);collecting=null;}
 lock=null;docked=false;stk=null;stickRing.hidden=true;vel.set(0,0,0);rot.set(0,0,0);
 warp={d,from,to,via,t:0,spool:1.4,dur:4+4*Math.log10(1+dist/AU),label:d.label,q0:cam.quaternion.clone()};
 snd.warp();}
function bez(w,k,out){if(!w.via)return out.copy(w.from).lerp(w.to,k);const a=(1-k)*(1-k),b=2*(1-k)*k,c=k*k;
 return out.set(a*w.from.x+b*w.via.x+c*w.to.x,a*w.from.y+b*w.via.y+c*w.to.y,a*w.from.z+b*w.via.z+c*w.to.z);}
const wq=new THREE.Quaternion(),wm=new THREE.Matrix4(),wp=new THREE.Vector3();
function warpTick(dt){
 const w=warp;w.t+=dt;const total=w.spool+w.dur;
 const k=Math.max(0,(w.t-w.spool)/w.dur),e=k<1?(k*k*(3-2*k)):1;
 // face along the route: during the spool, turn toward where you're going
 bez(w,Math.min(1,e+0.02),wp);wm.lookAt(cam.position,wp,cam.up);wq.setFromRotationMatrix(wm);
 cam.quaternion.slerp(wq,1-Math.exp(-(w.t<w.spool?3:6)*dt));
 if(w.t>w.spool)bez(w,e,cam.position);
 streaks(w.t<w.spool?w.t/w.spool*0.35:k<0.85?1:Math.max(0,(1-k)/0.15));
 if(w.t<total)return;
 warp=null;streaks(0);
 if(w.d.ring){const first=!workRing;workRing=w.d.ring;inaraT=0;VOICE.say('warp'+RINGS.indexOf(w.d.ring));if(first)VOICE.story('ring');inara('Dropping out in the '+w.d.ring.name+'. Debris all around you. Start sweeping.');}
 else if(w.d.key==='starship'){lock={name:'Starship',pos:DOCK_W.approach,aim:ship.position,stopAt:14,dock:1,auto:false};
  VOICE.say('arrived');toast('ARRIVED','The Starship is ahead. Double-tap it to come aboard.');}
 else toast('ARRIVED',w.label);}
// streaking stars while in warp (a 2D overlay)
const sc=$('streaks'),sx=sc.getContext('2d');let streakN=[];
function streaks(a){sc.style.opacity=a;if(a<=0)return;
 if(sc.width!==innerWidth){sc.width=innerWidth;sc.height=innerHeight;streakN=Array.from({length:160},()=>({ang:Math.random()*6.283,r:Math.random(),s:0.3+Math.random()}));}
 const cx=sc.width/2,cy=sc.height/2,M=Math.hypot(cx,cy);sx.clearRect(0,0,sc.width,sc.height);sx.strokeStyle='rgba(200,220,255,.8)';sx.lineWidth=1.2;
 for(const s of streakN){s.r+=0.02*s.s;if(s.r>1)s.r=Math.random()*0.15;const r0=s.r*M,r1=r0+M*0.12*s.s*s.r;
  sx.beginPath();sx.moveTo(cx+Math.cos(s.ang)*r0,cy+Math.sin(s.ang)*r0);sx.lineTo(cx+Math.cos(s.ang)*r1,cy+Math.sin(s.ang)*r1);sx.stroke();}}


// ── HELP / LOOP
let running=false;
function toggleHelp(force){const h=$('help');const show=force!==undefined?force:h.style.display==='none';h.style.display=show?'flex':'none';running=!show;}
let launched=false;
function closeHelp(){snd.resume();toggleHelp(false);if(!launched){launched=true;$('go').textContent='Back to flight';}}   // closing never restarts: you carry on where you were
$('go').addEventListener('click',closeHelp);$('helpX').addEventListener('click',closeHelp);
$('help').addEventListener('click',e=>{if(e.target===$('help')&&launched)closeHelp();});            // tap outside the card
addEventListener('keydown',e=>{if(e.code==='Escape'&&$('help').style.display!=='none')closeHelp();});
collectBtn.addEventListener('click',()=>{snd.resume();startCollect();});
holdEl.addEventListener('click',()=>{renderHold();$('holdpanel').hidden=!$('holdpanel').hidden;});
$('holdclose').addEventListener('click',()=>{$('holdpanel').hidden=true;});
$('warpbtn').addEventListener('click',()=>{snd.resume();if(warp)return;renderWarpMenu();$('warppanel').hidden=!$('warppanel').hidden;});
$('warpclose').addEventListener('click',()=>{$('warppanel').hidden=true;});
renderHold();
$('mute').addEventListener('click',()=>{snd.resume();if(snd.toggle()){$('mute').textContent='🔇';VOICE.stop();}else $('mute').textContent='🔊';});$('helpBtn').addEventListener('click',()=>toggleHelp(true));
function sky(){const d=cam.position.length();sunLight.intensity=1.6*Math.pow(AU/Math.max(d,SUN_R*30),2);
 sunLight.target.position.copy(cam.position);sunLight.position.copy(cam.position).addScaledVector(tv.copy(cam.position).normalize(),-1000);
 const s=placeFar(sun,SUN_POS,SUN_R);glow.position.copy(sun.position);
 const g=Math.max(s*14,IMP_D*0.01);glow.scale.set(g,g,1);
 LANDMARKS.forEach(l=>{if(l.far&&l.name!=='Sun')placeFar(l.draw,l.pos,l.rad);});
 stars.position.copy(cam.position);
 wormhole.children.forEach(c=>{if(c.userData.spin)c.material.rotation+=c.userData.spin*0.016;});}
let last=performance.now(),sightT=0;
function frame(now){const dt=Math.min(0.05,(now-last)/1000);last=now;
 if(running){if(warp)warpTick(dt);else{fly(dt);scan(dt);collectTick(dt);unloadTick(dt);}watchRing(now);}
 if(toastT&&now>toastT){document.getElementById('toast').hidden=true;toastT=0;}
 if(now>sightT){if(!warp){updateCells();updateSight();}sightT=now+200;}
 sky();pulseGuides(now/1000);
 hud();lockHud();approachHud();renderer.render(scene,cam);requestAnimationFrame(frame);}
updateCells();updateSight();requestAnimationFrame(frame);netStart();
window.__debris={receiptText,saveReceipt,RECEIPTS,STORE,SHIP_HOLD,startUnload,get xfer(){return xfer;},ship,DOCK_W,get docked(){return docked;},get SEED(){return SEED;},cargo,HOLD,startCollect,get collecting(){return collecting;},FIELDS,RINGS,cam,vel,lockAt,AU,startWarp,DEST,get warp(){return warp;},get workRing(){return workRing;},WORMHOLE_POS,
 get scan(){return{d:lock?Math.round(cam.position.distanceTo(lock.pos)):null,s:+scanStrength.toFixed(2),bearings:bearings.size,bestIs:scanBest,best:scanBest&&scanBest.size};},get lock(){return lock;},get throttle(){return throttle;}}; // for testing
