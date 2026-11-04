extends Control
## The drafting room at the Starship Library (rule 23, Eric 10-11; ported from static/quarters.js 11-04): the blueprint
## form as a series of questions, not a blank page. Players design; the game's review team reads every submission and
## may ask questions or request changes before approving it. Weight and size come from the real densities of the
## materials (the server works them out), never typed in. Designs are kept in the filing cabinet; an approved one is
## built at the Maintenance Deck.

const STATUS := {"draft": "Draft: only you can see it", "submitted": "With the review team",
	"changes_requested": "Changes requested: see the review team's note", "approved": "Approved", "rejected": "Not approved"}
const UNITS := [["minutes", 1], ["hours", 60], ["days", 1440]]

var body: VBoxContainer
var msg: Label
var opts: Dictionary = {}
var dens := {}
var d: Dictionary = {}              # the design open now ({} = a new one)
var w := {}                         # the form's inputs
var parts_box: VBoxContainer
var total_lbl: Label
var busy := false
# Easier to fill in on a phone (Eric 11-04: "I missed the name the first time … I spent a lot of time and even lost
# some text trying to remove the keypad and slide the page lower"): every box to fill in is tinted with a gold edge;
# a wide gold scroll bar; drag anywhere on the page to scroll (even over a box); tap a box to type in it, tap anywhere
# else to put the keyboard away; the page keeps the box you're typing in above the keyboard; drafts save themselves.
var scroll: ScrollContainer
var spacer: Control
var press_at := Vector2.ZERO
var pressing := false
var dragging := false
var dirty := false
var kb_h := -1.0
const DRAG_START := 14.0
const FILL := Color("1c2740")
const FILL_FOCUS := Color("24324f")


func _ready() -> void:
	var box := Ui.screen(self)
	var top := HBoxContainer.new()
	box.add_child(top)
	var back := Ui.button("◀ Library", false)
	back.custom_minimum_size = Vector2(190, 64)
	back.pressed.connect(func():
		await _autosave()
		get_tree().change_scene_to_file("res://scenes/library.tscn"))
	top.add_child(back)
	var t := Ui.label("  DRAFTING ROOM", 32, Ui.GOLD)
	t.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	top.add_child(t)
	scroll = ScrollContainer.new()
	scroll.size_flags_vertical = Control.SIZE_EXPAND_FILL
	scroll.horizontal_scroll_mode = ScrollContainer.SCROLL_MODE_DISABLED
	box.add_child(scroll)
	_wide_bar(scroll.get_v_scroll_bar())
	get_tree().node_added.connect(_on_node_added)
	var t_auto := Timer.new()
	t_auto.wait_time = 15.0
	t_auto.autostart = true
	t_auto.timeout.connect(_autosave)
	add_child(t_auto)
	body = VBoxContainer.new()
	body.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	body.add_theme_constant_override("separation", 14)
	var pad := MarginContainer.new()          # keeps the text clear of the wide scroll bar
	pad.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	pad.add_theme_constant_override("margin_right", 60)
	pad.mouse_filter = Control.MOUSE_FILTER_PASS
	scroll.add_child(pad)
	pad.add_child(body)
	_list()


func _clear() -> void:
	for c in body.get_children():
		c.queue_free()


func _text(s: String, size := 22, c := Ui.TEXT) -> Label:
	var l := Ui.label(s, size, c)
	l.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	return l


func _small(s: String, primary := false) -> Button:
	var b := Ui.button(s, primary)
	b.custom_minimum_size = Vector2(0, 60)
	b.add_theme_font_size_override("font_size", 22)
	b.clip_text = true
	return b


