// SIGN-IN AND PRIVATE QUARTERS (Eric 10-11). Loaded only by the page the game server itself serves (/play/), which sets
// window.STARDUST_API. The claude.ai preview of the flight test doesn't load this file and stays offline.
//   · Sign-in: language → phone or email → 6-digit code → (new player) first and last name from the game's lists.
//   · Signing in = waking up in bed in Private Quarters. Tabs: Bed, Desk, Closet, Bookshelf, Filing cabinet.
//   · Signing out happens from the bed: the character goes to sleep.
// No real names, no age, no free text (Eric 10-11). The only personal information sent is the phone or email.
(function(){
const API=window.STARDUST_API;if(!API)return;
const $=s=>document.querySelector(s);
let token=null;try{token=localStorage.getItem('stardust.token');}catch(e){}
function saveToken(t){token=t;try{t?localStorage.setItem('stardust.token',t):localStorage.removeItem('stardust.token');}catch(e){}}
async function call(path,body){
  const r=await fetch(API+path,{method:body?'POST':'GET',headers:Object.assign({'Content-Type':'application/json'},token?{Authorization:'Bearer '+token}:{}),
    body:body?JSON.stringify(body):undefined});
  let j={};try{j=await r.json();}catch(e){}
  if(r.status===401){saveToken(null);}
  if(!r.ok)throw new Error(j.error||'Something went wrong. Please try again.');
  return j;}
function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));}

const css=document.createElement('style');css.textContent=`
#sq{position:fixed;inset:0;z-index:20;background:radial-gradient(ellipse at 50% 0%,#141d33 0%,#060912 70%);color:#c9d1d9;
 font:15px/1.5 -apple-system,Segoe UI,Roboto,Arial,sans-serif;overflow:auto;padding:max(16px,env(safe-area-inset-top)) 16px 32px}
#sq .card{max-width:440px;margin:6vh auto 0;padding:22px 20px;border:1px solid #23304d;border-radius:16px;background:rgba(11,16,32,.92)}
#sq h1{font-size:13px;letter-spacing:.22em;color:#d9a441;text-align:center;margin:0}
#sq h2{font-size:22px;text-align:center;margin:6px 0 4px;color:#e8edf5}
#sq .sub{color:#9aa6bf;font-size:13px;text-align:center;margin-bottom:16px}
#sq label{display:block;font-size:12px;letter-spacing:.06em;color:#9aa6bf;margin:12px 0 4px}
#sq input,#sq select{width:100%;padding:12px;border-radius:10px;border:1px solid #2c3a5c;background:#0b1224;color:#e8edf5;font-size:16px}
#sq .seg{display:flex;gap:8px;margin-top:12px} #sq .seg button{flex:1;padding:10px;border-radius:10px;border:1px solid #2c3a5c;background:none;color:#9aa6bf;font-size:14px;cursor:pointer}
#sq .seg button.on{border-color:#d9a441;color:#d9a441;background:rgba(217,164,65,.1)}
#sq .go{width:100%;margin-top:16px;padding:13px;border:0;border-radius:11px;background:#d9a441;color:#1a1204;font-weight:700;font-size:15px;letter-spacing:.04em;cursor:pointer}
#sq .go:disabled{opacity:.5} #sq .link{display:block;margin:12px auto 0;background:none;border:0;color:#7fb0ff;font-size:13px;text-decoration:underline;cursor:pointer}
#sq .msg{min-height:20px;margin-top:10px;font-size:13px;text-align:center} #sq .msg.err{color:#ff8f8a} #sq .msg.ok{color:#7fe0a8}
#sq .top{max-width:720px;margin:0 auto;display:flex;flex-wrap:wrap;align-items:baseline;justify-content:space-between;gap:6px;
 border-bottom:1px solid #23304d;padding-bottom:10px}
#sq .loc{font-size:12px;letter-spacing:.22em;color:#d9a441} #sq .who{font-size:18px;color:#e8edf5}
#sq .wrap{max-width:720px;margin:0 auto}
#sq .tabs{display:flex;gap:6px;overflow-x:auto;margin:14px 0 12px;padding-bottom:4px}
#sq .tabs button{flex:0 0 auto;padding:9px 14px;border-radius:20px;border:1px solid #2c3a5c;background:none;color:#9aa6bf;font-size:14px;cursor:pointer}
#sq .tabs button.on{border-color:#7fb0ff;color:#e8edf5;background:rgba(127,176,255,.12)}
#sq .panel{border:1px solid #23304d;border-radius:14px;background:rgba(11,16,32,.9);padding:16px}
#sq .bar{margin:8px 0} #sq .bar .l{display:flex;justify-content:space-between;font-size:13px;color:#9aa6bf}
#sq .bar .t{height:10px;border-radius:5px;background:#141c30;overflow:hidden;margin-top:3px} #sq .bar .f{height:100%;border-radius:5px}
#sq .warn{margin-top:10px;padding:10px 12px;border-radius:10px;border:1px solid rgba(255,207,107,.45);color:#ffcf6b;font-size:13px}
#sq table{width:100%;border-collapse:collapse;font-size:13px} #sq td{padding:6px 4px;border-top:1px solid #1d2740;vertical-align:top}
#sq .soon{color:#9aa6bf;font-size:13px}
#sq details.fold{border:1px solid #23304d;border-radius:10px;padding:10px 12px;margin:8px 0;background:rgba(20,28,48,.5)}
#sq details.fold summary{cursor:pointer;font-size:14px;color:#e8edf5} #sq details.fold table{margin-top:8px}`;
document.head.appendChild(css);
const root=document.createElement('div');root.id='sq';document.body.appendChild(root);
const helpEl=document.getElementById('help');if(helpEl)helpEl.hidden=true;   // the flight help waits until the player heads to their ship

