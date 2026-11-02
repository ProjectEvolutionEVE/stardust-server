extends Node
## The look: dark space, gold accents. Screens build their layout in code with these helpers.

const BG := Color("07090f")
const PANEL := Color("121826")
const GOLD := Color("d9a441")
const TEXT := Color("eef0f5")
const MUTED := Color("8a94a6")
const GREEN := Color("4cc38a")        # done: a passed test, a chosen answer


func screen(root: Control) -> VBoxContainer:
	var bg := ColorRect.new()
	bg.color = BG
	bg.set_anchors_preset(Control.PRESET_FULL_RECT)
	root.add_child(bg)
	var margin := MarginContainer.new()
	margin.set_anchors_preset(Control.PRESET_FULL_RECT)
	for side in ["left", "right", "top", "bottom"]:
		margin.add_theme_constant_override("margin_" + side, 40)
	root.add_child(margin)
	var box := VBoxContainer.new()
	box.add_theme_constant_override("separation", 18)
	margin.add_child(box)
	return box


func label(text: String, size := 26, color := TEXT) -> Label:
	var l := Label.new()
	l.text = text
	l.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	l.add_theme_font_size_override("font_size", size)
	l.add_theme_color_override("font_color", color)
	return l


func button(text: String, primary := true) -> Button:
	var b := Button.new()
	b.text = text
	b.custom_minimum_size = Vector2(0, 76)
	b.add_theme_font_size_override("font_size", 28)
	var s := StyleBoxFlat.new()
	s.bg_color = GOLD if primary else PANEL
	s.border_color = GOLD
	s.set_border_width_all(2)
	s.set_corner_radius_all(14)
	for state in ["normal", "hover", "pressed", "focus"]:
		b.add_theme_stylebox_override(state, s)
	b.add_theme_color_override("font_color", BG if primary else GOLD)
	return b


func field(placeholder: String) -> LineEdit:
	var e := LineEdit.new()
	e.placeholder_text = placeholder
	e.custom_minimum_size = Vector2(0, 72)
	e.add_theme_font_size_override("font_size", 28)
	return e


func picker() -> OptionButton:
	var o := OptionButton.new()
	o.custom_minimum_size = Vector2(0, 72)
	o.add_theme_font_size_override("font_size", 26)
	return o


func error(parent: Node, text: String) -> void:
	var d := AcceptDialog.new()
	d.title = "Stardust"
	d.dialog_text = text
	parent.add_child(d)
	d.popup_centered()


## Whole numbers with thousands commas, as the browser shows them ("12,345"); "—" when there's none.
func num(v: Variant) -> String:
	if v == null:
		return "—"
	var n := int(round(float(v)))
	var s := str(absi(n))
	var out := ""
	while s.length() > 3:
		out = "," + s.right(3) + out
		s = s.left(s.length() - 3)
	return ("-" if n < 0 else "") + s + out


## Up to `places` decimals, trailing zeros dropped ("1.5", "12,000.25").
func dec(x: float, places: int) -> String:
	var whole := floori(absf(x))
	var frac := snappedf(absf(x) - whole, pow(10, -places))
	if frac >= 1.0:
		whole += 1
		frac = 0.0
	var f := ("%." + str(places) + "f") % frac
	f = f.substr(1).rstrip("0").rstrip(".")
	return ("-" if x < 0 else "") + num(whole) + f


## Local time from the server's ISO time (UTC): "time" 14:05:09 · "short" Oct 24, 14:05 · "date" Oct 24, 2026 · "full" Oct 24, 2026, 14:05.
func when(iso: String, style := "time") -> String:
	var t := Time.get_unix_time_from_datetime_string(iso.substr(0, 19))
	t += Time.get_time_zone_from_system().get("bias", 0) * 60
	var d := Time.get_datetime_dict_from_unix_time(int(t))
	var hm := "%02d:%02d" % [d.hour, d.minute]
	const MON := ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
	var day := "%s %d" % [MON[d.month - 1], d.day]
	match style:
		"short":
			return day + ", " + hm
		"date":
			return day + ", " + str(d.year)
		"full":
			return day + ", " + str(d.year) + ", " + hm
	return hm + ":%02d" % d.second


const SILVER := Color("c0c6d0")       # a silver career bar (rule 32)


## A career's five bars (rule 32), left to right: gold, silver, or an empty slot not earned yet.
func bar_strip(bars: Array, h := 22) -> HBoxContainer:
	var row := HBoxContainer.new()
	row.add_theme_constant_override("separation", 6)
	row.size_flags_vertical = Control.SIZE_SHRINK_CENTER
	for b in bars:
		var s := Panel.new()
		s.custom_minimum_size = Vector2(h * 2, h)
		var st := StyleBoxFlat.new()
		var medal = b.get("medal")
		st.bg_color = GOLD if medal == "gold" else (SILVER if medal == "silver" else Color(PANEL, 0.6))
		st.border_color = MUTED if medal == null else st.bg_color
		st.set_border_width_all(1)
		st.set_corner_radius_all(4)
		s.add_theme_stylebox_override("panel", st)
		s.tooltip_text = "%s: %s" % [b.title, b.note]
		row.add_child(s)
	return row


## A small square of a career's uniform colour ("2f6fd6").
func swatch(hex, size := 28) -> ColorRect:
	var c := ColorRect.new()
	c.color = Color(str(hex)) if hex != null else MUTED
	c.custom_minimum_size = Vector2(size, size)
	c.size_flags_vertical = Control.SIZE_SHRINK_CENTER
	return c


## Receipts are documented proof (rule 13; Eric 10-28): every player's saved copies go to their own device's Documents
## folder, in a folder anyone can recognise, "Stardust Receipts".
const RECEIPTS_FOLDER := "Stardust Receipts"


func receipts_dir() -> String:
	var dir := OS.get_system_dir(OS.SYSTEM_DIR_DOCUMENTS).path_join(RECEIPTS_FOLDER)
	DirAccess.make_dir_recursive_absolute(dir)
	return dir


## Save a receipt. On a computer the system's Save window opens in Stardust Receipts (the player may still choose
## elsewhere); on a phone it's written straight there. `done` gets the saved path, or "" if it couldn't be written.
func save_receipt(parent: Node, code: String, text: String, done: Callable) -> void:
	var file := "stardust-receipt-%s.txt" % code
	if OS.has_feature("mobile"):
		done.call(_write_receipt(receipts_dir().path_join(file), text))
		return
	var d := FileDialog.new()
	d.file_mode = FileDialog.FILE_MODE_SAVE_FILE
	d.access = FileDialog.ACCESS_FILESYSTEM
	d.use_native_dialog = true
	d.current_dir = receipts_dir()
	d.current_file = file
	d.filters = PackedStringArray(["*.txt ; Receipt"])
	d.file_selected.connect(func(path: String):
		done.call(_write_receipt(path, text))
		d.queue_free())
	d.canceled.connect(d.queue_free)
	parent.add_child(d)
	d.popup_centered_ratio(0.8)


func _write_receipt(path: String, text: String) -> String:
	var f := FileAccess.open(path, FileAccess.WRITE)
	if not f:
		return ""
	f.store_string(text)
	f.close()
	return path
