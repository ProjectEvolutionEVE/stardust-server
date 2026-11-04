class_name WheelPicker
extends Button
## The app's dropdown (Eric 11-02): a tap opens a chooser with a search box you can type in and a wheel you scroll either
## way; the item in the middle is always highlighted, and it snaps to the nearest item when you let go. Tap the middle
## item (or Choose) to pick it. It answers the same calls the screens used on Godot's OptionButton (add_item, select,
## selected, item_selected…), so every Ui.picker() gets it.

signal item_selected(index: int)

const ROW_H := 64
const ROWS := 7              # rows in view; the middle one is the choice

var selected := -1
var item_count: int:
	get: return _items.size()
var title := ""              # shown above the search box

var _items: Array = []       # {text, disabled, meta}


func _init() -> void:
	alignment = HORIZONTAL_ALIGNMENT_LEFT
	text_overrun_behavior = TextServer.OVERRUN_TRIM_ELLIPSIS
	custom_minimum_size = Vector2(0, 72)
	add_theme_font_size_override("font_size", 26)
	var s := StyleBoxFlat.new()
	s.bg_color = Color("101624")
	s.border_color = Color(Ui.GOLD, 0.45)
	s.set_border_width_all(1)
	s.set_corner_radius_all(10)
	s.content_margin_left = 16
	s.content_margin_right = 44
	for st in ["normal", "hover", "pressed", "focus", "disabled"]:
		add_theme_stylebox_override(st, s)
	for c in ["font_color", "font_hover_color", "font_pressed_color", "font_focus_color"]:
		add_theme_color_override(c, Ui.TEXT)
	var arrow := Label.new()
	arrow.text = "▾"
	arrow.add_theme_font_size_override("font_size", 26)
	arrow.add_theme_color_override("font_color", Ui.GOLD)
	arrow.anchor_left = 1.0
	arrow.anchor_right = 1.0
	arrow.anchor_top = 0.5
	arrow.anchor_bottom = 0.5
	arrow.offset_left = -38
	arrow.offset_top = -18
	arrow.offset_bottom = 18
	arrow.mouse_filter = Control.MOUSE_FILTER_IGNORE
	add_child(arrow)
	pressed.connect(show_popup)


func add_item(t: String) -> void:
	_items.append({"text": t, "disabled": false, "meta": null})
	if selected < 0:
		select(0)


func clear() -> void:
	_items.clear()
	selected = -1
	text = ""


func set_item_disabled(i: int, off: bool) -> void:
	_items[i].disabled = off


func set_item_metadata(i: int, v: Variant) -> void:
	_items[i].meta = v


func get_item_metadata(i: int) -> Variant:
	return _items[i].meta


func get_item_text(i: int) -> String:
	return _items[i].text


func select(i: int) -> void:
	selected = i
	text = _items[i].text if i >= 0 and i < _items.size() else ""


func show_popup() -> void:
	if _items.is_empty():
		return
	var layer := CanvasLayer.new()
	layer.layer = 50
	get_tree().root.add_child(layer)
	var c := Chooser.new()
	c.setup(self, layer)
	layer.add_child(c)


func _picked(i: int) -> void:
	select(i)
	item_selected.emit(i)


