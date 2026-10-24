extends Node
## THE HOLD, COLLECTING AND UNLOADING, ported from the live browser game (static/debris-flight.js: MATERIALS, HOLD AND
## COLLECTING; UNLOADING AT THE STARSHIP; THE GAME SERVER). Eric 10-10/10-11:
##  • Every piece IS a piece of material at its true size and shape. The hold has real interior dimensions: a piece goes in
##    only if its shape fits (its three dimensions, turned any way) and there is room left for its BULK (its box).
##  • Parked at a field, COLLECT draws pieces aboard one at a time, nearest first; bigger pieces take longer. Signed in,
##    each piece goes to the server (POST /api/dfg/collect), which decides what it is and keeps it; it refuses without the
##    Mining pass. One diamond in 100,000 is near-flawless (rule 26), noticed when the miner collects it.
##  • Docked, UNLOAD moves the hold into your space in the Starship's cargo hold (POST /api/dfg/unload): the cargo office
##    (the server) does the transfer and issues a receipt anyone can check (rule 13).

const Solar := preload("res://scripts/solar.gd")
const STORE_CAP := 12.0                          # your space aboard when not signed in (dfg settings cargo_m3_start)
const SHIP_HOLD := {"cap": 34000.0, "others": 21480.0}   # the whole Starship hold: an ESTIMATE, labelled as such
const RCPT_CHARS := "23456789ABCDEFGHJKMNPQRSTVWXYZ"

var bay: Node
var hold := {"name": "Starter hold", "dims": [1.6, 1.2, 1.0]}
var cargo: Array = []                            # pieces aboard
var store := {"cap": STORE_CAP, "kg": {}}
var session_id := ""
var net := false
var queue: Array = []                            # collects waiting for the server, in order
var sending := false
var last_sent := -10.0
var collecting := {}                             # {f, i, t, dur}
var first_piece := false
var xfer := {}

var hold_btn: Button
var hold_fill: ColorRect
var collect_btn: Button
var unload_btn: Button
var cwrap: Control
var cbar: ColorRect
var hold_panel: Panel
var hold_text: Label
var x_panel: Panel
var x_title: Label
var x_now: Label
var x_bars: Array = []                           # [fill, text] for your hold, your space aboard, the whole Starship hold
var x_sum: Label
var x_rcpt: Label
var x_done: Button
var x_save: Button


func _init() -> void:
	_hold_dims(hold.dims)


func _hold_dims(d: Array) -> void:
	hold.dims = d.duplicate()
	hold.cap = d[0] * d[1] * d[2]
	hold.sorted = d.duplicate()
	hold.sorted.sort()
	hold.sorted.reverse()


func bulk() -> float:
	return cargo.reduce(func(a, p): return a + p.box, 0.0)


func shape_fits(p: Dictionary) -> bool:
	for i in 3:
		if p.dims[i] > hold.sorted[i]:
			return false
	return true


func room_for(p: Dictionary) -> bool:
	return bulk() + p.box <= hold.cap + 1e-9


static func fmt_kg(kg: float) -> String:
	if kg >= 1000.0:
		return ("%.1f t" if kg >= 10000.0 else "%.2f t") % (kg / 1000.0)
	return "%d kg" % roundi(kg)


func mat_name(key: String) -> String:
	return bay.debris.material(key)[1]


func store_used() -> float:
	var v := 0.0
	for m in store.kg:
		v += store.kg[m] / float(bay.debris.material(m)[2])
	return v


# ── the server ──
## The session's ship, hold and storage, exactly as the server has them (browser netApplyShip).
func apply_ship(j: Dictionary) -> void:
	if j.has("session_id"):
		session_id = str(j.session_id)
		net = true
	if j.get("ship", {}).has("hold_dims_m"):
		_hold_dims(j.ship.hold_dims_m)
	if j.has("pieces"):
		cargo.clear()
		for p in j.pieces:
			var dims: Array = p.dims_m.duplicate()
			dims.sort()
			dims.reverse()
			cargo.append({"id": p.id, "mat": p.material, "dims": dims, "vol": p.volume_m3, "box": p.box_m3, "mass": p.kg,
				"taken": true, "flawless": p.get("flawless", false)})
	if j.has("storage"):
		store.cap = float(j.storage.capacity_m3)
		store.kg = j.storage.kg.duplicate()
	render_hold()


