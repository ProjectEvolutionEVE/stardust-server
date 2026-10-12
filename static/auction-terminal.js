// STARDUST · BLUEPRINT AUCTIONS, the second tab of the Market terminal (Eric 10-12; server: auctions.py).
// Copies go up one at a time; each sells 5 minutes after its last top bid; a winning bid pays the Starship 2.5% on top.
// Bidders and designers are never named (rule 8). Everything comes from /api/dfg/auctions; bids go to /auctions/bid.
'use strict';
(function () {
  const API = '/api/dfg';
  let token = null; try { token = localStorage.getItem('stardust.token'); } catch (e) {}
  if (!token) return;
  const $ = id => document.getElementById(id);
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const fmt = n => n == null ? '—' : Math.round(n).toLocaleString('en-US');
  async function call(path, body) {
    const r = await fetch(API + path, { method: body ? 'POST' : 'GET', headers: { 'Content-Type': 'application/json', Authorization: 'Bearer ' + token },
      body: body ? JSON.stringify(body) : undefined });
    const j = await r.json().catch(() => ({}));
    if (!r.ok) throw new Error(j.error || 'The auction office didn\'t answer. Try again in a moment.');
    return j;
  }
  let view = 'ore', data = null, skew = 0, timer = null;
  function show(v) {
    view = v;
    document.querySelectorAll('#views button').forEach(b => b.classList.toggle('on', b.dataset.v === v));
    $('oreView').hidden = $('oreNote').hidden = $('oreFoot').hidden = v !== 'ore';
    $('auView').hidden = v !== 'auctions';
    clearInterval(timer);
    if (v === 'auctions') { load(); timer = setInterval(load, 2000); }
  }
  $('views').addEventListener('click', e => { if (e.target.dataset.v) show(e.target.dataset.v); });
  async function load() {
    try { data = await call('/auctions'); skew = Date.parse(data.server_time) - Date.now(); render(); }
    catch (e) { $('auList').innerHTML = `<p class="down">${esc(e.message)}</p>`; }
  }
  const left = iso => Math.max(0, Math.round((Date.parse(iso) - (Date.now() + skew)) / 1000));
  const clock = s => `${Math.floor(s / 60)}:${String(s % 60).padStart(2, '0')}`;
  const fee = n => Math.ceil(n * data.rules.fee_pct / 100);
  function design(d) {
    const rows = [['What it is and the problem it solves', d.problem], ['What it does', d.does], ['What it fits', d.fits],
      ['What it improves', d.improves], ['How it\'s built', d.how]].filter(r => r[1]);
    return rows.map(r => `<p><b>${esc(r[0])}:</b> ${esc(r[1])}</p>`).join('') +
      (d.mass_kg ? `<p class="dim">Weight ${fmt(d.mass_kg)} kg from its materials.</p>` : '') +
      (d.books && d.books.length ? `<p class="dim">Library books it requires: ${d.books.map(esc).join(', ')}</p>` : '');
  }
  // Each auction's card is built ONCE and then only its words and numbers change (Eric 10-12: update in place), so the
  // Bid button under a player's finger is never replaced, typed amounts stay, and "About this design" stays open.
  function card(a) {
    const el = document.createElement('div');
    el.className = 'au'; el.dataset.auc = a.auction_id;
    el.innerHTML = `<h3>${esc(a.name)}</h3><div class="meta" data-f="meta"></div>
      <div class="live" data-f="sched"><span data-f="starts"></span></div>
      <div data-f="running"><div class="live"><span>Copy <span data-f="copy"></span> of ${a.copies} · <span style="font-family:var(--mono)" data-f="serial"></span></span>
        <span data-f="top"></span><span class="clock" data-f="clock"></span><span class="lead" data-f="lead">You have the top bid</span></div>
       <div class="dim" data-f="own">You can't bid on your own design.</div>
       <div class="bidrow" data-f="bidrow"><input type="number" step="1" inputmode="numeric" aria-label="Your bid" data-f="amount">
        <button data-f="bid">Bid</button><span class="dim" data-f="cost"></span></div>
       <div class="aumsg" data-f="msg"></div></div>
      <details><summary>About this design</summary>${design(a.design)}</details>`;
    const inp = el.querySelector('[data-f=amount]');
    inp.addEventListener('input', () => { inp.dataset.typed = '1'; costLine(el); });
    el.querySelector('[data-f=bid]').addEventListener('click', () => placeBid(el));
    return el;
  }
  const f = (el, name) => el.querySelector(`[data-f=${name}]`);
  function setText(node, t) { if (node.textContent !== t) node.textContent = t; }
  function setShown(node, on) { if (node.hidden === on) node.hidden = !on; }
  function costLine(el) {
    const n = Math.floor(Number(f(el, 'amount').value)) || 0;
    setText(f(el, 'cost'), n ? `${fmt(n)} + ${fmt(fee(n))} Starship fee = ${fmt(n + fee(n))} credits set aside` : '');
  }
  function update(el, a) {
    const l = a.lot, running = a.status === 'running' && !!l;
    el.dataset.lot = l ? l.lot_id : '';
    setText(f(el, 'meta'), `Model ${a.model} · ${a.copies} cop${a.copies > 1 ? 'ies' : 'y'} · ${a.sold} sold · floor ${fmt(a.floor)} credits${a.yours ? ' · your design' : ''}`);
    setShown(f(el, 'sched'), !running); setShown(f(el, 'running'), running);
    if (!running) { setText(f(el, 'starts'), 'Starts ' + new Date(a.start_at).toLocaleString()); return; }
    if (el.dataset.shownLot !== String(l.lot_id)) {        // the next copy went up: start its bid box afresh
      el.dataset.shownLot = l.lot_id; delete f(el, 'amount').dataset.typed; setText(f(el, 'msg'), '');
    }
    setText(f(el, 'copy'), String(l.copy)); setText(f(el, 'serial'), l.serial);
    f(el, 'top').innerHTML = l.top_bid ? 'Top bid <b>' + fmt(l.top_bid) + '</b>' : '<span class="dim">No bids yet</span>';
    setShown(f(el, 'lead'), l.you_lead); setShown(f(el, 'own'), a.yours); setShown(f(el, 'bidrow'), !a.yours && !l.you_lead);
    const inp = f(el, 'amount');
    inp.min = l.least;
    // the suggested bid follows the lowest allowed bid, unless the player has typed their own (and it's still enough)
    if (!inp.dataset.typed || Number(inp.value) < l.least) { if (document.activeElement !== inp) { inp.value = l.least; delete inp.dataset.typed; } }
    costLine(el);
    tickClock(el, a);
  }
  function tickClock(el, a) {
    const c = f(el, 'clock'); if (!a.lot) return;
    const s = left(a.lot.closes_at); setText(c, clock(s)); c.classList.toggle('soon', s < 60);
  }
  function render() {
    const list = data.auctions, box = $('auList'), have = new Map([...box.querySelectorAll('.au[data-auc]')].map(el => [el.dataset.auc, el]));
    const empty = box.querySelector('.empty');
    if (!list.length) { have.forEach(el => el.remove()); if (!empty) box.innerHTML = '<p class="dim empty">No blueprint auctions right now. Designers schedule them from their approved designs in the drafting room.</p>'; }
    else if (empty) empty.remove();
    const keep = new Set(list.map(a => String(a.auction_id)));
    have.forEach((el, id) => { if (!keep.has(id)) el.remove(); });     // finished, held or cancelled auctions leave the board
    list.forEach(a => { let el = have.get(String(a.auction_id)); if (!el) { el = card(a); box.appendChild(el); } update(el, a); });
    const mine = data.my_bids.length ? data.my_bids.map(b => `<tr><td>${esc(b.serial)}<div class="dim">${esc(b.name)}</div></td><td class="num">${fmt(b.bid)}</td>
      <td class="${b.status === 'won' || b.status === 'you lead' ? 'up' : b.status === 'outbid' ? 'down' : 'dim'}">${esc(b.status)}</td></tr>`).join('') : '<tr><td class="dim">No bids yet.</td></tr>';
    if ($('auMine').innerHTML !== mine) $('auMine').innerHTML = mine;
    const rec = data.recent.length ? data.recent.map(r => `<tr><td>${esc(r.serial)}<div class="dim">${esc(r.name)}</div></td><td class="num">${fmt(r.price)}</td></tr>`).join('') : '<tr><td class="dim">Nothing sold yet.</td></tr>';
    if ($('auRecent').innerHTML !== rec) $('auRecent').innerHTML = rec;
  }
  async function placeBid(el) {
    const lot = Number(el.dataset.lot), btn = f(el, 'bid'), n = Math.floor(Number(f(el, 'amount').value));
    if (!lot) return;
    btn.disabled = true;
    try { const r = await call('/auctions/bid', { lot_id: lot, amount: n });
      f(el, 'msg').innerHTML = `<span class="up">You have the top bid: ${fmt(r.bid)} + ${fmt(r.fee)} fee set aside. The clock is back to 5 minutes.</span>`;
      delete f(el, 'amount').dataset.typed; }
    catch (err) { f(el, 'msg').innerHTML = `<span class="down">${esc(err.message)}</span>`; }
    btn.disabled = false;
    load();
  }
  // the countdown ticks every second between refreshes
  setInterval(() => { if (view !== 'auctions' || !data) return;
    data.auctions.forEach(a => { const el = document.querySelector(`.au[data-auc="${a.auction_id}"]`); if (el) tickClock(el, a); }); }, 1000);
})();
