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
	lib_btn = _hud_button("Go to the Starship Library", Vector2(80, 330), Vector2(560, 76), 14, "")
	lib_btn.visible = false
	lib_btn.pressed.connect(func(): get_tree().change_scene_to_file("res://scenes/library.tscn"))
	root.add_child(lib_btn)
	var up := _hud_button("", Vector2(600, 760), Vector2(96, 96), 48, "up")
	up.pressed.connect(func(): _set_throttle(throttle + 1))
	root.add_child(up)
	thr_label = Ui.label("Throttle 0%", 22, HUD_RED)
	thr_label.autowrap_mode = TextServer.AUTOWRAP_OFF
	thr_label.position = Vector2(560, 868)
	root.add_child(thr_label)
	var dn := _hud_button("", Vector2(600, 910), Vector2(96, 96), 48, "down")
	dn.pressed.connect(func(): _set_throttle(throttle - 1))
	root.add_child(dn)
	for p in [["left", Vector2(30, 1010), -1], ["right", Vector2(150, 1010), 1]]:
		var bt := _hud_button("", p[1], Vector2(96, 96), 48, p[0])
		var dirn: int = p[2]
		bt.button_down.connect(func(): pivot = dirn)
		bt.button_up.connect(func(): pivot = 0)
		root.add_child(bt)
	var q := _hud_button("Quarters", Vector2(30, 1140), Vector2(220, 64), 14, "")
	q.pressed.connect(func(): get_tree().change_scene_to_file("res://scenes/quarters.tscn"))
	root.add_child(q)


## Flight buttons (Eric 10-24): nothing solid, so the pilot sees through them. A thin deep-red outline, red text, and
## arrows drawn as red outlines; a tap lights the whole button 35% brighter for half a second.
const HUD_RED := Color("a3121c")
const HUD_LIT := Color(0.88, 0.16, 0.24)      # HUD_RED x 1.35


class Glyph extends Control:
	var shape := ""
	var color := Color("a3121c")
	func _draw() -> void:
		var c := size / 2.0
		var r := minf(size.x, size.y) * 0.22
		var pts: PackedVector2Array
		match shape:
			"up": pts = [c + Vector2(0, -r), c + Vector2(r, r * 0.8), c + Vector2(-r, r * 0.8)]
			"down": pts = [c + Vector2(0, r), c + Vector2(-r, -r * 0.8), c + Vector2(r, -r * 0.8)]
			"left": pts = [c + Vector2(-r, 0), c + Vector2(r * 0.8, -r), c + Vector2(r * 0.8, r)]
			"right": pts = [c + Vector2(r, 0), c + Vector2(-r * 0.8, r), c + Vector2(-r * 0.8, -r)]
			_: return
		pts.append(pts[0])
		draw_polyline(pts, color, 2.0, true)


func _hud_button(text: String, at: Vector2, sz: Vector2, radius: int, shape: String) -> Button:
	var b := Button.new()
	b.text = text
	b.position = at
	b.size = sz
	b.focus_mode = Control.FOCUS_NONE
	b.add_theme_font_size_override("font_size", 22)
	var g := Glyph.new()
	g.shape = shape
	g.set_anchors_preset(Control.PRESET_FULL_RECT)
	g.mouse_filter = Control.MOUSE_FILTER_IGNORE
	b.add_child(g)
	_paint(b, g, HUD_RED, radius)
	b.button_down.connect(func():
		_paint(b, g, HUD_LIT, radius)
		get_tree().create_timer(0.5).timeout.connect(func(): if is_instance_valid(b): _paint(b, g, HUD_RED, radius)))
	return b


func _paint(b: Button, g: Glyph, c: Color, radius: int) -> void:
	var s := StyleBoxFlat.new()
	s.bg_color = Color(0, 0, 0, 0)          # transparent inside
	s.border_color = c
	s.set_border_width_all(1)
	s.set_corner_radius_all(radius)
	s.anti_aliasing = true
	for st in ["normal", "hover", "pressed", "focus", "hover_pressed"]:
		b.add_theme_stylebox_override(st, s)
	for fc in ["font_color", "font_hover_color", "font_pressed_color", "font_focus_color", "font_hover_pressed_color"]:
		b.add_theme_color_override(fc, c)
	g.color = c
	g.queue_redraw()


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
