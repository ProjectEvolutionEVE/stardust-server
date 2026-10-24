extends Node3D
## The Docking Bay (rule 19), in 3D: you start docked inside the Starship's belly bay, looking out past the bow, the same
## view as the browser game. Flight controls match the browser (Eric 10-17/10-24): the throttle arrows on the right set
## speed (10% a tap, 0% stops); press and hold anywhere to steer like a joystick (pull back = nose up, push = nose down,
## left/right = bank); the side thrusters bottom left turn you in place. Launching needs the Pilot Basic Training
## Handbook pass (Eric 10-23); without it the craft stays docked and the bay points you to the library.

const MAXV := 60.0
const ACC := 40.0
const STICK_R := 140.0

var ship: Node3D
var cam: Camera3D
var vel := Vector3.ZERO
var rot := Vector3.ZERO          # pitch, yaw, roll rates (rad/s)
var throttle := 0                # 0..10
var docked := true
var stick_from := Vector2.ZERO
var stick_at := Vector2.ZERO
var holding := false
var pivot := 0                   # -1 left, +1 right
var status: Label
var thr_label: Label
var note: Label
var note_until := 0.0
var lib_btn: Button


func _ready() -> void:
	var env := WorldEnvironment.new()
	var e := Environment.new()
	e.background_mode = Environment.BG_COLOR
	e.background_color = Color.BLACK
	e.ambient_light_source = Environment.AMBIENT_SOURCE_COLOR
	e.ambient_light_color = Color("0a0d14")
	e.ambient_light_energy = 1.2
	e.tonemap_mode = Environment.TONE_MAPPER_ACES
	env.environment = e
	add_child(env)
	var sun := DirectionalLight3D.new()      # the Sun ahead: the ship faces it (bow toward the Sun)
	sun.light_color = Color("fff1dc")
	sun.light_energy = 1.8
	sun.rotation = Vector3(-0.15, PI, 0)
	add_child(sun)
	ship = preload("res://scripts/starship.gd").new()
	add_child(ship)
	_stars()
	cam = Camera3D.new()
	cam.fov = 62
	cam.near = 0.3
	cam.far = 20000
	add_child(cam)
	_dock()
	_hud()


func _dock() -> void:
	docked = true
	vel = Vector3.ZERO
	rot = Vector3.ZERO
	throttle = 0
	cam.position = ship.DOCK.mouth
	cam.look_at(Vector3(0, -30, 400), Vector3.UP)     # facing out past the bow


func _stars() -> void:
	var mm := MultiMesh.new()
	mm.transform_format = MultiMesh.TRANSFORM_3D
	var qm := QuadMesh.new()
	qm.size = Vector2(6, 6)
	mm.mesh = qm
	mm.instance_count = 2500
	var rng := RandomNumberGenerator.new()
	rng.seed = 7
	for i in mm.instance_count:
		var d := Vector3(rng.randfn(), rng.randfn(), rng.randfn()).normalized()
		var p := d * 9000.0
		var b := Basis.looking_at(-d, Vector3.UP if absf(d.y) < 0.99 else Vector3.RIGHT)
		mm.set_instance_transform(i, Transform3D(b.scaled(Vector3.ONE * rng.randf_range(0.4, 1.4)), p))
	var mi := MultiMeshInstance3D.new()
	mi.multimesh = mm
	var m := StandardMaterial3D.new()
	m.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	m.albedo_color = Color("dfe6ff")
	m.billboard_mode = BaseMaterial3D.BILLBOARD_ENABLED
	mi.material_override = m
	add_child(mi)