func _apply_inventory(inv: Dictionary) -> void:
	for pl in inv.get("places", []):
		if pl.get("kind") == "starship_cargo":
			store.cap = float(pl.capacity_m3)
			store.kg = {}
			for g in pl.get("goods", []):
				if g.get("kg") != null:
					store.kg[g.item] = float(g.kg) + float(g.get("kg_set_aside", 0.0))
	render_hold()


## One collect at a time, in order, never closer together than the server allows (it refuses collects under 2 s apart).
func _send_collects() -> void:
	if sending:
		return
	sending = true
	while not queue.is_empty():
		var p: Dictionary = queue.pop_front()
		var wait := last_sent + 2.2 - Time.get_ticks_msec() / 1000.0
		if wait > 0.0:
			await get_tree().create_timer(wait).timeout
		last_sent = Time.get_ticks_msec() / 1000.0
		var r: Dictionary = await Api.call_api("POST", "/api/dfg/collect", {"session_id": session_id, "field": p.fid,
			"index": p.idx, "dims": p.dims, "volume_m3": p.vol})
		if not r.ok:
			cargo.erase(p)
			render_hold()
			bay._say("NOT COLLECTED\n" + r.error, r.code == 403)   # no Mining pass: the way to the Library
			continue
		var a: Dictionary = r.data.get("aboard", {})
		if a.get("material", p.mat) != p.mat:          # the server's word
			p.mat = a.material
			p.mass = float(a.kg)
		if a.get("flawless", false):                   # rule 26: keep the excitement with the miner
			p.flawless = true
			bay.sound.chime()
			get_tree().create_timer(0.35).timeout.connect(func(): bay.sound.chime())
			Voice.say("diamond")
			Voice.story(bay.hud_root, "diamond")
			bay._say("💎 NEAR-FLAWLESS DIAMOND\nOne in a hundred thousand. It stays apart from industrial diamond, and goes to your lockbox when you unload.")
		elif a.get("noticed", false):                  # lonsdaleite: noticed when collected (not the near-flawless diamond)
			bay.sound.chime()
			if p.mat == "brownleeite":
				get_tree().create_timer(0.35).timeout.connect(func(): bay.sound.chime())
				bay._say("✦ BROWNLEEITE\nManganese silicide, known from comet dust and never found naturally on Earth. Ultra rare. Read about it in the Starship Library.")
			else:
				bay._say("✦ LONSDALEITE\nHexagonal diamond: very rare. It is not ordinary diamond. Read about it in the Starship Library.")
		render_hold()
	sending = false


# ── collecting ──
func _next_piece(f: Dictionary) -> int:
	var best := -1
	var bd := 1e18
	var me: Vector3 = _field_local(f)
	for i in f.pieces.size():
		var p: Dictionary = f.pieces[i]
		if p.taken or not shape_fits(p) or not room_for(p):
			continue
		var d := (p.xf.origin as Vector3).distance_to(me)
		if d < bd:
			bd = d
			best = i
	return best


## Where the pilot is, in the field's own space (relative to its centre, the solar system's axes).
func _field_local(f: Dictionary) -> Vector3:
	return bay.debris.w2l.inverse() * Solar.vec(Solar.sub(bay._me(), f.center))


func start_collect() -> void:
	var f = bay.lock.get("field") if bay.lock.get("parked", false) else null
	if f == null:
		return
	if Session.me.get("skills", {}).get("mine", true) == false:   # no Mining pass: the server would refuse every piece
		bay._say("LIBRARY FIRST\nPass the Mining test before you can mine. Open QUARTERS, then Exit Private Quarters to the Starship Library.", true)
		return
	if not f.pieces.any(func(p): return not p.taken and shape_fits(p)):
		Voice.say("toobig")
		bay._say("TOO BIG TO TAKE\nThese pieces won't fit in your hold. Keep searching for a field of smaller debris.")
		return
	var i := _next_piece(f)
	if i < 0:
		Voice.say("full")
		bay._say("HOLD FULL\nNo room left for these pieces. Return to the Starship to unload.")
		return
	collecting = {"f": f, "i": i, "t": 0.0, "dur": 2.0 + minf(10.0, f.pieces[i].box * 12.0)}


