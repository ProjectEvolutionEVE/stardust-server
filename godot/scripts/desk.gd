extends VBoxContainer
## The Desk in Private Quarters (rules 20, 22), ported from the browser game (static/quarters.js): COMMS (only the game's
## own messages, rule 8), the wallet, My items (everything owned, a folder for each place it's kept) and the Market
## terminal button, the only way to the market.

const PLACE_ORDER := ["starship_cargo", "ship_hold", "hangar", "private_quarters", "filing_cabinet", "lockbox", "bookshelf"]
const PLACE_ICON := {"starship_cargo": "📦", "ship_hold": "🚀", "hangar": "🛰️", "private_quarters": "🛏️",
	"filing_cabinet": "🗂️", "lockbox": "🔒", "bookshelf": "📚"}
const PLACE_NAME := {"starship_cargo": "Starship cargo hold"}
const PLACE_EMPTY := {"starship_cargo": "No raw materials in storage.", "ship_hold": "Nothing aboard.",
	"filing_cabinet": "No blueprints yet.", "lockbox": "Empty. For small personal effects and valuables.",
	"bookshelf": "No library books checked out.", "private_quarters": "Nothing else here."}
const DESIGN_STATUS := {"draft": "your draft", "submitted": "with the review team", "changes_requested": "changes requested",
	"approved": "approved", "rejected": "not approved"}

var body: VBoxContainer


func _init() -> void:
	name = "Desk"
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
	load_desk()


func load_desk() -> void:
	for c in body.get_children():
		c.queue_free()
	body.add_child(_heading("COMMS"))
	body.add_child(Ui.label("No messages yet. News from Starship Central Command and job postings will arrive here.", 22, Ui.MUTED))
	body.add_child(_heading("WALLET"))
	var wallet := Ui.label("Loading…", 26)
	body.add_child(wallet)
	body.add_child(_heading("MY ITEMS"))
	body.add_child(Ui.label("Everything you own, in a folder for each place it's kept.", 22, Ui.MUTED))
	var items := VBoxContainer.new()
	items.add_theme_constant_override("separation", 8)
	body.add_child(items)
	body.add_child(_heading("MARKET"))
	body.add_child(Ui.label("Prices, the chart, instant buy and sell, your open orders and your trade history.", 22, Ui.MUTED))
	var mk := Ui.button("📈 Open the market terminal")
	mk.pressed.connect(func(): get_tree().change_scene_to_file("res://scenes/market.tscn"))
	body.add_child(mk)
	body.add_child(_heading("STARSHIP BANK"))
	body.add_child(Ui.label("Savings, term deposits, loans and your savings goals (rule 36).", 22, Ui.MUTED))
	var bk := Ui.button("🏦 Open the Starship Bank")
	bk.pressed.connect(func(): get_tree().change_scene_to_file("res://scenes/bank.tscn"))
	body.add_child(bk)
	var r := await Api.call_api("GET", "/api/dfg/inventory")
	if not r.ok:
		wallet.text = "—"
		items.add_child(Ui.label(r.error, 22, Ui.GOLD))
		return
	var inv: Dictionary = r.data
	wallet.text = Ui.num(inv.credits) + " credits"
	if int(inv.get("credits_set_aside", 0)) > 0:
		wallet.text += "  (+" + Ui.num(inv.credits_set_aside) + " set aside for orders and bids)"
	var all: Array = inv.get("places", [])
	var tops := all.filter(func(p): return p.get("inside") == null)
	tops.sort_custom(_by_place)
	for p in tops:
		items.add_child(_folder(p, all, 0))


func _heading(t: String) -> Label:
	return Ui.label(t, 24, Ui.GOLD)


func _by_place(a: Dictionary, b: Dictionary) -> bool:
	return PLACE_ORDER.find(a.kind) < PLACE_ORDER.find(b.kind)


