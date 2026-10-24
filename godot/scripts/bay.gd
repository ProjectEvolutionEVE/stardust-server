extends Node3D
## The Docking Bay (rule 19), in 3D: you start docked inside the Starship's belly bay, looking out past the bow, the same
## view as the browser game. Flight controls match the browser (Eric 10-17/10-24): the throttle arrows on the right set
## speed (10% a tap, 0% stops); press and hold anywhere to steer like a joystick (pull back = nose up, push = nose down,
## left/right = bank); the side thrusters bottom left turn you in place. Launching needs the Pilot Basic Training
## Handbook pass (Eric 10-23); without it the craft stays docked and the bay points you to the library.
## Around it, the solar system at true scale (scripts/solar.gd) with labels on the landmarks, and WARP (Eric 10-11) to
## any of the four rings, the Starship, the wormhole, Jupiter or Saturn, as in the browser.

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
var sol: Node3D
var org := [0.0, 0.0, 0.0]       # the scene's origin in the ship's frame, 64-bit metres (floating origin)
var warp := {}                   # the warp under way, if any
var warp_panel: Control
var warp_list: VBoxContainer
var marks: Control
var streaks: Control


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
	ship = preload("res://scripts/starship.gd").new()
	add_child(ship)
	sol = preload("res://scripts/solar.gd").new()     # the Sun (the one light), the planets, the wormhole, the stars
	add_child(sol)
	sol.setup(ship)
	cam = Camera3D.new()
	cam.fov = 62
	cam.near = 0.3
	cam.far = 400000
	add_child(cam)
	_dock()
	_hud()
	sol.place(org, cam)


func _dock() -> void:
	docked = true
	vel = Vector3.ZERO
	rot = Vector3.ZERO
	throttle = 0
	org = [0.0, 0.0, 0.0]
	cam.position = ship.DOCK.mouth
	cam.look_at(Vector3(0, -30, 400), Vector3.UP)     # facing out past the bow


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
	marks = Marks.new()
	marks.bay = self
	marks.set_anchors_preset(Control.PRESET_FULL_RECT)
	marks.mouse_filter = Control.MOUSE_FILTER_IGNORE
	root.add_child(marks)
	root.move_child(marks, 0)          # labels under the buttons
	streaks = Streaks.new()
	streaks.set_anchors_preset(Control.PRESET_FULL_RECT)
	streaks.mouse_filter = Control.MOUSE_FILTER_IGNORE
	root.add_child(streaks)
	root.move_child(streaks, 0)
	var wb := _hud_button("WARP", Vector2(540, 40), Vector2(150, 64), 32, "")
	wb.pressed.connect(func():
		if warp.is_empty():
			_warp_menu()
			warp_panel.visible = not warp_panel.visible)
	root.add_child(wb)
	_warp_panel(root)


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
	if not warp.is_empty():
		_warp_tick(dt)
	else:
		_fly(dt)
	if cam.position.length() > 1000.0:       # floating origin: keep the camera near the scene's origin
		org = Solar.add(org, [cam.position.x, cam.position.y, cam.position.z])
		cam.position = Vector3.ZERO
	sol.place(org, cam)
	marks.queue_redraw()
	if not warp.is_empty():
		status.text = "WARP · " + warp.label
	elif not docked:
		var me := _me()
		var here = sol.ring_of(sol.to_world_d(me))
		status.text = "Speed %.1f m/s · %.3f AU from the Sun" % [vel.length(), Solar.length(Solar.sub(me, sol.sun_l)) / Solar.AU]
		if here != null:
			status.text = here.name + " · " + status.text


func _fly(dt: float) -> void:
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


## The pilot's true position in the ship's frame, 64-bit metres.
func _me() -> Array:
	return Solar.add(org, [cam.position.x, cam.position.y, cam.position.z])


# ── WARP (Eric 10-11): pick a destination and you're there in seconds. Rings: you arrive on the ring's line at your
#    current longitude. The route bends around the Sun if a straight line would pass too close.
const Solar := preload("res://scripts/solar.gd")


