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
var pick_btn: Button                              # Science, fifth bar gold: choose the material to collect
var pick := ""                                   # "" = any, nearest first
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
var x_desk: Button                                # space full: Inara sends the pilot to the Desk's Market terminal (Eric 11-04)
var x_rent: Button                                # … or the Starship rents more space (rule 10)


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
		var wait := last_sent + 2.2 / (1.0 + Session.skill("mining")) - Time.get_ticks_msec() / 1000.0
		if wait > 0.0:
			await get_tree().create_timer(wait).timeout
		last_sent = Time.get_ticks_msec() / 1000.0
		var r: Dictionary = await Api.call_api("POST", "/api/dfg/collect", {"session_id": session_id, "field": p.fid,
			"index": p.idx, "dims": p.dims, "volume_m3": p.vol})
		if not r.ok:
			cargo.erase(p)
			render_hold()
			bay._say(tr("NOT COLLECTED\n%s") % r.error, r.code == 403)   # no Mining pass: the way to the Library
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
			bay._say(tr("💎 NEAR-FLAWLESS DIAMOND\nOne in a hundred thousand. It stays apart from industrial diamond, and goes to your lockbox when you unload."))
		elif a.get("noticed", false):                  # lonsdaleite: noticed when collected (not the near-flawless diamond)
			bay.sound.chime()
			if p.mat == "brownleeite":
				get_tree().create_timer(0.35).timeout.connect(func(): bay.sound.chime())
				bay._say(tr("✦ BROWNLEEITE\nManganese silicide, known from comet dust and never found naturally on Earth. Ultra rare. Read about it in the Starship Library."))
			else:
				bay._say(tr("✦ LONSDALEITE\nHexagonal diamond: very rare. It is not ordinary diamond. Read about it in the Starship Library."))
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
		if pick != "" and p.mat != pick:
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
		bay._say(tr("LIBRARY FIRST\nPass the Mining test before you can mine. Open QUARTERS, then Exit Private Quarters to the Starship Library."), true)
		return
	if not f.pieces.any(func(p): return not p.taken and shape_fits(p)):
		Voice.say("toobig")
		bay._say(tr("TOO BIG TO TAKE\nThese pieces won't fit in your hold. Keep searching for a field of smaller debris."))
		return
	var i := _next_piece(f)
	if i < 0 and pick != "":
		bay._say(tr("NONE LEFT\nNo %s you can take here. Pick another material, or ANY.") % bay.debris.material(pick)[1].to_upper())
		return
	if i < 0:
		Voice.say("full")
		bay._say(tr("HOLD FULL\nNo room left for these pieces. Return to the Starship to unload."))
		return
	collecting = {"f": f, "i": i, "t": 0.0, "dur": (2.0 + minf(10.0, f.pieces[i].box * 12.0)) / (1.0 + Session.skill("mining"))}


func tick(dt: float) -> void:
	var f = bay.lock.get("field") if bay.lock.get("parked", false) else null
	collect_btn.visible = f != null and collecting.is_empty() and xfer.is_empty()
	pick_btn.visible = collect_btn.visible and Session.can_pick_material()
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
	bay._say(tr("+ %s %s\n%s m · takes %.3f m³ of hold space") % [fmt_kg(p.mass), mat_name(p.mat).to_upper(),
		" × ".join(p.dims.map(func(d): return "%.2f" % d)), p.box])
	collecting = {}
	render_hold()
	if f.pieces.all(func(q): return q.taken):
		bay.lock = {}
		f.cleared = true
		Voice.say("cleared")
		bay._say(tr("FIELD CLEARED\nNothing left here. There's more debris all through the ring."))
		return
	start_collect()                              # keep going until full or nothing else fits


