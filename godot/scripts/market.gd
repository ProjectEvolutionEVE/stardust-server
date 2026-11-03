extends Control
## The Market terminal (rules 12, 20, 21), reached from the Desk only. Ported from the browser game's market.html,
## market-terminal.js and auction-terminal.js: the ore order book (best bid and ask, the chart, Buy now / Sell now and
## limit orders, the player's open orders and trades) and the Blueprint auctions tab. Nobody on the other side of a trade
## or a bid is ever named (rule 8). Prices are whole credits per lot; one lot is the smallest order.

const UP := Color("3fbf8a")
const DOWN := Color("e5605a")
const PERIODS := [[60, "1 min"], [300, "5 min"], [900, "15 min"], [3600, "1 hour"]]

var items: Array = []
var groups: Array = []     # the colour chart (Eric 11-03): kinds of component, each with its colour
var filter := ""           # "" every item, "ore" the raw ores, or a kind of component
var filter_box: HFlowContainer
var sel := "iron"
var side := "buy"
var type := "instant"
var period := 300
var book: Dictionary = {}
var mine: Dictionary = {}
var first_load := true
var inflight := 0          # requests still out; leaving waits for them so none returns to a freed screen
var refreshing := false
var leaving := false

var wallet: Label
var view_seg: HBoxContainer
var ore_page: VBoxContainer
var au_page: VBoxContainer
var picker: WheelPicker
var board_toggle: Button
var board_box: VBoxContainer
var head_name: Label
var head_price: Label
var head_info: Label
var period_seg: HBoxContainer
var chart: Chart
var side_seg: HBoxContainer
var type_seg: HBoxContainer
var price_lbl: Label
var price_in: LineEdit
var qty_lbl: Label
var qty_in: LineEdit
var explain: Label
var go: Button
var msg: Label
var to_library: Button
var book_box: VBoxContainer
var mine_box: VBoxContainer
var hist_box: VBoxContainer
var tape_box: VBoxContainer

var au_data: Dictionary = {}
var au_skew := 0.0
var au_cards := {}         # auction_id -> {root, parts…}
var au_list: VBoxContainer
var au_empty: Label
var au_mine: VBoxContainer
var au_recent: VBoxContainer


func _ready() -> void:
	var outer := Ui.screen(self)
	var top := HBoxContainer.new()
	var title := Ui.label("Starship Market", 40, Ui.GOLD)
	title.autowrap_mode = TextServer.AUTOWRAP_OFF
	title.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	top.add_child(title)
	var back := Ui.button("Back to my desk", false)
	back.custom_minimum_size = Vector2(220, 56)
	back.size_flags_vertical = Control.SIZE_SHRINK_CENTER
	back.add_theme_font_size_override("font_size", 22)
	back.pressed.connect(_leave)
	top.add_child(back)
	outer.add_child(top)
	outer.add_child(Ui.label("WSC Alexander von Humboldt · Market terminal", 20, Ui.MUTED))
	view_seg = _seg([["ore", "Ore market"], ["auctions", "Blueprint auctions"]], _show_view)
	outer.add_child(view_seg)
	wallet = Ui.label("● OPEN 24/7   ·   Credits …", 24)
	outer.add_child(wallet)
	var scroll := ScrollContainer.new()
	scroll.size_flags_vertical = Control.SIZE_EXPAND_FILL
	scroll.horizontal_scroll_mode = ScrollContainer.SCROLL_MODE_DISABLED
	outer.add_child(scroll)
	var pad := MarginContainer.new()          # keeps the right-hand numbers clear of the scroll bar
	pad.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	pad.add_theme_constant_override("margin_right", 16)
	scroll.add_child(pad)
	var pages := VBoxContainer.new()
	pages.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	pad.add_child(pages)
	ore_page = _page()
	pages.add_child(ore_page)
	au_page = _page()
	pages.add_child(au_page)
	_build_ore()
	_build_auctions()
	_show_view("ore")
	var t := Timer.new()
	t.wait_time = 4.0
	t.autostart = true
	t.timeout.connect(func(): if ore_page.visible: _refresh())
	add_child(t)
	var t2 := Timer.new()
	t2.wait_time = 2.0
	t2.autostart = true
	t2.timeout.connect(func(): if au_page.visible: _au_load())
	add_child(t2)
	var t3 := Timer.new()
	t3.wait_time = 1.0
	t3.autostart = true
	t3.timeout.connect(_au_tick)
	add_child(t3)
	_refresh()


func _page() -> VBoxContainer:
	var v := VBoxContainer.new()
	v.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	v.add_theme_constant_override("separation", 12)
	return v


func _leave() -> void:
	leaving = true
	for c in get_children():
		if c is Timer:
			c.stop()
	while inflight > 0:
		await get_tree().process_frame
	Session.quarters_tab = "Desk"
	get_tree().change_scene_to_file("res://scenes/quarters.tscn")


func _api(method: String, path: String, b: Dictionary = {}) -> Dictionary:
	inflight += 1
	var r := await Api.call_api(method, path, b)
	inflight -= 1
	return r


func _show_view(v: String) -> void:
	_seg_set(view_seg, v)
	ore_page.visible = v == "ore"
	au_page.visible = v == "auctions"
	if v == "auctions":
		_au_load()


# ── small builders ──