func _dests() -> Array:
	var d := [{"key": "starship", "label": "Starship", "note": "home · by the wormhole"}]
	for rg in Solar.RINGS:
		d.append({"key": rg.key, "label": rg.name, "ring": rg, "note": "%.3f AU from the Sun" % rg.au})
	d.append({"key": "wormhole", "label": "Wormhole", "note": "3,000,000 km beyond Jupiter"})
	for g in Solar.GIANTS:
		d.append({"key": g.name.to_lower(), "label": g.name, "note": "%.3f AU from the Sun" % g.au})
	return d


## Where a destination puts you, in the ship's frame.
func _dest_point(d: Dictionary) -> Array:
	if d.has("ring"):
		var w: Array = sol.to_world_d(_me())
		var lon := atan2(w[2], w[0])
		return sol.to_local_d([cos(lon) * d.ring.au * Solar.AU, (randf() - 0.5) * 2000.0, sin(lon) * d.ring.au * Solar.AU])
	if d.key == "starship":
		return [0.0, -34.0, 1100.0]
	if d.key == "wormhole":
		var out := Solar.norm(sol.wh_w)
		return sol.to_local_d(Solar.add(Solar.add(sol.wh_w, Solar.mul(out, -15000.0)), [0.0, 3000.0, 0.0]))
	for g in Solar.GIANTS:
		if g.name.to_lower() == d.key:
			var gw: Array = sol.giant_w(g)
			return sol.to_local_d(Solar.mul(gw, 1.0 - 12.0 * g.rad / Solar.length(gw)))
	return _me()


func _lon_deg(l: Array) -> float:
	var w: Array = sol.to_world_d(l)
	return fposmod(rad_to_deg(atan2(w[2], w[0])), 360.0)


func _warp_panel(root: Control) -> void:
	warp_panel = Panel.new()
	var sb := StyleBoxFlat.new()
	sb.bg_color = Color(0.043, 0.063, 0.125, 0.92)
	sb.border_color = HUD_RED
	sb.set_border_width_all(1)
	sb.set_corner_radius_all(14)
	warp_panel.add_theme_stylebox_override("panel", sb)
	warp_panel.position = Vector2(30, 120)
	warp_panel.size = Vector2(660, 880)
	warp_panel.visible = false
	root.add_child(warp_panel)
	var h := Ui.label("WARP", 26, HUD_RED)
	h.autowrap_mode = TextServer.AUTOWRAP_OFF
	h.position = Vector2(24, 18)
	warp_panel.add_child(h)
	var p := Ui.label("Pick where to go. For a ring, you arrive on the ring at your current longitude.", 18, Ui.MUTED)
	p.position = Vector2(24, 56)
	p.size = Vector2(540, 50)
	warp_panel.add_child(p)
	var x := _hud_button("×", Vector2(590, 14), Vector2(54, 54), 27, "")
	x.pressed.connect(func(): warp_panel.visible = false)
	warp_panel.add_child(x)
	warp_list = VBoxContainer.new()
	warp_list.position = Vector2(20, 120)
	warp_list.size = Vector2(620, 740)
	warp_list.add_theme_constant_override("separation", 10)
	warp_panel.add_child(warp_list)


func _warp_menu() -> void:
	for c in warp_list.get_children():
		c.queue_free()
	var me := _me()
	for d in _dests():
		var p := _dest_point(d)
		var b := _hud_button("", Vector2.ZERO, Vector2(620, 80), 12, "")
		b.custom_minimum_size = Vector2(620, 80)
		var t := Ui.label(d.label, 22, HUD_RED)
		t.autowrap_mode = TextServer.AUTOWRAP_OFF
		t.position = Vector2(16, 8)
		t.mouse_filter = Control.MOUSE_FILTER_IGNORE
		b.add_child(t)
		var coords := ("arrive at longitude %.1f°" if d.has("ring") else "longitude %.1f°") % _lon_deg(p)
		var n := Ui.label(d.note + " · " + coords, 16, Ui.MUTED)
		n.autowrap_mode = TextServer.AUTOWRAP_OFF
		n.position = Vector2(16, 42)
		n.mouse_filter = Control.MOUSE_FILTER_IGNORE
		b.add_child(n)
		var e := Ui.label(Solar.fmt_dist(Solar.length(Solar.sub(p, me))), 18, HUD_RED)
		e.autowrap_mode = TextServer.AUTOWRAP_OFF
		e.horizontal_alignment = HORIZONTAL_ALIGNMENT_RIGHT
		e.position = Vector2(440, 26)
		e.size = Vector2(164, 30)
		e.mouse_filter = Control.MOUSE_FILTER_IGNORE
		b.add_child(e)
		b.pressed.connect(func():
			warp_panel.visible = false
			start_warp(d))
		warp_list.add_child(b)


