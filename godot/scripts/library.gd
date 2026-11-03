extends Control
## The Starship Library (rule 24): read a book, take its five-question test (4 of 5 passes). Skills come from passes
## (Eric 10-23): flying needs the Pilot Basic Training Handbook, mining needs Mining, selling needs Trading & Markets,
## so those three are shelved first, under "Start here". The answers never leave the server.

const START := [["piloting", "fly"], ["mining", "mine"], ["trading", "sell"]]
const SKILL_WORD := {"fly": "Flying", "mine": "Mining", "sell": "Selling"}

var body: VBoxContainer


func _ready() -> void:
	var outer := Ui.screen(self)
	var top := HBoxContainer.new()
	var title := Ui.label("Starship Library", 40, Ui.GOLD)
	title.autowrap_mode = TextServer.AUTOWRAP_OFF          # one line; it takes the room the button doesn't
	title.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	top.add_child(title)
	var back := Ui.button("Quarters", false)
	back.custom_minimum_size = Vector2(160, 56)
	back.size_flags_vertical = Control.SIZE_SHRINK_CENTER
	back.add_theme_font_size_override("font_size", 22)
	back.pressed.connect(func(): get_tree().change_scene_to_file("res://scenes/quarters.tscn"))
	top.add_child(back)
	outer.add_child(top)
	var scroll := ScrollContainer.new()
	scroll.size_flags_vertical = Control.SIZE_EXPAND_FILL
	scroll.horizontal_scroll_mode = ScrollContainer.SCROLL_MODE_DISABLED
	outer.add_child(scroll)
	body = VBoxContainer.new()
	body.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	body.add_theme_constant_override("separation", 14)
	scroll.add_child(body)
	_shelves()


func _clear() -> void:
	for c in body.get_children():
		c.queue_free()


func _shelves() -> void:
	_clear()
	body.add_child(Ui.label("Loading the shelves…", 24, Ui.MUTED))
	var r := await Api.call_api("GET", "/api/dfg/library")
	_clear()
	if not r.ok:
		body.add_child(Ui.label(r.error, 24, Ui.GOLD))
		return
	render(r.data)


## The shelves from GET /api/dfg/library: Start here, then a shelf per career with its bars, then every subject.
func render(data: Dictionary) -> void:
	_clear()
	var books := {}
	for g in data.shelves:
		for b in g.books:
			books[b.code] = b
	body.add_child(Ui.label("Start here", 30, Ui.GOLD))
	body.add_child(Ui.label("Every Trainee learns these first. Each test you pass unlocks its skill.", 22, Ui.MUTED))
	for s in START:
		var b: Dictionary = books.get(s[0], {})
		if not b.is_empty():
			_book_row(b, tr(SKILL_WORD[s[1]]))
	if data.has("careers"):
		body.add_child(Ui.label("Careers", 30, Ui.GOLD))
		body.add_child(Ui.label("Each bar is earned by the number of a career's books you pass: 5, then 20, 65, 185 and 510 in all. Many Library subjects count toward more than one career. A bar is gold when every test that earned it is perfect; retake any test to turn silver gold.", 22, Ui.MUTED))
		for c in data.careers:
			_career(c, data.get("uniform") == c.code)
	for g in data.shelves:
		body.add_child(Ui.label(g.group, 28, Ui.GOLD))
		for b in g.books:
			_book_row(b, "")


## One career's shelf (rule 32): its colour, the title earned, its five bars, and its books by bar (tap to open).
func _career(c: Dictionary, worn: bool) -> void:
	var head := HBoxContainer.new()
	head.add_theme_constant_override("separation", 12)
	head.add_child(Ui.swatch(c.colour))
	var name := Ui.button((tr("%s  ·  %s  (wearing)") if worn else tr("%s  ·  %s")) % [c.name, c.title], false)
	name.alignment = HORIZONTAL_ALIGNMENT_LEFT
	name.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	name.add_theme_font_size_override("font_size", 24)
	head.add_child(name)
	body.add_child(head)
	var strip := Ui.bar_strip(c.bars, 16)             # its own line, so the shelf fits a phone's width
	strip.size_flags_horizontal = Control.SIZE_SHRINK_END
	body.add_child(strip)
	var shelf := VBoxContainer.new()
	shelf.add_theme_constant_override("separation", 10)
	shelf.visible = false
	body.add_child(shelf)
	name.pressed.connect(func(): shelf.visible = not shelf.visible)
	if float(c.skill_pct) > 0:
		shelf.add_child(Ui.label(tr("%s skill: +%s%%") % [c.name, Ui.dec(float(c.skill_pct), 2)], 22, Ui.GREEN))
	for bar in c.bars:
		var medal = bar.get("medal")
		var state: String = (tr("Gold") if medal == "gold" else tr("Silver")) if medal != null else tr("Not yet")
		shelf.add_child(Ui.label(tr("Bar %d · %s · %s") % [int(bar.bar), bar.title, state], 26,
			Ui.GOLD if medal == "gold" else (Ui.SILVER if medal == "silver" else Ui.TEXT)))
		shelf.add_child(Ui.label(str(bar.note), 20, Ui.MUTED))
		var saved := body
		body = shelf                         # _book_row adds to body; aim it at this shelf for a moment
		for b in c.books:
			if int(b.bar) == int(bar.bar):
				_book_row(b, "")
		body = saved