let opts=null;
async function options(){if(!opts)opts=await call('/signup-options');return opts;}
const state={channel:'sms',address:'',lang:null,region:null,shown:''};
try{const l=localStorage.getItem('stardust.lang');if(l)state.lang=l;const r=localStorage.getItem('stardust.region');if(r)state.region=r;}catch(e){}

// The country for phone numbers (Eric 10-11: "fool proof"). Preset from the browser, so most people never touch it;
// the number itself can then be typed any way (with or without the 1, spaces, dashes, brackets).
function guessRegion(list){
  const have=new Set(list.map(c=>c.iso));
  for(const l of (navigator.languages||[navigator.language||''])){const m=/[-_]([A-Za-z]{2})$/.exec(l||'');if(m&&have.has(m[1].toUpperCase()))return m[1].toUpperCase();}
  try{const tz=Intl.DateTimeFormat().resolvedOptions().timeZone||'';if(tz.startsWith('America/'))return 'US';if(tz==='Europe/London')return 'GB';}catch(e){}
  return have.has('US')?'US':list[0].iso;}
function flag(iso){return iso.length===2?String.fromCodePoint(...[...iso].map(c=>0x1F1A5+c.charCodeAt(0))):'';}
function countryOptions(list,lang,sel){
  let dn=null;try{dn=new Intl.DisplayNames([lang||'en','en'],{type:'region'});}catch(e){}
  const named=list.map(c=>{let n=c.iso;try{n=dn?dn.of(c.iso)||c.iso:c.iso;}catch(e){}return {...c,name:n};}).sort((a,b)=>a.name.localeCompare(b.name));
  return named.map(c=>`<option value="${esc(c.iso)}"${c.iso===sel?' selected':''}>${flag(c.iso)} ${esc(c.name)} +${c.dial}</option>`).join('');}