func start_warp(d: Dictionary) -> void:
	if docked and not Session.me.get("skills", {}).get("fly", false):    # warping out of the bay is flying too
		_say("LIBRARY FIRST\nPass the Pilot Basic Training Handbook test before you can fly.", true)
		return
	var to := _dest_point(d)
	var from := _me()
	var dist := Solar.length(Solar.sub(to, from))
	if dist < 20000.0:
		_say("You're already there.")
		return
	# bend the route around the Sun if the straight line passes within 0.25 AU of it
	var via = null
	var fw: Array = Solar.sub(from, sol.sun_l)
	var tw: Array = Solar.sub(to, sol.sun_l)
	var ab := Solar.sub(tw, fw)
	var t := clampf(-Solar.dot(fw, ab) / Solar.dot(ab, ab), 0.0, 1.0)
	if Solar.length(Solar.add(fw, Solar.mul(ab, t))) < 0.25 * Solar.AU:
		var mid := Solar.mul(Solar.add(fw, tw), 0.5)
		var dir: Array
		if Solar.length(mid) > 0.05 * Solar.AU:
			dir = Solar.norm(mid)
		else:     # straight through the Sun: go round its side, in the plane of the orbits
			var up: Array = sol.to_local_d(Solar.add(sol.sp, [0.0, 1.0, 0.0]))
			dir = Solar.norm(Solar.cross(up, fw))
		via = Solar.add(sol.sun_l, Solar.mul(dir, maxf(0.6 * Solar.AU, (Solar.length(fw) + Solar.length(tw)) / 2.0)))
	docked = false
	holding = false
	_set_throttle(0)
	vel = Vector3.ZERO
	rot = Vector3.ZERO
	warp = {"d": d, "from": from, "to": to, "via": via, "t": 0.0, "spool": 1.4,
		"dur": 4.0 + 4.0 * log(1.0 + dist / Solar.AU) / log(10.0), "label": d.label}


func _bez(w: Dictionary, k: float) -> Array:
	if w.via == null:
		return Solar.add(w.from, Solar.mul(Solar.sub(w.to, w.from), k))
	var a := (1.0 - k) * (1.0 - k)
	var b := 2.0 * (1.0 - k) * k
	var c := k * k
	return Solar.add(Solar.add(Solar.mul(w.from, a), Solar.mul(w.via, b)), Solar.mul(w.to, c))


func _warp_tick(dt: float) -> void:
	var w := warp
	w.t += dt
	var total: float = w.spool + w.dur
	var k := maxf(0.0, (w.t - w.spool) / w.dur)
	var e := k * k * (3.0 - 2.0 * k) if k < 1.0 else 1.0
	# face along the route: during the spool, turn toward where you're going
	var ahead := Solar.sub(_bez(w, minf(1.0, e + 0.02)), _me())
	if Solar.length(ahead) > 1.0:
		var want := Basis.looking_at(Solar.vec(Solar.norm(ahead)), cam.global_basis.y).get_rotation_quaternion()
		var q := cam.quaternion.slerp(want, 1.0 - exp(-(3.0 if w.t < w.spool else 6.0) * dt))
		cam.quaternion = q.normalized()
	if w.t > w.spool:
		org = _bez(w, e)
		cam.position = Vector3.ZERO
	streaks.alpha = w.t / w.spool * 0.35 if w.t < w.spool else (1.0 if k < 0.85 else maxf(0.0, (1.0 - k) / 0.15))
	streaks.queue_redraw()
	if w.t < total:
		return
	warp = {}
	streaks.alpha = 0.0
	streaks.queue_redraw()
	if w.d.has("ring"):
		_say("ARRIVED\nDropping out in the " + w.d.ring.name + ".")
	elif w.d.key == "starship":
		cam.look_at(cam.position + Solar.vec(Solar.sub([0.0, 0.0, 0.0], _me())), Vector3.UP)     # turned to face her
		_say("ARRIVED\nThe Starship is ahead.")
	else:
		_say("ARRIVED\n" + w.label)


