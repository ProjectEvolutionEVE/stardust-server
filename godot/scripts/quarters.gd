extends Control
## Private Quarters: a tab for each piece of furniture. The Bed shows the health bars (me.bars, 0-100).


func _ready() -> void:
	var me: Dictionary = Session.me
	var box := Ui.screen(self)
	box.add_child(Ui.label(me.get("location", "Private Quarters"), 40, Ui.GOLD))
	box.add_child(Ui.label(me.get("title", ""), 24, Ui.MUTED))
	_library_alert(box, me.get("skills", {}))
	var tabs := TabContainer.new()
	tabs.size_flags_vertical = Control.SIZE_EXPAND_FILL
	box.add_child(tabs)
	tabs.add_child(_bed(me))
	tabs.add_child(preload("res://scripts/desk.gd").new())
	for name in ["Closet", "Bookshelf"]:
		var t := VBoxContainer.new()
		t.name = name
		t.add_child(Ui.label("Coming to the app soon. Open it in the browser game for now.", 24, Ui.MUTED))
		tabs.add_child(t)
	tabs.add_child(preload("res://scripts/cabinet.gd").new())
	if Session.quarters_tab != "":
		var n := tabs.get_node_or_null(Session.quarters_tab)
		if n:
			tabs.current_tab = n.get_index()
		Session.quarters_tab = ""
	var out := Ui.button("Exit Private Quarters", false)   # rule 19: to the Library or the Docking Bay
	out.pressed.connect(_exit)
	box.add_child(out)
	var c := Session.call_on_enter
	Session.call_on_enter = ""
	if c == "welcome":
		Voice.ring(self, Voice.WELCOME, "welcome")
	elif c == "wake":
		Voice.ring(self, Voice.moment("wake"))


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
	for k in [["fly", "Pilot Basic Training Handbook (to fly)"], ["mine", "Mining (to mine)"], ["sell", "Trading & Markets (to sell)"]]:
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
	v.add_child(Ui.label("Study and pass: " + ", ".join(need) + ".", 22))
	var go := Ui.button("Go to the Library")
	go.pressed.connect(func(): get_tree().change_scene_to_file("res://scenes/library.tscn"))
	v.add_child(go)
	box.add_child(panel)


## Leaving the quarters (rule 19): two places only, the Starship Library or the Docking Bay.
func _exit() -> void:
	var d := ConfirmationDialog.new()
	d.title = "Exit Private Quarters"
	d.dialog_text = "Where to?"
	d.ok_button_text = "Starship Library"
	d.cancel_button_text = "Docking Bay"
	d.confirmed.connect(func(): get_tree().change_scene_to_file("res://scenes/library.tscn"))
	d.canceled.connect(func(): get_tree().change_scene_to_file("res://scenes/bay.tscn"))
	add_child(d)
	d.popup_centered()
