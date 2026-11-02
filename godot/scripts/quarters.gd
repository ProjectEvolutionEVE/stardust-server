extends Control
## Private Quarters: a tab for each piece of furniture. The Bed shows the health bars (me.bars, 0-100).


## The room as a picture (Eric 10-24, a feel test before the real art): the quarters open on the whole room, with a
## tap-point on each piece of furniture; a tap opens that tab, shown over its close-up. "Room" goes back.
const SPOTS := [["Bed", 0.20, 0.62], ["Desk", 0.68, 0.50], ["Closet", 0.47, 0.35], ["Bookshelf", 0.08, 0.40], ["Filing cabinet", 0.84, 0.82]]
const CLOSEUP := {"Bed": "bed", "Desk": "desk", "Closet": "closet", "Bookshelf": "bookshelf", "Filing cabinet": "filing"}

var tabs: TabContainer
var overview: Control
var tab_view: VBoxContainer
var backdrop: TextureRect
var shade: ColorRect
var who: HBoxContainer
var closet: VBoxContainer


func _ready() -> void:
	var me: Dictionary = Session.me
	var box := Ui.screen(self)
	# the close-up of the open tab fills the screen behind it, darkened so the text stays readable
	backdrop = TextureRect.new()
	backdrop.set_anchors_preset(Control.PRESET_FULL_RECT)
	backdrop.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	backdrop.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_COVERED
	add_child(backdrop)
	move_child(backdrop, 1)
	shade = ColorRect.new()
	shade.color = Color(0, 0, 0, 0.55)
	shade.set_anchors_preset(Control.PRESET_FULL_RECT)
	add_child(shade)
	move_child(shade, 2)
	box.add_child(Ui.label(me.get("location", "Private Quarters"), 40, Ui.GOLD))
	who = HBoxContainer.new()                  # the title, the worn uniform's colour and its bars (rule 32)
	who.add_theme_constant_override("separation", 12)
	box.add_child(who)
	_show_who(me)
	overview = _room()
	box.add_child(overview)
	_library_alert(box, me.get("skills", {}))
	tab_view = VBoxContainer.new()
	tab_view.size_flags_vertical = Control.SIZE_EXPAND_FILL
	box.add_child(tab_view)
	var room := Ui.button("◂ Room", false)
	room.custom_minimum_size = Vector2(150, 52)
	room.size_flags_horizontal = Control.SIZE_SHRINK_BEGIN
	room.add_theme_font_size_override("font_size", 22)
	room.pressed.connect(_show_room)
	tab_view.add_child(room)
	tabs = TabContainer.new()
	tabs.size_flags_vertical = Control.SIZE_EXPAND_FILL
	tabs.add_theme_stylebox_override("panel", StyleBoxEmpty.new())   # the close-up shows through
	tab_view.add_child(tabs)
	tabs.add_child(_bed(me))
	tabs.add_child(preload("res://scripts/desk.gd").new())
	closet = VBoxContainer.new()
	closet.name = "Closet"
	closet.add_theme_constant_override("separation", 12)
	tabs.add_child(closet)
	for name in ["Bookshelf"]:
		var t := VBoxContainer.new()
		t.name = name
		t.add_child(Ui.label("Coming to the app soon. Open it in the browser game for now.", 24, Ui.MUTED))
		tabs.add_child(t)
	tabs.add_child(preload("res://scripts/cabinet.gd").new())
	for i in tabs.get_tab_count():                 # node names stay English (code finds tabs by them); the title is translated
		tabs.set_tab_title(i, tr(tabs.get_child(i).name))
	tabs.tab_changed.connect(func(_i): _closeup())
	closet.visibility_changed.connect(func():
		if closet.is_visible_in_tree():
			_load_closet())
	var spacer := Control.new()                # on the room view, keeps the exit button at the bottom
	spacer.size_flags_vertical = Control.SIZE_EXPAND_FILL
	spacer.name = "spacer"
	box.add_child(spacer)
	var out := Ui.button("Exit Private Quarters", false)   # rule 19: to the Library or the Docking Bay
	out.pressed.connect(_exit)
	box.add_child(out)
	if Session.quarters_tab != "":
		_open(Session.quarters_tab)
		Session.quarters_tab = ""
	else:
		_show_room()
	var c := Session.call_on_enter
	Session.call_on_enter = ""
	if c == "welcome":
		Voice.ring(self, Voice.WELCOME, "welcome")
	elif c == "wake":
		Voice.ring(self, Voice.moment("wake"))