func _heading(t: String) -> Label:
	return Ui.label(t, 26, Ui.GOLD)


func _seg(opts: Array, on_pick: Callable) -> HBoxContainer:
	var h := HBoxContainer.new()
	h.add_theme_constant_override("separation", 8)
	for o in opts:
		var b := Button.new()
		b.text = tr(o[1])
		b.set_meta("v", o[0])
		b.size_flags_horizontal = Control.SIZE_EXPAND_FILL
		b.custom_minimum_size = Vector2(0, 56)
		b.add_theme_font_size_override("font_size", 22)
		b.pressed.connect(func(): on_pick.call(o[0]))
		h.add_child(b)
	return h


func _seg_set(h: HBoxContainer, v: Variant) -> void:
	for b in h.get_children():
		_paint(b, b.get_meta("v") == v)


func _paint(b: Button, on: bool, edge := Ui.GOLD) -> void:
	var s := StyleBoxFlat.new()
	s.bg_color = edge if on else Ui.PANEL
	s.border_color = edge
	s.set_border_width_all(2)
	s.set_corner_radius_all(12)
	for st in ["normal", "hover", "pressed", "focus", "disabled"]:
		b.add_theme_stylebox_override(st, s)
	for c in ["font_color", "font_hover_color", "font_pressed_color", "font_focus_color"]:
		b.add_theme_color_override(c, Ui.BG if on else edge)


func _row(cells: Array, colors: Array = []) -> HBoxContainer:
	var h := HBoxContainer.new()
	h.add_theme_constant_override("separation", 10)
	for i in cells.size():
		var l := Ui.label(str(cells[i]), 22, colors[i] if i < colors.size() and colors[i] != null else Ui.TEXT)
		if i == 0:
			l.size_flags_horizontal = Control.SIZE_EXPAND_FILL
		else:
			l.autowrap_mode = TextServer.AUTOWRAP_OFF
			l.horizontal_alignment = HORIZONTAL_ALIGNMENT_RIGHT
		h.add_child(l)
	return h


func _clear(box: Node) -> void:
	for c in box.get_children():
		c.queue_free()


# ── ore market ──

func item() -> Dictionary:
	for i in items:
		if i.item == sel:
			return i
	return {"item": sel, "name": sel, "floor": 1, "lot_kg": 1.0}


func _info(code: String) -> Dictionary:
	for i in items:
		if i.item == code:
			return i
	return {"name": code, "lot_kg": 1.0}


func _lot_kg(it: Dictionary) -> float:
	return float(it.get("lot_kg", 1.0))


## "kg" or "100 kg lot": what one price is for.
func _lot_name(it: Dictionary) -> String:
	return tr("kg") if _lot_kg(it) == 1.0 else tr("%s kg lot") % Ui.num(_lot_kg(it))


func _lots(n: Variant, it: Dictionary) -> String:
	var q := int(n)
	if _lot_kg(it) == 1.0:
		return tr("%s kg") % Ui.num(q)
	return (tr("%s lot (%s kg)") if q == 1 else tr("%s lots (%s kg)")) % [Ui.num(q), Ui.num(q * _lot_kg(it))]


