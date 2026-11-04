extends Control
## The Maintenance Deck (Eric 11-03, rule 25), up from the docking bay: where the mining craft are serviced, with a
## partitioned smelting area. Each player has a space here. Build an approved design you hold (the original or a copy)
## from the materials in your cargo hold; it stands here when its build time has passed, in real time. A furnace on
## the deck smelts ore from your cargo hold (Metallurgy pass): each metal's share by weight, the rest slag (rule 27).
## The Starship gives the space and the power. Every machine here is a player's own blueprint (rule 11).

var body: VBoxContainer
var msg: Label
var data: Dictionary = {}
var busy := false


func _ready() -> void:
	var box := Ui.screen(self)
	var top := HBoxContainer.new()
	box.add_child(top)
	var back := Ui.button("◀ Docking Bay", false)
	back.custom_minimum_size = Vector2(220, 64)
	back.pressed.connect(func(): get_tree().change_scene_to_file("res://scenes/bay.tscn"))
	top.add_child(back)
	var t := Ui.label("  MAINTENANCE DECK", 32, Ui.GOLD)
	t.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	top.add_child(t)
	msg = Ui.label("", 22, Ui.GOLD)
	msg.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	box.add_child(msg)
	var scroll := ScrollContainer.new()
	scroll.size_flags_vertical = Control.SIZE_EXPAND_FILL
	scroll.horizontal_scroll_mode = ScrollContainer.SCROLL_MODE_DISABLED
	box.add_child(scroll)
	body = VBoxContainer.new()
	body.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	body.add_theme_constant_override("separation", 14)
	scroll.add_child(body)
	_load()


func _load() -> void:
	var r: Dictionary = await Api.call_api("GET", "/api/dfg/deck")
	if not r.ok:
		msg.text = r.error
		return
	data = r.data
	_render()


func _act(op: String, payload: Dictionary, done: String) -> void:
	if busy:
		return
	busy = true
	var r: Dictionary = await Api.call_api("POST", "/api/dfg/deck/" + op, payload)
	busy = false
	if not r.ok:
		msg.text = r.error
		return
	msg.text = done % Ui.when(str(r.data.get("ready_at", "")))
	data = r.data.deck
	_render()


func _text(t: String, size := 22, c := Ui.TEXT) -> Label:
	var l := Ui.label(t, size, c)
	l.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	return l


func _heading(t: String) -> void:
	body.add_child(Ui.label(t, 26, Ui.GOLD))


func _small_button(t: String, primary := true) -> Button:
	var b := Ui.button(t, primary)
	b.custom_minimum_size = Vector2(0, 64)
	b.add_theme_font_size_override("font_size", 22)
	b.clip_text = true                       # never wider than the screen
	return b


func _kg(v: float) -> String:
	return (Ui.dec(v / 1000.0, 2) + " t") if v >= 1000.0 else (Ui.dec(v, 1) + " kg")


func _render() -> void:
	for c in body.get_children():
		c.queue_free()
	var d := data
	body.add_child(_text(tr("Your space here: %s of %s m³ used. The Starship supplies the power.") % [Ui.dec(d.used_m3, 2), Ui.dec(d.capacity_m3, 0)], 22, Ui.MUTED))
	_machines(d)
	_jobs(d)
	_buildable(d)


func _machines(d: Dictionary) -> void:
	_heading(tr("ON YOUR DECK"))
	if d.machines.is_empty():
		body.add_child(_text(tr("Nothing built yet. Build a design you hold, below."), 22, Ui.MUTED))
		return
	var running := {}
	for j in d.jobs:
		if j.kind == "smelt" and not j.done:
			running[int(j.detail.furnace)] = j
	for m in d.machines:
		body.add_child(_text("• " + str(m.name), 24))
		if m.furnace == null:
			continue
		var f: Dictionary = m.furnace
		body.add_child(_text(tr("Furnace: up to %s of ore a batch, %d minutes a batch.") % [_kg(f.batch_kg), int(f.minutes)], 20, Ui.MUTED))
		if running.has(int(m.id)):
			var j: Dictionary = running[int(m.id)]
			body.add_child(_text(tr("Smelting %s of %s, ready %s.") % [_kg(j.detail.kg), tr(str(j.detail.ore_name)), Ui.when(j.ready_at)], 20, Ui.GREEN))
			continue
		if not d.metallurgy:
			body.add_child(_text(tr("Pass the Metallurgy test in the Starship Library before you smelt."), 20, Ui.MUTED))
			continue
		if d.ores.is_empty():
			body.add_child(_text(tr("No ore in your space in the cargo hold to smelt."), 20, Ui.MUTED))
			continue
		for o in d.ores:
			var kg: float = minf(float(o.kg), float(f.batch_kg))
			var gives: Array = []
			for code in o.gives_pct:
				gives.append("%s%% %s" % [Ui.dec(o.gives_pct[code], 1), tr(str(code).trim_prefix("mat-").capitalize())])
			var b := _small_button(tr("Smelt %s of %s") % [_kg(kg), tr(str(o.name))], false)
			var fid := int(m.id)
			var ore := str(o.ore)
			b.pressed.connect(func(): _act("smelt", {"furnace": fid, "ore": ore, "kg": kg}, tr("Loaded. The batch is ready %s; the metal and slag go to your cargo hold.")))
			body.add_child(b)
			body.add_child(_text(tr("Gives %s; the rest is slag.") % ", ".join(gives), 18, Ui.MUTED))


func _jobs(d: Dictionary) -> void:
	var builds: Array = d.jobs.filter(func(j): return j.kind == "build" and not j.done)
	if builds.is_empty():
		return
	_heading(tr("BEING BUILT"))
	for j in builds:
		body.add_child(_text(tr("%s, ready %s.") % [tr(str(j.detail.name)), Ui.when(j.ready_at)], 22, Ui.GREEN))


func _buildable(d: Dictionary) -> void:
	_heading(tr("BUILD FROM YOUR BLUEPRINTS"))
	if d.buildable.is_empty():
		body.add_child(_text(tr("You hold no approved blueprints yet. Design one in the drafting room at the Starship Library, or win a copy at auction."), 22, Ui.MUTED))
		return
	for b in d.buildable:
		body.add_child(_text(str(b.name) + ("   " + str(b.model) if b.model else ""), 24))
		var lines: Array = []
		for m in b.materials:
			lines.append(tr("%s: needs %s, you have %s") % [tr(str(m.name)), _kg(m.kg), _kg(m.have_kg)])
		for k in b.books:
			lines.append(tr("Library test: %s (%s)") % [tr(str(k.title)), tr("passed") if k.passed else tr("not passed yet")])
		lines.append(tr("Build time: %d minutes") % int(b.minutes))
		body.add_child(_text("\n".join(lines), 20, Ui.MUTED))
		var btn := _small_button(tr("Build it"), b.ready)
		btn.disabled = not b.ready
		var code := str(b.design)
		btn.pressed.connect(func(): _act("build", {"design": code}, tr("Building. It will stand on your deck %s.")))
		body.add_child(btn)