## The whole room, full width, with a small glowing gold tap-point on each piece of furniture.
func _room() -> Control:
	var pic := TextureRect.new()
	pic.texture = load("res://assets/quarters/room.jpg")
	pic.expand_mode = TextureRect.EXPAND_FIT_HEIGHT_PROPORTIONAL
	pic.stretch_mode = TextureRect.STRETCH_SCALE
	for s in SPOTS:
		var b := Button.new()
		b.text = tr(s[0])
		b.add_theme_font_size_override("font_size", 17)
		var st := StyleBoxFlat.new()
		st.bg_color = Color(Ui.BG, 0.7)
		st.border_color = Ui.GOLD
		st.set_border_width_all(1)
		st.set_corner_radius_all(14)
		st.content_margin_left = 10
		st.content_margin_right = 10
		st.content_margin_top = 3
		st.content_margin_bottom = 3
		st.shadow_color = Color(Ui.GOLD, 0.45)
		st.shadow_size = 8
		for state in ["normal", "hover", "pressed", "focus"]:
			b.add_theme_stylebox_override(state, st)
		for c in ["font_color", "font_hover_color", "font_pressed_color", "font_focus_color"]:
			b.add_theme_color_override(c, Ui.GOLD)
		b.anchor_left = s[1]
		b.anchor_right = s[1]
		b.anchor_top = s[2]
		b.anchor_bottom = s[2]
		b.grow_horizontal = Control.GROW_DIRECTION_BOTH
		b.grow_vertical = Control.GROW_DIRECTION_BOTH
		b.pressed.connect(_open.bind(s[0]))
		pic.add_child(b)
		var glow := b.create_tween().set_loops()     # a soft, slow glow
		glow.tween_property(b, "modulate", Color(1.25, 1.2, 1.05), 1.2).set_trans(Tween.TRANS_SINE)
		glow.tween_property(b, "modulate", Color(0.85, 0.85, 0.85), 1.2).set_trans(Tween.TRANS_SINE)
	return pic


## Where the player's name shows: their title (the worn career's highest step), its uniform colour and its bars.
func _show_who(me: Dictionary) -> void:
	for c in who.get_children():
		c.queue_free()
	var career: Dictionary = me.get("career") if me.get("career") is Dictionary else {}
	if career.get("colour") != null:
		who.add_child(Ui.swatch(career.colour, 24))
	var t := Ui.label(str(me.get("title", "")), 24, Ui.MUTED)
	t.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	who.add_child(t)
	var bars: Array = career.get("bars", [])
	if not bars.is_empty():
		who.add_child(Ui.bar_strip(bars, 18))


## The Closet (rule 32): a uniform for every career studied; one is worn, and its title is the one the player goes by.
func _load_closet() -> void:
	var r := await Api.call_api("GET", "/api/dfg/careers")
	if not r.ok:
		_closet_clear()
		closet.add_child(Ui.label(r.error, 24, Ui.GOLD))
		return
	render_closet(r.data)


func _closet_clear() -> void:
	for c in closet.get_children():
		c.queue_free()


func render_closet(data: Dictionary) -> void:
	_closet_clear()
	closet.add_child(Ui.label("Your uniforms", 30, Ui.GOLD))
	closet.add_child(Ui.label("Wear one at a time. The career you wear gives its skill bonus and the title you are addressed by.", 22, Ui.MUTED))
	var scroll := ScrollContainer.new()
	scroll.size_flags_vertical = Control.SIZE_EXPAND_FILL
	scroll.horizontal_scroll_mode = ScrollContainer.SCROLL_MODE_DISABLED
	closet.add_child(scroll)
	var list := VBoxContainer.new()
	list.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	list.add_theme_constant_override("separation", 10)
	scroll.add_child(list)
	var worn = data.get("uniform")
	list.add_child(_uniform_row(null, tr("Trainee coveralls"), tr("Trainee"), null, [], worn == null, true))
	for c in data.careers:
		var skill: String = tr(" · skill +%s%%") % Ui.dec(float(c.skill_pct), 2) if float(c.skill_pct) > 0 else ""
		list.add_child(_uniform_row(c.code, c.name, str(c.title) + skill, c.colour, c.bars, worn == c.code, c.studied))


func _uniform_row(code, name: String, sub: String, colour, bars: Array, worn: bool, open: bool) -> Control:
	var row := HBoxContainer.new()
	row.add_theme_constant_override("separation", 12)
	row.add_child(Ui.swatch(colour, 40))
	var b := Ui.button(tr("%s  ·  %s") % [name, sub], false)
	b.alignment = HORIZONTAL_ALIGNMENT_LEFT
	b.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	b.clip_text = true
	b.add_theme_font_size_override("font_size", 22)
	b.disabled = worn or not open
	if not open:
		b.text = tr("%s  ·  not studied yet") % name
	if worn:   # the uniform being worn: a bold green check and a green-highlighted box (Eric 10-27)
		b.text = tr("✔  %s  ·  %s   (wearing)") % [name, sub]
		var hl := StyleBoxFlat.new()
		hl.bg_color = Color(Ui.GREEN, 0.18)
		hl.border_color = Ui.GREEN
		hl.set_border_width_all(3)
		hl.set_corner_radius_all(14)
		for state in ["normal", "hover", "pressed", "focus", "disabled"]:
			b.add_theme_stylebox_override(state, hl)
		b.add_theme_color_override("font_disabled_color", Ui.GREEN)
		b.add_theme_color_override("font_color", Ui.GREEN)
	b.pressed.connect(_wear.bind(code))
	row.add_child(b)
	if open and not bars.is_empty():
		row.add_child(Ui.bar_strip(bars, 12))
	return row