func _build_ore() -> void:
	var p := ore_page
	p.add_child(Ui.label("The Starship bank trades on this market too. It always has a bid, so you can sell even when no other player is buying.", 22, Ui.MUTED))
	p.add_child(_heading("Market board"))
	filter_box = HFlowContainer.new()
	filter_box.add_theme_constant_override("h_separation", 8)
	filter_box.add_theme_constant_override("v_separation", 8)
	p.add_child(filter_box)
	picker = Ui.picker()
	picker.item_selected.connect(func(i): _pick(str(picker.get_item_metadata(i))))
	p.add_child(picker)
	board_toggle = Ui.button("▸ " + tr("All prices"), false)
	board_toggle.custom_minimum_size = Vector2(0, 56)
	board_toggle.add_theme_font_size_override("font_size", 22)
	board_toggle.pressed.connect(func():
		board_box.visible = not board_box.visible
		board_toggle.text = ("▾ " if board_box.visible else "▸ ") + tr("All prices")
		_render_board())
	p.add_child(board_toggle)
	board_box = VBoxContainer.new()
	board_box.visible = false
	p.add_child(board_box)
	head_name = Ui.label("…", 30, Ui.GOLD)
	p.add_child(head_name)
	head_price = Ui.label("", 34)
	p.add_child(head_price)
	head_info = Ui.label("", 22, Ui.MUTED)
	p.add_child(head_info)
	var per := HBoxContainer.new()
	var cl := Ui.label("Candles:", 22, Ui.MUTED)
	cl.autowrap_mode = TextServer.AUTOWRAP_OFF
	cl.size_flags_vertical = Control.SIZE_SHRINK_CENTER
	per.add_child(cl)
	period_seg = _seg(PERIODS, func(v):
		period = v
		_seg_set(period_seg, v)
		_load_item())
	period_seg.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	per.add_child(period_seg)
	_seg_set(period_seg, period)
	p.add_child(per)
	chart = Chart.new()
	chart.custom_minimum_size = Vector2(0, 380)
	p.add_child(chart)

	p.add_child(_heading("Trade"))
	side_seg = _seg([["buy", "BUY"], ["sell", "SELL"]], func(v):
		side = v
		_suggest_price()
		_render_trade())
	p.add_child(side_seg)
	type_seg = _seg([["instant", "BUY / SELL NOW"], ["limit", "SET MY PRICE"]], func(v):
		type = v
		_render_trade())
	p.add_child(type_seg)
	price_lbl = Ui.label("PRICE", 20, Ui.MUTED)
	p.add_child(price_lbl)
	price_in = Ui.field("Credits")
	price_in.text_changed.connect(func(_t): _render_trade())
	p.add_child(price_in)
	qty_lbl = Ui.label("QUANTITY", 20, Ui.MUTED)
	p.add_child(qty_lbl)
	qty_in = Ui.field("How many")
	qty_in.text_changed.connect(func(_t): _render_trade())
	p.add_child(qty_in)
	explain = Ui.label("", 22, Ui.MUTED)
	p.add_child(explain)
	go = Ui.button("BUY")
	go.pressed.connect(_place)
	p.add_child(go)
	msg = Ui.label("", 22)
	p.add_child(msg)
	to_library = Ui.button("Go to the Library", false)   # selling is learned there first (Eric 10-23)
	to_library.visible = false
	to_library.pressed.connect(func(): _go_library())
	p.add_child(to_library)

	p.add_child(_heading("Order book"))
	p.add_child(Ui.label("Tap a price to use it. The book never shows who is trading.", 20, Ui.MUTED))
	book_box = VBoxContainer.new()
	p.add_child(book_box)
	p.add_child(_heading("Your cargo & open orders"))
	mine_box = VBoxContainer.new()
	mine_box.add_theme_constant_override("separation", 8)
	p.add_child(mine_box)
	p.add_child(_heading("Your trade history"))
	hist_box = VBoxContainer.new()
	p.add_child(hist_box)
	p.add_child(_heading("Recent trades"))
	tape_box = VBoxContainer.new()
	p.add_child(tape_box)
	p.add_child(Ui.label("Minerals trade in lots (bulk rock, ice and ores 100 kg; valuable ores and most shock minerals 10 kg; native metals, diamond and the rarest minerals 1 kg; each item shows its lot); one lot is the smallest order, and prices are per lot. Every item has a floor price; nothing trades below it. Every trade gives you a receipt (filing cabinet, in your quarters).", 18, Ui.MUTED))
	_render_trade()


func _go_library() -> void:
	leaving = true
	while inflight > 0:
		await get_tree().process_frame
	get_tree().change_scene_to_file("res://scenes/library.tscn")


func _refresh() -> void:
	if refreshing or leaving:
		return
	refreshing = true
	await _load_board()
	await _load_item()
	await _load_mine()
	if first_load and not items.is_empty():
		first_load = false
		_suggest_price()
		_render_trade()
	refreshing = false


func _load_board() -> void:
	var r := await _api("GET", "/api/dfg/market")
	if leaving:
		return
	if not r.ok:
		_say(r.error, true)
		return
	items = r.data.get("items", [])
	if groups.is_empty():
		groups = r.data.get("groups", [])
		_render_filters()
	_fill_picker()
	_render_board()
	_render_head()


## Only the items the filter shows: all, the raw ores, or one kind of component (refined goods, by their colour).
func _shown() -> Array:
	var out: Array = []
	for it in items:
		if filter == "" or (filter == "ore" and not it.get("refined", false)) or filter in it.get("groups", []):
			out.append(it)
	return out


func _fill_picker() -> void:
	var shown := _shown()
	var same := picker.item_count == shown.size()
	for i in min(picker.item_count, shown.size()):
		same = same and str(picker.get_item_metadata(i)) == shown[i].item
	if not same:
		picker.clear()
		for i in shown.size():
			picker.add_item(shown[i].name)
			picker.set_item_metadata(i, shown[i].item)
	for i in shown.size():
		if shown[i].item == sel:
			picker.select(i)


func _render_filters() -> void:
	for c in filter_box.get_children():
		c.queue_free()
	var opts := [["", tr("All"), null], ["ore", tr("Raw ores"), null]]
	for g in groups:
		opts.append([g.code, g.name, g.color])
	for o in opts:
		var b := Button.new()
		b.text = o[1]
		b.custom_minimum_size = Vector2(0, 52)
		b.add_theme_font_size_override("font_size", 20)
		if o[2] != null:
			b.icon = _dot(str(o[2]))
		_paint(b, filter == o[0], Color(str(o[2])) if o[2] != null else Ui.GOLD)
		for st in ["normal", "hover", "pressed", "focus"]:
			(b.get_theme_stylebox(st) as StyleBoxFlat).content_margin_left = 12
			(b.get_theme_stylebox(st) as StyleBoxFlat).content_margin_right = 14
		b.pressed.connect(func():
			filter = o[0]
			_render_filters()
			_fill_picker()
			var shown := _shown()
			var has_sel := false
			for it in shown:
				has_sel = has_sel or it.item == sel
			if not shown.is_empty() and not has_sel:
				_pick(shown[0].item)
			_render_board())
		filter_box.add_child(b)


## A small colour square for a button.
func _dot(hex: String) -> ImageTexture:
	var img := Image.create(22, 22, false, Image.FORMAT_RGBA8)
	img.fill(Color(hex))
	return ImageTexture.create_from_image(img)