# ── the screen ──
func build(root: Control) -> void:
	hold_btn = bay._hud_button("", Vector2(24, 76), Vector2(240, 42), 8, "")
	hold_btn.add_theme_font_size_override("font_size", 15)
	hold_btn.pressed.connect(func():
		render_hold()
		hold_panel.visible = not hold_panel.visible)
	root.add_child(hold_btn)
	var bg := ColorRect.new()
	bg.color = Color(0.64, 0.07, 0.11, 0.18)
	bg.position = Vector2(10, 34)
	bg.size = Vector2(220, 3)
	bg.mouse_filter = Control.MOUSE_FILTER_IGNORE
	hold_btn.add_child(bg)
	hold_fill = ColorRect.new()
	hold_fill.color = bay.HUD_RED
	hold_fill.position = Vector2(10, 34)
	hold_fill.size = Vector2(0, 3)
	hold_fill.mouse_filter = Control.MOUSE_FILTER_IGNORE
	hold_btn.add_child(hold_fill)
	collect_btn = bay._hud_button("COLLECT", Vector2(256, 1120), Vector2(208, 64), 32, "")
	collect_btn.add_theme_font_size_override("font_size", 21)
	collect_btn.visible = false
	collect_btn.pressed.connect(func():
		bay.sound.ping(660.0)
		start_collect())
	root.add_child(collect_btn)
	pick_btn = bay._hud_button("PICK: ANY", Vector2(256, 1048), Vector2(208, 56), 32, "")
	pick_btn.add_theme_font_size_override("font_size", 17)
	pick_btn.visible = false
	pick_btn.pressed.connect(_cycle_pick)
	root.add_child(pick_btn)
	unload_btn = bay._hud_button("UNLOAD", Vector2(212, 1072), Vector2(176, 60), 32, "")   # right above the Maintenance Deck button (Eric 11-04)
	unload_btn.add_theme_font_size_override("font_size", 21)
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
	_panel_head(hold_panel, tr("YOUR HOLD"), func(): hold_panel.visible = false)
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
	hold_btn.text = tr("HOLD %.2f / %.2f m³") % [used, hold.cap]
	hold_fill.size.x = 220.0 * clampf(used / hold.cap, 0.0, 1.0)
	var rows := {}
	for p in cargo:
		var k: String = "flawless" if p.get("flawless", false) else p.mat
		if not rows.has(k):
			rows[k] = {"n": 0, "kg": 0.0, "box": 0.0}
		rows[k].n += 1
		rows[k].kg += p.mass
		rows[k].box += p.box
	var t := tr("%s: %s m inside (%.2f m³). Used %.2f m³ · %s aboard.\n\n") % [tr(hold.name),
		" × ".join(hold.dims.map(func(d): return "%.1f" % d)), hold.cap, used, fmt_kg(cargo.reduce(func(a, p): return a + p.mass, 0.0))]
	if cargo.is_empty():
		t += tr("Your hold is empty.") + "\n"
	for m in bay.debris.MATERIALS.map(func(x): return x[0]) + ["flawless"]:   # the near-flawless diamond is never mixed in
		if rows.has(m):
			t += "%s · %d · %s · %.3f m³\n" % [tr("💎 Near-flawless diamond") if m == "flawless" else mat_name(m), rows[m].n, fmt_kg(rows[m].kg), rows[m].box]
	t += tr("\nYOUR SPACE IN THE STARSHIP'S CARGO HOLD\n%.3f of %.2f m³ used.\n") % [store_used(), store.cap]
	for m in bay.debris.MATERIALS:
		if store.kg.get(m[0], 0.0) > 0.0:
			t += "%s · %s · %.3f m³\n" % [tr(m[1]), fmt_kg(store.kg[m[0]]), store.kg[m[0]] / float(m[2])]
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
	var sc := ScrollContainer.new()                # what moved: scrolls when there are many materials (Eric 10-24)
	sc.position = Vector2(24, 344)
	sc.size = Vector2(612, 196)
	sc.horizontal_scroll_mode = ScrollContainer.SCROLL_MODE_DISABLED
	x_panel.add_child(sc)
	x_sum = Ui.label("", 20, Ui.TEXT)
	x_sum.custom_minimum_size = Vector2(596, 0)
	sc.add_child(x_sum)
	x_rcpt = Ui.label("", 18, Ui.TEXT)
	x_rcpt.position = Vector2(24, 552)
	x_rcpt.size = Vector2(612, 170)
	x_panel.add_child(x_rcpt)
	x_save = bay._hud_button("SAVE RECEIPT", Vector2(24, 730), Vector2(300, 64), 32, "")
	x_save.pressed.connect(_save_receipt)
	x_panel.add_child(x_save)
	x_desk = bay._hud_button("GO TO MY DESK", Vector2(24, 650), Vector2(300, 64), 32, "")
	x_desk.pressed.connect(func(): get_tree().change_scene_to_file("res://scenes/quarters.tscn"))   # the market is at the Desk (rule 20)
	x_desk.visible = false
	x_panel.add_child(x_desk)
	x_rent = bay._hud_button("RENT MORE SPACE", Vector2(336, 650), Vector2(300, 64), 32, "")
	x_rent.pressed.connect(_ask_rent)
	x_rent.visible = false
	x_panel.add_child(x_rent)
	x_done = bay._hud_button("DONE", Vector2(336, 730), Vector2(300, 64), 32, "")
	x_done.pressed.connect(close_xfer)
	x_panel.add_child(x_done)


