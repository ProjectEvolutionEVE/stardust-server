extends Control
## First sign-in: a name from the game's lists and a language. Names are never typed (rule 6).

var opts := {}
var first: OptionButton
var last: OptionButton
var lang: OptionButton
var langs: Array = []


func _ready() -> void:
	var box := Ui.screen(self)
	box.add_child(Ui.label("Welcome aboard, Trainee", 40, Ui.GOLD))
	box.add_child(Ui.label("Choose your name and language.", 24, Ui.MUTED))
	first = Ui.picker()
	last = Ui.picker()
	lang = Ui.picker()
	for w in [first, last, lang]:
		box.add_child(w)
	var go := Ui.button("Report for duty")
	go.pressed.connect(_save.bind(go))
	box.add_child(go)
	var r := await Api.call_api("GET", "/api/dfg/signup-options", {}, false)
	if not r.ok:
		return Ui.error(self, r.error)
	for n in r.data.first_names:
		first.add_item(n)
	for n in r.data.last_names:
		last.add_item(n)
	langs = r.data.languages
	for i in langs.size():
		var l: Dictionary = langs[i]
		lang.add_item("%s %s" % [l.get("flag", ""), l.get("native", l.name)] + ("" if l.supported else " (soon)"))
		lang.set_item_disabled(i, not l.supported)
		if l.code == "en":
			lang.select(i)


func _save(go: Button) -> void:
	if first.selected < 0 or last.selected < 0 or lang.selected < 0:
		return
	go.disabled = true
	var r := await Api.call_api("POST", "/api/dfg/me/setup", {"first_name": first.get_item_text(first.selected),
		"last_name": last.get_item_text(last.selected), "language": langs[lang.selected].code})
	go.disabled = false
	if not r.ok:
		return Ui.error(self, r.error)
	var me := await Api.call_api("GET", "/api/dfg/me")
	if me.ok:
		Session.me = me.data
	get_tree().change_scene_to_file("res://scenes/quarters.tscn")