func _load_item() -> void:
	var r := await _api("GET", "/api/dfg/market/item/" + sel.uri_encode() + "?period=" + str(period))
	if leaving or not r.ok:
		return
	book = r.data
	chart.set_candles(book.get("candles", []))
	_render_book()
	_render_tape()
	_render_trade()


func _load_mine() -> void:
	var r := await _api("GET", "/api/dfg/market/mine")
	if leaving or not r.ok:
		return
	mine = r.data
	_render_mine()
	_render_trade()


func _pick(code: String) -> void:
	sel = code
	book = {}
	_render_board()
	_render_head()
	_suggest_price()
	_render_trade()
	await _load_item()


func _render_board() -> void:
	if not board_box.visible:
		return
	_clear(board_box)
	var colour := {}
	for g in groups:
		colour[g.code] = g.color
	for it in _shown():
		var ch := float(it.get("change_24h_pct", 0))
		var b := Button.new()
		if not it.get("groups", []).is_empty():
			b.icon = _dot(colour.get(it.groups[0], "8a94a6"))
		b.flat = true
		b.alignment = HORIZONTAL_ALIGNMENT_LEFT
		b.add_theme_font_size_override("font_size", 20)
		b.text = tr("%s%s   %s (%s%.2f%%)   bid %s · ask %s") % ["▶ " if it.item == sel else "", it.name, Ui.num(it.last),
			"+" if ch >= 0 else "", ch, Ui.num(it.bid), Ui.num(it.ask)]
		var col: Color = Ui.GOLD if it.item == sel else Ui.TEXT
		for c in ["font_color", "font_hover_color", "font_pressed_color", "font_focus_color"]:
			b.add_theme_color_override(c, col)
		b.pressed.connect(func(): _pick(it.item))
		board_box.add_child(b)


func _render_head() -> void:
	var it := item()
	var ch := float(it.get("change_24h_pct", 0))
	head_name.text = str(it.name)
	head_price.text = tr("%s   %s%.2f%% in 24 h") % [Ui.num(it.get("last")), "+" if ch >= 0 else "", ch]
	head_price.add_theme_color_override("font_color", UP if ch >= 0 else DOWN)
	head_info.text = tr("per %s · Bid %s · Ask %s · %s traded in 24 h · floor %s") % [_lot_name(it), Ui.num(it.get("bid")),
		Ui.num(it.get("ask")), _lots(it.get("volume_24h", 0), it), Ui.num(it.get("floor"))]


func _render_book() -> void:
	_clear(book_box)
	if book.is_empty():
		return
	var it := item()
	var mine_at := {}
	for o in mine.get("orders", []):
		if o.item == sel:
			mine_at[o.side + str(int(o.price))] = true
	book_box.add_child(_row([tr("PRICE / %s") % _lot_name(it).to_upper(), tr("KG") if _lot_kg(it) == 1.0 else tr("LOTS")], [Ui.MUTED, Ui.MUTED]))
	var asks: Array = book.get("asks", []).duplicate()
	asks.reverse()
	if asks.is_empty():
		book_box.add_child(Ui.label(tr("Nothing for sale right now"), 22, Ui.MUTED))
	for l in asks:
		book_box.add_child(_level(l, DOWN, mine_at.has("sell" + str(int(l.price)))))
	var bids: Array = book.get("bids", [])
	var spread := ""
	if not bids.is_empty() and not book.asks.is_empty():
		spread = tr("spread %s") % Ui.num(float(book.asks[0].price) - float(bids[0].price))
	book_box.add_child(_row([tr("Last %s") % Ui.num(it.get("last")), spread], [Ui.GOLD, Ui.MUTED]))
	if bids.is_empty():
		book_box.add_child(Ui.label(tr("No bids"), 22, Ui.MUTED))
	for l in bids:
		book_box.add_child(_level(l, UP, mine_at.has("buy" + str(int(l.price)))))


## One price level of the book: tap it to use that price for your own order.
func _level(l: Dictionary, col: Color, yours: bool) -> Button:
	var b := Button.new()
	b.flat = true
	b.custom_minimum_size = Vector2(0, 44)
	var r := _row([(tr("%s   • you") % Ui.num(l.price)) if yours else Ui.num(l.price), Ui.num(l.qty)], [col, col])
	r.set_anchors_preset(Control.PRESET_FULL_RECT)
	r.mouse_filter = Control.MOUSE_FILTER_IGNORE
	for c in r.get_children():
		c.mouse_filter = Control.MOUSE_FILTER_IGNORE
	b.add_child(r)
	b.pressed.connect(func():
		price_in.text = str(int(l.price))
		type = "limit"
		_render_trade())
	return b


func _render_tape() -> void:
	_clear(tape_box)
	var trs: Array = book.get("trades", [])
	if trs.is_empty():
		tape_box.add_child(Ui.label(tr("No trades yet."), 22, Ui.MUTED))
	for t in trs.slice(0, 14):
		tape_box.add_child(_row([Ui.when(t.at), Ui.num(t.price), _lots(t.qty, item())],
			[Ui.MUTED, UP if t.side == "buy" else DOWN, Ui.TEXT]))