## One place as a folder: tap its name to open or close it. The cargo hold starts open, as in the browser.
func _folder(p: Dictionary, all: Array, depth: int) -> VBoxContainer:
	var goods: Array = p.get("goods", [])
	var its: Array = p.get("items", [])
	var designs: Array = p.get("designs", [])
	var kids := all.filter(func(c): return c.get("inside") == p.kind)
	kids.sort_custom(_by_place)
	var n := goods.size() + its.size() + designs.size()
	var space := ""
	if p.get("capacity_m3") != null:
		var u := float(p.get("used_m3", 0))
		space = ("under 0.01" if u > 0 and u < 0.01 else Ui.dec(u, 2)) + " of " + Ui.dec(float(p.capacity_m3), 2) + " m³ used"
	elif p.get("capacity_slots") != null:
		space = "%d of %d bays used" % [int(p.get("used_slots", 0)), int(p.capacity_slots)]
	var f := VBoxContainer.new()
	f.add_theme_constant_override("separation", 6)
	var head := Button.new()
	head.flat = true
	head.alignment = HORIZONTAL_ALIGNMENT_LEFT
	head.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	head.add_theme_font_size_override("font_size", 24)
	for c in ["font_color", "font_hover_color", "font_pressed_color", "font_focus_color"]:
		head.add_theme_color_override(c, Ui.TEXT)
	var title: String = str(PLACE_ICON.get(p.kind, "📁")) + " " + str(PLACE_NAME.get(p.kind, p.name))
	var meta := ("%d item%s" % [n, "" if n == 1 else "s"]) if n else "empty"
	if space != "":
		meta += " · " + space
	f.add_child(head)
	var inner := MarginContainer.new()
	inner.add_theme_constant_override("margin_left", 28)
	var v := VBoxContainer.new()
	v.add_theme_constant_override("separation", 6)
	inner.add_child(v)
	f.add_child(inner)
	for g in goods:
		v.add_child(_row(str(g.get("name", g.item)), _amount(g)))
	for i in its:
		var nm: String = i.name
		var d: Variant = i.get("details", {})
		if d is Dictionary and d.has("serial"):
			nm += "\nSerial " + str(d.serial)
		v.add_child(_row(nm, "set aside" if i.get("set_aside") else "1"))
	for d in designs:
		v.add_child(_row(str(d.title) + " (your design)", str(DESIGN_STATUS.get(d.status, d.status))))
	if n == 0 and kids.is_empty():
		v.add_child(Ui.label(str(PLACE_EMPTY.get(p.kind, "Empty.")), 20, Ui.MUTED))
	for k in kids:
		v.add_child(_folder(k, all, depth + 1))
	var open: bool = p.kind == "starship_cargo"
	inner.visible = open
	var set_head := func(o: bool): head.text = ("▾ " if o else "▸ ") + title + "   · " + meta
	set_head.call(open)
	head.pressed.connect(func():
		inner.visible = not inner.visible
		set_head.call(inner.visible))
	return f


func _row(left: String, right: String) -> HBoxContainer:
	var h := HBoxContainer.new()
	var l := Ui.label(left, 22)
	l.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	h.add_child(l)
	var r := Ui.label(right, 22, Ui.MUTED)
	r.horizontal_alignment = HORIZONTAL_ALIGNMENT_RIGHT
	r.autowrap_mode = TextServer.AUTOWRAP_OFF
	h.add_child(r)
	return h


func _amount(g: Dictionary) -> String:
	if g.get("kg") != null:
		var kg := float(g.kg)
		var s := (Ui.dec(kg / 1000.0, 2) + " t") if kg >= 1000 else (Ui.dec(kg, 1) + " kg")
		var pcs := int(g.get("pieces", 0))
		if pcs:
			s += " · %d piece%s" % [pcs, "" if pcs == 1 else "s"]
		if float(g.get("kg_set_aside", 0)) > 0:
			s += " · " + Ui.num(g.kg_set_aside) + " kg set aside for an order"
		return s
	var s2 := str(int(g.get("count", 0)))
	if int(g.get("set_aside", 0)):
		s2 += " · %d set aside" % int(g.set_aside)
	return s2
