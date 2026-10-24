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
	top.add_child(Ui.label("Starship Library", 40, Ui.GOLD))
	var spacer := Control.new()
	spacer.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	top.add_child(spacer)
	var back := Ui.button("Quarters", false)
	back.custom_minimum_size = Vector2(180, 64)
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
	var books := {}
	for g in r.data.shelves:
		for b in g.books:
			books[b.code] = b
	body.add_child(Ui.label("Start here", 30, Ui.GOLD))
	body.add_child(Ui.label("Every Trainee learns these first. Each test you pass unlocks its skill.", 22, Ui.MUTED))
	for s in START:
		var b: Dictionary = books.get(s[0], {})
		if not b.is_empty():
			_book_row(b, SKILL_WORD[s[1]])
	for g in r.data.shelves:
		body.add_child(Ui.label(g.group, 28, Ui.GOLD))
		for b in g.books:
			_book_row(b, "")


func _book_row(b: Dictionary, unlocks: String) -> void:
	var text: String = b.title
	if b.passed:
		text = "✓ " + text + "  (" + str(b.score) + ")"
	elif unlocks != "":
		text += "  · unlocks " + unlocks
	if not b.written:
		text += "  · being written"
	var btn := Ui.button(text, false)
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
	body.add_child(Ui.label(r.data.title + ": test", 32, Ui.GOLD))
	body.add_child(Ui.label("Pick one answer for each. %d of %d passes." % [r.data.pass_mark, r.data.questions.size()], 22, Ui.MUTED))
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
			c.toggled.connect(func(on): if on: picks[str(q.id)] = o.id)
			body.add_child(c)
	var send := Ui.button("Hand in the test")
	send.pressed.connect(_mark.bind(code, picks, r.data.questions.size()))
	body.add_child(send)


func _mark(code: String, picks: Dictionary, total: int) -> void:
	if picks.size() < total:
		Ui.error(self, "Answer every question first.")
		return
	var r := await Api.call_api("POST", "/api/dfg/library/test", {"book": code, "answers": picks})
	_clear()
	if not r.ok:
		body.add_child(Ui.label(r.error, 24, Ui.GOLD))
		return
	var passed: bool = r.data.passed
	body.add_child(Ui.label("Passed: %d of %d" % [r.data.score, r.data.of] if passed else "Not yet: %d of %d" % [r.data.score, r.data.of], 34, Ui.GOLD))
	for q in r.data.review:
		body.add_child(Ui.label(("✓ " if q.right else "✗ ") + q.question, 22, Ui.TEXT if q.right else Ui.MUTED))
	if passed:
		var me := await Api.call_api("GET", "/api/dfg/me")
		if me.ok:
			Session.me = me.data
	var again := Ui.button("Back to the shelves" if passed else "Read it again", not passed)
	again.pressed.connect(_shelves if passed else _read.bind(code))
	body.add_child(again)