## My blueprints, and a button to start a new one.
func _list() -> void:
	_clear()
	body.add_child(_text("Loading…", 22, Ui.MUTED))
	var r := await Api.call_api("GET", "/api/dfg/blueprints")
	_clear()
	body.add_child(_text("You design it; the game's review team checks it. Only an approved blueprint can be built and sold. Your designs are kept in your filing cabinet.", 22, Ui.MUTED))
	var nb := Ui.button("📐 Design a new blueprint")
	nb.pressed.connect(func(): _open(0))
	body.add_child(nb)
	body.add_child(Ui.label("MY BLUEPRINTS", 26, Ui.GOLD))
	if not r.ok:
		body.add_child(_text(r.error, 22, Ui.GOLD))
		return
	var list: Array = r.data.get("blueprints", [])
	if list.is_empty():
		body.add_child(_text("No blueprints yet.", 22, Ui.MUTED))
	for b in list:
		var sub := tr(STATUS.get(b.status, str(b.status)))
		if int(b.get("version", 0)):
			sub += " · " + tr("version %d") % int(b.version)
		var btn := _small("📐 " + str(b.title) + "   ·   " + sub)
		var id := int(b.id)
		btn.pressed.connect(func(): _open(id))
		body.add_child(btn)


func _open(id: int) -> void:
	if opts.is_empty():
		var o := await Api.call_api("GET", "/api/dfg/blueprints/options")
		if not o.ok:
			Ui.error(self, o.error)
			return
		opts = o.data
		for m in opts.materials:
			dens[m.code] = float(m.density_kg_m3)
	d = {}
	if id:
		var r := await Api.call_api("GET", "/api/dfg/blueprints/%d" % id)
		if not r.ok:
			Ui.error(self, r.error)
			return
		d = r.data
	_form()


func _q(n: int, title: String, hint := "") -> void:
	body.add_child(Ui.label("%d.  %s" % [n, tr(title)], 24, Ui.GOLD))
	if hint != "":
		body.add_child(_text(hint, 19, Ui.MUTED))


func _area(key: String, ph: String, f: Dictionary, edit: bool) -> TextEdit:
	var e := TextEdit.new()
	e.placeholder_text = tr(ph)
	e.text = str(f.get(key, "") if f.get(key) != null else "")
	e.custom_minimum_size = Vector2(0, 150)
	e.wrap_mode = TextEdit.LINE_WRAPPING_BOUNDARY
	e.add_theme_font_size_override("font_size", 22)
	e.editable = edit
	body.add_child(e)
	w[key] = e
	return e


func _pick(items: Array, sel: String, edit: bool, first := "Choose one…") -> WheelPicker:
	var p := Ui.picker()
	p.add_item(tr(first))
	p.set_item_metadata(0, "")
	for it in items:
		p.add_item(tr(str(it[1])))
		p.set_item_metadata(p.item_count - 1, it[0])
		if str(it[0]) == sel:
			p.select(p.item_count - 1)
	p.disabled = not edit
	return p