// ── SIGN IN ──
async function showSignIn(){
  const o=await options().catch(()=>null);
  const langs=o?o.languages:[{code:'en',name:'English',native:'English',flag:'🇬🇧'}];
  const guess=state.lang||((navigator.language||'en').split('-')[0]);
  root.innerHTML=`<div class="card"><h1>STARDUST</h1><h2>Sign in</h2>
   <div class="sub">No passwords. A 6-digit code to your phone or email.</div>
   <label for="sqLang">Your language</label><select id="sqLang">${langs.map(l=>`<option value="${esc(l.code)}"${l.code===guess?' selected':''}>${esc(l.flag)} ${esc(l.native)}${l.native!==l.name?' · '+esc(l.name):''}</option>`).join('')}</select>
   <div class="seg"><button data-c="sms" class="${state.channel==='sms'?'on':''}">📱 Phone</button><button data-c="email" class="${state.channel==='email'?'on':''}">✉️ Email</button></div>
   <label for="sqAddr" id="sqAddrL"></label>
   <select id="sqCountry" aria-label="Country" style="margin-bottom:8px"></select>
   <input id="sqAddr" autocomplete="tel"><div class="sub" id="sqHint" style="margin-top:6px;text-align:left;font-size:13px"></div>
   <button class="go" id="sqSend"></button><div class="msg" id="sqMsg"></div></div>`;
  const addr=$('#sqAddr'),lab=$('#sqAddrL'),send=$('#sqSend'),ctry=$('#sqCountry'),hint=$('#sqHint');
  const countries=(o&&o.countries)||[{iso:'US',dial:1}];
  if(!state.region)state.region=guessRegion(countries);
  function fillCountries(){ctry.innerHTML=countryOptions(countries,state.lang,state.region);}
  fillCountries();
  ctry.onchange=()=>{state.region=ctry.value;try{localStorage.setItem('stardust.region',state.region);}catch(e){}mode();};
  function mode(){const ph=state.channel==='sms';lab.textContent=ph?'Mobile number':'Email address';
    ctry.hidden=!ph;hint.hidden=!ph;
    const dial=(countries.find(c=>c.iso===state.region)||{dial:1}).dial;
    hint.textContent=`Type it the way it\u2019s saved in your phone. Spaces, dashes or a leading ${dial===1?'1':'0'} are all fine.`;
    addr.type=ph?'tel':'email';addr.placeholder=ph?'5745550123':'you@example.com';addr.autocomplete=ph?'tel-national':'email';
    addr.inputMode=ph?'tel':'email';
    send.textContent=ph?'Text me a code':'Email me a code';}
  mode();addr.value=state.address;
  root.querySelectorAll('.seg button').forEach(b=>b.onclick=()=>{state.channel=b.dataset.c;root.querySelectorAll('.seg button').forEach(x=>x.classList.toggle('on',x===b));mode();});
  $('#sqLang').onchange=e=>{state.lang=e.target.value;try{localStorage.setItem('stardust.lang',state.lang);}catch(err){}fillCountries();};
  state.lang=$('#sqLang').value;fillCountries();
  send.onclick=async()=>{state.address=addr.value.trim();const m=$('#sqMsg');m.className='msg';m.textContent='Sending…';send.disabled=true;
    try{const j=await call('/auth/start',{channel:state.channel,address:state.address,region:state.region});
      state.shown=j.to||state.address;showCode(j.dev_code);}
    catch(e){m.className='msg err';m.textContent=e.message;send.disabled=false;}};}

function showCode(devCode){
  root.innerHTML=`<div class="card"><h1>STARDUST</h1><h2>Enter your code</h2>
   <div class="sub">We sent a 6-digit code to ${esc(state.shown||state.address)}.</div>
   <label for="sqCode">6-digit code</label><input id="sqCode" inputmode="numeric" autocomplete="one-time-code" maxlength="6" placeholder="123456">
   <button class="go" id="sqVerify">Wake up</button><button class="link" id="sqBack">Use a different number or email</button>
   <div class="msg" id="sqMsg">${devCode?'Test code: '+esc(devCode):''}</div></div>`;
  const c=$('#sqCode');c.focus();
  $('#sqBack').onclick=showSignIn;
  $('#sqVerify').onclick=async()=>{const m=$('#sqMsg');m.className='msg';m.textContent='Checking…';
    try{const j=await call('/auth/verify',{channel:state.channel,address:state.address,region:state.region,code:c.value});saveToken(j.token);
      if(j.me.needs_setup)showSetup();else showQuarters(j.me,'bed');}
    catch(e){m.className='msg err';m.textContent=e.message;}};}

