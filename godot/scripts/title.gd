extends Control
## Title: STARDUST / TERRA DELETA. A saved sign-in goes straight in; otherwise to sign-in.


func _ready() -> void:
	var box := Ui.screen(self)
	box.alignment = BoxContainer.ALIGNMENT_CENTER
	var t := Ui.label("STARDUST", 72, Ui.GOLD)
	t.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	box.add_child(t)
	var s := Ui.label("TERRA DELETA", 32, Ui.MUTED)
	s.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	box.add_child(s)
	var go := Ui.button("Launch")
	go.pressed.connect(_launch.bind(go))
	box.add_child(go)


func _launch(go: Button) -> void:
	go.disabled = true
	if Session.token == "":
		get_tree().change_scene_to_file("res://scenes/signin.tscn")
		return
	go.text = "Contacting the Starship…"
	var r := await Api.call_api("GET", "/api/dfg/me")
	if r.ok:
		Session.me = r.data
		Session.call_on_enter = "wake"
		get_tree().change_scene_to_file(Session.next_scene())
	elif r.code == 0:   # no answer: keep the sign-in, let the player try again
		go.text = "Launch"
		go.disabled = false
		Ui.error(self, r.error)
	else:
		Session.clear()
		get_tree().change_scene_to_file("res://scenes/signin.tscn")