func start_unload() -> void:
	if not bay.docked or cargo.is_empty() or not xfer.is_empty():
		return
	xfer = {"t": 0.0, "per": clampf(3.5 / cargo.size(), 0.6, 1.6), "moved": {}, "n": 0, "full": false,
		"start": cargo.size(), "done": false, "wait": false, "gems": 0}
	x_title.text = tr("TRANSFERRING TO THE STARSHIP")
	x_title.add_theme_color_override("font_color", bay.HUD_RED)
	x_sum.text = ""
	x_rcpt.text = ""
	x_save.visible = false
	x_done.visible = false
	x_desk.visible = false
	x_rent.visible = false
	x_panel.visible = true
	if net:   # signed in: the cargo office (the server) does the transfer and issues the receipt; the bars then show it
		var x := xfer
		x.wait = true
		x_now.text = tr("Contacting the cargo office…")
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
		# the cargo office skips a piece too big for the space left and takes smaller ones: show those leaving first
		var ids: Array = r.data.get("moved", [])
		if not ids.is_empty():
			var first: Array = cargo.filter(func(p): return ids.has(p.get("id")))
			var rest: Array = cargo.filter(func(p): return not ids.has(p.get("id")))
			cargo = first + rest
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
	x_now.text = "" if p == null else tr("Moving %s of %s…") % [fmt_kg(p.mass), mat_name(p.mat).to_lower()]