func tick(dt: float) -> void:
	var f = bay.lock.get("field") if bay.lock.get("parked", false) else null
	collect_btn.visible = f != null and collecting.is_empty() and xfer.is_empty()
	cwrap.visible = not collecting.is_empty()
	unload_btn.visible = bay.docked and not cargo.is_empty() and xfer.is_empty()
	_xfer_tick(dt)
	if collecting.is_empty():
		return
	var c := collecting
	var p: Dictionary = c.f.pieces[c.i]
	if f == null or f.id != c.f.id or not is_instance_valid(c.f.node):   # flew off: put the half-drawn piece back
		if is_instance_valid(c.f.node):
			bay.debris.show_piece(c.f, c.i, p.xf)
		collecting = {}
		return
	c.t += dt
	var k := minf(1.0, c.t / c.dur)
	var e := k * k * (3.0 - 2.0 * k)
	# the piece drifts in toward the ship (field-local space), shrinking as it comes aboard
	var xf: Transform3D = p.xf
	bay.debris.show_piece(f, c.i, Transform3D(xf.basis.scaled_local(Vector3.ONE * (1.0 - 0.8 * e)), xf.origin.lerp(_field_local(f), e)))
	cbar.size.x = 300.0 * k
	if k < 1.0:
		return
	p.taken = true
	cargo.append(p)
	bay.debris.show_piece(f, c.i)
	if net:
		queue.append(p)
		_send_collects()
	if not first_piece:
		first_piece = true
		Voice.say("firstpiece")
		if net:
			Voice.story(bay.hud_root, "piece")
	bay.sound.ping(520.0)
	bay._say("+ %s %s\n%s m · takes %.3f m³ of hold space" % [fmt_kg(p.mass), mat_name(p.mat).to_upper(),
		" × ".join(p.dims.map(func(d): return "%.2f" % d)), p.box])
	collecting = {}
	render_hold()
	if f.pieces.all(func(q): return q.taken):
		bay.lock = {}
		f.cleared = true
		Voice.say("cleared")
		bay._say("FIELD CLEARED\nNothing left here. There's more debris all through the ring.")
		return
	start_collect()                              # keep going until full or nothing else fits


# ── the screen ──
func build(root: Control) -> void:
	hold_btn = bay._hud_button("", Vector2(24, 76), Vector2(300, 52), 10, "")
	hold_btn.add_theme_font_size_override("font_size", 18)
	hold_btn.pressed.connect(func():
		render_hold()
		hold_panel.visible = not hold_panel.visible)
	root.add_child(hold_btn)
	var bg := ColorRect.new()
	bg.color = Color(0.64, 0.07, 0.11, 0.18)
	bg.position = Vector2(10, 42)
	bg.size = Vector2(280, 4)
	bg.mouse_filter = Control.MOUSE_FILTER_IGNORE
	hold_btn.add_child(bg)
	hold_fill = ColorRect.new()
	hold_fill.color = bay.HUD_RED
	hold_fill.position = Vector2(10, 42)
	hold_fill.size = Vector2(0, 4)
	hold_fill.mouse_filter = Control.MOUSE_FILTER_IGNORE
	hold_btn.add_child(hold_fill)
	collect_btn = bay._hud_button("COLLECT", Vector2(230, 1100), Vector2(260, 80), 40, "")
	collect_btn.add_theme_font_size_override("font_size", 26)
	collect_btn.visible = false
	collect_btn.pressed.connect(func():
		bay.sound.ping(660.0)
		start_collect())
	root.add_child(collect_btn)
	unload_btn = bay._hud_button("UNLOAD", Vector2(230, 1100), Vector2(260, 80), 40, "")
	unload_btn.add_theme_font_size_override("font_size", 26)
	unload_btn.visible = false
	unload_btn.pressed.connect(start_unload)
	root.add_child(unload_btn)
	cwrap = Control.new()
	cwrap.position = Vector2(210, 1110)
	cwrap.size = Vector2(300, 60)
	cwrap.mouse_filter = Control.MOUSE_FILTER_IGNORE
	cwrap.visible = false
	root.add_child(cwrap)
	var cl := Ui.label("COLLECTING", 20, Color("7fe0a8"))
	cl.autowrap_mode = TextServer.AUTOWRAP_OFF
	cl.size = Vector2(300, 28)
	cl.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	cwrap.add_child(cl)
	var cbg := ColorRect.new()
	cbg.color = Color(0.5, 0.88, 0.66, 0.15)
	cbg.position = Vector2(0, 34)
	cbg.size = Vector2(300, 8)
	cwrap.add_child(cbg)
	cbar = ColorRect.new()
	cbar.color = Color("7fe0a8")
	cbar.position = Vector2(0, 34)
	cbar.size = Vector2(0, 8)
	cwrap.add_child(cbar)
	hold_panel = _panel(root, Vector2(30, 140), Vector2(660, 760))
	hold_text = Ui.label("", 20, Ui.TEXT)
	hold_text.position = Vector2(24, 80)
	hold_text.size = Vector2(612, 660)
	hold_panel.add_child(hold_text)
	_panel_head(hold_panel, "YOUR HOLD", func(): hold_panel.visible = false)
	_xfer_panel(root)
	render_hold()