func _form() -> void:
	_clear()
	w = {}
	var f: Dictionary = d.get("form", {})
	var edit: bool = d.is_empty() or bool(d.get("editable", false))
	body.add_child(Ui.label(str(d.title) if d.has("title") else tr("New blueprint"), 30, Ui.TEXT))
	var st := tr("Answer each question. You can save a draft and come back any time.")
	if not d.is_empty():
		st = tr(STATUS.get(d.status, str(d.status))) + ((" · " + tr("version %d") % int(d.version)) if int(d.get("version", 0)) else "")
	body.add_child(_text(st, 20, Ui.MUTED))
	if d.get("model"):
		body.add_child(_text(tr("Model %s. Build it at the Maintenance Deck; print copies and auction them from your filing cabinet's design.") % str(d.model), 20, Ui.GREEN))
	_notes()
	msg = _text("", 22, Ui.GOLD)

	_q(1, "What is it called, and what kind of thing is it?")
	body.add_child(_text("Its name", 20, Ui.MUTED))
	var name := Ui.field("e.g. Clay brick kiln")
	name.text = str(f.get("name", "") if f.get("name") != null else "")
	name.max_length = int(opts.limits.text.name)
	name.editable = edit
	body.add_child(name)
	w.name = name
	var kinds: Array = opts.kinds.map(func(k): return [k.code, k.name])
	body.add_child(_text("What kind of thing it is", 20, Ui.MUTED))
	w.kind = _pick(kinds, str(f.get("kind", "")), edit, "Choose the kind…")
	body.add_child(w.kind)

	_q(2, "Is it brand new, an upgrade, or a newer version or model?")
	w.origin = _pick(opts.origins.map(func(o): return [o.code, o.name]), str(f.get("origin", "")), edit)
	body.add_child(w.origin)
	var base_box := VBoxContainer.new()
	base_box.add_theme_constant_override("separation", 10)
	body.add_child(base_box)
	base_box.add_child(_text("What does it build on?", 20, Ui.MUTED))
	w.based_on = _pick(opts.bases.map(func(b): return [b.code, str(b.name) + ("  (" + tr("Starship standard") + ")" if b.from == "Starship standard" else "")]), str(f.get("based_on", "")), edit, "Choose…")
	base_box.add_child(w.based_on)
	base_box.add_child(_text("What's different from it?", 20, Ui.MUTED))
	var ch := TextEdit.new()
	ch.text = str(f.get("changes", "") if f.get("changes") != null else "")
	ch.custom_minimum_size = Vector2(0, 120)
	ch.wrap_mode = TextEdit.LINE_WRAPPING_BOUNDARY
	ch.add_theme_font_size_override("font_size", 22)
	ch.editable = edit
	base_box.add_child(ch)
	w.changes = ch
	var show_base := func(_i := 0): base_box.visible = str(w.origin.get_item_metadata(w.origin.selected)) in ["upgrade", "version"]
	w.origin.item_selected.connect(show_base)
	show_base.call()

	_q(3, "What is it, and what problem does it solve?", tr("Who needs it, and why?"))
	_area("problem", "e.g. Nothing aboard can heat ore hot enough to smelt it.", f, edit)
	_q(4, "Everything it does, in detail.", tr("Describe each thing it does and how. The review team reads this closely."))
	_area("does", "e.g. A box of dried clay bricks with a coil inside, heated by the Starship's power…", f, edit)
	_q(5, "What does it fit?", tr("A ship, a machine, or \"stands alone\"."))
	_area("fits", "e.g. Stands alone on the Maintenance Deck", f, edit)
	_q(6, "What does it improve, and by how much?")
	_area("improves", "e.g. Makes smelting possible", f, edit)

	_q(7, "Which library books does it require?", tr("To build it, you pass the short test on each one."))
	var chosen: Array = f.get("books", []) if f.get("books") != null else []
	w.books = []
	for g in opts.books:
		body.add_child(_text(str(g.group), 20, Ui.MUTED))
		for b in g.books:
			var cb := CheckBox.new()
			cb.text = tr(str(b.name))
			cb.button_pressed = chosen.has(b.code)
			cb.disabled = not edit
			cb.add_theme_font_size_override("font_size", 22)
			cb.set_meta("code", b.code)
			body.add_child(cb)
			w.books.append(cb)

	_q(8, "Its parts and materials", tr("Most designs need only one part: name it, then list every material it's made of and how much. Add another part only for a piece made separately. Weight and size are worked out from the real materials."))
	parts_box = VBoxContainer.new()
	parts_box.add_theme_constant_override("separation", 12)
	body.add_child(parts_box)
	var plist: Array = f.get("parts", []) if f.get("parts") != null else []
	if plist.is_empty():
		plist = [{}]
	for p in plist:
		_part(p, edit)
	if edit:
		var addp := _small("+ Add another part (made separately)")
		addp.pressed.connect(func(): _part({}, true))
		body.add_child(addp)
	total_lbl = _text("", 22, Ui.TEXT)
	body.add_child(total_lbl)
	_total()

	_q(9, "How is it built?", tr("The tools, the skills and the steps."))
	_area("how", "e.g. Lay the bricks, wind the coil inside, connect it to ship power.", f, edit)

	_q(10, "How long does it take to build?", tr("Builds run in real time."))
	var row := HBoxContainer.new()
	row.add_theme_constant_override("separation", 12)
	body.add_child(row)
	var bm := int(f.get("build_minutes", 0) if f.get("build_minutes") != null else 0)
	var unit := "days" if bm and bm % 1440 == 0 else ("hours" if (bm and bm % 60 == 0) or not bm else "minutes")
	var mult := {"minutes": 1, "hours": 60, "days": 1440}
	var tf := Ui.field("")
	tf.text = str(bm / mult[unit]) if bm else ""
	tf.custom_minimum_size = Vector2(160, 0)
	tf.editable = edit
	row.add_child(tf)
	w.time = tf
	var up := Ui.picker()
	for u in UNITS:
		up.add_item(tr(u[0]))
		up.set_item_metadata(up.item_count - 1, u[0])
		if u[0] == unit:
			up.select(up.item_count - 1)
	up.disabled = not edit
	up.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	row.add_child(up)
	w.unit = up

	body.add_child(msg)
	if edit:
		var save := Ui.button("Save draft", false)
		save.pressed.connect(_save)
		body.add_child(save)
		var send := Ui.button("Send to the review team")
		send.pressed.connect(_submit)
		body.add_child(send)
	if not d.is_empty() and d.status in ["draft", "submitted", "changes_requested"]:
		var wd := _small("Withdraw this blueprint")
		wd.pressed.connect(_withdraw)
		body.add_child(wd)
	var back := _small("Back to my blueprints")
	back.pressed.connect(func():
		await _autosave()
		_list())
	body.add_child(back)
	_add_spacer()
	dirty = false


