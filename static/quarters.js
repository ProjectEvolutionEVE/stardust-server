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
function saveToken(t){token=t;try{t?localStorage.setItem('stardust.token',t):localStorage.removeItem('stardust.token');}catch(e){}
  window.dispatchEvent(new Event(t?'stardust:signedin':'stardust:signedout'));}   // the flight connects to the server (or stops) at once
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
#sq details.fold summary{cursor:pointer;font-size:14px;color:#e8edf5} #sq details.fold table{margin-top:8px}
#sq textarea{width:100%;min-height:84px;padding:10px 12px;border-radius:10px;border:1px solid #2c3a5c;background:#0b1224;color:#e8edf5;font-family:inherit;font-size:15px;line-height:1.45;resize:vertical}
#sq .q{margin:18px 0 0} #sq .q>.n{font-size:12px;letter-spacing:.12em;color:#d9a441} #sq .q>.h{font-size:15px;color:#e8edf5;margin:2px 0 2px}
#sq .q>.hint{font-size:13px;color:#9aa6bf;margin-bottom:6px}
#sq .part{border:1px solid #23304d;border-radius:12px;padding:10px;margin:8px 0;background:rgba(20,28,48,.5)}
#sq .mrow{display:flex;gap:6px;margin-top:6px;align-items:center} #sq .mrow select{flex:1 1 auto;min-width:0} #sq .mrow input{flex:0 0 110px;width:110px}
#sq .x{flex:0 0 auto;padding:8px 11px;border-radius:9px;border:1px solid #2c3a5c;background:none;color:#ff8f8a;cursor:pointer}
#sq .small{padding:8px 12px;border-radius:9px;border:1px solid #2c3a5c;background:none;color:#7fb0ff;font-size:13px;cursor:pointer;margin-top:8px}
#sq .books label{display:flex;gap:8px;align-items:center;margin:6px 0;font-size:14px;letter-spacing:0;color:#e8edf5}
#sq .books input{width:auto} #sq .tot{margin-top:10px;padding:10px 12px;border-radius:10px;border:1px solid #2c3a5c;background:#0b1224;font-size:14px}
#sq .note{padding:10px 12px;border-radius:10px;margin:8px 0;font-size:14px;border:1px solid #2c3a5c} #sq .note.team{border-color:rgba(127,176,255,.5)}
#sq .btns{display:flex;gap:8px;flex-wrap:wrap} #sq .btns .go{flex:1 1 160px}
#sq .go.alt{background:none;border:1px solid #d9a441;color:#d9a441}`;
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
    +items.map(i=>`<tr><td>${esc(i.name)}${i.details&&i.details.serial?`<div class="soon" style="font-family:ui-monospace,Menlo,monospace">Serial ${esc(i.details.serial)}</div>`:''}</td><td style="text-align:right" class="soon">${i.set_aside?'set aside':'1'}</td></tr>`).join('')
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
  if(tab==='cabinet'){let r=null,bp=null,inv=null;try{r=await call('/receipts');}catch(e){}try{bp=await call('/blueprints');}catch(e){}try{inv=await call('/inventory');}catch(e){}
    let cr=null;try{cr=await call('/library/certificates');}catch(e){}
    const certs=cr?cr.certificates:[];
    const list=r?r.receipts:[];
    // every blueprint copy filed here (bought at auction, or printed to sell), grouped by design, each with its serial
    const fc=inv?(inv.places||[]).find(p=>p.kind==='filing_cabinet'):null,groups={};
    ((fc&&fc.items)||[]).filter(i=>i.kind==='blueprint').forEach(i=>{(groups[i.name]=groups[i.name]||[]).push(i);});
    const copies=Object.entries(groups).map(([n,is])=>`<details class="fold"><summary>📐 ${esc(n.replace('Blueprint · ',''))} <span class="soon">· ${is.length} cop${is.length>1?'ies':'y'}</span></summary>
      ${is.map(i=>`<div style="font-family:ui-monospace,Menlo,monospace;font-size:13px">${esc(i.details.serial||'')}${i.set_aside?' <span class="soon">(in an auction)</span>':''}</div>`).join('')}</details>`).join('');
    return `<h3 style="margin:0 0 6px;font-size:14px;color:#d9a441">MY DESIGNS</h3>${blueprintList(bp?bp.blueprints:[])}
     <h3 style="margin:14px 0 6px;font-size:14px;color:#d9a441">BLUEPRINT COPIES</h3>${copies||'<p class="soon">No blueprint copies yet. Win them at auction in the Market terminal, at your desk.</p>'}
     <h3 style="margin:14px 0 6px;font-size:14px;color:#d9a441">CERTIFICATES</h3>${certs.length?`<table>${certs.map(c=>`<tr><td>🎓 ${esc(c.title)}<div class="soon">Passed ${esc(new Date(c.passed_at).toLocaleDateString())}</div></td><td style="text-align:right">${esc(c.score)}</td></tr>`).join('')}</table>`:'<p class="soon">None yet. Pass a library book’s test to earn one.</p>'}
     <h3 style="margin:14px 0 6px;font-size:14px;color:#d9a441">RECEIPTS LOG</h3>${list.length?`<table>${list.map(x=>`<tr><td style="font-family:ui-monospace,Menlo,monospace">${esc(x.code)}<div class="soon">${esc(new Date(x.issued_at).toLocaleString())}</div></td><td>${receiptLine(x)}</td></tr>`).join('')}</table>`:'<p class="soon">No receipts yet. Every unload at the Starship gives you one.</p>'}
     <h3 style="margin:14px 0 6px;font-size:14px;color:#d9a441">LOCKBOX</h3><p class="soon">Empty. A small, secure box for valuables.</p>`;}
  if(tab==='closet')return `<p class="soon">Your clothing and uniforms will hang here. Uniforms change as you rise through the ranks.</p>`;
  if(tab==='bookshelf'){let inv=null;try{inv=await call('/inventory');}catch(e){}
    const sh=inv?(inv.places||[]).find(p=>p.kind==='bookshelf'):null,books=(sh&&sh.items)||[];
    return `<h3 style="margin:0 0 6px;font-size:14px;color:#d9a441">BOOKSHELF</h3>${books.length?`<table>${books.map(b=>`<tr><td>📘 ${esc(b.name)}</td><td style="text-align:right"><button class="small" data-shelf="${esc(b.item.replace(/^book-/,''))}">Read</button></td></tr>`).join('')}</table>`
      :'<p class="soon">No books checked out. The Starship Library lends them free: Exit Private Quarters, then the Library.</p>'}`;}
  return '';}
