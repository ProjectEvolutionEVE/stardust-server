extends VBoxContainer
## The Filing cabinet in Private Quarters (rules 13, 22, 23, 24, 26), ported from the browser game (static/quarters.js):
## my designs, the blueprint copies filed here, library certificates, the receipts log (each receipt opens, can be checked
## with the server and saved to the player's own device) and the lockbox inside the cabinet for valuables.

const BP_STATUS := {"draft": "Draft: only you can see it", "submitted": "With the review team",
	"changes_requested": "Changes requested: see the review team’s note", "approved": "Approved", "rejected": "Not approved"}

var body: VBoxContainer
var names := {}            # material code -> name, from the market board, for the receipts


func _init() -> void:
	name = "Filing cabinet"
	var scroll := ScrollContainer.new()
	scroll.size_flags_vertical = Control.SIZE_EXPAND_FILL
	scroll.horizontal_scroll_mode = ScrollContainer.SCROLL_MODE_DISABLED
	add_child(scroll)
	var pad := MarginContainer.new()          # keeps the right-hand numbers clear of the scroll bar
	pad.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	pad.add_theme_constant_override("margin_right", 16)
	scroll.add_child(pad)
	body = VBoxContainer.new()
	body.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	body.add_theme_constant_override("separation", 12)
	pad.add_child(body)


func _ready() -> void:
	show_cabinet()


func _clear() -> void:
	for c in body.get_children():
		c.queue_free()


func _heading(t: String) -> Label:
	return Ui.label(t, 24, Ui.GOLD)


func _muted(t: String) -> Label:
	return Ui.label(t, 22, Ui.MUTED)


func _row(left: String, sub: String, right: String) -> HBoxContainer:
	var h := HBoxContainer.new()
	h.add_theme_constant_override("separation", 10)
	var v := VBoxContainer.new()
	v.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	v.add_child(Ui.label(left, 22))
	if sub != "":
		v.add_child(Ui.label(sub, 20, Ui.MUTED))
	h.add_child(v)
	if right != "":
		var r := Ui.label(right, 22, Ui.MUTED)
		r.autowrap_mode = TextServer.AUTOWRAP_OFF
		h.add_child(r)
	return h


func show_cabinet() -> void:
	_clear()
	body.add_child(_muted("Opening the cabinet…"))
	var r := await Api.call_api("GET", "/api/dfg/receipts")
	var bp := await Api.call_api("GET", "/api/dfg/blueprints")
	var inv := await Api.call_api("GET", "/api/dfg/inventory")
	var cr := await Api.call_api("GET", "/api/dfg/library/certificates")
	if names.is_empty():
		var mk := await Api.call_api("GET", "/api/dfg/market")
		for it in mk.data.get("items", []):
			names[it.item] = it.name
	_clear()
	if not inv.ok and not r.ok:
		body.add_child(Ui.label(inv.error, 22, Ui.GOLD))
		return
	var places: Array = inv.data.get("places", [])
	var fc := {}
	var lb := {}
	for p in places:
		if p.kind == "filing_cabinet":
			fc = p
		elif p.kind == "lockbox":
			lb = p

	body.add_child(_heading("MY DESIGNS"))
	var designs: Array = bp.data.get("blueprints", [])
	if designs.is_empty():
		body.add_child(_muted("No blueprints yet. Design one in the drafting room at the Starship Library."))
	for b in designs:
		var sub := tr(BP_STATUS[b.status]) if BP_STATUS.has(b.status) else str(b.status)
		if int(b.get("version", 0)):
			sub += " · " + tr("version %d") % int(b.version)
		if int(b.get("unread", 0)) and b.status == "changes_requested":
			sub += " · " + tr("1 new note")
		body.add_child(_row("📐 " + str(b.title), sub, ""))

	# every blueprint copy filed here (bought at auction, or printed to sell), grouped by design, each with its serial
	body.add_child(_heading("BLUEPRINT COPIES"))
	var groups := {}
	for i in fc.get("items", []):
		if i.kind == "blueprint":
			if not groups.has(i.name):
				groups[i.name] = []
			groups[i.name].append(i)
	if groups.is_empty():
		body.add_child(_muted("No blueprint copies yet. Win them at auction in the Market terminal, at your desk."))
	for n in groups:
		var its: Array = groups[n]
		var lines := []
		for i in its:
			var d: Variant = i.get("details", {})
			lines.append(str(d.get("serial", "")) if d is Dictionary else "")
			if i.get("set_aside"):
				lines[-1] += "  " + tr("(in an auction)")
		body.add_child(_fold((tr("📐 %s · %d copies") if its.size() > 1 else tr("📐 %s · %d copy")) % [str(n).replace("Blueprint · ", ""), its.size()],
			"\n".join(lines)))

	body.add_child(_heading("CERTIFICATES"))
	var certs: Array = cr.data.get("certificates", [])
	if certs.is_empty():
		body.add_child(_muted("None yet. Pass a library book’s test to earn one."))
	for c in certs:
		body.add_child(_row("🎓 " + str(c.title), tr("Passed %s") % Ui.when(c.passed_at, "date"), str(c.score)))

	body.add_child(_heading("RECEIPTS LOG"))
	var list: Array = r.data.get("receipts", [])
	if list.is_empty():
		body.add_child(_muted("No receipts yet. Every unload at the Starship gives you one."))
	for x in list:
		var b := Button.new()
		b.flat = true
		b.custom_minimum_size = Vector2(0, 64)
		var row := _row(str(x.code) + "   " + Ui.when(x.issued_at, "full"), _line(x), "Open ›")
		row.set_anchors_preset(Control.PRESET_FULL_RECT)
		row.mouse_filter = Control.MOUSE_FILTER_IGNORE
		for c in row.find_children("*", "Control", true, false):
			c.mouse_filter = Control.MOUSE_FILTER_IGNORE
		b.add_child(row)
		b.pressed.connect(_receipt.bind(x))
		body.add_child(b)
		row.resized.connect(func(): b.custom_minimum_size.y = row.get_combined_minimum_size().y + 8)

	body.add_child(_heading("LOCKBOX"))
	var vals: Array = lb.get("items", [])
	if vals.is_empty():
		body.add_child(_muted("Empty. A small, secure box for valuables."))
	for v in vals:
		var d: Variant = v.get("details", {})
		var sub := ""
		if d is Dictionary and d.has("kg"):
			sub = _kg(float(d.kg))
		body.add_child(_row("💎 " + str(v.name) if str(v.item).begins_with("diamond") else str(v.name), sub, tr("set aside") if v.get("set_aside") else ""))