func _render_mine() -> void:
	_clear(mine_box)
	var c := Ui.num(mine.get("credits"))
	var held := int(mine.get("credits_set_aside", 0))
	wallet.text = tr("● OPEN 24/7   ·   Credits %s") % c + (("  " + tr("(+%s set aside)") % Ui.num(held)) if held else "")
	mine_box.add_child(_row([tr("Credits"), c + (("\n" + tr("+%s set aside") % Ui.num(held)) if held else "")]))
	var hold: Dictionary = mine.get("holdings", {})
	for code in hold:
		var h: Dictionary = hold[code]
		if float(h.kg) >= 1:
			var t := Ui.num(h.kg) + " kg"
			if _lot_kg(_info(code)) > 1:
				t += "\n" + (tr("%s lot to trade") if int(h.lots) == 1 else tr("%s lots to trade")) % Ui.num(h.lots)
			mine_box.add_child(_row([_info(code).name, t]))
	var orders: Array = mine.get("orders", [])
	if not orders.is_empty():
		mine_box.add_child(Ui.label(tr("OPEN ORDERS"), 20, Ui.MUTED))
	for o in orders:
		var h := HBoxContainer.new()
		var l := Ui.label((tr("Bid %s") if o.side == "buy" else tr("Ask %s")) % _info(o.item).name + "\n" + tr("%s @ %s") % [_lots(o.remaining, _info(o.item)), Ui.num(o.price)], 22,
			UP if o.side == "buy" else DOWN)
		l.size_flags_horizontal = Control.SIZE_EXPAND_FILL
		h.add_child(l)
		var x := Ui.button("Cancel", false)
		x.custom_minimum_size = Vector2(140, 56)
		x.size_flags_vertical = Control.SIZE_SHRINK_CENTER
		x.add_theme_font_size_override("font_size", 22)
		x.pressed.connect(_cancel.bind(int(o.id), x))
		h.add_child(x)
		mine_box.add_child(h)
	_clear(hist_box)
	var trs: Array = mine.get("trades", [])
	if trs.is_empty():
		hist_box.add_child(Ui.label(tr("No trades yet."), 22, Ui.MUTED))
	for t in trs.slice(0, 12):
		hist_box.add_child(_row([Ui.when(t.at, "short") + "  " + (tr("Bought %s") if t.side == "buy" else tr("Sold %s")) % _info(t.item).name,
			tr("%s @ %s") % [_lots(t.qty, _info(t.item)), Ui.num(t.price)]], [UP if t.side == "buy" else DOWN, Ui.TEXT]))
	_render_book()


func _cancel(id: int, btn: Button) -> void:
	btn.disabled = true
	var r := await _api("POST", "/api/dfg/market/cancel", {"order_id": id})
	if leaving:
		return
	_say(tr("Order cancelled. What it set aside is back with you.") if r.ok else r.error, not r.ok)
	refreshing = false
	_refresh()


## What Buy now / Sell now would do with the book as it stands.
func _preview(n: int) -> Dictionary:
	var opp: Array = book.get("asks" if side == "buy" else "bids", [])
	var left := n
	var got := 0
	var cost := 0
	var cash: float = float(mine.get("credits", 0)) if side == "buy" else INF
	for l in opp:
		if left == 0:
			break
		var pr := int(l.price)
		var q := mini(left, int(l.qty))
		if side == "buy":
			q = mini(q, int(floor(cash / pr)))
		if q <= 0:
			break
		left -= q
		got += q
		cost += q * pr
		cash -= q * pr
	return {"got": got, "cost": cost, "unfilled": n - got}


func _render_trade() -> void:
	if go == null:
		return
	var it := item()
	_seg_set(side_seg, side)
	_seg_set(type_seg, type)
	price_in.editable = type == "limit"
	go.text = ((tr("BUY %s NOW") if type == "instant" else tr("BUY %s")) if side == "buy" else (tr("SELL %s NOW") if type == "instant" else tr("SELL %s"))) % str(it.name).to_upper()
	_paint(go, true, UP if side == "buy" else DOWN)
	go.custom_minimum_size = Vector2(0, 76)
	var n := qty_in.text.to_int()
	var p := price_in.text.to_int()
	var hold: Dictionary = mine.get("holdings", {}).get(sel, {"lots": 0, "kg": 0})
	qty_lbl.text = tr("QUANTITY (kg)") if _lot_kg(it) == 1.0 else tr("QUANTITY (lots of %s kg)") % Ui.num(_lot_kg(it))
	price_lbl.text = tr("PRICE (credits per %s)") % _lot_name(it)
	var t := ""
	if side == "sell":
		if _lot_kg(it) > 1:
			t = tr("You have %s kg in your cargo hold: %s to sell. The smallest order is one lot.") % [Ui.num(hold.kg), _lots(hold.lots, it)]
		else:
			t = tr("You have %s kg in your cargo hold.") % Ui.num(hold.kg)
		t += " "
	elif _lot_kg(it) > 1:
		t = tr("Sold in lots of %s kg; one lot is the smallest order.") % Ui.num(_lot_kg(it)) + " "
	if book.is_empty():
		pass
	elif type == "instant":
		var pv := _preview(n)
		if n <= 0:
			t += tr("Enter how many.")
		elif pv.got == 0:
			t += tr("Nothing you can buy right now: no one is selling, or not enough credits.") if side == "buy" else tr("No bids right now. Set your price and wait for a buyer.")
		else:
			t += (tr("Buys %s now at an average of %s each, %s credits in all.") if side == "buy" else tr("Sells %s now at an average of %s each, %s credits in all.")) % [_lots(pv.got, it),
				Ui.num(float(pv.cost) / pv.got), Ui.num(pv.cost)]
			if pv.unfilled:
				t += " " + tr("%s can't be filled right now.") % _lots(pv.unfilled, it)
	else:
		if n <= 0 or p <= 0:
			t += tr("Enter your price and how many.")
		elif p < int(it.get("floor", 0)):
			t += tr("The floor for %s is %s. Nothing trades below it.") % [it.name, Ui.num(it.floor)]
		elif side == "buy":
			t += tr("Your bid waits in the queue at %s until a seller meets it. %s credits are set aside now; anything that fills cheaper gives the difference back.") % [Ui.num(p), Ui.num(n * p)]
		else:
			t += tr("Your ask waits in the queue at %s until a buyer meets it. %s set aside until it sells or you cancel.") % [Ui.num(p), _lots(n, it)]
	explain.text = t