func _panel(root: Control, at: Vector2, sz: Vector2) -> Panel:
	var p := Panel.new()
	var sb := StyleBoxFlat.new()
	sb.bg_color = Color(0.043, 0.063, 0.125, 0.94)
	sb.border_color = bay.HUD_RED
	sb.set_border_width_all(1)
	sb.set_corner_radius_all(14)
	p.add_theme_stylebox_override("panel", sb)
	p.position = at
	p.size = sz
	p.visible = false
	root.add_child(p)
	return p


func _panel_head(p: Panel, title: String, close: Callable) -> Label:
	var h := Ui.label(title, 24, bay.HUD_RED)
	h.autowrap_mode = TextServer.AUTOWRAP_OFF
	h.position = Vector2(24, 20)
	p.add_child(h)
	var x: Button = bay._hud_button("×", Vector2(p.size.x - 70, 14), Vector2(54, 54), 27, "")
	x.pressed.connect(close)
	p.add_child(x)
	return h


func render_hold() -> void:
	if hold_btn == null:
		return
	var used := bulk()
	hold_btn.text = "HOLD %.2f / %.2f m³" % [used, hold.cap]
	hold_fill.size.x = 280.0 * clampf(used / hold.cap, 0.0, 1.0)
	var rows := {}
	for p in cargo:
		var k: String = "flawless" if p.get("flawless", false) else p.mat
		if not rows.has(k):
			rows[k] = {"n": 0, "kg": 0.0, "box": 0.0}
		rows[k].n += 1
		rows[k].kg += p.mass
		rows[k].box += p.box
	var t := "%s: %s m inside (%.2f m³). Used %.2f m³ · %s aboard.\n\n" % [hold.name,
		" × ".join(hold.dims.map(func(d): return "%.1f" % d)), hold.cap, used, fmt_kg(cargo.reduce(func(a, p): return a + p.mass, 0.0))]
	if cargo.is_empty():
		t += "Your hold is empty.\n"
	for m in bay.debris.MATERIALS.map(func(x): return x[0]) + ["flawless"]:   # the near-flawless diamond is never mixed in
		if rows.has(m):
			t += "%s · %d · %s · %.3f m³\n" % ["💎 Near-flawless diamond" if m == "flawless" else mat_name(m), rows[m].n, fmt_kg(rows[m].kg), rows[m].box]
	t += "\nYOUR SPACE IN THE STARSHIP'S CARGO HOLD\n%.3f of %.2f m³ used.\n" % [store_used(), store.cap]
	for m in bay.debris.MATERIALS:
		if store.kg.get(m[0], 0.0) > 0.0:
			t += "%s · %s · %.3f m³\n" % [m[1], fmt_kg(store.kg[m[0]]), store.kg[m[0]] / float(m[2])]
	hold_text.text = t


