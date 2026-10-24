extends Control
## The Docking Bay (rule 19): the way out to the flight. Flying needs the Pilot Basic Training Handbook pass (Eric 10-23).
## The 3D flight is not in the app yet; until it is, the bay says so and the browser game is where to fly.


func _ready() -> void:
	var box := Ui.screen(self)
	box.add_child(Ui.label("Docking Bay", 40, Ui.GOLD))
	var sk: Dictionary = Session.me.get("skills", {})
	if not sk.get("fly", false):
		box.add_child(Ui.label("Your starter mining craft stays docked until you pass the Pilot Basic Training Handbook test in the Starship Library.", 26))
		var lib := Ui.button("Go to the Starship Library")
		lib.pressed.connect(func(): get_tree().change_scene_to_file("res://scenes/library.tscn"))
		box.add_child(lib)
	else:
		box.add_child(Ui.label("Your starter mining craft is ready for launch.", 26))
		if not sk.get("mine", false):
			box.add_child(Ui.label("You can fly, but pass the Mining test before you can collect from the debris fields.", 24, Ui.GOLD))
		box.add_child(Ui.label("Space flight is coming to the app next. For now, fly in the browser game; your account is the same.", 24, Ui.MUTED))
	var back := Ui.button("Back to quarters", false)
	back.pressed.connect(func(): get_tree().change_scene_to_file("res://scenes/quarters.tscn"))
	box.add_child(back)