func _suggest_price() -> void:
	qty_in.text = "1"
	var it := item()
	var v: Variant = it.get("bid") if side == "buy" else it.get("ask")
	if v == null:
		v = it.get("last")
	if v == null:
		v = it.get("floor", 1)
	price_in.text = str(int(v))


func _say(t: String, bad := false) -> void:
	msg.text = t
	msg.add_theme_color_override("font_color", DOWN if bad else UP)


func _place() -> void:
	var it := item()
	var qty := qty_in.text.to_int()
	var price := price_in.text.to_int()
	var b := {"item": sel, "side": side, "type": type, "qty": qty}
	if type == "limit":
		b["price"] = price
	go.disabled = true
	to_library.visible = false
	var r := await _api("POST", "/api/dfg/market/order", b)
	if leaving:
		return
	go.disabled = false
	if not r.ok:
		_say(r.error, true)
		to_library.visible = side == "sell" and "Starship Library" in r.error
	else:
		var d: Dictionary = r.data
		var got := 0
		var total := 0
		for f in d.fills:
			got += int(f.qty)
			total += int(f.qty) * int(f.price)
		var t := ""
		if got:
			t = (tr("Bought %s of %s at an average of %s each (%s credits).") if side == "buy" else tr("Sold %s of %s at an average of %s each (%s credits).")) % [_lots(got, it),
				str(it.name).to_lower(), Ui.num(float(total) / got), Ui.num(total)]
		if d.order.status == "open":
			t += " " + tr("%s waiting in the queue at %s.") % [_lots(d.order.remaining, it), Ui.num(price)]
			Voice.say("order")   # Inara: "Your order's in" (only when it waits in the book)
		if int(d.get("unfilled", 0)):
			t += " " + tr("%s couldn't be filled.") % _lots(d.unfilled, it)
		if d.get("receipt") is Dictionary:
			t += " " + tr("Receipt %s is in your filing cabinet.") % d.receipt.code
		_say(t.strip_edges() if t.strip_edges() != "" else tr("Nothing filled."), got == 0 and d.order.status != "open")
	refreshing = false
	_refresh()


# ── blueprint auctions (Eric 10-12; server: auctions.py) ──

func _build_auctions() -> void:
	var p := au_page
	p.add_child(Ui.label("Blueprint copies are sold one at a time. Each copy sells 5 minutes after its last top bid. A winning bid pays the Starship a 2.5% fee on top. Bidders are never named, and a bought copy can't be resold.", 22, Ui.MUTED))
	au_list = VBoxContainer.new()
	au_list.add_theme_constant_override("separation", 14)
	p.add_child(au_list)
	au_empty = Ui.label("No blueprint auctions right now. Designers schedule them from their approved designs in the drafting room.", 22, Ui.MUTED)
	au_empty.visible = false
	p.add_child(au_empty)
	p.add_child(_heading("Your bids"))
	au_mine = VBoxContainer.new()
	p.add_child(au_mine)
	p.add_child(_heading("Recently sold"))
	au_recent = VBoxContainer.new()
	p.add_child(au_recent)


func _au_load() -> void:
	if leaving or inflight > 2:
		return
	var r := await _api("GET", "/api/dfg/auctions")
	if leaving:
		return
	if not r.ok:
		au_empty.text = r.error
		au_empty.visible = true
		return
	au_data = r.data
	au_skew = Time.get_unix_time_from_datetime_string(str(au_data.server_time).substr(0, 19)) - Time.get_unix_time_from_system()
	_au_render()


func _left(iso: String) -> int:
	return maxi(0, int(round(Time.get_unix_time_from_datetime_string(iso.substr(0, 19)) - (Time.get_unix_time_from_system() + au_skew))))


func _fee(n: int) -> int:
	return int(ceil(n * float(au_data.rules.fee_pct) / 100.0))