## The chooser itself: search box, wheel, Choose and Cancel.
class Chooser extends Control:
	var owner_picker: WheelPicker
	var layer: CanvasLayer
	var search: LineEdit
	var scroll: ScrollContainer
	var list: VBoxContainer
	var shown: Array = []      # item indices in view, after the search
	var rows: Array = []       # their Labels
	var centre := -1           # position in `shown` under the band
	var still := 0.0           # seconds the wheel hasn't moved
	var last_v := -1.0
	var snapping: Tween
	var choose: Button

	func setup(p: WheelPicker, l: CanvasLayer) -> void:
		owner_picker = p
		layer = l

	func _ready() -> void:
		size = get_viewport_rect().size          # a CanvasLayer isn't a Control, so fill the screen by hand
		layout_direction = Control.LAYOUT_DIRECTION_LOCALE
		get_viewport().size_changed.connect(func(): size = get_viewport_rect().size)
		var dim := ColorRect.new()
		dim.color = Color(0, 0, 0, 0.75)
		dim.set_anchors_preset(Control.PRESET_FULL_RECT)
		add_child(dim)
		var panel := PanelContainer.new()
		var st := StyleBoxFlat.new()
		st.bg_color = Ui.PANEL
		st.border_color = Ui.GOLD
		st.set_border_width_all(2)
		st.set_corner_radius_all(16)
		st.set_content_margin_all(20)
		panel.add_theme_stylebox_override("panel", st)
		panel.custom_minimum_size = Vector2(640, 0)
		var centre_box := CenterContainer.new()
		centre_box.set_anchors_preset(Control.PRESET_FULL_RECT)
		add_child(centre_box)
		centre_box.add_child(panel)
		var v := VBoxContainer.new()
		v.add_theme_constant_override("separation", 14)
		panel.add_child(v)
		if owner_picker.title != "":
			v.add_child(Ui.label(owner_picker.title, 28, Ui.GOLD))
		search = Ui.field("🔍 Type to search")
		search.clear_button_enabled = true
		search.text_changed.connect(func(_t): _fill())
		v.add_child(search)
		var wheel := Control.new()
		wheel.custom_minimum_size = Vector2(0, ROW_H * ROWS)
		wheel.clip_contents = true
		v.add_child(wheel)
		var band := Panel.new()          # the highlighted middle row
		var bs := StyleBoxFlat.new()
		bs.bg_color = Color(Ui.GOLD, 0.14)
		bs.border_color = Ui.GOLD
		bs.set_border_width_all(2)
		bs.set_corner_radius_all(10)
		band.add_theme_stylebox_override("panel", bs)
		band.anchor_right = 1.0
		band.offset_top = ROW_H * (ROWS / 2)
		band.offset_bottom = ROW_H * (ROWS / 2 + 1)
		band.mouse_filter = Control.MOUSE_FILTER_IGNORE
		wheel.add_child(band)
		scroll = ScrollContainer.new()
		scroll.set_anchors_preset(Control.PRESET_FULL_RECT)
		scroll.horizontal_scroll_mode = ScrollContainer.SCROLL_MODE_DISABLED
		scroll.vertical_scroll_mode = ScrollContainer.SCROLL_MODE_SHOW_NEVER
		wheel.add_child(scroll)
		wheel.move_child(band, 1)        # drawn over the rows
		list = VBoxContainer.new()
		list.size_flags_horizontal = Control.SIZE_EXPAND_FILL
		list.add_theme_constant_override("separation", 0)
		scroll.add_child(list)
		var buttons := HBoxContainer.new()
		buttons.add_theme_constant_override("separation", 12)
		var cancel := Ui.button("Cancel", false)
		cancel.size_flags_horizontal = Control.SIZE_EXPAND_FILL
		cancel.pressed.connect(_close)
		buttons.add_child(cancel)
		choose = Ui.button("Choose")
		choose.size_flags_horizontal = Control.SIZE_EXPAND_FILL
		choose.pressed.connect(_choose)
		buttons.add_child(choose)
		v.add_child(buttons)
		_fill()

	## Rebuild the wheel for the search text, keeping the current choice in the middle if it's still listed.
	func _fill() -> void:
		for c in list.get_children():
			c.queue_free()
		rows.clear()
		shown.clear()
		var q := search.text.strip_edges().to_lower()
		for i in owner_picker._items.size():
			if q == "" or q in str(owner_picker._items[i].text).to_lower():
				shown.append(i)
		list.add_child(_pad())
		for k in shown.size():
			var it: Dictionary = owner_picker._items[shown[k]]
			var l := Label.new()
			l.text = it.text
			l.custom_minimum_size = Vector2(0, ROW_H)
			l.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
			l.vertical_alignment = VERTICAL_ALIGNMENT_CENTER
			l.text_overrun_behavior = TextServer.OVERRUN_TRIM_ELLIPSIS
			l.mouse_filter = Control.MOUSE_FILTER_PASS
			l.gui_input.connect(_row_input.bind(k))
			list.add_child(l)
			rows.append(l)
		list.add_child(_pad())
		if shown.is_empty():
			var none := Label.new()
			none.text = tr("Nothing matches.")
			none.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
			none.add_theme_color_override("font_color", Ui.MUTED)
			list.add_child(none)
		var at := maxi(0, shown.find(owner_picker.selected))
		centre = -1
		await get_tree().process_frame
		scroll.scroll_vertical = at * ROW_H
		_mark(at)

	func _pad() -> Control:
		var c := Control.new()
		c.custom_minimum_size = Vector2(0, ROW_H * (ROWS / 2))
		c.mouse_filter = Control.MOUSE_FILTER_PASS
		return c

	## A tap (not a drag) on a row: the middle row is chosen, any other row rolls to the middle.
	var _press_v := 0.0
	func _row_input(e: InputEvent, k: int) -> void:
		if e.device == InputEvent.DEVICE_ID_EMULATION:
			return    # a phone's touch also arrives as a copied mouse event: count it once
		if (e is InputEventMouseButton and e.button_index == MOUSE_BUTTON_LEFT) or e is InputEventScreenTouch:
			if e.pressed:
				_press_v = scroll.scroll_vertical
			elif absf(scroll.scroll_vertical - _press_v) < 8:
				if k == centre:
					_choose()
				else:
					_roll(k)

	func _roll(k: int) -> void:
		if snapping:
			snapping.kill()
		snapping = create_tween()
		snapping.tween_property(scroll, "scroll_vertical", k * ROW_H, 0.18).set_trans(Tween.TRANS_SINE)

	func _process(delta: float) -> void:
		if rows.is_empty():
			return
		var v := float(scroll.scroll_vertical)
		var k := clampi(int(round(v / ROW_H)), 0, rows.size() - 1)
		if k != centre:
			_mark(k)
		if absf(v - last_v) < 0.5:
			still += delta
			if still > 0.15 and absf(v - k * ROW_H) > 0.5 and not (snapping and snapping.is_running()):
				_roll(k)                 # let go between two rows: settle on the nearer one
		else:
			still = 0.0
		last_v = v

	## Highlight the middle row; rows fade the further they are from it.
	func _mark(k: int) -> void:
		centre = k
		for j in rows.size():
			var it: Dictionary = owner_picker._items[shown[j]]
			var d := absi(j - k)
			var l: Label = rows[j]
			l.add_theme_font_size_override("font_size", 32 if d == 0 else 26)
			var col: Color = Ui.GOLD if d == 0 else Ui.TEXT
			if it.disabled:
				col = Ui.MUTED
			col.a = 1.0 if d == 0 else maxf(0.3, 0.85 - 0.18 * d)
			l.add_theme_color_override("font_color", col)
		choose.disabled = shown.is_empty() or owner_picker._items[shown[k]].disabled

	func _choose() -> void:
		if shown.is_empty() or centre < 0 or owner_picker._items[shown[centre]].disabled:
			return
		owner_picker._picked(shown[centre])
		_close()

	func _close() -> void:
		layer.queue_free()