func _wear(code) -> void:
	var r := await Api.call_api("POST", "/api/dfg/closet/uniform", {"career": code})
	if not r.ok:
		Ui.error(self, r.error)
		return
	var me := await Api.call_api("GET", "/api/dfg/me")
	if me.ok:
		Session.me = me.data
		_show_who(me.data)
	_load_closet()


func _show_room() -> void:
	overview.visible = true
	tab_view.visible = false
	backdrop.visible = false
	shade.visible = false
	_spacer(true)


func _open(tab: String) -> void:
	var n := tabs.get_node_or_null(tab)
	if n:
		tabs.current_tab = n.get_index()
	overview.visible = false
	tab_view.visible = true
	_spacer(false)
	_closeup()


func _spacer(on: bool) -> void:
	for c in tab_view.get_parent().get_children():
		if c.name == "spacer":
			c.visible = on


func _closeup() -> void:
	var name := str(tabs.get_current_tab_control().name)
	backdrop.texture = load("res://assets/quarters/%s.jpg" % CLOSEUP.get(name, "room"))
	backdrop.visible = tab_view.visible
	shade.visible = tab_view.visible


func _bed(me: Dictionary) -> VBoxContainer:
	var bed := VBoxContainer.new()
	bed.name = "Bed"
	bed.add_theme_constant_override("separation", 14)
	var bars: Dictionary = me.get("bars", {})
	for k in ["stamina", "energy", "focus"]:
		bed.add_child(Ui.label(k.capitalize(), 24))
		var p := ProgressBar.new()
		p.max_value = 100
		p.value = float(bars.get(k, 0))
		p.custom_minimum_size = Vector2(0, 36)
		bed.add_child(p)
	if me.get("warning", "") != "" and me.get("warning") != null:
		bed.add_child(Ui.label(str(me.warning), 24, Ui.GOLD))
	var out := Ui.button("Sign out (go to sleep)", false)
	out.pressed.connect(_sign_out.bind(out))
	bed.add_child(out)
	return bed


func _sign_out(out: Button) -> void:
	out.disabled = true
	await Api.call_api("POST", "/api/dfg/auth/signout")
	Session.clear()
	get_tree().change_scene_to_file("res://scenes/title.tscn")


## Skills come from the library first (Eric 10-23): while any is missing, the quarters say where to go and what for.
func _library_alert(box: VBoxContainer, sk: Dictionary) -> void:
	var need := []
	for k in [["fly", tr("Pilot Basic Training Handbook (to fly)")], ["mine", tr("Mining (to mine)")], ["sell", tr("Trading & Markets (to sell)")]]:
		if not sk.get(k[0], false):
			need.append(k[1])
	if need.is_empty():
		return
	var panel := PanelContainer.new()
	var st := StyleBoxFlat.new()
	st.bg_color = Ui.PANEL
	st.border_color = Ui.GOLD
	st.set_border_width_all(2)
	st.set_corner_radius_all(12)
	st.set_content_margin_all(16)
	panel.add_theme_stylebox_override("panel", st)
	var v := VBoxContainer.new()
	v.add_theme_constant_override("separation", 10)
	panel.add_child(v)
	v.add_child(Ui.label("Report to the Starship Library", 28, Ui.GOLD))
	v.add_child(Ui.label(tr("Study and pass: %s.") % ", ".join(need), 22))
	var go := Ui.button("Go to the Library")
	go.pressed.connect(func(): get_tree().change_scene_to_file("res://scenes/library.tscn"))
	v.add_child(go)
	box.add_child(panel)


## Leaving the quarters (rule 19): two places only, the Starship Library or the Docking Bay.
func _exit() -> void:
	var d := ConfirmationDialog.new()
	d.title = tr("Exit Private Quarters")
	d.dialog_text = tr("Where to?")
	d.ok_button_text = tr("Starship Library")
	d.cancel_button_text = tr("Docking Bay")
	d.confirmed.connect(func(): get_tree().change_scene_to_file("res://scenes/library.tscn"))
	d.canceled.connect(func(): get_tree().change_scene_to_file("res://scenes/bay.tscn"))
	add_child(d)
	d.popup_centered()