async function showSetup(){
  const o=await options();
  root.innerHTML=`<div class="card"><h1>WELCOME ABOARD</h1><h2>Choose your name</h2>
   <div class="sub">Everyone aboard the WSC Alexander von Humboldt starts as a Trainee. Pick the name the crew will know you by.</div>
   <label for="sqFirst">First name</label><select id="sqFirst">${o.first_names.map(n=>`<option>${esc(n)}</option>`).join('')}</select>
   <label for="sqLast">Last name</label><select id="sqLast">${o.last_names.map(n=>`<option>${esc(n)}</option>`).join('')}</select>
   <div class="sub" style="margin-top:14px">You'll be known as <b id="sqPreview" style="color:#e8edf5"></b></div>
   <button class="go" id="sqSet">That's me</button><div class="msg" id="sqMsg"></div></div>`;
  const f=$('#sqFirst'),l=$('#sqLast');
  f.selectedIndex=Math.floor(Math.random()*o.first_names.length);l.selectedIndex=Math.floor(Math.random()*o.last_names.length);
  const pv=()=>{$('#sqPreview').textContent='Trainee '+f.value+' '+l.value;};pv();f.onchange=pv;l.onchange=pv;
  $('#sqSet').onclick=async()=>{const m=$('#sqMsg');m.className='msg';m.textContent='Saving…';
    try{const me=await call('/me/setup',{first_name:f.value,last_name:l.value,language:state.lang||'en'});showQuarters(me,'bed');}
    catch(e){m.className='msg err';m.textContent=e.message;}};}

// ── PRIVATE QUARTERS ──
const TABS=[['bed','🛏️ Bed'],['desk','🗄️ Desk'],['closet','👔 Closet'],['bookshelf','📚 Bookshelf'],['cabinet','🗂️ Filing cabinet']];
function bars(me){const c=v=>v>=65?'#7fe0a8':v>=50?'#ffcf6b':'#ff8f8a';
  return Object.entries(me.bars).map(([k,v])=>`<div class="bar"><div class="l"><span>${k[0].toUpperCase()+k.slice(1)}</span><span>${v.toFixed(0)}%</span></div>
   <div class="t"><div class="f" style="width:${v}%;background:${c(v)}"></div></div></div>`).join('')+(me.warning?`<div class="warn">${esc(me.warning)}</div>`:'');}
// The desk's list of everything the player owns (Eric 10-11): a folder for each place it's kept. Raw materials wait in
// the Starship's cargo hold; Private Quarters holds the filing cabinet (every blueprint, with the lockbox for small
// personal effects and valuables inside it) and the bookshelf (library books checked out).
const PLACE_ORDER=['starship_cargo','ship_hold','hangar','private_quarters','filing_cabinet','lockbox','bookshelf'];
const PLACE_ICON={starship_cargo:'📦',ship_hold:'🚀',hangar:'🛰️',private_quarters:'🛏️',filing_cabinet:'🗂️',lockbox:'🔒',bookshelf:'📚'};
const PLACE_NAME={starship_cargo:'Starship cargo hold'};
const PLACE_EMPTY={starship_cargo:'No raw materials in storage.',ship_hold:'Nothing aboard.',filing_cabinet:'No blueprints yet.',
  lockbox:'Empty. For small personal effects and valuables.',bookshelf:'No library books checked out.',private_quarters:'Nothing else here.'};
const DESIGN_STATUS={draft:'your draft',submitted:'with the review team',changes_requested:'changes requested',approved:'approved',rejected:'not approved'};
function amount(g){
  if(g.kg!=null){const kg=Number(g.kg);return (kg>=1000?(kg/1000).toLocaleString(undefined,{maximumFractionDigits:2})+' t':kg.toLocaleString(undefined,{maximumFractionDigits:1})+' kg')
    +(g.pieces?` · ${g.pieces} piece${g.pieces>1?'s':''}`:'')+(g.kg_set_aside?` · ${Number(g.kg_set_aside).toLocaleString()} kg set aside for an order`:'');}
  return (g.count||0)+(g.set_aside?` · ${g.set_aside} set aside`:'');}