async function showQuarters(me,tab){
  root.hidden=false;
  root.innerHTML=`<div class="wrap"><div class="top"><div><div class="loc">PRIVATE QUARTERS</div><div class="who">${esc(me.title)}</div>${me.account_no?`<div class="soon" style="font-size:11px">Account ${esc(me.account_no)}</div>`:""}</div>
   <div style="text-align:right"><div class="soon">WSC Alexander von Humboldt</div><button id="sqExit" style="margin-top:6px;padding:8px 14px;border-radius:20px;border:1px solid #d9a441;background:rgba(217,164,65,.1);color:#d9a441;font-size:14px;cursor:pointer">🚪 Exit Private Quarters</button></div></div>
   <div class="tabs">${TABS.map(([k,n])=>`<button data-t="${k}" class="${k===tab?'on':''}">${n}</button>`).join('')}</div>
   <div class="panel" id="sqPanel">…</div></div>`;
  root.querySelectorAll('.tabs button').forEach(b=>b.onclick=()=>showQuarters(me,b.dataset.t));
  $('#sqPanel').innerHTML=await tabBody(tab,me);
  const ship=$('#sqShip');if(ship)ship.onclick=()=>showExit(me);
  $('#sqExit').onclick=()=>showExit(me);
  const mk=$('#sqMarket');if(mk)mk.onclick=()=>showMarket(me);
  root.querySelectorAll('[data-bp]').forEach(b=>b.onclick=()=>showBlueprintForm(me,Number(b.dataset.bp),'cabinet'));
  root.querySelectorAll('[data-shelf]').forEach(b=>b.onclick=()=>showBook(me,b.dataset.shelf,'shelf'));
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
// ── THE STARSHIP LIBRARY (rules 22, 24): free shelves, a reader, short friendly tests and certificates ──
async function showLibrary(me){
  let L=null;try{L=await call('/library');}catch(e){}
  const shelf=g=>`<details class="fold"${g.books.some(b=>b.written)?' open':''}><summary>${esc(g.group)}</summary>
    <table>${g.books.map(b=>`<tr><td>${b.written?'📘':'📕'} ${esc(b.title)}<div class="soon">${!b.written?'Being written':b.reference?'Reference: read any time':b.passed?'✅ Passed '+esc(b.score):'Test: 5 short questions'}${b.checked_out?' · on your bookshelf':''}</div></td>
      <td style="text-align:right">${b.written?`<button class="small" data-read="${esc(b.code)}">Read</button>`:''}</td></tr>`).join('')}</table></details>`;
  place('STARSHIP LIBRARY',me,`<p>Shelves of books, and quiet desks for study. The library is free: read here, or check a book out to your bookshelf.</p>
   ${L?`<p class="soon">Each book has a short, friendly test: get ${L.pass_mark} of 5 right to pass, and try again any time. You've passed ${L.passed}.</p>${L.shelves.map(shelf).join('')}`:'<p class="soon">The library is closed for a moment. Try again shortly.</p>'}
   ${L&&L.archives&&L.archives.shelves.length?`<h3 style="margin:14px 0 6px;font-size:14px;color:#d9a441">${esc(L.archives.wing.toUpperCase())}</h3><p class="soon">Records of how people first went to space, kept aboard as reference: read them here in the library.</p>${L.archives.shelves.map(g=>`<details class="fold"><summary>${esc(g.group)} (${g.books.length})</summary>
    <table>${g.books.map(b=>`<tr><td>📜 ${esc(b.title)}<div class="soon">${esc(b.date?b.date.slice(0,4):'Undated')} · Reference: read in the library</div></td>
      <td style="text-align:right"><button class="small" data-arch="${esc(b.code)}">Read</button></td></tr>`).join('')}</table></details>`).join('')}`:''}
   <button class="go" id="sqDraft">📐 Drafting room: design a blueprint</button>
   <button class="go" id="sqBay2">🚀 Go to the Docking Bay</button><button class="link" id="sqBack">Back to my quarters</button>`);
  root.querySelectorAll('[data-read]').forEach(x=>x.onclick=()=>showBook(me,x.dataset.read,'library'));
  root.querySelectorAll('[data-arch]').forEach(x=>x.onclick=()=>showArchive(me,x.dataset.arch,1));
  $('#sqDraft').onclick=()=>showBlueprints(me);
  $('#sqBay2').onclick=()=>{root.hidden=true;if(helpEl)helpEl.hidden=false;};
  $('#sqBack').onclick=()=>showQuarters(me,'bed');}
const para=t=>esc(t).split('\n').map(l=>`<p style="margin:6px 0">${l}</p>`).join('');
// Archives of Earth (Eric 10-19): real records from the NASA Technical Reports Server, one page at a time
async function showArchive(me,code,n){
  let b=null;try{b=await call('/library/archive/'+encodeURIComponent(code)+'?page='+n);}catch(e){}
  if(!b)return place('STARSHIP LIBRARY · ARCHIVES OF EARTH',me,`<p class="msg err">That record isn't in the archives.</p><button class="link" id="sqBack">Back</button>`)||($('#sqBack').onclick=()=>showLibrary(me));
  const nav=`<div class="btns" style="margin:8px 0">${b.page>1?'<button class="small" data-pg="'+(b.page-1)+'">‹ Previous page</button>':''}<span class="soon"> Page ${b.page} of ${b.pages} </span>${b.page<b.pages?'<button class="small" data-pg="'+(b.page+1)+'">Next page ›</button>':''}</div>`;
  place('STARSHIP LIBRARY · ARCHIVES OF EARTH',me,`<h2 style="margin:0">${esc(b.title)}</h2>
   <p class="soon" style="margin:2px 0 4px">${esc(b.program)} · ${esc(b.date?b.date.slice(0,4):'Undated')}</p>
   <p class="soon" style="margin:0">Source: ${esc(b.source)}</p><p class="soon" style="margin:0 0 6px">${esc(b.legal)}</p>
   ${nav}<pre style="white-space:pre-wrap;font:13px/1.45 Georgia,serif;margin:0">${esc(b.text)}</pre>${nav}
   <button class="link" id="sqBack">Back to the shelves</button>`);
  root.querySelectorAll('[data-pg]').forEach(x=>x.onclick=()=>{showArchive(me,code,Number(x.dataset.pg));root.scrollTop=0;});
  $('#sqBack').onclick=()=>showLibrary(me);}
async function showBook(me,code,from){
  let b=null,L=null;try{[b,L]=await Promise.all([call('/library/book/'+encodeURIComponent(code)),call('/library')]);}catch(e){}
  if(!b)return place('STARSHIP LIBRARY',me,`<p class="msg err">That book is still being written.</p><button class="link" id="sqBack">Back</button>`)||($('#sqBack').onclick=()=>showLibrary(me));
  const e=L?L.shelves.flatMap(g=>g.books).find(x=>x.code===code):null;
  place(from==='shelf'?'PRIVATE QUARTERS · BOOKSHELF':'STARSHIP LIBRARY',me,`<h2 style="margin:0">${esc(b.title)}</h2><p class="soon" style="margin:2px 0 8px">${esc(b.subtitle)}</p>
   ${b.chapters.map((c,i)=>`<details class="fold"${i===0?' open':''}><summary>${i+1}. ${esc(c.title)}</summary>${para(c.text)}</details>`).join('')}
   <div class="btns" style="margin-top:12px">${b.reference?'':`<button class="go" id="bkTest">${e&&e.passed?'Take the test again':'Take the test'}</button>`}
    ${e&&e.checked_out?'<button class="go alt" id="bkReturn">Return to the library</button>':'<button class="go alt" id="bkOut">Check out to my bookshelf</button>'}</div>
   <div class="msg" id="bkMsg"></div><button class="link" id="sqBack">${from==='shelf'?'Back to my bookshelf':'Back to the shelves'}</button>`);
  const m=(t,ok)=>{const x=$('#bkMsg');x.className='msg '+(ok?'ok':'err');x.textContent=t;};
  const t=$('#bkTest');if(t)t.onclick=()=>showTest(me,code,from);
  const o=$('#bkOut');if(o)o.onclick=async()=>{try{await call('/library/checkout',{book:code});await showBook(me,code,from);m('Checked out. It’s on the bookshelf in your quarters.',true);}catch(err){m(err.message);}};
  const r=$('#bkReturn');if(r)r.onclick=async()=>{try{await call('/library/return',{book:code});await showBook(me,code,from);m('Returned to the library.',true);}catch(err){m(err.message);}};
  $('#sqBack').onclick=()=>from==='shelf'?showQuarters(me,'bookshelf'):showLibrary(me);}
async function showTest(me,code,from){
  let t=null;try{t=await call('/library/test/'+encodeURIComponent(code));}catch(e){}
  if(!t)return showBook(me,code,from);
  place('STARSHIP LIBRARY · TEST',me,`<h2 style="margin:0">${esc(t.title)}</h2><p class="soon" style="margin:2px 0 8px">${t.questions.length} questions. Get ${t.pass_mark} right to pass. No time limit.</p>
   ${t.questions.map((q,i)=>`<div class="q"><div class="n">${i+1}</div><div class="h">${esc(q.question)}</div>
     <div class="books">${q.options.map(o=>`<label><input type="radio" name="q${q.id}" value="${esc(o.id)}"> ${esc(o.text)}</label>`).join('')}</div></div>`).join('')}
   <button class="go" id="tsGo">Hand it in</button><div class="msg" id="tsMsg"></div><button class="link" id="sqBack">Back to the book</button>`);
  $('#sqBack').onclick=()=>showBook(me,code,from);
  $('#tsGo').onclick=async()=>{const answers={};t.questions.forEach(q=>{const x=root.querySelector(`input[name="q${q.id}"]:checked`);if(x)answers[q.id]=x.value;});
    if(Object.keys(answers).length<t.questions.length){const m=$('#tsMsg');m.className='msg err';m.textContent='Answer every question first.';return;}
    try{const r=await call('/library/test',{book:code,answers});
      place('STARSHIP LIBRARY · TEST',me,`<h2 style="margin:0">${r.passed?'✅ Passed':'Not quite'}: ${r.score} of ${r.of}</h2>
       <p class="soon">${r.passed?'Your certificate is in the filing cabinet in your quarters.':`You need ${r.pass_mark} right. Have another look at the book and try again any time.`}</p>
       <table>${r.review.map(q=>`<tr><td>${q.right?'✅':'❌'} ${esc(q.question)}${q.right?'':`<div class="soon">The answer: ${esc(q.answer)}</div>`}</td></tr>`).join('')}</table>
       <button class="go" id="tsBook">Back to the book</button><button class="link" id="tsLib">Back to the shelves</button>`);
      $('#tsBook').onclick=()=>showBook(me,code,from);$('#tsLib').onclick=()=>showLibrary(me);}
    catch(e){const m=$('#tsMsg');m.className='msg err';m.textContent=e.message;}};}
function showMarket(me){   // the full board, over everything (rule 20: reached from the Desk only)
  const f=document.createElement('iframe');f.src='market.html';f.id='sqMarketFrame';f.title='Starship market';
  f.style.cssText='position:fixed;inset:0;width:100%;height:100%;border:0;z-index:60;background:#060912';
  document.body.appendChild(f);
  const close=e=>{if(e.origin!==location.origin||e.data!=='stardust:closeMarket')return;window.removeEventListener('message',close);
    f.remove();showQuarters(me,'desk');};
  window.addEventListener('message',close);}

// ── THE BLUEPRINT FORM (rule 23, Eric 10-11): a series of questions, not a blank page. In the Library's drafting room;
// the designs are kept in the filing cabinet. Weight and size are worked out from the real materials, never typed in.
// The game's review team reads every submission and may ask questions or request changes before approving it.
// One line per receipt in the filing cabinet's log, whatever kind it is.
function receiptLine(x){
  if(x.kind==='trade')return `Market: ${esc(x.trade)} ${esc(x.lots)} lot${x.lots>1?'s':''} of ${esc(x.item)} for ${esc(Number(x.credits).toLocaleString())} credits`;
  if(x.kind==='auction')return `Auction: ${x.trade==='won'?'won':'sold'} ${esc(x.serial)} (${esc(x.item)}) for ${esc(Number(x.bid).toLocaleString())} credits${x.trade==='won'&&x.starship_fee?` + ${esc(x.starship_fee)} Starship fee`:''}`;
  if(x.kind==='print')return `Printed ${esc(x.copies)} cop${x.copies>1?'ies':'y'} of ${esc(x.item)}, run ${esc(x.run)} (${esc(x.first)} to ${esc(x.last)}) for ${esc(Number(x.credits).toLocaleString())} credits`;
  if(x.kg)return `${esc(x.pieces)} pieces: ${Object.entries(x.kg).map(([m,k])=>esc(m)+' '+esc(k)+' kg').join(', ')}`;
  return esc(x.kind);}
const BP_STATUS={draft:'Draft: only you can see it',submitted:'With the review team',changes_requested:'Changes requested: see the review team’s note',
  approved:'Approved',rejected:'Not approved'};
function blueprintList(list){
  return (list.length?`<table>${list.map(b=>`<tr><td>📐 ${esc(b.title)}<div class="soon">${esc(BP_STATUS[b.status]||b.status)}${b.version?' · version '+b.version:''}${b.unread&&b.status==='changes_requested'?' · 1 new note':''}</div></td>
     <td style="text-align:right"><button class="small" data-bp="${b.id}">Open</button></td></tr>`).join('')}</table>`
    :'<p class="soon">No blueprints yet. Design one in the drafting room at the Starship Library.</p>');}
async function showBlueprints(me){
  let bp=null;try{bp=await call('/blueprints');}catch(e){}
  place('DRAFTING ROOM · STARSHIP LIBRARY',me,`<h2 style="margin:0 0 4px">Blueprints</h2>
   <p class="soon">You design it; the game's review team checks it. Only an approved blueprint can be built and sold. Your designs are kept in your filing cabinet.</p>
   <button class="go" id="bpNew">📐 Design a new blueprint</button>
   <h3 style="margin:16px 0 6px;font-size:14px;color:#d9a441">MY BLUEPRINTS</h3>${blueprintList(bp?bp.blueprints:[])}
   <button class="link" id="sqBack">Back to the Library</button>`);
  $('#bpNew').onclick=()=>showBlueprintForm(me,null,'library');
  root.querySelectorAll('[data-bp]').forEach(b=>b.onclick=()=>showBlueprintForm(me,Number(b.dataset.bp),'library'));
  $('#sqBack').onclick=()=>showLibrary(me);}
let bpOpts=null;
const UNITS=[['minutes',1],['hours',60],['days',1440]];
function kgText(kg){return kg>=1000?(kg/1000).toLocaleString(undefined,{maximumFractionDigits:3})+' t':kg.toLocaleString(undefined,{maximumFractionDigits:3})+' kg';}
function m3Text(m3){return m3<0.001&&m3>0?(m3*1e6).toLocaleString(undefined,{maximumFractionDigits:1})+' cm³':m3.toLocaleString(undefined,{maximumFractionDigits:3})+' m³';}
async function showBlueprintForm(me,id,from){
  try{if(!bpOpts)bpOpts=await call('/blueprints/options');}catch(e){return place('DRAFTING ROOM',me,`<p class="msg err">${esc(e.message)}</p>`);}
  let d=null;if(id){try{d=await call('/blueprints/'+id);}catch(e){return place('DRAFTING ROOM',me,`<p class="msg err">${esc(e.message)}</p>`);}}
  const f=d?d.form:{},edit=!d||d.editable,dis=edit?'':' disabled',L=bpOpts.limits.text;
  const mats=bpOpts.materials,dens=Object.fromEntries(mats.map(m=>[m.code,m.density_kg_m3]));
  const cats=[...new Set(mats.map(m=>m.category))];
  const matSelect=sel=>`<select class="bpMat"${dis} aria-label="Material"><option value="">Choose a material…</option>${cats.map(c=>`<optgroup label="${esc(c)}">${mats.filter(m=>m.category===c).map(m=>
    `<option value="${esc(m.code)}"${m.code===sel?' selected':''}>${esc(m.name)}</option>`).join('')}</optgroup>`).join('')}</select>`;
  const matRow=m=>`<div class="mrow">${matSelect(m&&m.item)}<input class="bpKg" type="number" inputmode="decimal" min="0" step="any" placeholder="kg" aria-label="Amount in kg"${dis}
    value="${m&&m.grams?m.grams/1000:''}">${edit?'<button class="x bpDelM" aria-label="Remove material">✕</button>':''}</div>`;
  const partBox=p=>`<div class="part"><input class="bpPart" maxlength="60" placeholder="Part name, e.g. Housing"${dis} value="${esc(p&&p.name||'')}">
    <div class="bpRows">${((p&&p.materials&&p.materials.length)?p.materials:[null]).map(matRow).join('')}</div>
    ${edit?'<button class="small bpAddM">+ Add a material</button> <button class="small bpDelP" style="color:#ff8f8a">Remove this part</button>':''}</div>`;
  const bm=f.build_minutes||0,unit=bm&&bm%1440===0?'days':bm&&bm%60===0?'hours':bm?'minutes':'hours';
  const uval=bm?bm/Object.fromEntries(UNITS)[unit]:'';
  let qn=0;const q=(n,h,hint,body)=>`<div class="q"><div class="n">${++qn}</div><div class="h">${h}</div>${hint?`<div class="hint">${hint}</div>`:''}${body}</div>`;
  const ta=(k,ph)=>`<textarea id="bp_${k}" maxlength="${L[k]}" placeholder="${esc(ph)}"${dis}>${esc(f[k]||'')}</textarea>`;
  const notes=(d&&d.messages||[]).map(m=>`<div class="note ${m.from==='You'?'':'team'}"><div class="soon">${esc(m.from)} · version ${m.version} · ${esc(new Date(m.at).toLocaleString())}</div>${esc(m.body)}</div>`).join('');
  const canReply=d&&(d.status==='submitted'||d.status==='changes_requested');
  place('DRAFTING ROOM · STARSHIP LIBRARY',me,`<h2 style="margin:0 0 4px">${d?esc(d.title):'New blueprint'}</h2>
   <p class="soon" style="margin:0">${d?esc(BP_STATUS[d.status]||d.status)+(d.version?' · version '+d.version:''):'Answer each question. You can save a draft and come back any time.'}</p>
   ${d&&d.model?`<div class="note team"><b>Model ${esc(d.model)}</b><div class="soon">Every copy of this design carries its own serial, so anyone can check it is genuine.</div>
     <details class="fold"><summary>Your serials (${d.serials.length})</summary>${d.serials.map(x=>`<div style="font-family:ui-monospace,Menlo,monospace">${esc(x)}</div>`).join('')}</details>
     <h3 style="margin:12px 0 4px;font-size:14px;color:#d9a441">PRINT COPIES TO SELL</h3>
     <div class="soon">A one-time setup fee on your first run, then a price for each copy. Copies are filed in your filing cabinet. A buyer can build from a copy but can never resell it.</div>
     <div class="mrow"><input id="bpCopies" type="number" inputmode="numeric" min="1" step="1" value="25" style="flex:0 0 110px" aria-label="Copies"><span class="soon">copies</span></div>
     <div id="bpQuote" class="soon" style="margin-top:6px"></div>
     <button class="go" id="bpPrint">Print copies</button>
     <h3 style="margin:16px 0 4px;font-size:14px;color:#d9a441">AUCTION COPIES</h3>
     <div class="soon">Copies go up one at a time. Each sells 5 minutes after its last top bid. If a copy gets no bid at your floor, the auction holds and your copies stay with you. Bidders are never named. ${d.copies_free} cop${d.copies_free===1?'y':'ies'} free to auction${d.cost_per_copy?`; each cost you ${Number(d.cost_per_copy).toLocaleString(undefined,{maximumFractionDigits:2})} credits`:''}.</div>
     ${d.copies_free?`<div class="mrow"><input id="auCopies" type="number" inputmode="numeric" min="1" max="${d.copies_free}" step="1" value="${Math.min(d.copies_free,5)}" style="flex:0 0 90px" aria-label="Copies to auction"><span class="soon">copies</span>
       <input id="auFloor" type="number" inputmode="numeric" min="1" step="1" value="${Math.max(1,Math.ceil((d.cost_per_copy||1)*1.5))}" style="flex:0 0 100px" aria-label="Floor price"><span class="soon">floor (credits)</span></div>
     <label for="auStart">Starts</label><input id="auStart" type="datetime-local">
     <label id="auWarn" style="display:none;margin-top:10px;letter-spacing:0;font-size:14px;color:#ffcf6b;align-items:flex-start;gap:8px"><input type="checkbox" id="auAck" style="width:auto;margin-top:3px"> I know this floor is below what each copy cost me, and I may sell at a loss.</label>
     <button class="go" id="auGo">Schedule the auction</button>`:''}
     ${(d.auctions||[]).length?`<table style="margin-top:10px">${d.auctions.map(a=>`<tr><td>${esc(new Date(a.start_at).toLocaleString())}<div class="soon">${a.copies} copies · floor ${a.floor}</div></td>
       <td style="text-align:right">${esc({scheduled:'scheduled',running:'live now',held:'held (no bid at the floor)',done:'finished',cancelled:'cancelled'}[a.status]||a.status)}<div class="soon">${a.sold} sold${a.earned?' · '+Number(a.earned).toLocaleString()+' credits':''}</div>
       ${a.status==='scheduled'?`<button class="small" data-aucancel="${a.auction_id}">Cancel</button>`:''}</td></tr>`).join('')}</table>`:''}</div>`:''}
   ${notes?`<h3 style="margin:14px 0 4px;font-size:14px;color:#d9a441">NOTES WITH THE REVIEW TEAM</h3>${notes}`:''}
   ${canReply?`<textarea id="bpReply" maxlength="2000" placeholder="Answer the review team"></textarea><button class="small" id="bpSendReply">Send answer</button>`:''}
   ${q('','What is it called, and what kind of thing is it?','',`<input id="bp_name" maxlength="${L.name}" placeholder="e.g. Long-range scanner"${dis} value="${esc(f.name||'')}">
     <select id="bp_kind" style="margin-top:8px"${dis}><option value="">Choose the kind…</option>${bpOpts.kinds.map(k=>`<option value="${k.code}"${k.code===f.kind?' selected':''}>${esc(k.name)}</option>`).join('')}</select>`)}
   ${q('','Is it brand new, an upgrade, or a newer version or model?','',`<select id="bp_origin"${dis}><option value="">Choose one…</option>${bpOpts.origins.map(o=>`<option value="${o.code}"${o.code===f.origin?' selected':''}>${esc(o.name)}</option>`).join('')}</select>
     <div id="bpBase"${f.origin==='upgrade'||f.origin==='version'?'':' hidden'}>
      <label for="bp_based_on">What does it build on?</label><select id="bp_based_on"${dis}><option value="">Choose…</option>${['Starship standard',"a player's approved design"].map(g=>{const b=bpOpts.bases.filter(x=>x.from===g);
        return b.length?`<optgroup label="${g==='Starship standard'?'Starship standard equipment':'Approved player designs'}">${b.map(x=>`<option value="${esc(x.code)}"${x.code===f.based_on?' selected':''}>${esc(x.name)}</option>`).join('')}</optgroup>`:'';}).join('')}</select>
      <label for="bp_changes">What's different from it?</label>${ta('changes','e.g. Twice the range, half the weight; the old housing is replaced with titanium.')}</div>`)}
   ${q('','What is it, and what problem does it solve?','Who needs it, and why?',ta('problem','e.g. Small debris fields are too faint for the starter scanner to hear.'))}
   ${q('','Everything it does, in detail.','Describe each thing it does and how. The review team reads this closely.',ta('does','e.g. It pushes a stronger wave out and listens for the faint return…'))}
   ${q('','What does it fit?','A ship, a machine, or “stands alone”.',ta('fits','e.g. Small mining craft'))}
   ${q('','What does it improve, and by how much?','',ta('improves','e.g. Scanner range, by about 30%'))}
   ${q('','Which library books does it require?','To build it, you pass the short test on each one.',`<div class="books">${bpOpts.books.map(g=>`<details class="fold"${g.books.some(b=>(f.books||[]).includes(b.code))?' open':''}><summary>${esc(g.group)}</summary>
     ${g.books.map(b=>`<label><input type="checkbox" class="bpBook" value="${b.code}"${(f.books||[]).includes(b.code)?' checked':''}${dis}> ${esc(b.name)}</label>`).join('')}</details>`).join('')}</div>`)}
   ${q('','Its parts and materials','Each part, with the materials it’s made of and how much. Its weight and size are worked out from the real materials.',
     `<div id="bpParts">${((f.parts&&f.parts.length)?f.parts:[null]).map(partBox).join('')}</div>${edit?'<button class="small" id="bpAddP">+ Add a part</button>':''}<div class="tot" id="bpTot"></div>`)}
   ${q('','How is it built?','The tools, the skills and the steps.',ta('how','e.g. Etch the circuit board, wind the coil, seal the housing.'))}
   ${q('','How long does it take to build?','Builds run in real time.',`<div class="mrow"><input id="bpTime" type="number" inputmode="decimal" min="0" step="any" style="flex:0 0 110px" value="${uval}"${dis}>
     <select id="bpUnit"${dis}>${UNITS.map(([u])=>`<option${u===unit?' selected':''}>${u}</option>`).join('')}</select></div>`)}
   <div class="msg" id="bpMsg"></div>
   ${edit?`<div class="btns"><button class="go alt" id="bpSave">Save draft</button><button class="go" id="bpSubmit">Send to the review team</button></div>`:''}
   ${d&&['draft','submitted','changes_requested'].includes(d.status)?'<button class="link" id="bpWithdraw" style="color:#ff8f8a">Withdraw this blueprint</button>':''}
   <button class="link" id="bpBack">${from==='cabinet'?'Back to my filing cabinet':'Back to the drafting room'}</button>`);
  const panel=root.querySelector('.panel');
  function gather(){
    const t=Number($('#bpTime').value),mult=Object.fromEntries(UNITS)[$('#bpUnit').value];
    const form={name:$('#bp_name').value,kind:$('#bp_kind').value||undefined,origin:$('#bp_origin').value||undefined,based_on:$('#bp_based_on').value||undefined,changes:$('#bp_changes').value,problem:$('#bp_problem').value,does:$('#bp_does').value,
      fits:$('#bp_fits').value,improves:$('#bp_improves').value,how:$('#bp_how').value,
      books:[...panel.querySelectorAll('.bpBook:checked')].map(x=>x.value),
      parts:[...panel.querySelectorAll('.part')].map(p=>({name:p.querySelector('.bpPart').value,
        materials:[...p.querySelectorAll('.mrow')].map(r=>({item:r.querySelector('.bpMat').value,kg:r.querySelector('.bpKg').value}))
          .filter(m=>m.item).map(m=>({item:m.item,grams:m.kg===''?null:Math.round(Number(m.kg)*1000)}))}))
        .filter(p=>p.name.trim()||p.materials.length)};
    if(t>0)form.build_minutes=Math.max(1,Math.round(t*mult));
    return form;}
  function total(){
    let kg=0,m3=0;for(const p of gather().parts)for(const m of p.materials){if(m.grams>0&&dens[m.item]){kg+=m.grams/1000;m3+=m.grams/1000/dens[m.item];}}
    $('#bpTot').innerHTML=`⚖️ Weight <b>${kgText(kg)}</b> · 📦 Material volume <b>${m3Text(m3)}</b><div class="soon">From the real density of each material.</div>`;}
  function wire(){
    panel.querySelectorAll('.bpAddM').forEach(b=>b.onclick=()=>{b.parentNode.querySelector('.bpRows').insertAdjacentHTML('beforeend',matRow(null));wire();total();});
    panel.querySelectorAll('.bpDelM').forEach(b=>b.onclick=()=>{b.parentNode.remove();total();});
    panel.querySelectorAll('.bpDelP').forEach(b=>b.onclick=()=>{b.parentNode.remove();total();});}
  wire();total();
  $('#bp_origin').addEventListener('change',e=>{$('#bpBase').hidden=!(e.target.value==='upgrade'||e.target.value==='version');});
  panel.addEventListener('input',total);panel.addEventListener('change',total);
  const addP=$('#bpAddP');if(addP)addP.onclick=()=>{$('#bpParts').insertAdjacentHTML('beforeend',partBox(null));wire();};
  const msg=(t,ok)=>{const m=$('#bpMsg');m.className='msg '+(ok?'ok':'err');m.textContent=t;};
  const sv=$('#bpSave');if(sv)sv.onclick=async()=>{try{const r=await call('/blueprints/save',d?{id:d.id,form:gather()}:{form:gather()});
      await showBlueprintForm(me,r.id,from);msg(r.missing.length?'Saved. Still to answer: '+r.missing.length+(r.missing.length>1?' questions.':' question.'):'Saved. Ready to send to the review team.',true);}
    catch(e){msg(e.message);}};
  const sb=$('#bpSubmit');if(sb)sb.onclick=async()=>{let bid=d&&d.id;const form=gather();
    try{if(!bid)bid=(await call('/blueprints/save',{form})).id;
      await call('/blueprints/submit',{id:bid,form});await showBlueprintForm(me,bid,from);msg('Sent. The review team will read it, and any questions or changes will appear here.',true);}
    catch(e){if(bid&&!d){await showBlueprintForm(me,bid,from);}msg(e.message);}};
  const cp=$('#bpCopies');
  if(cp){const quote=async()=>{const n=Math.floor(Number(cp.value));const b=$('#bpPrint');
      if(!(n>0)){$('#bpQuote').textContent='';b.disabled=true;return;}
      try{const q=await call('/blueprints/print',{id:d.id,copies:n,quote:true});b.disabled=false;
        b.textContent=`Print ${n.toLocaleString()} cop${n>1?'ies':'y'} for ${q.total.toLocaleString()} credits`;
        $('#bpQuote').textContent=(q.setup_fee?`Setup fee ${q.setup_fee} (first run only) + `:'')+`${n} × ${q.per_copy} = ${q.total.toLocaleString()} credits. That's ${(q.total/n).toLocaleString(undefined,{maximumFractionDigits:2})} credits a copy, so price your copies above that.`;}
      catch(e){$('#bpQuote').textContent=e.message;}};
    cp.addEventListener('input',quote);quote();
    $('#bpPrint').onclick=async()=>{const n=Math.floor(Number(cp.value));
      try{const r=await call('/blueprints/print',{id:d.id,copies:n});await showBlueprintForm(me,d.id,from);
        msg(`Printed run ${r.run}: ${r.serials[0]} to ${r.serials[r.serials.length-1]}. Paid ${r.price.total.toLocaleString()} credits. Your receipt is ${r.receipt.code}.`,true);}
      catch(e){msg(e.message);}};}
  const ag=$('#auGo');
  if(ag){const st=$('#auStart'),pad=n=>String(n).padStart(2,'0'),t=new Date(Date.now()+60000);
    st.value=`${t.getFullYear()}-${pad(t.getMonth()+1)}-${pad(t.getDate())}T${pad(t.getHours())}:${pad(t.getMinutes())}`;
    const warn=()=>{const below=Number($('#auFloor').value)<(d.cost_per_copy||0);$('#auWarn').style.display=below?'flex':'none';};
    $('#auFloor').addEventListener('input',warn);warn();
    ag.onclick=async()=>{try{const r=await call('/auctions/schedule',{id:d.id,copies:Math.floor(Number($('#auCopies').value)),floor:Math.floor(Number($('#auFloor').value)),
        start_at:new Date(st.value).toISOString(),below_cost_ok:$('#auAck').checked});
      await showBlueprintForm(me,d.id,from);msg(`Auction scheduled: ${r.copies} cop${r.copies>1?'ies':'y'} (${r.first} to ${r.last}) from ${new Date(r.start_at).toLocaleString()}, floor ${r.floor} credits. It shows in the Market terminal's Blueprint auctions tab.`,true);}
    catch(e){msg(e.message);}};}
  root.querySelectorAll('[data-aucancel]').forEach(b=>b.onclick=async()=>{try{await call('/auctions/cancel',{auction_id:Number(b.dataset.aucancel)});await showBlueprintForm(me,d.id,from);msg('Auction cancelled. The copies are free again.',true);}catch(e){msg(e.message);}});
  const rp=$('#bpSendReply');if(rp)rp.onclick=async()=>{try{await call('/blueprints/reply',{id:d.id,body:$('#bpReply').value});await showBlueprintForm(me,d.id,from);}catch(e){msg(e.message);}};
  const wd=$('#bpWithdraw');if(wd)wd.onclick=async()=>{if(!confirm('Withdraw this blueprint? It will be removed from your filing cabinet.'))return;
    try{await call('/blueprints/withdraw',{id:d.id});from==='cabinet'?showQuarters(me,'cabinet'):showBlueprints(me);}catch(e){msg(e.message);}};
  $('#bpBack').onclick=()=>from==='cabinet'?showQuarters(me,'cabinet'):showBlueprints(me);}

// a QUARTERS button while docked opens the real Private Quarters
window.addEventListener('click',async e=>{if(e.target&&e.target.id==='quartersbtn'&&token){e.stopImmediatePropagation();
  try{showQuarters(await call('/me'),'desk');}catch(err){showSignIn();}}},true);

(async()=>{if(token){try{const me=await call('/me');if(me.needs_setup)return showSetup();return showQuarters(me,'bed');}catch(e){}}
  showSignIn();})();
})();
