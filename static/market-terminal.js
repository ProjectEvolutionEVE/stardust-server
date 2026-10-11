// STARDUST · MARKET TERMINAL (Eric 10-11, rules 12, 20, 21). Everything here comes from the game server: the board, the
// order book (no names, rule 8), the candles, the player's own orders and trades. Orders go to /api/dfg/market/order.
// Opened from the Market terminal button at the Desk; "Back to my desk" returns there.
'use strict';
(function () {
  const API = '/api/dfg';
  let token = null; try { token = localStorage.getItem('stardust.token'); } catch (e) {}
  const $ = id => document.getElementById(id);
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const fmt = n => n === null || n === undefined ? '—' : Math.round(n).toLocaleString('en-US');
  async function call(path, body) {
    const r = await fetch(API + path, { method: body ? 'POST' : 'GET', headers: { 'Content-Type': 'application/json', Authorization: 'Bearer ' + token },
      body: body ? JSON.stringify(body) : undefined });
    const j = await r.json().catch(() => ({}));
    if (r.status === 401) { location.href = '/play/'; throw new Error('Please sign in.'); }
    if (!r.ok) throw new Error(j.error || 'The market didn\'t answer. Try again in a moment.');
    return j;
  }
  $('back').onclick = () => { if (window.parent !== window) window.parent.postMessage('stardust:closeMarket', location.origin); else location.href = '/play/'; };
  if (!token) { location.href = '/play/'; return; }

  let items = [], sel = 'iron', side = 'buy', type = 'instant', period = 300, book = null, mine = null, firstLoad = true;
  const item = () => items.find(i => i.item === sel) || { name: sel, floor: 1, lot_kg: 1 };
  // minimum orders (Eric 10-11): each item trades in lots, priced per lot; one lot is the smallest order
  const lotName = it => (it.lot_kg || 1) === 1 ? 'kg' : `${fmt(it.lot_kg)} kg lot`;
  const lots = (n, it) => (it.lot_kg || 1) === 1 ? `${fmt(n)} kg` : `${fmt(n)} lot${n === 1 ? '' : 's'} (${fmt(n * it.lot_kg)} kg)`;

  // ---- chart (TradingView Lightweight Charts, Apache 2.0; attribution in the footer) ----
  const LC = window.LightweightCharts;
  const chart = LC.createChart($('chart'), { autoSize: true,
    layout: { background: { type: 'solid', color: '#0b1020' }, textColor: '#7d8aa5' },
    grid: { vertLines: { color: '#131b2e' }, horzLines: { color: '#131b2e' } },
    timeScale: { timeVisible: true, secondsVisible: false, borderColor: '#1d2740' }, rightPriceScale: { borderColor: '#1d2740' } });
  const candles = chart.addSeries(LC.CandlestickSeries, { upColor: '#3fbf8a', downColor: '#e5605a', borderVisible: false,
    wickUpColor: '#3fbf8a', wickDownColor: '#e5605a', priceFormat: { type: 'price', precision: 0, minMove: 1 } });
  const volume = chart.addSeries(LC.HistogramSeries, { priceScaleId: '', priceFormat: { type: 'volume' } });
  volume.priceScale().applyOptions({ scaleMargins: { top: .8, bottom: 0 } });
  let chartKey = '';

  // ---- loading ----
  async function loadBoard() { const j = await call('/market'); items = j.items; renderWatch(); renderHead(); }
  async function loadItem() {
    book = await call('/market/item/' + encodeURIComponent(sel) + '?period=' + period);
    const key = sel + ':' + period;
    candles.setData(book.candles.map(c => ({ time: c.time, open: c.open, high: c.high, low: c.low, close: c.close })));
    volume.setData(book.candles.map(c => ({ time: c.time, value: c.volume, color: c.close >= c.open ? 'rgba(63,191,138,.45)' : 'rgba(229,96,90,.45)' })));
    if (key !== chartKey) { chart.timeScale().fitContent(); chartKey = key; }
    renderBook(); renderTape(); renderTrade();
  }
  async function loadMine() { mine = await call('/market/mine'); renderMine(); renderTrade(); }
  async function refresh() {
    try { await Promise.all([loadBoard(), loadItem(), loadMine()]); if (firstLoad) { firstLoad = false; suggestPrice(); renderTrade(); } }
    catch (e) { say(esc(e.message), true); }
  }

  // ---- screen ----
  function renderWatch() {
    $('wl').innerHTML = items.map(it => {
      const ch = it.change_24h_pct, cls = ch > 0 ? 'up' : ch < 0 ? 'down' : 'dim';
      return `<tr data-id="${esc(it.item)}" class="${it.item === sel ? 'sel' : ''}"><td><span class="nm">${esc(it.name)}</span><br>
        <span class="u">per ${esc(lotName(it))} · floor ${fmt(it.floor)}</span></td><td class="num">${fmt(it.last)}<br><span class="${cls}">${ch >= 0 ? '+' : ''}${ch.toFixed(2)}%</span></td>
        <td class="num"><span class="up">${fmt(it.bid)}</span><br><span class="down">${fmt(it.ask)}</span></td></tr>`;
    }).join('');
  }
  function renderHead() {
    const it = item(), ch = it.change_24h_pct || 0;
    $('chartHead').innerHTML = `<span class="nm">${esc(it.name)}</span><span class="big ${ch >= 0 ? 'up' : 'down'}">${fmt(it.last)}</span>
      <span class="${ch >= 0 ? 'up' : 'down'}">${ch >= 0 ? '+' : ''}${ch.toFixed(2)}% in 24 h</span>
      <span class="dim">per ${esc(lotName(it))} · Bid <b class="up">${fmt(it.bid)}</b> · Ask <b class="down">${fmt(it.ask)}</b> · ${lots(it.volume_24h || 0, it)} traded in 24 h · floor ${fmt(it.floor)}</span>`;
  }
  function renderBook() {
    if (!book) return;
    const max = Math.max(1, ...book.asks.map(l => l.qty), ...book.bids.map(l => l.qty));
    const mineAt = new Set((mine ? mine.orders : []).filter(o => o.item === sel).map(o => o.side + o.price));
    const row = (l, cls, s) => `<tr class="${cls}" data-p="${l.price}"><td>${fmt(l.price)}${mineAt.has(s + l.price) ? ' <span class="dim">•you</span>' : ''}</td>
      <td class="num">${fmt(l.qty)}<span class="bar" style="width:${(l.qty / max * 100).toFixed(1)}%"></span></td></tr>`;
    const asks = book.asks.slice().reverse().map(l => row(l, 'ask', 'sell')).join('') ||
      '<tr><td colspan="2" class="dim" style="cursor:default">Nothing for sale right now</td></tr>';
    const bids = book.bids.map(l => row(l, 'bid', 'buy')).join('') || '<tr><td colspan="2" class="dim" style="cursor:default">No bids</td></tr>';
    const it = item(), spread = book.bids.length && book.asks.length ? 'spread ' + fmt(book.asks[0].price - book.bids[0].price) : '';
    $('book').innerHTML = `<tr><td class="dim" style="cursor:default">PRICE / ${esc(lotName(item()).toUpperCase())}</td><td class="num dim">${(item().lot_kg || 1) === 1 ? 'KG' : 'LOTS'}</td></tr>` + asks +
      `<tr class="mid"><td>Last <b>${fmt(it.last)}</b></td><td class="num dim">${spread}</td></tr>` + bids;
  }
  function renderTape() {
    if (!book) return;
    $('tape').innerHTML = book.trades.slice(0, 14).map(t => `<tr><td class="dim">${new Date(t.at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' })}</td>
      <td class="num ${t.side === 'buy' ? 'up' : 'down'}">${fmt(t.price)}</td><td class="num">${lots(t.qty, item())}</td></tr>`).join('') ||
      '<tr><td class="dim">No trades yet.</td></tr>';
  }
  function renderMine() {
    if (!mine) return;
    const info = code => items.find(i => i.item === code) || { name: code, lot_kg: 1 }, name = code => info(code).name;
    const rows = [`<tr><td>Credits</td><td class="num">${fmt(mine.credits)}${mine.credits_set_aside ? `<br><span class="dim">+${fmt(mine.credits_set_aside)} set aside</span>` : ''}</td><td></td></tr>`];
    Object.entries(mine.holdings).forEach(([code, h]) => { if (h.kg >= 1) rows.push(`<tr><td>${esc(name(code))}</td><td class="num">${fmt(h.kg)} kg${info(code).lot_kg > 1 ? `<br><span class="dim">${fmt(h.lots)} lot${h.lots === 1 ? '' : 's'} to trade</span>` : ''}</td><td></td></tr>`); });
    if (mine.orders.length) rows.push('<tr><td colspan="3" class="dim" style="padding-top:10px">OPEN ORDERS</td></tr>');
    mine.orders.forEach(o => rows.push(`<tr><td><span class="${o.side === 'buy' ? 'up' : 'down'}">${o.side === 'buy' ? 'Bid' : 'Ask'}</span> ${esc(name(o.item))}</td>
      <td class="num">${lots(o.remaining, info(o.item))} @ ${fmt(o.price)}</td><td class="num"><button data-cancel="${o.id}">Cancel</button></td></tr>`));
    $('mineT').innerHTML = rows.join('');
    $('wCredits').textContent = fmt(mine.credits); $('wHeld').textContent = mine.credits_set_aside ? `(+${fmt(mine.credits_set_aside)} set aside)` : '';
    $('hist').innerHTML = mine.trades.slice(0, 12).map(t => `<tr><td class="dim">${new Date(t.at).toLocaleString([], { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' })}</td>
      <td class="${t.side === 'buy' ? 'up' : 'down'}">${t.side === 'buy' ? 'Bought' : 'Sold'}</td><td>${esc(name(t.item))}</td>
      <td class="num">${lots(t.qty, info(t.item))} @ ${fmt(t.price)}</td></tr>`).join('') || '<tr><td class="dim">No trades yet.</td></tr>';
  }
  // what Buy now / Sell now would do with the book as it stands
  function preview(n) {
    const opp = side === 'buy' ? book.asks : book.bids; let left = n, got = 0, cost = 0, cash = side === 'buy' ? (mine ? mine.credits : 0) : Infinity;
    for (const l of opp) { if (!left) break; let q = Math.min(left, l.qty); if (side === 'buy') q = Math.min(q, Math.floor(cash / l.price)); if (q <= 0) break;
      left -= q; got += q; cost += q * l.price; cash -= q * l.price; }
    return { got, cost, unfilled: n - got };
  }
  function renderTrade() {
    const it = item();
    document.querySelectorAll('#sideSeg button').forEach(b => b.classList.toggle('on', b.dataset.v === side));
    document.querySelectorAll('#typeSeg button').forEach(b => b.classList.toggle('on', b.dataset.v === type));
    $('price').disabled = type === 'instant';
    $('go').textContent = (side === 'buy' ? 'BUY ' : 'SELL ') + it.name.toUpperCase() + (type === 'instant' ? ' NOW' : '');
    $('go').className = side;
    const n = parseInt($('qty').value, 10) || 0, p = parseInt($('price').value, 10) || 0;
    const h = mine && mine.holdings[sel] ? mine.holdings[sel] : { lots: 0, kg: 0 };
    $('qtyLbl').textContent = (it.lot_kg || 1) === 1 ? 'QUANTITY (kg)' : `QUANTITY (lots of ${fmt(it.lot_kg)} kg)`;
    $('priceLbl').textContent = `PRICE (credits per ${lotName(it)})`;
    let t = side === 'sell' ? `You have ${fmt(h.kg)} kg in your cargo hold${(it.lot_kg || 1) > 1 ? `: ${lots(h.lots, it)} to sell. The smallest order is one lot` : ''}. ` : ((it.lot_kg || 1) > 1 ? `Sold in lots of ${fmt(it.lot_kg)} kg; one lot is the smallest order. ` : '');
    if (!book) t += '';
    else if (type === 'instant') {
      const pv = preview(n);
      if (!n) t += 'Enter how many.';
      else if (!pv.got) t += side === 'buy' ? 'Nothing you can buy right now: no one is selling, or not enough credits.' : 'No bids right now. Set your price and wait for a buyer.';
      else t += `${side === 'buy' ? 'Buys' : 'Sells'} ${lots(pv.got, it)} now at an average of ${fmt(pv.cost / pv.got)} each, ${fmt(pv.cost)} credits in all.` +
        (pv.unfilled ? ` <b>${lots(pv.unfilled, it)} can't be filled</b> right now.` : '');
    } else {
      if (!n || !p) t += 'Enter your price and how many.';
      else if (p < it.floor) t += `<b>The floor for ${esc(it.name)} is ${fmt(it.floor)}.</b> Nothing trades below it.`;
      else if (side === 'buy') t += `Your bid waits in the queue at ${fmt(p)} until a seller meets it. ${fmt(n * p)} credits are set aside now; anything that fills cheaper gives the difference back.`;
      else t += `Your ask waits in the queue at ${fmt(p)} until a buyer meets it. ${lots(n, it)} set aside until it sells or you cancel.`;
    }
    $('explain').innerHTML = t;
  }
  function suggestPrice() { $('qty').value = 1; const it = item(); $('price').value = (side === 'buy' ? (it.bid || it.last) : (it.ask || it.last)) || it.floor; }
  function say(t, bad) { $('msg').innerHTML = t; $('msg').className = bad ? 'down' : 'up'; }

  // ---- input ----
  $('wl').addEventListener('click', e => { const tr = e.target.closest('tr[data-id]'); if (!tr) return;
    sel = tr.dataset.id; renderWatch(); renderHead(); suggestPrice(); loadItem().catch(err => say(esc(err.message), true)); });
  $('book').addEventListener('click', e => { const tr = e.target.closest('tr[data-p]'); if (!tr) return; $('price').value = tr.dataset.p; type = 'limit'; renderTrade(); });
  $('sideSeg').addEventListener('click', e => { if (!e.target.dataset.v) return; side = e.target.dataset.v; suggestPrice(); renderTrade(); });
  $('typeSeg').addEventListener('click', e => { if (!e.target.dataset.v) return; type = e.target.dataset.v; renderTrade(); });
  $('per').addEventListener('click', e => { const p = +e.target.dataset.p; if (!p) return; period = p;
    document.querySelectorAll('#per button').forEach(b => b.classList.toggle('on', +b.dataset.p === p)); loadItem().catch(() => {}); });
  ['price', 'qty'].forEach(id => $(id).addEventListener('input', renderTrade));
  $('mineT').addEventListener('click', async e => { const id = e.target.dataset.cancel; if (!id) return;
    try { await call('/market/cancel', { order_id: +id }); say('Order cancelled. What it set aside is back with you.'); } catch (err) { say(esc(err.message), true); }
    refresh(); });
  $('go').addEventListener('click', async () => {
    const it = item(), qty = parseInt($('qty').value, 10), price = parseInt($('price').value, 10);
    $('go').disabled = true;
    try {
      const r = await call('/market/order', { item: sel, side, type, qty, price: type === 'limit' ? price : undefined });
      const got = r.fills.reduce((n, f) => n + f.qty, 0), total = r.fills.reduce((n, f) => n + f.qty * f.price, 0);
      let t = got ? `${side === 'buy' ? 'Bought' : 'Sold'} ${lots(got, it)} of ${esc(it.name.toLowerCase())} at an average of ${fmt(total / got)} each (${fmt(total)} credits).` : '';
      if (r.order.status === 'open') t += ` ${lots(r.order.remaining, it)} waiting in the queue at ${fmt(price)}.`;
      if (r.unfilled) t += ` ${lots(r.unfilled, it)} couldn't be filled.`;
      if (r.receipt) t += ` Receipt ${esc(r.receipt.code)} is in your filing cabinet.`;
      say(t.trim() || 'Nothing filled.', !got && r.order.status !== 'open');
    } catch (err) { say(esc(err.message), true); }
    $('go').disabled = false; refresh();
  });

  refresh(); setInterval(refresh, 4000);
})();