func _au_render() -> void:
	var list: Array = au_data.get("auctions", [])
	au_empty.text = tr("No blueprint auctions right now. Designers schedule them from their approved designs in the drafting room.")
	au_empty.visible = list.is_empty()
	var keep := {}
	for a in list:
		keep[int(a.auction_id)] = true
	for id in au_cards.keys():                     # finished, held or cancelled auctions leave the board
		if not keep.has(id):
			au_cards[id].root.queue_free()
			au_cards.erase(id)
	for a in list:
		var id := int(a.auction_id)
		if not au_cards.has(id):
			au_cards[id] = _au_card(a)
			au_list.add_child(au_cards[id].root)
		_au_update(au_cards[id], a)
	_clear(au_mine)
	if au_data.my_bids.is_empty():
		au_mine.add_child(Ui.label(tr("No bids yet."), 22, Ui.MUTED))
	for b in au_data.my_bids:
		var st: String = b.status
		au_mine.add_child(_row([str(b.serial) + "\n" + str(b.name), Ui.num(b.bid), st],
			[Ui.TEXT, Ui.TEXT, UP if st in ["won", "you lead"] else DOWN if st == "outbid" else Ui.MUTED]))
	_clear(au_recent)
	if au_data.recent.is_empty():
		au_recent.add_child(Ui.label(tr("Nothing sold yet."), 22, Ui.MUTED))
	for x in au_data.recent:
		au_recent.add_child(_row([str(x.serial) + "\n" + str(x.name), Ui.num(x.price)]))


## Each auction's card is built once; then only its words and numbers change, so a typed bid stays put (Eric 10-12).
func _au_card(a: Dictionary) -> Dictionary:
	var c := {}
	var panel := PanelContainer.new()
	var st := StyleBoxFlat.new()
	st.bg_color = Ui.PANEL
	st.border_color = Ui.GOLD
	st.set_border_width_all(1)
	st.set_corner_radius_all(12)
	st.set_content_margin_all(16)
	panel.add_theme_stylebox_override("panel", st)
	var v := VBoxContainer.new()
	v.add_theme_constant_override("separation", 8)
	panel.add_child(v)
	c.root = panel
	v.add_child(Ui.label(str(a.name), 28, Ui.GOLD))
	c.meta = Ui.label("", 20, Ui.MUTED)
	v.add_child(c.meta)
	c.starts = Ui.label("", 22)
	v.add_child(c.starts)
	c.running = VBoxContainer.new()
	c.running.add_theme_constant_override("separation", 8)
	v.add_child(c.running)
	c.copy = Ui.label("", 22)
	c.running.add_child(c.copy)
	var line := HBoxContainer.new()
	c.top = Ui.label("", 24)
	c.top.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	line.add_child(c.top)
	c.clock = Ui.label("", 30, Ui.GOLD)
	c.clock.autowrap_mode = TextServer.AUTOWRAP_OFF
	line.add_child(c.clock)
	c.running.add_child(line)
	c.lead = Ui.label("You have the top bid", 22, UP)
	c.running.add_child(c.lead)
	c.own = Ui.label("You can't bid on your own design.", 22, Ui.MUTED)
	c.running.add_child(c.own)
	c.bidrow = HBoxContainer.new()
	c.amount = Ui.field("Your bid")
	c.amount.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	c.typed = false
	c.amount.text_changed.connect(func(_t):
		c.typed = true
		_au_cost(c))
	c.bidrow.add_child(c.amount)
	c.bid = Ui.button("Bid")
	c.bid.custom_minimum_size = Vector2(140, 72)
	c.bid.pressed.connect(func(): _au_bid(c))
	c.bidrow.add_child(c.bid)
	c.running.add_child(c.bidrow)
	c.cost = Ui.label("", 20, Ui.MUTED)
	c.running.add_child(c.cost)
	c.msg = Ui.label("", 22)
	c.running.add_child(c.msg)
	var about := Ui.label(_design(a.get("design", {})), 20)
	about.visible = false
	var tog := Ui.button("▸ " + tr("About this design"), false)
	tog.custom_minimum_size = Vector2(0, 52)
	tog.add_theme_font_size_override("font_size", 20)
	tog.pressed.connect(func():
		about.visible = not about.visible
		tog.text = ("▾ " if about.visible else "▸ ") + tr("About this design"))
	v.add_child(tog)
	v.add_child(about)
	c.lot = 0
	c.shown_lot = 0
	return c


func _design(d: Dictionary) -> String:
	var out := []
	for r in [["What it is and the problem it solves", "problem"], ["What it does", "does"], ["What it fits", "fits"],
			["What it improves", "improves"], ["How it's built", "how"]]:
		if d.get(r[1]):
			out.append(tr(r[0]) + ": " + str(d[r[1]]))
	if d.get("mass_kg"):
		out.append(tr("Weight %s kg from its materials.") % Ui.num(d.mass_kg))
	if d.get("books") is Array and not d.books.is_empty():
		out.append(tr("Library books it requires: %s") % ", ".join(d.books))
	return "\n\n".join(out)


func _au_update(c: Dictionary, a: Dictionary) -> void:
	var l: Variant = a.get("lot")
	var running: bool = a.status == "running" and l is Dictionary
	c.lot = int(l.lot_id) if l is Dictionary else 0
	c.auction = a
	var n := int(a.copies)
	c.meta.text = (tr("Model %s · %d copies · %d sold · floor %s credits%s") if n > 1 else tr("Model %s · %d copy · %d sold · floor %s credits%s")) % [a.model, n, int(a.sold),
		Ui.num(a.floor), (" · " + tr("your design")) if a.yours else ""]
	c.starts.visible = not running
	c.running.visible = running
	if not running:
		c.starts.text = tr("Starts %s") % Ui.when(a.start_at, "short")
		return
	if c.shown_lot != c.lot:                      # the next copy went up: start its bid box afresh
		c.shown_lot = c.lot
		c.typed = false
		c.msg.text = ""
	c.copy.text = tr("Copy %d of %d · %s") % [int(l.copy), n, l.serial]
	c.top.text = (tr("Top bid %s") % Ui.num(l.top_bid)) if l.top_bid else tr("No bids yet")
	c.lead.visible = l.you_lead
	c.own.visible = a.yours
	c.bidrow.visible = not a.yours and not l.you_lead
	var least := int(l.least)
	if (not c.typed or c.amount.text.to_int() < least) and not c.amount.has_focus():
		c.amount.text = str(least)
		c.typed = false
	_au_cost(c)
	_au_clock(c)