func _notes() -> void:
	var notes: Array = d.get("messages", [])
	if not notes.is_empty():
		body.add_child(Ui.label("NOTES WITH THE REVIEW TEAM", 24, Ui.GOLD))
		for m in notes:
			body.add_child(_text("%s · %s\n%s" % [tr(str(m.from)), tr("version %d") % int(m.version), str(m.body)], 20,
				Ui.TEXT if m.from == "You" else Ui.GREEN))
	if not d.is_empty() and d.status in ["submitted", "changes_requested"]:
		var r := TextEdit.new()
		r.placeholder_text = tr("Answer the review team")
		r.custom_minimum_size = Vector2(0, 110)
		r.wrap_mode = TextEdit.LINE_WRAPPING_BOUNDARY
		r.add_theme_font_size_override("font_size", 22)
		body.add_child(r)
		var sb := _small("Send answer")
		sb.pressed.connect(func(): _reply(r.text))
		body.add_child(sb)


## One part: its name and its material rows (material, kg).
## Each part is its own card (Eric 11-04: the part's name box looked like one more material): PART 1, its name, then
## "What it's made of" with one line per material.
func _part(p: Dictionary, edit: bool) -> void:
	var card := PanelContainer.new()
	var cs := StyleBoxFlat.new()
	cs.bg_color = Ui.PANEL
	cs.border_color = Color(Ui.GOLD, 0.35)
	cs.set_border_width_all(1)
	cs.set_corner_radius_all(12)
	cs.content_margin_left = 16
	cs.content_margin_right = 16
	cs.content_margin_top = 14
	cs.content_margin_bottom = 14
	card.add_theme_stylebox_override("panel", cs)
	card.mouse_filter = Control.MOUSE_FILTER_PASS
	parts_box.add_child(card)
	var box := VBoxContainer.new()
	box.add_theme_constant_override("separation", 8)
	card.add_child(box)
	var head := Ui.label("", 22, Ui.GOLD)
	box.add_child(head)
	card.set_meta("head", head)
	box.add_child(_text("What this part is called", 20, Ui.MUTED))
	var pn := Ui.field("e.g. Kiln body")
	pn.text = str(p.get("name", "") if p.get("name") != null else "")
	pn.editable = edit
	box.add_child(pn)
	card.set_meta("name", pn)
	box.add_child(_text("What it's made of, and how much", 20, Ui.MUTED))
	var rows := VBoxContainer.new()
	rows.add_theme_constant_override("separation", 8)
	box.add_child(rows)
	card.set_meta("rows", rows)
	_renumber.call_deferred()
	var mats: Array = p.get("materials", []) if p.get("materials") != null else []
	if mats.is_empty():
		mats = [{}]
	for m in mats:
		_mat_row(rows, m, edit)
	if edit:
		var h := HBoxContainer.new()
		box.add_child(h)
		var am := _small("+ Another material")
		am.size_flags_horizontal = Control.SIZE_EXPAND_FILL
		am.pressed.connect(func(): _mat_row(rows, {}, true))
		h.add_child(am)
		var rp := _small("Remove this part")
		rp.size_flags_horizontal = Control.SIZE_EXPAND_FILL
		rp.pressed.connect(func(): card.queue_free(); _total.call_deferred(); _renumber.call_deferred())
		h.add_child(rp)