# ── unloading at the Starship ──
func _xfer_panel(root: Control) -> void:
	x_panel = _panel(root, Vector2(30, 200), Vector2(660, 820))
	x_title = _panel_head(x_panel, "", close_xfer)
	x_now = Ui.label("", 20, Ui.TEXT)
	x_now.position = Vector2(24, 70)
	x_now.size = Vector2(612, 60)
	x_panel.add_child(x_now)
	var y := 140.0
	for name in ["Your ship's hold", "Your space aboard the Starship", "The Starship's whole cargo hold (estimate)"]:
		var l := Ui.label(name, 18, Ui.MUTED)
		l.autowrap_mode = TextServer.AUTOWRAP_OFF
		l.position = Vector2(24, y)
		x_panel.add_child(l)
		var v := Ui.label("", 18, Ui.TEXT)
		v.autowrap_mode = TextServer.AUTOWRAP_OFF
		v.horizontal_alignment = HORIZONTAL_ALIGNMENT_RIGHT
		v.position = Vector2(336, y)
		v.size = Vector2(300, 26)
		x_panel.add_child(v)
		var bg := ColorRect.new()
		bg.color = Color(0.5, 0.88, 0.66, 0.15)
		bg.position = Vector2(24, y + 32)
		bg.size = Vector2(612, 10)
		x_panel.add_child(bg)
		var fill := ColorRect.new()
		fill.color = Color("7fe0a8")
		fill.position = Vector2(24, y + 32)
		fill.size = Vector2(0, 10)
		x_panel.add_child(fill)
		x_bars.append([fill, v])
		y += 66.0
	x_sum = Ui.label("", 20, Ui.TEXT)
	x_sum.position = Vector2(24, 350)
	x_sum.size = Vector2(612, 200)
	x_panel.add_child(x_sum)
	x_rcpt = Ui.label("", 18, Ui.TEXT)
	x_rcpt.position = Vector2(24, 560)
	x_rcpt.size = Vector2(612, 150)
	x_panel.add_child(x_rcpt)
	x_save = bay._hud_button("SAVE RECEIPT", Vector2(24, 730), Vector2(300, 64), 32, "")
	x_save.pressed.connect(_save_receipt)
	x_panel.add_child(x_save)
	x_done = bay._hud_button("DONE", Vector2(336, 730), Vector2(300, 64), 32, "")
	x_done.pressed.connect(close_xfer)
	x_panel.add_child(x_done)


func start_unload() -> void:
	if not bay.docked or cargo.is_empty() or not xfer.is_empty():
		return
	xfer = {"t": 0.0, "per": clampf(3.5 / cargo.size(), 0.6, 1.6), "moved": {}, "n": 0, "full": false,
		"start": cargo.size(), "done": false, "wait": false, "gems": 0}
	x_title.text = "TRANSFERRING TO THE STARSHIP"
	x_title.add_theme_color_override("font_color", bay.HUD_RED)
	x_sum.text = ""
	x_rcpt.text = ""
	x_save.visible = false
	x_done.visible = false
	x_panel.visible = true
	if net:   # signed in: the cargo office (the server) does the transfer and issues the receipt; the bars then show it
		var x := xfer
		x.wait = true
		x_now.text = "Contacting the cargo office…"
		_render_xfer(0.0)
		while sending or not queue.is_empty():   # every collect first
			await get_tree().process_frame
		var r: Dictionary = await Api.call_api("POST", "/api/dfg/unload", {"docked": true})
		if xfer != x:
			return
		x.wait = false
		if not r.ok:
			x.error = r.error
			_finish_xfer(false)
			return
		x.server = r.data
		if int(r.data.get("unloaded_pieces", 0)) == 0:
			x.full = r.data.get("storage_full", false)
			_finish_xfer(false)
			return
		_now(cargo[0])
		return
	_now(cargo[0])
	_render_xfer(0.0)


func _move() -> void:
	var p: Dictionary = cargo.pop_front()
	if p.get("flawless", false):
		xfer.gems += 1                           # kept apart: to the lockbox, not the cargo-hold storage
	else:
		store.kg[p.mat] = store.kg.get(p.mat, 0.0) + p.mass
		xfer.moved[p.mat] = xfer.moved.get(p.mat, 0.0) + p.mass
	xfer.n += 1
	render_hold()