func _au_cost(c: Dictionary) -> void:
	var n: int = c.amount.text.to_int()
	c.cost.text = tr("%s + %s Starship fee = %s credits set aside") % [Ui.num(n), Ui.num(_fee(n)), Ui.num(n + _fee(n))] if n > 0 else ""
	c.cost.visible = c.bidrow.visible


func _au_clock(c: Dictionary) -> void:
	var a: Dictionary = c.get("auction", {})
	if not (a.get("lot") is Dictionary):
		return
	var s := _left(a.lot.closes_at)
	c.clock.text = "%d:%02d" % [s / 60, s % 60]
	c.clock.add_theme_color_override("font_color", DOWN if s < 60 else Ui.GOLD)


func _au_tick() -> void:
	if au_page.visible:
		for id in au_cards:
			_au_clock(au_cards[id])


func _au_bid(c: Dictionary) -> void:
	if c.lot == 0:
		return
	c.bid.disabled = true
	var r := await _api("POST", "/api/dfg/auctions/bid", {"lot_id": int(c.lot), "amount": c.amount.text.to_int()})
	if leaving:
		return
	c.bid.disabled = false
	if r.ok:
		c.msg.text = tr("You have the top bid: %s + %s fee set aside. The clock is back to 5 minutes.") % [Ui.num(r.data.bid), Ui.num(r.data.fee)]
		c.msg.add_theme_color_override("font_color", UP)
		c.typed = false
	else:
		c.msg.text = r.error
		c.msg.add_theme_color_override("font_color", DOWN)
	_au_load()


## The price chart: candles with volume under them, drawn here (the browser uses TradingView's library).
class Chart extends Control:
	var candles: Array = []

	func set_candles(c: Array) -> void:
		candles = c
		queue_redraw()

	func _draw() -> void:
		var w := size.x
		var h := size.y
		draw_rect(Rect2(Vector2.ZERO, size), Color("0b1020"))
		var font := ThemeDB.fallback_font
		if candles.is_empty():
			draw_string(font, Vector2(20, h / 2), tr("No trades in this period yet."), HORIZONTAL_ALIGNMENT_LEFT, -1, 22, Color("7d8aa5"))
			return
		var axis := 90.0                              # room on the right for the prices
		var slot := 12.0
		var n := mini(candles.size(), int((w - axis) / slot))
		var shown := candles.slice(candles.size() - n)
		var hi := -INF
		var lo := INF
		var vmax := 1.0
		for c in shown:
			hi = maxf(hi, float(c.high))
			lo = minf(lo, float(c.low))
			vmax = maxf(vmax, float(c.volume))
		if hi == lo:
			hi += 1
			lo -= 1
		var top := 16.0
		var price_h := h * 0.78 - top
		var y := func(p: float) -> float: return top + (hi - p) / (hi - lo) * price_h
		for i in 4:                                   # grid lines with their prices
			var p := lo + (hi - lo) * i / 3.0
			var gy: float = y.call(p)
			draw_line(Vector2(0, gy), Vector2(w - axis, gy), Color("131b2e"))
			draw_string(font, Vector2(w - axis + 8, gy + 7), str(int(round(p))), HORIZONTAL_ALIGNMENT_LEFT, -1, 18, Color("7d8aa5"))
		var x0 := w - axis - n * slot
		for i in shown.size():
			var c: Dictionary = shown[i]
			var o := float(c.open)
			var cl := float(c.close)
			var col := Color("3fbf8a") if cl >= o else Color("e5605a")
			var cx := x0 + i * slot + slot / 2
			draw_line(Vector2(cx, y.call(float(c.high))), Vector2(cx, y.call(float(c.low))), col, 1.5)
			var y1: float = y.call(maxf(o, cl))
			var y2: float = y.call(minf(o, cl))
			draw_rect(Rect2(cx - slot * 0.35, y1, slot * 0.7, maxf(1.5, y2 - y1)), col)
			var vh := float(c.volume) / vmax * h * 0.18
			draw_rect(Rect2(cx - slot * 0.35, h - vh, slot * 0.7, vh), Color(col, 0.45))
		var last := float(shown[-1].close)
		var ly: float = y.call(last)
		draw_line(Vector2(0, ly), Vector2(w - axis, ly), Color(Ui.GOLD, 0.5), 1.0)
		draw_rect(Rect2(w - axis + 2, ly - 13, axis - 4, 26), Ui.GOLD)
		draw_string(font, Vector2(w - axis + 8, ly + 7), str(int(round(last))), HORIZONTAL_ALIGNMENT_LEFT, -1, 18, Ui.BG)