func _mat_row(rows: VBoxContainer, m: Dictionary, edit: bool) -> void:
	var h := HBoxContainer.new()
	h.add_theme_constant_override("separation", 8)
	rows.add_child(h)
	var items := []
	for x in opts.materials:
		items.append([x.code, tr(str(x.name)) + "  ·  " + tr(str(x.category))])
	var mp := _pick(items, str(m.get("item", "")), edit, "Choose a material…")
	mp.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	mp.item_selected.connect(func(_i): _total())
	h.add_child(mp)
	var kg := Ui.field("kg")
	kg.custom_minimum_size = Vector2(130, 0)
	kg.text = str(float(m.grams) / 1000.0) if m.get("grams") != null else ""
	kg.editable = edit
	kg.text_changed.connect(func(_t): _total())
	h.add_child(kg)
	h.set_meta("mat", mp)
	h.set_meta("kg", kg)
	if edit:
		var x := _small("✕")
		x.custom_minimum_size = Vector2(64, 60)
		x.pressed.connect(func(): h.queue_free(); _total.call_deferred())
		h.add_child(x)


func _gather() -> Dictionary:
	var form := {}
	for k in ["problem", "does", "fits", "improves", "how", "changes"]:
		if w.has(k):                  # the form is still being laid out when the first totals are drawn
			form[k] = w[k].text
	form.name = w.name.text
	for k in ["kind", "origin", "based_on"]:
		var v = w[k].get_item_metadata(w[k].selected)
		if str(v) != "":
			form[k] = v
	form.books = []
	for cb in w.books:
		if cb.button_pressed:
			form.books.append(cb.get_meta("code"))
	form.parts = []
	for box in parts_box.get_children():
		if box.is_queued_for_deletion():
			continue
		var mats := []
		for h in box.get_meta("rows").get_children():
			if h.is_queued_for_deletion():
				continue
			var code = h.get_meta("mat").get_item_metadata(h.get_meta("mat").selected)
			if str(code) == "":
				continue
			var t: String = h.get_meta("kg").text.replace(",", ".").strip_edges()
			mats.append({"item": code, "grams": (roundi(float(t) * 1000.0) if t != "" else null)})
		var pname: String = box.get_meta("name").text
		if pname.strip_edges() != "" or not mats.is_empty():
			form.parts.append({"name": pname, "materials": mats})
	if not w.has("unit"):
		return form
	var tv := float(w.time.text.replace(",", ".")) if w.time.text.strip_edges() != "" else 0.0
	var mult := {"minutes": 1, "hours": 60, "days": 1440}
	var u := str(w.unit.get_item_metadata(w.unit.selected))
	if tv > 0:
		form.build_minutes = maxi(1, roundi(tv * mult.get(u, 60)))
	return form


func _total() -> void:
	if total_lbl == null or not is_instance_valid(total_lbl):
		return
	var kg := 0.0
	var m3 := 0.0
	for p in _gather().parts:
		for m in p.materials:
			if m.grams != null and m.grams > 0 and dens.has(m.item):
				kg += m.grams / 1000.0
				m3 += m.grams / 1000.0 / dens[m.item]
	total_lbl.text = tr("Weight %s · Material volume %s m³ (from the real density of each material)") % [
		(Ui.dec(kg / 1000.0, 3) + " t") if kg >= 1000.0 else (Ui.dec(kg, 3) + " kg"), Ui.dec(m3, 4)]