func _now(p) -> void:
	x_now.text = "" if p == null else "Moving %s of %s…" % [fmt_kg(p.mass), mat_name(p.mat).to_lower()]


func _render_xfer(sub: float) -> void:
	var used := maxf(0.0, bulk() - sub)
	var su := store_used()
	var all: float = SHIP_HOLD.others + su
	x_bars[0][0].size.x = 612.0 * clampf(used / hold.cap, 0.0, 1.0)
	x_bars[0][1].text = "%.2f / %.2f m³" % [used, hold.cap]
	x_bars[1][0].size.x = 612.0 * clampf(maxf(0.015 if su > 0.0 else 0.0, su / store.cap), 0.0, 1.0)
	x_bars[1][1].text = "%.3f / %.2f m³" % [su, store.cap]
	x_bars[2][0].size.x = 612.0 * all / SHIP_HOLD.cap
	x_bars[2][1].text = "%.1f%% full · %s m³ free" % [100.0 * all / SHIP_HOLD.cap, Solar._commas(roundi(SHIP_HOLD.cap - all))]


func _xfer_tick(dt: float) -> void:
	if xfer.is_empty():
		return
	var x := xfer
	if not bay.docked:                            # launching leaves a clean view (Eric 10-11)
		if not x.done and x.has("server"):         # the cargo office already moved them: finish at once
			while x.n < int(x.server.unloaded_pieces) and not cargo.is_empty():
				_move()
			x.full = int(x.server.get("left_aboard", 0)) > 0
			_finish_xfer(false)
			bay._say("TRANSFER COMPLETE\n%d %s moved to the Starship. Your receipt is in your quarters." % [x.n, "piece" if x.n == 1 else "pieces"])
		elif not x.done and not x.wait:
			_finish_xfer(true)
			bay._say("TRANSFER STOPPED\n%d of %d pieces moved before you launched; the rest are still in your hold." % [x.n, x.start])
		close_xfer()
		return
	if x.done or x.wait:
		return
	x.t += dt
	var p: Dictionary = cargo[0]
	_render_xfer(p.box * minf(1.0, x.t / x.per))   # the piece leaving drains the hold smoothly
	if x.t < x.per:
		return
	x.t = 0.0
	if x.has("server"):
		if x.n >= int(x.server.unloaded_pieces):
			x.full = int(x.server.get("left_aboard", 0)) > 0
			_finish_xfer(false)
			return
	elif store_used() + p.mass / float(bay.debris.material(p.mat)[2]) > store.cap + 1e-9:
		x.full = true
		_finish_xfer(false)
		return
	_move()
	bay.sound.ping(440.0)
	if cargo.is_empty() or (x.has("server") and x.n >= int(x.server.unloaded_pieces)):
		x.full = x.has("server") and int(x.server.get("left_aboard", 0)) > 0
		_finish_xfer(false)
		return
	_now(cargo[0])