## A folder that opens when its title is tapped.
func _fold(title: String, text: String) -> VBoxContainer:
	var f := VBoxContainer.new()
	var head := Button.new()
	head.flat = true
	head.alignment = HORIZONTAL_ALIGNMENT_LEFT
	head.add_theme_font_size_override("font_size", 22)
	for c in ["font_color", "font_hover_color", "font_pressed_color", "font_focus_color"]:
		head.add_theme_color_override(c, Ui.TEXT)
	head.text = "▸ " + title
	f.add_child(head)
	var l := Ui.label(text, 20, Ui.MUTED)
	l.visible = false
	var m := MarginContainer.new()
	m.add_theme_constant_override("margin_left", 28)
	m.add_child(l)
	f.add_child(m)
	head.pressed.connect(func():
		l.visible = not l.visible
		head.text = ("▾ " if l.visible else "▸ ") + title)
	return f


func _mat(code: String) -> String:
	return str(names.get(code, code))


## One line per receipt in the log, whatever kind it is.
func _line(x: Dictionary) -> String:
	match str(x.kind):
		"trade":
			var n := int(x.get("lots", 0))
			return (tr("Market: %s %d lots of %s for %s credits") if n > 1 else tr("Market: %s %d lot of %s for %s credits")) % [x.trade, n, x.item, Ui.num(x.credits)]
		"auction":
			var t := (tr("Auction: won %s (%s) for %s credits") if x.trade == "won" else tr("Auction: sold %s (%s) for %s credits")) % [x.serial, x.item, Ui.num(x.bid)]
			if x.trade == "won" and x.get("starship_fee"):
				t += " + " + tr("%s Starship fee") % Ui.num(x.starship_fee)
			return t
		"print":
			var c := int(x.copies)
			return (tr("Printed %d copies of %s, run %s (%s to %s) for %s credits") if c > 1 else tr("Printed %d copy of %s, run %s (%s to %s) for %s credits")) % [c, x.item, str(x.run),
				x.first, x.last, Ui.num(x.credits)]
	if x.get("kg") is Dictionary:
		var parts := []
		for m in x.kg:
			parts.append(_mat(m) + " " + _kg(float(x.kg[m])))
		return tr("%d pieces: %s") % [int(x.get("pieces", 0)), ", ".join(parts)]
	return str(x.kind)