func _save() -> void:
	if busy:
		return
	busy = true
	var payload := {"form": _gather()}
	if not d.is_empty():
		payload.id = d.id
	var r := await Api.call_api("POST", "/api/dfg/blueprints/save", payload)
	busy = false
	if not r.ok:
		msg.text = r.error
		return
	d = r.data
	dirty = false
	_form()
	var miss: Array = d.get("missing", [])
	msg.text = tr("Saved. Ready to send to the review team.") if miss.is_empty() else tr("Saved. Still to answer: %s.") % ", ".join(miss.map(_missing_text))


func _submit() -> void:
	if busy:
		return
	busy = true
	var form := _gather()
	var id := int(d.get("id", 0))
	if not id:
		var s := await Api.call_api("POST", "/api/dfg/blueprints/save", {"form": form})
		if not s.ok:
			busy = false
			msg.text = s.error
			return
		id = int(s.data.id)
	var r := await Api.call_api("POST", "/api/dfg/blueprints/submit", {"id": id, "form": form})
	busy = false
	var dr := await Api.call_api("GET", "/api/dfg/blueprints/%d" % id)
	if dr.ok:
		d = dr.data
		_form()
	if not r.ok:
		msg.text = r.error
		return
	msg.text = tr("Sent. The review team will read it, and any questions or changes will appear here.")
	Voice.say("submitted")
	Voice.story(self, "blueprint")


func _reply(text: String) -> void:
	if text.strip_edges() == "":
		return
	var r := await Api.call_api("POST", "/api/dfg/blueprints/reply", {"id": d.id, "body": text})
	if not r.ok:
		msg.text = r.error
		return
	await _open(int(d.id))
	msg.text = tr("Sent to the review team.")


func _withdraw() -> void:
	var r := await Api.call_api("POST", "/api/dfg/blueprints/withdraw", {"id": d.id})
	if not r.ok:
		msg.text = r.error
		return
	_list()


## The scroll bar, wide enough to grab with a thumb, with a gold handle.
func _wide_bar(bar: VScrollBar) -> void:
	bar.custom_minimum_size.x = 44
	var track := StyleBoxFlat.new()
	track.bg_color = Ui.PANEL
	track.set_corner_radius_all(14)
	track.content_margin_left = 6
	track.content_margin_right = 6
	bar.add_theme_stylebox_override("scroll", track)
	bar.add_theme_stylebox_override("scroll_focus", track)
	for k in ["grabber", "grabber_highlight", "grabber_pressed"]:
		var g := StyleBoxFlat.new()
		g.bg_color = Ui.GOLD if k == "grabber" else Ui.GOLD.lightened(0.2)
		g.set_corner_radius_all(12)
		g.content_margin_left = 16
		g.content_margin_right = 16
		bar.add_theme_stylebox_override(k, g)


## Room below the form for the keyboard, so the last boxes can be scrolled up above it.
func _add_spacer() -> void:
	spacer = Control.new()
	spacer.mouse_filter = Control.MOUSE_FILTER_IGNORE
	body.add_child(spacer)
	kb_h = -1.0


func _fill_style(c: Color, edge: float, wide: int) -> StyleBoxFlat:
	var st := StyleBoxFlat.new()
	st.bg_color = c
	st.border_color = Color(Ui.GOLD, edge)
	st.set_border_width_all(wide)
	st.set_corner_radius_all(10)
	st.content_margin_left = 16
	st.content_margin_right = 16
	st.content_margin_top = 10
	st.content_margin_bottom = 10
	return st


## Every box to fill in: tinted, with a gold edge (brighter while typing in it), so none is missed.
func _on_node_added(n: Node) -> void:
	if not body or not body.is_ancestor_of(n):
		return
	if n is LineEdit or n is TextEdit:
		_setup_box.call_deferred(n)
	elif n is WheelPicker:
		n.item_selected.connect(func(_i): dirty = true)
	elif n is CheckBox:
		n.toggled.connect(func(_on): dirty = true)


