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
