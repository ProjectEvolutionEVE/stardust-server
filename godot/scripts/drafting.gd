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


func _ready() -> void:
	var box := Ui.screen(self)
	var top := HBoxContainer.new()
	box.add_child(top)
	var back := Ui.button("◀ Library", false)
	back.custom_minimum_size = Vector2(190, 64)
	back.pressed.connect(func(): get_tree().change_scene_to_file("res://scenes/library.tscn"))
	top.add_child(back)
	var t := Ui.label("  DRAFTING ROOM", 32, Ui.GOLD)
	t.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	top.add_child(t)
	var scroll := ScrollContainer.new()
	scroll.size_flags_vertical = Control.SIZE_EXPAND_FILL
	scroll.horizontal_scroll_mode = ScrollContainer.SCROLL_MODE_DISABLED
	box.add_child(scroll)
	body = VBoxContainer.new()
	body.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	body.add_theme_constant_override("separation", 14)
	scroll.add_child(body)
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
	var name := Ui.field("e.g. Clay brick kiln")
	name.text = str(f.get("name", "") if f.get("name") != null else "")
	name.max_length = int(opts.limits.text.name)
	name.editable = edit
	body.add_child(name)
	w.name = name
	var kinds: Array = opts.kinds.map(func(k): return [k.code, k.name])
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

	_q(8, "Its parts and materials", tr("Each part, with the materials it's made of and how much. Its weight and size are worked out from the real materials."))
	parts_box = VBoxContainer.new()
	parts_box.add_theme_constant_override("separation", 12)
	body.add_child(parts_box)
	var plist: Array = f.get("parts", []) if f.get("parts") != null else []
	if plist.is_empty():
		plist = [{}]
	for p in plist:
		_part(p, edit)
	if edit:
		var addp := _small("+ Add a part")
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
	back.pressed.connect(_list)
	body.add_child(back)


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
func _part(p: Dictionary, edit: bool) -> void:
	var box := VBoxContainer.new()
	box.add_theme_constant_override("separation", 8)
	parts_box.add_child(box)
	var pn := Ui.field("Part name, e.g. Bricks")
	pn.text = str(p.get("name", "") if p.get("name") != null else "")
	pn.editable = edit
	box.add_child(pn)
	box.set_meta("name", pn)
	var rows := VBoxContainer.new()
	rows.add_theme_constant_override("separation", 8)
	box.add_child(rows)
	box.set_meta("rows", rows)
	var mats: Array = p.get("materials", []) if p.get("materials") != null else []
	if mats.is_empty():
		mats = [{}]
	for m in mats:
		_mat_row(rows, m, edit)
	if edit:
		var h := HBoxContainer.new()
		box.add_child(h)
		var am := _small("+ Add a material")
		am.size_flags_horizontal = Control.SIZE_EXPAND_FILL
		am.pressed.connect(func(): _mat_row(rows, {}, true))
		h.add_child(am)
		var rp := _small("Remove this part")
		rp.size_flags_horizontal = Control.SIZE_EXPAND_FILL
		rp.pressed.connect(func(): box.queue_free(); _total.call_deferred())
		h.add_child(rp)


func _mat_row(rows: VBoxContainer, m: Dictionary, edit: bool) -> void:
	var h := HBoxContainer.new()
	h.add_theme_constant_override("separation", 8)
	rows.add_child(h)
	var items := []
	for x in opts.materials:
		items.append([x.code, str(x.name) + "  ·  " + tr(str(x.category))])
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
	_form()
	var miss: Array = d.get("missing", [])
	msg.text = tr("Saved. Ready to send to the review team.") if miss.is_empty() else tr("Saved. Still to answer: %s.") % ", ".join(miss.map(func(x): return tr(str(x))))


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