func _setup_box(e: Control) -> void:
	if not is_instance_valid(e):
		return
	var on: bool = e.editable
	if on:
		e.add_theme_stylebox_override("normal", _fill_style(FILL, 0.55, 2))
		e.add_theme_stylebox_override("focus", _fill_style(FILL_FOCUS, 1.0, 3))
	e.add_theme_color_override("font_placeholder_color", Color(Ui.MUTED, 0.7))
	# A box takes touches only while it is being typed in; otherwise a drag over it scrolls the page.
	e.mouse_filter = Control.MOUSE_FILTER_IGNORE
	e.focus_entered.connect(func():
		e.mouse_filter = Control.MOUSE_FILTER_STOP
		_show_box.call_deferred(e))
	e.focus_exited.connect(func(): e.mouse_filter = Control.MOUSE_FILTER_IGNORE)
	if on:
		e.text_changed.connect(func(_t = null): dirty = true)


## Bring the box being typed in near the top of the page, clear of the keyboard.
func _show_box(e: Control) -> void:
	if is_instance_valid(e) and scroll and e.is_inside_tree():
		var y := e.global_position.y - body.global_position.y
		scroll.scroll_vertical = int(maxf(0.0, y - 110.0))


func _boxes(n: Node, out: Array) -> Array:
	for c in n.get_children():
		if (c is LineEdit or c is TextEdit) and c.is_visible_in_tree() and c.editable:
			out.append(c)
		_boxes(c, out)
	return out


func _input(ev: InputEvent) -> void:
	if scroll == null or not is_visible_in_tree():
		return
	if ev is InputEventMouseButton and ev.button_index == MOUSE_BUTTON_LEFT:
		if ev.pressed:
			pressing = scroll.get_global_rect().has_point(ev.position) and ev.position.x < scroll.get_global_rect().end.x - 50
			dragging = false
			press_at = ev.position
		elif pressing:
			pressing = false
			if dragging:
				dragging = false
				get_viewport().set_input_as_handled()
				return
			_tap(ev.position)
	elif ev is InputEventMouseMotion and pressing:
		if not dragging and absf(ev.position.y - press_at.y) > DRAG_START:
			dragging = true
			# let go of whatever the finger first touched (a button, a box), so lifting it doesn't press it
			var up := InputEventMouseButton.new()
			up.button_index = MOUSE_BUTTON_LEFT
			up.pressed = false
			up.position = Vector2(-4000, -4000)
			up.global_position = up.position
			get_viewport().push_input(up)
		if dragging:
			scroll.scroll_vertical -= int(ev.relative.y)
			get_viewport().set_input_as_handled()


## A tap on a box starts typing in it; a tap anywhere else puts the keyboard away.
func _tap(at: Vector2) -> void:
	var fo := get_viewport().gui_get_focus_owner()
	for e in _boxes(body, []):
		if e.get_global_rect().has_point(at):
			if e != fo:
				e.grab_focus()
				if e is LineEdit:
					e.caret_column = e.text.length()
				else:
					var last: int = e.get_line_count() - 1
					e.set_caret_line(last)
					e.set_caret_column(e.get_line(last).length())
			return
	if fo is LineEdit or fo is TextEdit:
		fo.release_focus()


func _process(_dt: float) -> void:
	if spacer == null or not is_instance_valid(spacer):
		return
	var kb := float(DisplayServer.virtual_keyboard_get_height())
	if kb != kb_h:
		kb_h = kb
		var win := float(DisplayServer.window_get_size().y)
		var scale := get_viewport_rect().size.y / win if win > 0 else 1.0
		spacer.custom_minimum_size.y = kb * scale
		var fo := get_viewport().gui_get_focus_owner()
		if kb > 0 and (fo is LineEdit or fo is TextEdit):
			_show_box.call_deferred(fo)


func _notification(what: int) -> void:
	if what == NOTIFICATION_APPLICATION_PAUSED or what == NOTIFICATION_APPLICATION_FOCUS_OUT:
		_autosave()