function folder(p,all){
  const goods=p.goods||[],items=p.items||[],designs=p.designs||[];
  const kids=all.filter(c=>c.inside===p.kind).sort((x,y)=>PLACE_ORDER.indexOf(x.kind)-PLACE_ORDER.indexOf(y.kind));
  const n=goods.length+items.length+designs.length;
  const u=Number(p.used_m3||0),m3=u>0&&u<0.01?'under 0.01':u.toLocaleString(undefined,{maximumFractionDigits:2});
  const space=p.capacity_m3!=null?`${m3} of ${Number(p.capacity_m3).toLocaleString(undefined,{maximumFractionDigits:2})} m³ used`
    :p.capacity_slots!=null?`${p.used_slots} of ${p.capacity_slots} bays used`:'';
  const rows=goods.map(g=>`<tr><td>${esc(g.name||g.item)}</td><td style="text-align:right">${esc(amount(g))}</td></tr>`).join('')
    +items.map(i=>`<tr><td>${esc(i.name)}</td><td style="text-align:right" class="soon">${i.set_aside?'set aside':'1'}</td></tr>`).join('')
    +designs.map(d=>`<tr><td>${esc(d.title)} <span class="soon">(your design)</span></td><td style="text-align:right" class="soon">${esc(DESIGN_STATUS[d.status]||d.status)}</td></tr>`).join('');
  return `<details class="fold"${p.kind==='starship_cargo'?' open':''}><summary>${PLACE_ICON[p.kind]||'📁'} ${esc(PLACE_NAME[p.kind]||p.name)}
    <span class="soon"> · ${n?n+' item'+(n>1?'s':''):'empty'}${space?' · '+esc(space):''}</span></summary>
    ${n?`<table>${rows}</table>`:(kids.length?'':`<p class="soon" style="margin:6px 0 0">${esc(PLACE_EMPTY[p.kind]||'Empty.')}</p>`)}
    ${kids.map(k=>folder(k,all)).join('')}</details>`;}
function itemFolders(places){
  const all=places||[];
  return all.filter(p=>!p.inside).sort((a,b)=>PLACE_ORDER.indexOf(a.kind)-PLACE_ORDER.indexOf(b.kind)).map(p=>folder(p,all)).join('');}
async function tabBody(tab,me){
  if(tab==='bed')return `<p>${me.asleep?'You are asleep.':'You\'re awake, in your bed.'} Every session starts and ends here.</p>${bars(me)}
   <button class="go" id="sqShip">Get up</button><button class="link" id="sqOut">Sign out (go to sleep)</button>`;
  if(tab==='desk'){let inv=null;try{inv=await call('/inventory');}catch(e){}

    return `<h3 style="margin:0 0 6px;font-size:14px;color:#d9a441">COMMS</h3><p class="soon">No messages yet. News from Starship Central Command and job postings will arrive here.</p>
     <h3 style="margin:14px 0 6px;font-size:14px;color:#d9a441">WALLET</h3><p>${inv?esc(inv.credits)+' credits':'—'}</p>
     <h3 style="margin:14px 0 6px;font-size:14px;color:#d9a441">MY ITEMS</h3>
     <p class="soon" style="margin-top:0">Everything you own, in a folder for each place it's kept.</p>${inv?itemFolders(inv.places):'<p class="soon">—</p>'}
     <h3 style="margin:14px 0 6px;font-size:14px;color:#d9a441">MARKET</h3><p class="soon">Prices, the chart, instant buy and sell, your open orders and your trade history.</p>
     <button class="go" id="sqMarket">📈 Open the market terminal</button>`;}
  if(tab==='cabinet'){let r=null;try{r=await call('/receipts');}catch(e){}
    const list=r?r.receipts:[];
    return `<h3 style="margin:0 0 6px;font-size:14px;color:#d9a441">RECEIPTS LOG</h3>${list.length?`<table>${list.map(x=>`<tr><td style="font-family:ui-monospace,Menlo,monospace">${esc(x.code)}<div class="soon">${esc(new Date(x.issued_at).toLocaleString())}</div></td><td>${esc(x.pieces)} pieces: ${Object.entries(x.kg).map(([m,k])=>esc(m)+' '+esc(k)+' kg').join(', ')}</td></tr>`).join('')}</table>`:'<p class="soon">No receipts yet. Every unload at the Starship gives you one.</p>'}
     <h3 style="margin:14px 0 6px;font-size:14px;color:#d9a441">LOCKBOX</h3><p class="soon">Empty. A small, secure box for valuables.</p>`;}
  if(tab==='closet')return `<p class="soon">Your clothing and uniforms will hang here. Uniforms change as you rise through the ranks.</p>`;
  if(tab==='bookshelf')return `<p class="soon">Your own books for continued learning and study. Courses and certification tests are in the Starship library.</p>`;
  return '';}
