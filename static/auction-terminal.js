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
  const msgs = {}, typed = {};
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
  let lastSig = '';
  function render() {
    const list = data.auctions;
    // redraw only when something changed (a bid, a sale, the next copy), so a click never lands on a button being replaced
    const sig = JSON.stringify([list.map(a => [a.auction_id, a.status, a.sold, a.lot && [a.lot.lot_id, a.lot.top_bid, a.lot.you_lead, a.lot.closes_at]]),
      data.my_bids.map(b => [b.serial, b.bid, b.status]), data.recent.length && data.recent[0].serial, Object.values(msgs)]);
    if (sig === lastSig) return;
    lastSig = sig;
    const open = new Set([...document.querySelectorAll('#auList details[open]')].map(d => d.dataset.a));
    if (!list.length) $('auList').innerHTML = '<p class="dim">No blueprint auctions right now. Designers schedule them from their approved designs in the drafting room.</p>';
    else {
      // keep what the player is typing while the list refreshes
      document.querySelectorAll('#auList input[data-lot]').forEach(i => { typed[i.dataset.lot] = i.value; });
      $('auList').innerHTML = list.map(a => {
        const l = a.lot, head = `<h3>${esc(a.name)}</h3><div class="meta">Model ${esc(a.model)} · ${a.copies} cop${a.copies > 1 ? 'ies' : 'y'} · ${a.sold} sold · floor ${fmt(a.floor)} credits${a.yours ? ' · your design' : ''}</div>`;
        if (a.status === 'scheduled' || !l) return `<div class="au">${head}<div class="live"><span>Starts ${esc(new Date(a.start_at).toLocaleString())}</span></div>
          <details data-a="${a.auction_id}"><summary>About this design</summary>${design(a.design)}</details></div>`;
        const s = left(l.closes_at), v = typed[l.lot_id] != null && Number(typed[l.lot_id]) >= l.least ? typed[l.lot_id] : l.least;
        return `<div class="au">${head}
          <div class="live"><span>Copy ${l.copy} of ${a.copies} · <span style="font-family:var(--mono)">${esc(l.serial)}</span></span>
            <span>${l.top_bid ? 'Top bid <b>' + fmt(l.top_bid) + '</b>' : '<span class="dim">No bids yet</span>'}</span>
            <span class="clock ${s < 60 ? 'soon' : ''}">${clock(s)}</span>${l.you_lead ? '<span class="lead">You have the top bid</span>' : ''}</div>
          ${a.yours ? '<div class="dim">You can\'t bid on your own design.</div>' : l.you_lead ? '' : `<div class="bidrow"><input type="number" min="${l.least}" step="1" data-lot="${l.lot_id}" value="${esc(v)}" inputmode="numeric" aria-label="Your bid">
            <button data-bid="${l.lot_id}">Bid</button><span class="dim" data-cost="${l.lot_id}"></span></div>`}
          <div class="aumsg" id="m${l.lot_id}">${msgs[l.lot_id] || ''}</div>
          <details data-a="${a.auction_id}"><summary>About this design</summary>${design(a.design)}</details></div>`;
      }).join('');
      document.querySelectorAll('#auList details[data-a]').forEach(d => { if (open.has(d.dataset.a)) d.open = true; });
      document.querySelectorAll('#auList input[data-lot]').forEach(i => { const c = () => { const n = Math.floor(Number(i.value)) || 0;
        document.querySelector(`[data-cost="${i.dataset.lot}"]`).textContent = n ? `${fmt(n)} + ${fmt(fee(n))} Starship fee = ${fmt(n + fee(n))} credits set aside` : ''; };
        i.addEventListener('input', () => { typed[i.dataset.lot] = i.value; c(); }); c(); });
    }
    $('auMine').innerHTML = data.my_bids.length ? data.my_bids.map(b => `<tr><td>${esc(b.serial)}<div class="dim">${esc(b.name)}</div></td><td class="num">${fmt(b.bid)}</td>
      <td class="${b.status === 'won' || b.status === 'you lead' ? 'up' : b.status === 'outbid' ? 'down' : 'dim'}">${esc(b.status)}</td></tr>`).join('') : '<tr><td class="dim">No bids yet.</td></tr>';
    $('auRecent').innerHTML = data.recent.length ? data.recent.map(r => `<tr><td>${esc(r.serial)}<div class="dim">${esc(r.name)}</div></td><td class="num">${fmt(r.price)}</td></tr>`).join('') : '<tr><td class="dim">Nothing sold yet.</td></tr>';
  }
  $('auList').addEventListener('click', async e => {
    const id = e.target.dataset.bid; if (!id) return;
    const n = Math.floor(Number(document.querySelector(`input[data-lot="${id}"]`).value));
    e.target.disabled = true;
    try { const r = await call('/auctions/bid', { lot_id: +id, amount: n });
      msgs[id] = `<span class="up">You have the top bid: ${fmt(r.bid)} + ${fmt(r.fee)} fee set aside. The clock is back to 5 minutes.</span>`; delete typed[id]; }
    catch (err) { msgs[id] = `<span class="down">${esc(err.message)}</span>`; }
    load();
  });
  // the countdown ticks every second between refreshes
  setInterval(() => { if (view !== 'auctions' || !data) return;
    document.querySelectorAll('#auList .clock').forEach((el, i) => { const a = data.auctions.filter(x => x.status === 'running' && x.lot)[i];
      if (a) { const s = left(a.lot.closes_at); el.textContent = clock(s); el.classList.toggle('soon', s < 60); } }); }, 1000);
})();