## Drafts save themselves (every 15 seconds while there are changes, and on leaving), so no typing is ever lost.
func _autosave() -> void:
	if not dirty or busy or not w.has("name"):
		return
	if not (d.is_empty() or bool(d.get("editable", false))):
		return
	var form := _gather()
	if d.is_empty() and str(form.get("name", "")).strip_edges() == "" and \
			["problem", "does", "fits", "improves", "how"].all(func(k): return str(form.get(k, "")).strip_edges() == ""):
		return                        # nothing written yet: don't start an empty draft
	busy = true
	var payload := {"form": form}
	if not d.is_empty():
		payload.id = d.id
	var r := await Api.call_api("POST", "/api/dfg/blueprints/save", payload)
	busy = false
	if r.ok:
		dirty = false
		var keep_msgs = d.get("messages", [])
		d = r.data
		if not d.has("messages"):
			d.messages = keep_msgs
		if is_instance_valid(msg):
			msg.text = tr("Draft saved.")


func _renumber() -> void:
	var n := 0
	for c in parts_box.get_children():
		if c.is_queued_for_deletion() or not c.has_meta("head"):
			continue
		n += 1
		c.get_meta("head").text = tr("PART %d") % n


# what the server can say a part still needs (listed here so they are translated)
const PART_NEEDS := ["a name for this part", "at least one material", "an amount for every material"]

# the server's form choices and missing answers (blueprints.py kinds, origins, books, materials, questions), listed so they are translated
const FORM_CHOICES := [
	"A part (fits onto a ship or machine)", "A tool or machine", "A ship", "Something else", "Brand new",
	"An upgrade to something", "A newer version or model", "Raw materials and processing", "Prospecting & Geology",
	"Mining", "Metallurgy", "Assaying", "Refining & Chemistry", "Ceramics & Glassmaking", "Making things",
	"Engineering & Drafting", "Fabrication", "Electronics", "Power Systems", "Business and trading",
	"Trading & Markets", "Commodities", "Logistics & Hauling", "Contracts & Services", "Bookkeeping", "Appraisal",
	"Ship and survival", "Pilot Basic Training Handbook", "Ship Maintenance & Repair", "Life Support",
	"Health & Fitness", "Botany & Hydroponics", "Combat (arrives with the military track)",
	"Advanced Aerial Combat Strategies", "Earth habitats", "Farming & Soils", "Water Management", "Forestry",
	"Construction", "Iron", "Nickel", "Native iron-nickel (meteoritic metal)", "Cobalt", "Copper", "Aluminium",
	"Titanium", "Magnesium", "Zinc", "Tin", "Lead", "Chromium", "Manganese", "Tungsten", "Molybdenum", "Lithium",
	"Silver", "Gold", "Platinum", "Palladium", "Iridium", "Silicon", "Carbon (graphite)", "Diamond (rough)", "Boron",
	"Sulfur", "Phosphorus", "Neodymium (rare earth)", "Dysprosium (rare earth)", "Water ice", "Hydrogen", "Oxygen",
	"Nitrogen", "Methane", "Ammonia", "Carbon dioxide", "Helium-3", "Sand (silica sand, bulk)", "Clay", "Limestone",
	"Basalt", "Soil (bulk)", "Timber - softwood (Douglas-fir)", "Timber - hardwood (white oak)", "Uranium", "Thorium",
	"metal", "precious metal", "electronics / structure", "rare earth", "ice / volatile", "habitat building", "energy",
	"its name", "what kind of thing it is", "whether it's brand new, an upgrade, or a newer version or model",
	"what it is and the problem it solves", "everything it does, in detail", "what it fits",
	"what it improves, and by how much", "the library books it requires", "its parts and materials", "how it's built",
	"how long it takes to build", "what it builds on", "what's different from it"
]


## The server's "part 2: a name for this part" becomes "Part 2: a name for this part" in the player's language.
func _missing_text(x) -> String:
	var t := str(x)
	var m := RegEx.create_from_string("^part (\\d+): (.+)$").search(t)
	if m:
		return tr("Part %d") % int(m.get_string(1)) + ": " + tr(m.get_string(2))
	return tr(t)