func _kg(kg: float) -> String:
	return Ui.dec(kg * 1000.0, 1) + " g" if kg < 1 else Ui.dec(kg, 2) + " kg"


## The receipt as text: what's shown here and what "Save a copy" writes (the browser's receiptText, for every kind).
func _text(x: Dictionary) -> String:
	var L := [tr("WORLD SPACE CONSORTIUM"), str(x.get("issued_by", "WSC Alexander von Humboldt")), "", tr("RECEIPT %s") % str(x.code),
		tr("Issued: %s") % Ui.when(x.issued_at, "full")]
	if x.kind == "unload":
		var n := int(x.get("pieces", 0))
		L.append((tr("Transfer: %d piece from %s to %s") if n == 1 else tr("Transfer: %d pieces from %s to %s")) % [n, x.get("from", tr("your ship's hold")), x.get("to", tr("your space in the Starship's cargo hold"))])
		if int(x.get("left_aboard", 0)):
			L.append((tr("Left aboard your ship: %d piece") if int(x.left_aboard) == 1 else tr("Left aboard your ship: %d pieces")) % int(x.left_aboard))
		L.append_array(["", (tr("Material") + "                          ").left(26) + tr("Weight")])
		for m in x.get("kg", {}):
			L.append((_mat(m) + "                          ").left(26) + _kg(float(x.kg[m])))
		for g in x.get("near_flawless_diamonds", []):
			L.append((tr("Near-flawless diamond") + "                    ").left(26) + _kg(float(g.kg)) + "  (" + (tr("lockbox") if g.get("kept_in") == "lockbox" else tr("Starship cargo hold")) + ")")
		if x.has("space_used_m3"):
			L.append_array(["", tr("Your space after: %.3f of %.2f m³ used") % [float(x.space_used_m3), float(x.get("space_total_m3", 0))]])
	else:
		L.append(_line(x))
		if x.get("average_price_per_lot") != null:
			L.append(tr("Average price per lot: %s") % Ui.num(x.average_price_per_lot))
	L.append_array(["", tr("Issued by the game server. Anyone can check this code at:"), Api.BASE_URL + "/api/dfg/receipt/" + str(x.code), ""])
	return "\n".join(L)


func _receipt(x: Dictionary) -> void:
	_clear()
	var text := _text(x)
	body.add_child(Ui.label(tr("RECEIPT %s") % str(x.code), 30, Ui.GOLD))
	var check := _muted("Checking with the Starship…")
	body.add_child(check)
	var paper := PanelContainer.new()
	var st := StyleBoxFlat.new()
	st.bg_color = Ui.PANEL
	st.border_color = Ui.GOLD
	st.set_border_width_all(1)
	st.set_corner_radius_all(10)
	st.set_content_margin_all(16)
	paper.add_theme_stylebox_override("panel", st)
	var t := Ui.label(text, 18)
	var mono := SystemFont.new()
	mono.font_names = PackedStringArray(["Menlo", "Consolas", "DejaVu Sans Mono", "monospace"])
	t.add_theme_font_override("font", mono)
	paper.add_child(t)
	body.add_child(paper)
	var save := Ui.button("Save a copy")
	var msg := Ui.label("", 22, Ui.GREEN)
	save.pressed.connect(_save.bind(str(x.code), text, msg))
	body.add_child(save)
	body.add_child(msg)
	var back := Ui.button("Back to the filing cabinet", false)
	back.pressed.connect(show_cabinet)
	body.add_child(back)
	var v := await Api.call_api("GET", "/api/dfg/receipt/" + str(x.code).uri_encode(), {}, false)
	if not is_instance_valid(check):
		return
	if v.ok and v.data.get("valid", false):
		check.text = tr("✓ Checked: the game server issued this receipt.")
		check.add_theme_color_override("font_color", Ui.GREEN)
	else:
		check.text = v.error


## Rule 13: the player saves a copy to their own device, in Documents › Stardust Receipts (Ui.save_receipt).
func _save(code: String, text: String, msg: Label) -> void:
	Ui.save_receipt(self, code, text, func(path: String):
		if path != "":
			msg.text = tr("Saved: %s › %s") % [path.get_base_dir().get_file(), path.get_file()]
			msg.add_theme_color_override("font_color", Ui.GREEN)
		else:
			msg.text = tr("Couldn't save. Your receipt is still in the receipts log in your quarters. Try again from there.")
			msg.add_theme_color_override("font_color", Ui.GOLD))