func _book_row(b: Dictionary, unlocks: String) -> void:
	var text: String = b.title
	if b.passed:
		text = tr("✓ %s  (%s)") % [text, str(b.score)]
	elif unlocks != "":
		text = tr("%s  · unlocks %s") % [text, unlocks]
	if not b.written:
		text = tr("%s  · being written") % text
	var btn := Ui.button(text, false)
	if b.passed:   # a completed book shows green
		var g := StyleBoxFlat.new()
		g.bg_color = Ui.PANEL
		g.border_color = Ui.GREEN
		g.set_border_width_all(2)
		g.set_corner_radius_all(14)
		for state in ["normal", "hover", "pressed", "focus"]:
			btn.add_theme_stylebox_override(state, g)
		for c in ["font_color", "font_hover_color", "font_pressed_color", "font_focus_color"]:
			btn.add_theme_color_override(c, Ui.GREEN)
	btn.disabled = not b.written
	btn.alignment = HORIZONTAL_ALIGNMENT_LEFT
	btn.add_theme_font_size_override("font_size", 24)
	btn.pressed.connect(_read.bind(b.code))
	body.add_child(btn)


func _read(code: String) -> void:
	_clear()
	var r := await Api.call_api("GET", "/api/dfg/library/book/" + code)
	if not r.ok:
		body.add_child(Ui.label(r.error, 24, Ui.GOLD))
		return
	var b: Dictionary = r.data
	body.add_child(Ui.label(b.title, 34, Ui.GOLD))
	body.add_child(Ui.label(b.subtitle, 22, Ui.MUTED))
	if int(b.questions) > 0:
		body.add_child(_test_button(code))
	for ch in b.chapters:
		body.add_child(Ui.label(ch.title, 28, Ui.GOLD))
		body.add_child(Ui.label(ch.text, 24))
	if int(b.questions) > 0:
		body.add_child(_test_button(code))
	var back := Ui.button("Back to the shelves", false)
	back.pressed.connect(_shelves)
	body.add_child(back)


func _test_button(code: String) -> Button:
	var t := Ui.button("Take the test")
	t.pressed.connect(_test.bind(code))
	return t


func _test(code: String) -> void:
	_clear()
	var r := await Api.call_api("GET", "/api/dfg/library/test/" + code)
	if not r.ok:
		body.add_child(Ui.label(r.error, 24, Ui.GOLD))
		return
	body.add_child(Ui.label(tr("%s: test") % r.data.title, 32, Ui.GOLD))
	body.add_child(Ui.label(tr("Pick one answer for each. %d of %d passes.") % [r.data.pass_mark, r.data.questions.size()], 22, Ui.MUTED))
	var picks := {}
	for q in r.data.questions:
		body.add_child(Ui.label(q.question, 26))
		var group := ButtonGroup.new()
		for o in q.options:
			var c := CheckBox.new()
			c.text = o.text
			c.button_group = group
			c.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
			c.add_theme_font_size_override("font_size", 24)
			c.add_theme_color_override("font_pressed_color", Ui.GREEN)
			c.add_theme_color_override("font_hover_pressed_color", Ui.GREEN)
			c.toggled.connect(func(on):
				c.text = ("✓ " if on else "") + o.text   # the chosen answer shows a green check
				if on:
					picks[str(int(q.id))] = o.id)   # JSON numbers arrive as floats: "0", not "0.0"
			body.add_child(c)
	var send := Ui.button("Hand in the test")
	send.pressed.connect(_mark.bind(code, picks, r.data.questions.size()))
	body.add_child(send)


func _mark(code: String, picks: Dictionary, total: int) -> void:
	if picks.size() < total:
		Ui.error(self, tr("Answer every question first."))
		return
	var r := await Api.call_api("POST", "/api/dfg/library/test", {"book": code, "answers": picks})
	_clear()
	if not r.ok:
		body.add_child(Ui.label(r.error, 24, Ui.GOLD))
		return
	var passed: bool = r.data.passed
	body.add_child(Ui.label((tr("Passed: %d of %d") if passed else tr("Not yet: %d of %d")) % [r.data.score, r.data.of], 34, Ui.GOLD))
	for q in r.data.review:
		body.add_child(Ui.label(("✓ " if q.right else "✗ ") + q.question, 22, Ui.TEXT if q.right else Ui.MUTED))
	if passed:
		var me := await Api.call_api("GET", "/api/dfg/me")
		if me.ok:
			Session.me = me.data
	var again := Ui.button("Back to the shelves" if passed else "Read it again", not passed)
	again.pressed.connect(_shelves if passed else _read.bind(code))
	body.add_child(again)