func _render_xfer(sub: float) -> void:
	var used := maxf(0.0, bulk() - sub)
	var su := store_used()
	var all: float = SHIP_HOLD.others + su
	x_bars[0][0].size.x = 612.0 * clampf(used / hold.cap, 0.0, 1.0)
	x_bars[0][1].text = "%.2f / %.2f m³" % [used, hold.cap]
	x_bars[1][0].size.x = 612.0 * clampf(maxf(0.015 if su > 0.0 else 0.0, su / store.cap), 0.0, 1.0)
	x_bars[1][1].text = "%.3f / %.2f m³" % [su, store.cap]
	x_bars[2][0].size.x = 612.0 * all / SHIP_HOLD.cap
	x_bars[2][1].text = tr("%.1f%% full · %s m³ free") % [100.0 * all / SHIP_HOLD.cap, Solar._commas(roundi(SHIP_HOLD.cap - all))]


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
			bay._say((tr("TRANSFER COMPLETE\n%d piece moved to the Starship. Your receipt is in your quarters.") if x.n == 1 else tr("TRANSFER COMPLETE\n%d pieces moved to the Starship. Your receipt is in your quarters.")) % x.n)
		elif not x.done and not x.wait:
			_finish_xfer(true)
			bay._say(tr("TRANSFER STOPPED\n%d of %d pieces moved before you launched; the rest are still in your hold.") % [x.n, x.start])
		close_xfer()
		return
	if x.done or x.wait:
		return
	if cargo.is_empty():                          # the hold was refreshed from the server meanwhile
		_finish_xfer(false)
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
		x_title.text = tr("TRANSFER NOT MADE")
		x_now.text = tr("%s Your cargo is still in your hold.") % x.error
	elif stopped:
		x_title.text = tr("TRANSFER STOPPED")
		x_now.text = tr("You launched. %d of %d pieces moved; the rest are still in your hold.") % [x.n, x.start]
	elif x.full:
		x_desk.visible = net
		x_rent.visible = net
		x_title.text = tr("STARSHIP SPACE FULL")
		x_now.text = (tr("%d of %d pieces moved. Your space aboard is full, so %d piece stays in your hold.") if cargo.size() == 1
			else tr("%d of %d pieces moved. Your space aboard is full, so %d pieces stay in your hold.")) % [x.n, x.start, cargo.size()]

	else:
		x_title.text = tr("TRANSFER COMPLETE")
		x_title.add_theme_color_override("font_color", Color("7fe0a8"))
		Voice.say("unloaded")
		if x.has("server"):
			Voice.story(bay.hud_root, "unload")
		x_now.text = (tr("All %d piece is aboard the Starship. Your hold is empty.") if x.n == 1 else tr("All %d pieces are aboard the Starship. Your hold is empty.")) % x.n
		bay.sound.chime()
	var sum := ""
	for m in bay.debris.MATERIALS:
		if x.moved.has(m[0]):
			sum += "%s · + %s\n" % [tr(m[1]), fmt_kg(x.moved[m[0]])]
	if x.gems > 0:
		sum += tr("💎 Near-flawless diamond · + %d to your lockbox") % x.gems + "\n"
	if x.full and net:   # Inara steps in (Eric 11-04, rule 10): sell at the Desk's Market terminal, or rent more space
		sum = tr("Inara: Let's free up some room, Pilot. Sell some of what you've stored at the Market terminal at your desk, or rent more space from the Starship: double the space for 10,000 credits a week.") + "\n\n" + sum
	x_sum.text = sum
	if x.has("server"):
		_apply_inventory(x.server.get("inventory", {}))   # the server's figures are the truth
	if x.n > 0:
		var sr: Dictionary = x.server.get("receipt", {}) if x.has("server") else {}
		var rc := {"code": sr.code, "at": _when(str(sr.get("issued_at", ""))), "pieces": int(sr.pieces), "left": int(sr.get("left_aboard", 0)),
			"kg": sr.get("kg", {}), "used": float(sr.space_used_m3), "total": float(sr.space_total_m3), "server": true} if not sr.is_empty() \
			else {"code": _receipt_code(), "at": _when(""), "pieces": x.n, "left": cargo.size(),
			"kg": x.moved, "used": store_used(), "total": store.cap, "server": false}
		x.receipt = rc
		x_rcpt.text = tr("RECEIPT %s · %s\n%s from your ship's hold to your space in the Starship's cargo hold%s. Your space after: %.3f of %.2f m³ used.\n%s") % [
			rc.code, rc.at, (tr("%d piece") if rc.pieces == 1 else tr("%d pieces")) % rc.pieces, tr(" (%d left aboard)") % rc.left if rc.left else "",
			rc.used, rc.total, tr("Issued by the Starship's cargo office (the game server). Anyone can check this code. A copy is in your quarters, in the filing cabinet.") if rc.server
			else tr("PROTOTYPE RECEIPT: made without a sign-in, so this code cannot be checked.")]
		x_save.visible = true
	x_done.visible = true


## A receipt's time in the player's own time zone, e.g. "Oct 24, 2026 · 7:35 AM" (the server sends UTC).
static func _when(iso: String) -> String:
	var t := Time.get_unix_time_from_system()
	if iso != "":
		t = Time.get_unix_time_from_datetime_string(iso.substr(0, 19))   # UTC, without fractions or offset
	t += Time.get_time_zone_from_system().bias * 60
	var d := Time.get_datetime_dict_from_unix_time(int(t))
	var mon: String = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"][d.month - 1]
	var h: int = d.hour % 12
	return "%s %d, %d · %d:%02d %s" % [mon, d.day, d.year, 12 if h == 0 else h, d.minute, "PM" if d.hour >= 12 else "AM"]