# ── the screen: status, throttle arrows (right), side thrusters (bottom left), Quarters ──
func _hud() -> void:
	var layer := CanvasLayer.new()
	add_child(layer)
	var root := Control.new()
	root.set_anchors_preset(Control.PRESET_FULL_RECT)
	root.mouse_filter = Control.MOUSE_FILTER_IGNORE
	layer.add_child(root)
	status = Ui.label("", 24, Color("7fe0a8"))
	status.autowrap_mode = TextServer.AUTOWRAP_OFF
	status.position = Vector2(0, 1220)
	status.size = Vector2(720, 40)
	status.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	root.add_child(status)
	note = Ui.label("", 26, Ui.TEXT)
	note.position = Vector2(40, 130)
	note.size = Vector2(640, 180)
	note.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	root.add_child(note)
	lib_btn = Ui.button("Go to the Starship Library")
	lib_btn.position = Vector2(80, 330)
	lib_btn.size = Vector2(560, 76)
	lib_btn.visible = false
	lib_btn.pressed.connect(func(): get_tree().change_scene_to_file("res://scenes/library.tscn"))
	root.add_child(lib_btn)
	var up := _round_button("▲", Vector2(600, 760))
	up.pressed.connect(func(): _set_throttle(throttle + 1))
	root.add_child(up)
	thr_label = Ui.label("Throttle 0%", 22, Ui.GOLD)
	thr_label.autowrap_mode = TextServer.AUTOWRAP_OFF
	thr_label.position = Vector2(560, 868)
	root.add_child(thr_label)
	var dn := _round_button("▼", Vector2(600, 910))
	dn.pressed.connect(func(): _set_throttle(throttle - 1))
	root.add_child(dn)
	for p in [["◀", Vector2(30, 1010), -1], ["▶", Vector2(150, 1010), 1]]:
		var b := _round_button(p[0], p[1])
		var dirn: int = p[2]
		b.button_down.connect(func(): pivot = dirn)
		b.button_up.connect(func(): pivot = 0)
		root.add_child(b)
	var q := Ui.button("Quarters", false)
	q.position = Vector2(30, 1140)
	q.size = Vector2(220, 64)
	q.add_theme_font_size_override("font_size", 22)
	q.pressed.connect(func(): get_tree().change_scene_to_file("res://scenes/quarters.tscn"))
	root.add_child(q)


func _round_button(text: String, at: Vector2) -> Button:
	var b := Ui.button(text, false)
	b.position = at
	b.size = Vector2(96, 96)
	b.custom_minimum_size = Vector2(96, 96)
	var s := StyleBoxFlat.new()
	s.bg_color = Color(0.1, 0.12, 0.18, 0.55)
	s.border_color = Ui.GOLD
	s.set_border_width_all(2)
	s.set_corner_radius_all(48)
	for st in ["normal", "hover", "pressed", "focus"]:
		b.add_theme_stylebox_override(st, s)
	return b


func _set_throttle(n: int) -> void:
	throttle = clampi(n, 0, 10)
	thr_label.text = "Throttle %d%%" % (throttle * 10)


func _say(text: String, library := false) -> void:
	note.text = text
	note_until = Time.get_ticks_msec() / 1000.0 + 5.0
	lib_btn.visible = library


# ── steering: press and hold anywhere on the screen (not on a button) ──
func _unhandled_input(ev: InputEvent) -> void:
	if ev is InputEventMouseButton and ev.button_index == MOUSE_BUTTON_LEFT or ev is InputEventScreenTouch:
		holding = ev.pressed
		stick_from = ev.position
		stick_at = ev.position
	elif (ev is InputEventMouseMotion or ev is InputEventScreenDrag) and holding:
		stick_at = ev.position


func _process(dt: float) -> void:
	var now := Time.get_ticks_msec() / 1000.0
	if note.text != "" and now > note_until:
		note.text = ""
		lib_btn.visible = false
	if docked and (throttle > 0 or holding):
		if not Session.me.get("skills", {}).get("fly", false):
			_set_throttle(0)
			holding = false
			_say("LIBRARY FIRST\nPass the Pilot Basic Training Handbook test before you can fly.", true)
		else:
			docked = false
	if docked:
		status.text = "DOCKED · throttle up to launch"
		return
	status.text = "Speed %.1f m/s" % vel.length()
	# turning: the stick (pull back = nose up, right = bank right) and the side thrusters (turn in place)
	var s := Vector2.ZERO
	if holding:
		s = ((stick_at - stick_from) / STICK_R).limit_length(1.0)
	var tp := s.y * 1.1
	var tr := -s.x * 1.5
	var ty := -s.x * 0.55 - pivot * 0.8
	var k := 1.0 - exp(-4.0 * dt)
	rot += (Vector3(tp, ty, tr) - rot) * k
	cam.rotate_object_local(Vector3.RIGHT, rot.x * dt)
	cam.rotate_object_local(Vector3.UP, rot.y * dt)
	cam.rotate_object_local(Vector3.FORWARD, -rot.z * dt)
	# thrust: the throttle sets the speed (0% = drift to a stop)
	var fwd := -cam.global_basis.z
	var cap := MAXV * throttle / 10.0
	var tf := 1.0 if throttle > 0 and vel.length() < cap else 0.0
	vel += fwd * tf * ACC * dt
	var idle := tf == 0.0
	vel *= exp(-(0.35 if throttle > 0 else 1.2) * dt) if idle else 1.0
	cam.position += vel * dt