## Labels on the landmarks (browser .mk): a small ring and "name · distance"; off screen, a diamond at the edge pointing
## the way. Labels never pile up (Eric 10-20): one that would cover another steps down, up, down further... until clear.
class Marks extends Control:
	var bay: Node
	func _draw() -> void:
		var cam: Camera3D = bay.cam
		var me: Array = bay._me()
		var W := size.x
		var H := size.y
		var th := tan(deg_to_rad(cam.fov) / 2.0)
		var aspect := W / H
		var inv := cam.global_transform.affine_inverse()
		var font := get_theme_default_font()
		var fs := 20
		var placed: Array = []
		for l in bay.sol.landmarks:
			var n: Node3D = l.node
			var v: Vector3 = inv * n.global_position
			var behind := v.z >= 0.0
			var x := v.x / (th * aspect)
			var y := v.y / th
			if not behind:
				x /= -v.z
				y /= -v.z
			var on := not behind and absf(x) < 0.95 and absf(y) < 0.92
			if not on:
				var m := maxf(maxf(absf(x) / 0.92, absf(y) / 0.86), 1e-6)
				x /= m
				y /= m
			var text: String = l.name + " · " + bay.Solar.fmt_dist(bay.sol.dist_to(l, me))
			var tw := font.get_string_size(text, HORIZONTAL_ALIGNMENT_LEFT, -1, fs).x
			var w := tw
			var h := 48.0
			var bx := clampf((x + 1.0) / 2.0 * W, w / 2.0 + 6.0, W - w / 2.0 - 6.0)
			var by := (1.0 - y) / 2.0 * H
			var px := bx
			var py := clampf(by, h / 2.0 + 6.0, H - h / 2.0 - 6.0)
			for k in range(1, 13):
				var hit := false
				for q in placed:
					if absf(q.x - px) < (w + q.w) / 2.0 + 8.0 and absf(q.y - py) < (h + q.h) / 2.0 + 3.0:
						hit = true
				if not hit:
					break
				var step := ceili(k / 2.0) * (1 if k % 2 else -1)
				py = clampf(by + step * (h + 4.0), h / 2.0 + 6.0, H - h / 2.0 - 6.0)
			placed.append({"x": px, "y": py, "w": w, "h": h})
			var c: Color = l.color
			var mc := Vector2(px, py - h / 2.0 + 8.0)
			if on:
				draw_arc(mc, 7.0, 0.0, TAU, 24, c, 2.5, true)
			else:
				var r := 8.0
				draw_polyline(PackedVector2Array([mc + Vector2(0, -r), mc + Vector2(r, 0), mc + Vector2(0, r), mc + Vector2(-r, 0), mc + Vector2(0, -r)]), c, 2.5, true)
			var base := Vector2(px - tw / 2.0, py + h / 2.0 - 6.0)
			draw_string(font, base + Vector2(0, 2), text, HORIZONTAL_ALIGNMENT_LEFT, -1, fs, Color(0, 0, 0, 0.85))
			draw_string(font, base, text, HORIZONTAL_ALIGNMENT_LEFT, -1, fs, c)


## Streaking stars while in warp (the browser's 2D overlay).
class Streaks extends Control:
	var alpha := 0.0
	var st: Array = []
	func _draw() -> void:
		if alpha <= 0.0:
			return
		if st.is_empty():
			for i in 160:
				st.append({"ang": randf() * TAU, "r": randf(), "s": 0.3 + randf()})
		var c := size / 2.0
		var M := c.length()
		var col := Color(200 / 255.0, 220 / 255.0, 1.0, 0.8 * alpha)
		for s in st:
			s.r += 0.02 * s.s
			if s.r > 1.0:
				s.r = randf() * 0.15
			var r0: float = s.r * M
			var r1: float = r0 + M * 0.12 * s.s * s.r
			var d := Vector2(cos(s.ang), sin(s.ang))
			draw_line(c + d * r0, c + d * r1, col, 1.2 * 1.85, true)