func _receipt_code() -> String:
	var c := ""
	for i in 8:
		c += RCPT_CHARS[randi() % RCPT_CHARS.length()]
	return "WSC-" + c.substr(0, 4) + "-" + c.substr(4)


func receipt_text(rc: Dictionary) -> String:
	var L := [tr("WORLD SPACE CONSORTIUM"), tr("WSC Alexander von Humboldt · Cargo office"), "", tr("RECEIPT %s") % rc.code, tr("Issued: %s") % rc.at,
		tr("Transfer: %s from your ship's hold to your space in the Starship's cargo hold") % ((tr("%d piece") if rc.pieces == 1 else tr("%d pieces")) % rc.pieces)]
	if rc.left:
		L.append(tr("Left aboard your ship: %s") % ((tr("%d piece") if rc.left == 1 else tr("%d pieces")) % rc.left))
	L.append_array(["", tr("Material                 Weight")])
	for m in rc.kg:
		L.append((mat_name(m) + "                         ").substr(0, 25) + fmt_kg(float(rc.kg[m])))
	L.append_array(["", tr("Your space after: %.3f of %.2f m³ used") % [rc.used, rc.total], ""])
	if rc.server:
		L.append_array([tr("Issued by the game server. Anyone can check this code at:"), Api.BASE_URL + "/api/dfg/receipt/" + rc.code, ""])
	else:
		L.append_array([tr("PROTOTYPE RECEIPT: made without a sign-in, so this code cannot be checked."), ""])
	return "\n".join(L)


## Save a copy to the player's own device (rule 13), in Documents › Stardust Receipts (Ui.save_receipt).
func _save_receipt() -> void:
	var rc: Dictionary = xfer.get("receipt", {})
	if rc.is_empty():
		return
	Ui.save_receipt(self, rc.code, receipt_text(rc), func(path: String):
		if path != "":
			bay._say(tr("RECEIPT SAVED\n%s is in %s on your device, and in the filing cabinet in your quarters.") % [rc.code, path.get_base_dir().get_file()])
		else:
			bay._say(tr("COULDN'T SAVE\nYour receipt is still in the filing cabinet in your quarters. Try again from there.")))


## Rent more cargo space from the Starship (Eric 11-04, rule 10): doubles the space for 10,000 credits a week, to the WSC.
func _ask_rent() -> void:
	var st: Dictionary = await Api.call_api("GET", "/api/dfg/storage")
	if not st.ok:
		bay._say(st.error)
		return
	if st.data.get("rental") != null:
		bay._say(tr("You already rent extra cargo space."))
		return
	Ui.dialog(bay.hud_root, tr("Rent more cargo space"),
		tr("%s m³ more for %s credits a week, paid to the WSC each week until you cancel it. You have %s credits.") % [
			Ui.dec(float(st.data.adds_m3), 0), Ui.num(int(st.data.weekly)), Ui.num(int(st.data.credits))],
		[["Not now", false, Callable()], ["Rent it", true, _rent]])


func _rent() -> void:
	var r: Dictionary = await Api.call_api("POST", "/api/dfg/storage/rent", {})
	if not r.ok:
		bay._say(r.error)
		return
	store.cap = float(r.data.capacity_m3)
	x_rent.visible = false
	x_sum.text = tr("Rented: your space aboard is now %s m³. Tap UNLOAD again to move the rest.") % Ui.dec(store.cap, 0)
	_render_xfer(0.0)


func close_xfer() -> void:
	x_panel.visible = false
	xfer = {}


## Step through the materials still in this field (then ANY). Only for a Science uniform with its fifth bar gold.
func _cycle_pick() -> void:
	var f = bay.lock.get("field") if bay.lock.get("parked", false) else null
	if f == null:
		return
	var mats: Array = [""]
	for p in f.pieces:
		if not p.taken and not mats.has(p.mat):
			mats.append(p.mat)
	pick = mats[(mats.find(pick) + 1) % mats.size()]
	pick_btn.text = tr("PICK: %s") % (tr("ANY") if pick == "" else bay.debris.material(pick)[1].split(" (")[0].to_upper())
	bay.sound.ping(520.0)