func _finish_xfer(stopped: bool) -> void:
	var x := xfer
	x.done = true
	_render_xfer(0.0)
	_now(null)
	if x.has("error"):
		x_title.text = "TRANSFER NOT MADE"
		x_now.text = x.error + " Your cargo is still in your hold."
	elif stopped:
		x_title.text = "TRANSFER STOPPED"
		x_now.text = "You launched. %d of %d pieces moved; the rest are still in your hold." % [x.n, x.start]
	elif x.full:
		x_title.text = "STARSHIP SPACE FULL"
		x_now.text = "%d of %d pieces moved. Your space aboard is full, so %d %s in your hold." % [x.n, x.start, cargo.size(),
			"piece stays" if cargo.size() == 1 else "pieces stay"]
	else:
		x_title.text = "TRANSFER COMPLETE"
		x_title.add_theme_color_override("font_color", Color("7fe0a8"))
		Voice.say("unloaded")
		if x.has("server"):
			Voice.story(bay.hud_root, "unload")
		x_now.text = "All %d %s aboard the Starship. Your hold is empty." % [x.n, "piece is" if x.n == 1 else "pieces are"]
		bay.sound.chime()
	var sum := ""
	for m in bay.debris.MATERIALS:
		if x.moved.has(m[0]):
			sum += "%s · + %s\n" % [m[1], fmt_kg(x.moved[m[0]])]
	if x.gems > 0:
		sum += "💎 Near-flawless diamond · + %d to your lockbox\n" % x.gems
	x_sum.text = sum
	if x.has("server"):
		_apply_inventory(x.server.get("inventory", {}))   # the server's figures are the truth
	if x.n > 0:
		var sr: Dictionary = x.server.get("receipt", {}) if x.has("server") else {}
		var rc := {"code": sr.code, "at": str(sr.get("issued_at", "")), "pieces": int(sr.pieces), "left": int(sr.get("left_aboard", 0)),
			"kg": sr.get("kg", {}), "used": float(sr.space_used_m3), "total": float(sr.space_total_m3), "server": true} if not sr.is_empty() \
			else {"code": _receipt_code(), "at": Time.get_datetime_string_from_system(), "pieces": x.n, "left": cargo.size(),
			"kg": x.moved, "used": store_used(), "total": store.cap, "server": false}
		x.receipt = rc
		x_rcpt.text = "RECEIPT %s · %s\n%d %s from your ship's hold to your space in the Starship's cargo hold%s. Your space after: %.3f of %.2f m³ used.\n%s" % [
			rc.code, rc.at, rc.pieces, "piece" if rc.pieces == 1 else "pieces", " (%d left aboard)" % rc.left if rc.left else "",
			rc.used, rc.total, "Issued by the Starship's cargo office (the game server). Anyone can check this code. A copy is in your quarters, in the filing cabinet." if rc.server
			else "PROTOTYPE RECEIPT: made without a sign-in, so this code cannot be checked."]
		x_save.visible = true
	x_done.visible = true


func _receipt_code() -> String:
	var c := ""
	for i in 8:
		c += RCPT_CHARS[randi() % RCPT_CHARS.length()]
	return "WSC-" + c.substr(0, 4) + "-" + c.substr(4)


func receipt_text(rc: Dictionary) -> String:
	var L := ["WORLD SPACE CONSORTIUM", "WSC Alexander von Humboldt · Cargo office", "", "RECEIPT " + rc.code, "Issued: " + rc.at,
		"Transfer: %d %s from your ship's hold to your space in the Starship's cargo hold" % [rc.pieces, "piece" if rc.pieces == 1 else "pieces"]]
	if rc.left:
		L.append("Left aboard your ship: %d %s" % [rc.left, "piece" if rc.left == 1 else "pieces"])
	L.append_array(["", "Material                 Weight"])
	for m in rc.kg:
		L.append((mat_name(m) + "                         ").substr(0, 25) + fmt_kg(float(rc.kg[m])))
	L.append_array(["", "Your space after: %.3f of %.2f m³ used" % [rc.used, rc.total], ""])
	if rc.server:
		L.append_array(["Issued by the game server. Anyone can check this code at:", Api.BASE_URL + "/api/dfg/receipt/" + rc.code, ""])
	else:
		L.append_array(["PROTOTYPE RECEIPT: made without a sign-in, so this code cannot be checked.", ""])
	return "\n".join(L)


## Save a copy to the player's own device (rule 13): the system's own Save window, so the player picks where.
func _save_receipt() -> void:
	var rc: Dictionary = xfer.get("receipt", {})
	if rc.is_empty():
		return
	var d := FileDialog.new()
	d.file_mode = FileDialog.FILE_MODE_SAVE_FILE
	d.access = FileDialog.ACCESS_FILESYSTEM
	d.use_native_dialog = true
	d.current_file = "stardust-receipt-%s.txt" % rc.code
	d.filters = PackedStringArray(["*.txt ; Receipt"])
	d.file_selected.connect(func(path: String):
		var fa := FileAccess.open(path, FileAccess.WRITE)
		if fa:
			fa.store_string(receipt_text(rc))
			fa.close()
			bay._say("RECEIPT SAVED\n%s is on your device, and in the filing cabinet in your quarters." % rc.code)
		else:
			bay._say("COULDN'T SAVE\nYour receipt is still in the filing cabinet in your quarters. Try again from there.")
		d.queue_free())
	d.canceled.connect(func(): d.queue_free())
	add_child(d)
	d.popup_centered()


func close_xfer() -> void:
	x_panel.visible = false
	xfer = {}