async function showQuarters(me,tab){
  root.hidden=false;
  root.innerHTML=`<div class="wrap"><div class="top"><div><div class="loc">PRIVATE QUARTERS</div><div class="who">${esc(me.title)}</div></div>
   <div style="text-align:right"><div class="soon">WSC Alexander von Humboldt</div><button id="sqExit" style="margin-top:6px;padding:8px 14px;border-radius:20px;border:1px solid #d9a441;background:rgba(217,164,65,.1);color:#d9a441;font-size:14px;cursor:pointer">🚪 Exit Private Quarters</button></div></div>
   <div class="tabs">${TABS.map(([k,n])=>`<button data-t="${k}" class="${k===tab?'on':''}">${n}</button>`).join('')}</div>
   <div class="panel" id="sqPanel">…</div></div>`;
  root.querySelectorAll('.tabs button').forEach(b=>b.onclick=()=>showQuarters(me,b.dataset.t));
  $('#sqPanel').innerHTML=await tabBody(tab,me);
  const ship=$('#sqShip');if(ship)ship.onclick=()=>showExit(me);
  $('#sqExit').onclick=()=>showExit(me);
  const mk=$('#sqMarket');if(mk)mk.onclick=()=>showMarket(me);
  const out=$('#sqOut');if(out)out.onclick=async()=>{try{await call('/auth/signout',{});}catch(e){}saveToken(null);
    root.innerHTML=`<div class="card"><h1>STARDUST</h1><h2>Sleep well</h2><div class="sub">You're in your bed. Your body rests while you're away, in real time.</div>
     <button class="go" id="sqAgain">Sign in again</button></div>`;$('#sqAgain').onclick=showSignIn;};}

// ── LEAVING THE QUARTERS (Eric 10-11): two ways out, the Library or the Docking Bay. The market is reached from the Desk.
function place(title,me,body){
  root.hidden=false;
  root.innerHTML=`<div class="wrap"><div class="top"><div><div class="loc">${esc(title)}</div><div class="who">${esc(me.title)}</div></div>
   <div class="soon">WSC Alexander von Humboldt</div></div><div class="panel">${body}</div></div>`;}
function showExit(me){
  place('CORRIDOR',me,`<h2 style="margin:0 0 4px">Where to?</h2><p class="soon">You step out of your quarters.</p>
   <button class="go" id="sqLib">📚 Starship Library</button><button class="go" id="sqBay">🚀 Docking Bay</button>
   <button class="link" id="sqBack">Back to my quarters</button>`);
  $('#sqLib').onclick=()=>showLibrary(me);
  $('#sqBay').onclick=()=>{root.hidden=true;if(helpEl)helpEl.hidden=false;};
  $('#sqBack').onclick=()=>showQuarters(me,'bed');}
function showLibrary(me){
  place('STARSHIP LIBRARY',me,`<p>Shelves of books, and quiet desks for study.</p>
   <p class="soon">The library opens soon. The starter books, the courses and tests that earn promotions, and the blueprint form will all be here.</p>
   <button class="go" id="sqBay2">🚀 Go to the Docking Bay</button><button class="link" id="sqBack">Back to my quarters</button>`);
  $('#sqBay2').onclick=()=>{root.hidden=true;if(helpEl)helpEl.hidden=false;};
  $('#sqBack').onclick=()=>showQuarters(me,'bed');}
function showMarket(me){
  place('MARKET TERMINAL',me,`<p>The live market: the price chart, the best bid and ask, instant <b>Buy now</b> and <b>Sell now</b>, your open orders and your trade history.</p>
   <p class="soon">The terminal is being connected to the Starship's market. It arrives in the next update.</p>
   <p class="soon">The Starship bank trades on this market too.</p>
   <button class="link" id="sqBack">Back to my desk</button>`);
  $('#sqBack').onclick=()=>showQuarters(me,'desk');}

// a QUARTERS button while docked opens the real Private Quarters
window.addEventListener('click',async e=>{if(e.target&&e.target.id==='quartersbtn'&&token){e.stopImmediatePropagation();
  try{showQuarters(await call('/me'),'desk');}catch(err){showSignIn();}}},true);

(async()=>{if(token){try{const me=await call('/me');if(me.needs_setup)return showSetup();return showQuarters(me,'bed');}catch(e){}}
  showSignIn();})();
})();
