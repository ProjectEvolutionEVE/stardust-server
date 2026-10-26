extends Node3D
## The Docking Bay (rule 19), in 3D: you start docked inside the Starship's belly bay, looking out past the bow, the same
## view as the browser game. Flight controls match the browser (Eric 10-17/10-24): the throttle arrows in the bottom right corner, under WARP, for the right thumb (Eric 10-24), set
## speed (10% a tap, 0% stops); press and hold anywhere to steer like a joystick (pull back = nose up, push = nose down,
## left/right = bank); the side thrusters bottom left turn you in place. Launching needs the Pilot Basic Training
## Handbook pass (Eric 10-23); without it the craft stays docked and the bay points you to the library.
## Around it, the solar system at true scale (scripts/solar.gd) with labels on the landmarks, and WARP (Eric 10-11) to
## any of the four rings, the Starship, the wormhole, Jupiter or Saturn, as in the browser.
## In the rings, the debris fields (scripts/debris.gd) and the scanner (spec §5, Eric's design): a soft hiss means nothing
## ahead; a tone rises out of it as you point at a field. Take a bearing, move to one side and sweep again: where the two
## bearings cross, the field locks and the scanner goes quiet. While you hold the stick, a faint gold glow on its rim
## points to the nearest field. Double-tap a locked field (or a field or landmark you can see) and the autopilot flies you
## there and parks in front of it; double-tap the Starship and it brings you in to dock.

const MAXV := 60.0
const ACC := 40.0
const STICK_R := 140.0
const AUTOV := 900.0             # autopilot cruises fast on long trips and slows as it arrives
const FAR_FLY := 200000.0        # beyond 200 km, flying would take too long: use WARP
const CUE_RANGE := 4500.0
const SCAN_CONE := 30.0 * PI / 180.0
const SCAN_RANGE := {"large": 1800.0, "medium": 900.0, "small": 300.0, "tiny": 200.0}   # bigger fields are heard farther
const SCAN_SIG := {"large": 1.0, "medium": 0.7, "small": 0.4, "tiny": 0.3}             # and louder

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
var debris: Node3D
var sound: Node
var lock := {}                   # {name, pos (ship frame), aim, stop_at, auto, parked, field, dock, aft}; auto = autopilot on
var bearings := {}               # field id -> where you were when you took its first bearing
var scan_strength := 0.0
var scan_best := {}
var static_v := 0.0
var cue := {"alpha": 0.0, "want": 0.0, "angle": 0.0, "ahead": false}
var last_tap := -1.0
var last_tap_at := Vector2.ZERO
var cells_at := 0.0
var scan_bar: ColorRect
var info: Label
var appr: Label
var stick: Control
var hud_root: Control
var sleep_btn: Button
var sleep_panel: ColorRect
var sleep_bars: Label
var sleep_at := 0.0
var quarters_btn: Button
# FUEL (rule 38, Eric 10-25): the WSC's craft comes with fuel, topped up at every return to the Starship. Out in space it
# ticks down slowly (more slowly when stopped); run dry and Inara has you towed home, for a pretty penny.
const FUEL_FLY_H := 6.0           # hours of flying on a full tank
const FUEL_IDLE_H := 24.0         # hours stopped or asleep in the cockpit on a full tank
const FUEL_WARP := 4.0            # % a warp takes
const FUEL_FILE := "user://fuel.dat"
var fuel := 100.0
var fuel_warned := 100
var towing := false
var fuel_saved_at := 0.0
var fuel_label: Label
var flight_secs := 0.0            # flight time not yet reported to the WSC (rule 38: 50 credits an hour, or the lease)
var fuel_fill: ColorRect          # only while docked: the quarters are aboard (Eric 10-24: not out in space)
var cargo: Node
var mute_btn: Button
var work_ring = null             # the ring you're working (Inara watches you drift out of it)
var inara_t := 0.0
var band := {}                   # where you are against the ring you're working: {ring, out, radial, height, point}
var edge: Control
var _band_node := Node3D.new()   # stands where the band's nearest point is drawn, for its label
var radar: Control
var voiced := {}                 # this session's once-only moments (first strong return, first bearing)


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
	add_child(_band_node)
	debris = preload("res://scripts/debris.gd").new()
	add_child(debris)
	debris.setup(sol, randi())     # until the server's seed arrives (or for good, when not signed in)
	sound = preload("res://scripts/scanner_sound.gd").new()
	add_child(sound)
	_dock()
	_hud()
	_wake_parked()
	_fuel_load()
	sol.place(org, cam)
	_server_seed()


## Signed out in the cockpit last time (Eric 10-24): wake up out there, where the craft was left, not in the bay.
func _wake_parked() -> void:
	var pk = Session.me.get("parked")
	if not (pk is Dictionary and pk.get("pos") is Array):
		return
	docked = false
	org = sol.to_local_d(pk.pos)
	cam.position = Vector3.ZERO
	Session.me.parked = null
	_say("You wake in your cockpit, right where you left your craft.")
	Voice.ring(hud_root, Voice.moment("wake"))
	if Session.token != "":
		Api.call_api("POST", "/api/dfg/rest", {"unpark": true})


func _fuel_ui(root: Control) -> void:
	fuel_label = Ui.label("", 15, Color("7fe0a8"))
	fuel_label.autowrap_mode = TextServer.AUTOWRAP_OFF
	fuel_label.position = Vector2(26, 124)
	root.add_child(fuel_label)
	var bg := ColorRect.new()
	bg.color = Color(0.5, 0.88, 0.66, 0.15)
	bg.position = Vector2(26, 148)
	bg.size = Vector2(236, 5)
	bg.mouse_filter = Control.MOUSE_FILTER_IGNORE
	root.add_child(bg)
	fuel_fill = ColorRect.new()
	fuel_fill.position = Vector2(26, 148)
	fuel_fill.size = Vector2(236, 5)
	fuel_fill.mouse_filter = Control.MOUSE_FILTER_IGNORE
	root.add_child(fuel_fill)


## Out in the cockpit last time: the tank kept ticking while you were away (at the stopped rate).
func _fuel_load() -> void:
	var f := FileAccess.open(FUEL_FILE, FileAccess.READ)
	if f == null:
		return
	var d = JSON.parse_string(f.get_as_text())
	f.close()
	if d is Dictionary and not docked:
		var hours := maxf(0.0, (Time.get_unix_time_from_system() - float(d.get("at", 0))) / 3600.0)
		fuel = clampf(float(d.get("fuel", 100)) - hours * 100.0 / FUEL_IDLE_H, 0.0, 100.0)


func _fuel_tick(dt: float, now: float) -> void:
	if docked:
		if fuel < 100.0:
			fuel = 100.0                 # topped up at the Starship (fuel is included)
			fuel_warned = 100
	elif not towing:
		flight_secs += dt
		if flight_secs >= 60.0 and Session.token != "":   # each minute out in the craft is reported; the server bills it
			var secs := flight_secs
			flight_secs = 0.0
			Api.call_api("POST", "/api/dfg/craft/flight", {"seconds": secs})
		var flying: bool = not warp.is_empty() or vel.length() > 0.5
		var stretch := 1.0 + Session.skill("flight")   # the Flight uniform stretches fuel (Eric 10-26)
		fuel = maxf(0.0, fuel - dt / 3600.0 * 100.0 / ((FUEL_FLY_H if flying else FUEL_IDLE_H) * stretch))
		for mark in [25, 10]:
			if fuel <= mark and fuel_warned > mark:
				fuel_warned = mark
				_say("INARA\nFuel at %d%%. Time to head home to the Starship." % mark)
		if fuel <= 0.0:
			_tow()
	fuel_label.text = "FUEL %d%%" % ceili(fuel)
	var c := Color("7fe0a8") if fuel > 25.0 else (Color(1.0, 0.81, 0.42) if fuel > 10.0 else Color("e5605a"))
	fuel_label.add_theme_color_override("font_color", c)
	fuel_fill.color = c
	fuel_fill.size.x = 236.0 * fuel / 100.0
	if now > fuel_saved_at:              # kept on this device, so a cockpit sign-out remembers it
		fuel_saved_at = now + 5.0
		var f := FileAccess.open(FUEL_FILE, FileAccess.WRITE)
		if f:
			f.store_string(JSON.stringify({"fuel": fuel, "at": Time.get_unix_time_from_system()}))
			f.close()


## Out of fuel: Inara sends a tow. It brings you home and it isn't cheap (the server charges the fee, rule 38).
func _tow() -> void:
	towing = true
	lock = {}
	warp = {}
	vel = Vector3.ZERO
	_set_throttle(0)
	_say("INARA\nYou're out of fuel. Sit tight, I'm sending a tow to bring you in. It won't be cheap.")
	await get_tree().create_timer(6.0).timeout
	var charged := 0
	if Session.token != "":
		var r: Dictionary = await Api.call_api("POST", "/api/dfg/tow", {})
		if r.ok:
			charged = int(r.data.get("charged", 0))
	_dock()
	fuel = 100.0
	fuel_warned = 100
	towing = false
	_say("TOWED HOME\nThe tow cost you %s credits. Keep an eye on your fuel." % Ui.num(charged))


# ── RESTING IN THE COCKPIT (Eric 10-24): stopped out in space, sleep at half the bed's rate, or sign out right here ──
func _can_sleep() -> bool:
	return not docked and warp.is_empty() and vel.length() < 0.5 and throttle == 0 and not lock.get("auto", false) \
		and not sleep_panel.visible


func _sleep() -> void:
	sleep_panel.move_to_front()          # over every instrument
	sleep_panel.visible = true
	holding = false
	sleep_bars.text = "Resting…"
	Voice.say("sleep")
	if Session.token == "":
		sleep_bars.text = "Not signed in: your rest isn't kept."
		return
	var r: Dictionary = await Api.call_api("POST", "/api/dfg/rest", {"asleep": true, "place": "cockpit"})
	_show_bars(r)


func _show_bars(r: Dictionary) -> void:
	if not r.get("ok", false):
		sleep_bars.text = r.get("error", "")
		return
	Session.me = r.data
	var b: Dictionary = r.data.get("bars", {})
	sleep_bars.text = "Stamina %d%% · Energy %d%% · Focus %d%%" % [roundi(b.get("stamina", 0)), roundi(b.get("energy", 0)), roundi(b.get("focus", 0))]


func _refresh_bars() -> void:
	_show_bars(await Api.call_api("GET", "/api/dfg/me"))


func _wake() -> void:
	sleep_panel.visible = false
	if Session.token != "":
		_show_bars(await Api.call_api("POST", "/api/dfg/rest", {"asleep": false}))


func _sign_out_here() -> void:
	var w: Array = sol.to_world_d(_me())
	if Session.token != "":
		var r: Dictionary = await Api.call_api("POST", "/api/dfg/auth/signout", {"place": "cockpit", "pos": w})
		if not r.ok:
			sleep_bars.text = r.error
			return
	Session.clear()
	get_tree().change_scene_to_file("res://scenes/title.tscn")


func _sleep_ui(root: Control) -> void:
	sleep_btn = _hud_button("SLEEP", Vector2(24, 976), Vector2(120, 51), 26, "")
	sleep_btn.pressed.connect(_sleep)
	root.add_child(sleep_btn)
	sleep_panel = ColorRect.new()
	sleep_panel.color = Color(0, 0, 0, 0.78)
	sleep_panel.set_anchors_preset(Control.PRESET_FULL_RECT)
	sleep_panel.mouse_filter = Control.MOUSE_FILTER_STOP
	sleep_panel.visible = false
	root.add_child(sleep_panel)
	var box := VBoxContainer.new()
	box.position = Vector2(60, 440)
	box.size = Vector2(600, 400)
	box.add_theme_constant_override("separation", 22)
	sleep_panel.add_child(box)
	var t := Ui.label("ASLEEP IN THE COCKPIT", 30, HUD_RED)
	t.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	box.add_child(t)
	var n := Ui.label("Your craft holds its position. You rest here at half the rate of your own bed back aboard the Starship.", 20, Ui.MUTED)
	n.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	box.add_child(n)
	sleep_bars = Ui.label("", 22, Color("7fe0a8"))
	sleep_bars.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	box.add_child(sleep_bars)
	var row := HBoxContainer.new()
	row.add_theme_constant_override("separation", 20)
	row.alignment = BoxContainer.ALIGNMENT_CENTER
	box.add_child(row)
	var wk := _hud_button("WAKE UP", Vector2.ZERO, Vector2(260, 64), 32, "")
	wk.custom_minimum_size = Vector2(260, 64)
	wk.pressed.connect(_wake)
	row.add_child(wk)
	var so := _hud_button("SIGN OUT HERE", Vector2.ZERO, Vector2(260, 64), 32, "")
	so.custom_minimum_size = Vector2(260, 64)
	so.pressed.connect(_sign_out_here)
	row.add_child(so)


## The universe comes from the server's seed, so the server can tell what every piece is (as the browser's netStart).
func _server_seed() -> void:
	if Session.token == "":
		return
	var r: Dictionary = await Api.call_api("POST", "/api/dfg/session", {})
	if r.ok and r.data.has("seed"):
		debris.reset(int(r.data.seed))
		cargo.apply_ship(r.data)
		lock = {}
		bearings.clear()


func _dock(aft := false) -> void:
	docked = true
	vel = Vector3.ZERO
	rot = Vector3.ZERO
	throttle = 0
	if thr_label:
		_set_throttle(0)
	holding = false                  # only a NEW throttle-up or stick press launches again
	org = [0.0, 0.0, 0.0]
	cam.position = ship.DOCK.aftMouth if aft else ship.DOCK.mouth
	cam.look_at(Vector3(0, -30, -400 if aft else 400), Vector3.UP)     # facing out of the end you came in by


# ── the screen: status, throttle arrows (right), side thrusters (bottom left), Quarters ──
func _hud() -> void:
	var layer := CanvasLayer.new()
	add_child(layer)
	var root := Control.new()
	root.set_anchors_preset(Control.PRESET_FULL_RECT)
	root.mouse_filter = Control.MOUSE_FILTER_IGNORE
	layer.add_child(root)
	status = Ui.label("", 22, Color("7fe0a8"))       # the scanner's line (browser #scan)
	status.autowrap_mode = TextServer.AUTOWRAP_OFF
	status.position = Vector2(0, 1214)
	status.size = Vector2(720, 36)
	status.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	root.add_child(status)
	var bar_bg := ColorRect.new()
	bar_bg.color = Color(0.5, 0.88, 0.66, 0.15)
	bar_bg.position = Vector2(144, 1252)
	bar_bg.size = Vector2(432, 10)
	bar_bg.mouse_filter = Control.MOUSE_FILTER_IGNORE
	root.add_child(bar_bg)
	scan_bar = ColorRect.new()
	scan_bar.color = Color("7fe0a8")
	scan_bar.position = Vector2(144, 1252)
	scan_bar.size = Vector2(0, 10)
	scan_bar.mouse_filter = Control.MOUSE_FILTER_IGNORE
	root.add_child(scan_bar)
	info = Ui.label("", 18, Color(0.5, 0.88, 0.66, 0.8))   # speed, distance from the Sun, the ring you're in
	info.autowrap_mode = TextServer.AUTOWRAP_OFF
	info.position = Vector2(24, 40)
	root.add_child(info)
	appr = Ui.label("", 80, Color(1, 1, 1, 0.45))           # approach distance, big and faint (Eric 10-17)
	appr.autowrap_mode = TextServer.AUTOWRAP_OFF
	appr.position = Vector2(0, 96)
	appr.size = Vector2(720, 100)
	appr.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	root.add_child(appr)
	note = Ui.label("", 26, Ui.TEXT)
	note.position = Vector2(40, 230)
	note.size = Vector2(640, 180)
	note.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	root.add_child(note)
	lib_btn = _hud_button("Go to the Starship Library", Vector2(80, 330), Vector2(560, 76), 14, "")
	lib_btn.visible = false
	lib_btn.pressed.connect(func(): get_tree().change_scene_to_file("res://scenes/library.tscn"))
	root.add_child(lib_btn)
	var up := _hud_button("", Vector2(619, 1004), Vector2(77, 77), 38, "up")
	up.pressed.connect(func(): _set_throttle(throttle + 1))
	root.add_child(up)
	thr_label = Ui.label("Throttle 0%", 18, HUD_RED)
	thr_label.autowrap_mode = TextServer.AUTOWRAP_OFF
	thr_label.position = Vector2(588, 1084)
	root.add_child(thr_label)
	var dn := _hud_button("", Vector2(619, 1124), Vector2(77, 77), 38, "down")
	dn.pressed.connect(func(): _set_throttle(throttle - 1))
	root.add_child(dn)
	for p in [["left", Vector2(24, 1040), -1], ["right", Vector2(121, 1040), 1]]:
		var bt := _hud_button("", p[1], Vector2(77, 77), 38, p[0])
		var dirn: int = p[2]
		bt.button_down.connect(func(): pivot = dirn)
		bt.button_up.connect(func(): pivot = 0)
		root.add_child(bt)
	quarters_btn = _hud_button("Quarters", Vector2(24, 1140), Vector2(176, 51), 11, "")
	quarters_btn.pressed.connect(func(): get_tree().change_scene_to_file("res://scenes/quarters.tscn"))
	root.add_child(quarters_btn)
	marks = Marks.new()
	marks.bay = self
	marks.set_anchors_preset(Control.PRESET_FULL_RECT)
	marks.mouse_filter = Control.MOUSE_FILTER_IGNORE
	root.add_child(marks)
	root.move_child(marks, 0)          # labels under the buttons
	edge = EdgeGlow.new()            # a faint gold glow round the whole screen when something needs you (Eric 10-24)
	edge.set_anchors_preset(Control.PRESET_FULL_RECT)
	edge.mouse_filter = Control.MOUSE_FILTER_IGNORE
	root.add_child(edge)
	root.move_child(edge, 0)
	stick = Stick.new()
	stick.bay = self
	stick.set_anchors_preset(Control.PRESET_FULL_RECT)
	stick.mouse_filter = Control.MOUSE_FILTER_IGNORE
	root.add_child(stick)
	root.move_child(stick, 0)
	streaks = Streaks.new()
	streaks.set_anchors_preset(Control.PRESET_FULL_RECT)
	streaks.mouse_filter = Control.MOUSE_FILTER_IGNORE
	root.add_child(streaks)
	root.move_child(streaks, 0)
	var wb := _hud_button("WARP", Vector2(576, 942), Vector2(120, 51), 26, "")
	wb.pressed.connect(func():
		if warp.is_empty():
			_warp_menu()
			warp_panel.visible = not warp_panel.visible)
	root.add_child(wb)
	_warp_panel(root)
	hud_root = root
	_sleep_ui(root)
	_fuel_ui(root)
	cargo = preload("res://scripts/cargo.gd").new()   # the hold, COLLECT and UNLOAD
	cargo.bay = self
	add_child(cargo)
	cargo.build(root)
	radar = preload("res://scripts/radar.gd").new()   # the long-range scanner, pulled down from the top (Eric 10-24)
	radar.bay = self
	root.add_child(radar)
	var rt := _hud_button("RADAR", Vector2(300, 76), Vector2(110, 42), 21, "")
	rt.pressed.connect(func(): radar.toggle())
	root.add_child(rt)
	mute_btn = _hud_button("Sound on", Vector2(576, 40), Vector2(120, 51), 26, "")   # silences the scanner and Inara
	mute_btn.pressed.connect(func():
		sound.muted = not sound.muted
		Voice.set_muted(sound.muted)
		mute_btn.text = "Muted" if sound.muted else "Sound on")
	root.add_child(mute_btn)


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
	b.add_theme_font_size_override("font_size", 18)   # flight buttons 20% smaller (Eric 10-24)
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
		if ev.pressed and warp.is_empty():      # double-tap: lock what's under the tap and fly there
			var now := Time.get_ticks_msec() / 1000.0
			if now - last_tap < 0.32 and ev.position.distance_to(last_tap_at) < 74.0:
				last_tap = -1.0
				holding = false
				_lock_at(ev.position)
				return
			last_tap = now
			last_tap_at = ev.position
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
	if not lock.is_empty() and lock.get("field") and not is_instance_valid(lock.field.node):
		lock = {}                                # its cell was left behind
	if not warp.is_empty():
		_warp_tick(dt)
		sound.scanner(-1.0)
	else:
		_fly(dt)
		_scan(dt)
		_watch_ring(now)
		if now > cells_at:
			debris.update_cells(_me())
			cells_at = now + 0.2
	if cam.position.length() > 1000.0:       # floating origin: keep the camera near the scene's origin
		org = Solar.add(org, [cam.position.x, cam.position.y, cam.position.z])
		cam.position = Vector3.ZERO
	sol.place(org, cam)
	debris.place(org)
	cargo.tick(dt)
	note.position.y = 640.0 if radar.open else 230.0      # out from under the radar while it's down
	appr.position.y = 548.0 if radar.open else 96.0
	edge.on = not band.is_empty() and band.out > 1.0 and warp.is_empty() and not docked
	edge.queue_redraw()
	quarters_btn.visible = docked
	_fuel_tick(dt, now)
	sleep_btn.visible = _can_sleep()
	if sleep_panel.visible and now > sleep_at and Session.token != "":   # the bars as they refill, once a minute
		sleep_at = now + 60.0
		_refresh_bars()
	marks.queue_redraw()
	cue.alpha += (cue.want - cue.alpha) * (1.0 - exp(-dt / 0.15))
	stick.queue_redraw()
	scan_bar.size.x = 432.0 * scan_strength
	var me := _me()
	if not warp.is_empty():
		status.text = "WARP · " + warp.label
	info.text = ""
	if not docked:
		var here = sol.ring_of(sol.to_world_d(me))
		info.text = "%.1f m/s · %.3f AU from the Sun" % [vel.length(), Solar.length(Solar.sub(me, sol.sun_l)) / Solar.AU]
		if here != null:
			info.text = here.name + " · " + info.text
	# approach distance: to whatever the scanner is tracking
	var p = null
	if not docked and warp.is_empty():
		if not lock.is_empty():
			p = lock.get("aim", lock.pos)
		elif not scan_best.is_empty() and scan_strength > 0.25:
			p = scan_best.center
	appr.text = "" if p == null else Solar.fmt_dist(Solar.length(Solar.sub(p, me)))


func _fly(dt: float) -> void:
	var s := Vector2.ZERO
	if holding:
		s = ((stick_at - stick_from) / STICK_R).limit_length(1.0)
	if holding and not lock.is_empty():          # leaving a field you parked at releases it; otherwise the lock stays
		if lock.get("parked", false):
			lock = {}
		else:
			lock.auto = false
	if docked and (throttle > 0 or holding):
		if not Session.me.get("skills", {}).get("fly", false):
			_set_throttle(0)
			holding = false
			_say("LIBRARY FIRST\nPass the Pilot Basic Training Handbook test before you can fly.", true)
		else:
			docked = false
			Voice.say("launch")              # cleared for launch
			Voice.story(hud_root, "launch")
	if docked:
		return
	var me := _me()
	var b := cam.global_basis
	var fwd := -b.z
	# turning: the stick (pull back = nose up, right = bank right) and the side thrusters (turn in place)
	var tp := s.y * 1.1
	var tr := -s.x * 1.5
	var ty := -s.x * 0.55 - pivot * 0.8
	var want := fwd
	var auto: bool = not lock.is_empty() and lock.auto
	var parked: bool = not lock.is_empty() and lock.get("parked", false)
	if auto or parked:                           # autopilot (and parked): keep the nose on the target
		want = Solar.vec(Solar.sub(lock.pos, me)).normalized()
		ty = -want.dot(b.x) * 2.2
		tp = want.dot(b.y) * 2.2
		tr = 0.0
	if not lock.is_empty():
		var d := Solar.length(Solar.sub(lock.pos, me))
		if lock.get("dock", 0) == 1 and auto and d < lock.stop_at:
			lock.dock = 2
			lock.pos = Solar.vec3d(ship.DOCK.aftMouth if lock.aft else ship.DOCK.mouth)
			lock.stop_at = 22.0
			lock.name = "Starship · docking"
			Voice.say("approach")
			if throttle > 0:
				_set_throttle(0)
			_say("Tractor beam has control. Throttle set to zero.")
		elif lock.get("dock", 0) == 2 and d < lock.stop_at:
			var aft: bool = lock.aft
			lock = {}
			_dock(aft)
			Voice.say("docked")
			_say("DOCKED\nWelcome home. Your Market terminal is at the Desk in your quarters.")
			return
		elif auto and lock.get("dock", 0) == 0 and d < lock.stop_at:
			lock.auto = false
			lock.parked = true
			auto = false
			parked = true
			if lock.get("field"):
				Voice.say("parked")
			_say("Holding position: " + lock.name)
			if lock.get("field"):
				lock.field.known = true
		elif not auto and not parked and lock.get("field") and lock.field.known and d > lock.stop_at * 4.0:
			lock = {}                            # flew away from a visited field
	var k := 1.0 - exp(-(5.0 if auto else 4.0) * dt)
	rot += (Vector3(tp, ty, tr) - rot) * k
	cam.rotate_object_local(Vector3.RIGHT, rot.x * dt)
	cam.rotate_object_local(Vector3.UP, rot.y * dt)
	cam.rotate_object_local(Vector3.FORWARD, -rot.z * dt)
	fwd = -cam.global_basis.z
	# thrust: the throttle sets the speed (0% = drift to a stop); the autopilot flies itself and slows as it arrives
	var tf := 1.0 if throttle > 0 and not parked else 0.0
	var cap := MAXV * throttle / 10.0
	if auto:
		var dist := maxf(0.0, Solar.length(Solar.sub(lock.pos, me)) - lock.stop_at)
		cap = minf(AUTOV, maxf(6.0, dist * 0.6)) * maxf(0.0, want.dot(fwd))
		tf = 1.0
	if vel.length() > cap:
		tf = 0.0                                 # throttled down: coast down to the new speed
	vel += fwd * tf * ACC * (3.2 if auto else 1.0) * dt
	var idle := tf == 0.0
	vel *= exp(-(2.6 if parked else ((0.35 if throttle > 0 else 1.2) if idle else 0.12)) * dt)   # parked = station-keeping brake
	if vel.length() > cap:
		vel = vel.normalized() * maxf(cap, vel.length() * exp(-1.5 * dt))
	if not auto and tf > 0.0:                    # under power the ship flies where it points
		vel = vel.lerp(fwd * vel.length(), 1.0 - exp(-3.0 * dt))
	cam.position += vel * dt


## INARA keeps an eye on you (Eric 10-11): she welcomes you into a ring, and tells you when you drift out of the one
## you're working (every 15 s, with her recorded line the first time).
func _watch_ring(now: float) -> void:
	var w: Array = sol.to_world_d(_me())
	var here = sol.ring_of(w)
	_measure_band(w, here if here != null else work_ring)
	if here != null:
		if work_ring == null or here.key != work_ring.key:
			var first: bool = work_ring == null
			work_ring = here
			Voice.say("ring%d" % Solar.RINGS.find(here))
			if first:
				Voice.story(hud_root, "ring")
			_say("INARA\nYou're in the " + here.name + ". Debris all around you. Start sweeping.")
		inara_t = 0.0
		return
	if work_ring == null:
		return
	var r: float = work_ring.au * Solar.AU
	var out := maxf(maxf(absf(Vector2(w[0], w[2]).length() - r) - sol.BAND_HALF, absf(w[1]) - sol.BAND_THICK), 0.0)
	if out > 2e6:                                # well clear: you've left on purpose
		work_ring = null
		return
	if now > inara_t:
		if inara_t == 0.0:
			Voice.say("drift%d" % Solar.RINGS.find(work_ring))
		inara_t = now + 15.0
		_say("INARA\nYou're drifting out of the %s, %s outside it. Turn back toward the debris." % [work_ring.name, Solar.fmt_dist(out)])


## Where you are against a ring's band (BAND: 25 km either side of its line, 6 km above and below): how far out, which
## way, and the nearest point of the band, so the screen can point you back to it.
func _measure_band(w: Array, rg) -> void:
	if rg == null:
		band = {}
		return
	var r: float = rg.au * Solar.AU
	var rxy := Vector2(w[0], w[2]).length()
	var rt := clampf(rxy, r - sol.BAND_HALF, r + sol.BAND_HALF)
	var yt := clampf(w[1], -sol.BAND_THICK, sol.BAND_THICK)
	var pw := [w[0] / rxy * rt, yt, w[2] / rxy * rt]
	band = {"ring": rg, "radial": rxy - r, "height": w[1], "point": sol.to_local_d(pw),
		"out": Solar.length(Solar.sub(pw, w))}


# ── LOCK (double-tap): a scanner-locked field, or the field or landmark you can see nearest the tap ──
func _lock_at(at: Vector2) -> void:
	if docked:
		return
	var W := get_viewport().get_visible_rect().size
	var th := tan(deg_to_rad(cam.fov) / 2.0)
	var ray := (cam.global_basis * Vector3((at.x / W.x * 2.0 - 1.0) * th * W.x / W.y, (1.0 - at.y / W.y * 2.0) * th, -1.0)).normalized()
	var me := _me()
	var cands: Array = []
	for f in debris.fields:
		if f.shown:
			cands.append({"name": Debris.label_of(f), "pos": f.center, "stop_at": Debris.stand_off(f), "field": f})
	for l in sol.landmarks:
		if l.get("home", false):
			cands.append(_dock_lock())
		else:
			cands.append({"name": l.name, "pos": l.pos, "stop_at": l.rad * 1.6})
	var best := {}
	var best_ang := 0.2                          # within ~11° of the tap
	for c in cands:
		var a := Solar.vec(Solar.sub(c.get("aim", c.pos), me)).angle_to(ray)
		if a < best_ang:
			best_ang = a
			best = c
	if best.is_empty():                          # nothing under the tap: resume the current lock, if there is one
		if not lock.is_empty() and not lock.auto:
			lock.auto = true
			return
		_say("Nothing to lock there. Double-tap a field or landmark you can see.")
		return
	if Solar.length(Solar.sub(best.pos, me)) > FAR_FLY:
		_say(best.name + " is too far to fly. Use WARP.")
		return
	if not lock.is_empty() and lock.pos == best.pos:   # tapped what's already locked: go
		lock.auto = true
		lock.parked = false
		return
	lock = best
	lock.auto = true
	if best.has("dock"):
		Voice.say("home")


## Docking (Eric 10-23): the bay is open at both ends, so the autopilot comes in from whichever end you are nearer.
func _dock_lock() -> Dictionary:
	var aft: bool = _me()[2] < -26.0
	return {"name": "Starship", "pos": Solar.vec3d(ship.DOCK.aftApproach if aft else ship.DOCK.approach), "aim": [0.0, 0.0, 0.0],
		"stop_at": 14.0, "dock": 1, "aft": aft}


# ── SCANNER (spec §5). Sweeps a cone ahead of the ship. A field's return weakens with distance, is fainter for smaller
#    fields, and is strongest dead centre; random static rides on top, so faint returns flicker. One sweep gives a
#    DIRECTION only: take a bearing, move, take another from somewhere else; where they cross, the field is FIXED and
#    the scanner LOCKS it and goes quiet (Eric 10-10). Close, strong fields fix from one bearing.
func _scan_return(f: Dictionary, me: Array, fwd: Vector3) -> float:
	if f.known:
		return 0.0
	var sv := Solar.vec(Solar.sub(f.center, me))
	var d := maxf(0.0, sv.length() - f.rad)
	var R: float = SCAN_RANGE[f.size] * (1.0 + Session.skill("flight"))   # a Flight uniform hears fields from farther (Eric 10-26)
	if d > R:
		return 0.0
	var ang := sv.angle_to(fwd)
	if ang > SCAN_CONE:
		return 0.0
	var aim := pow((cos(ang) - cos(SCAN_CONE)) / (1.0 - cos(SCAN_CONE)), 2)
	return SCAN_SIG[f.size] * pow(1.0 - d / R, 1.4) * aim


func _scan(dt: float) -> void:
	var me := _me()
	_field_cue(me)
	var fwd := -cam.global_basis.z
	var best := {}
	var bv := 0.0
	var quiet: bool = docked or (not lock.is_empty() and (lock.get("field") != null or lock.get("dock", 0) > 0))
	if not quiet:                                # quiet while locked, docking or docked
		for f in debris.fields:
			var r := _scan_return(f, me, fwd)
			if r > bv:
				bv = r
				best = f
	static_v += ((randf() - 0.5) * 0.9 - static_v * 1.5) * dt * 6.0     # wandering static
	var raw := clampf(bv + static_v * 0.18 * (1.0 - bv), 0.0, 1.0)
	scan_strength += (raw - scan_strength) * (1.0 - exp(-9.0 * dt))
	scan_best = best
	if not best.is_empty() and bv > 0.28:        # strong enough to take a bearing on
		if not voiced.has("ret"):
			voiced.ret = true
			Voice.say("ret")
		var sv := Solar.vec(Solar.sub(best.center, me))
		var dist := sv.length()
		if sv.angle_to(fwd) < deg_to_rad(7.0):
			if dist < 170.0 and bv > 0.75:
				_fix_field(best)
			elif not bearings.has(best.id):
				bearings[best.id] = me
				if not voiced.has("bearing"):
					voiced.bearing = true
					Voice.say("bearing")
				sound.ping(660.0)
				_say("BEARING TAKEN\nMove off to one side, then sweep this return again to fix its position.")
			else:
				var from: Array = bearings[best.id]
				var moved := Solar.length(Solar.sub(me, from))
				var a1 := Solar.vec(Solar.sub(best.center, from)).normalized()
				if moved > maxf(35.0, dist * 0.12) and a1.angle_to(sv.normalized()) > deg_to_rad(2.5):
					_fix_field(best)
	if docked:
		status.text = "DOCKED · throttle up to launch"
	elif lock.get("dock", 0) > 0:
		status.text = "DOCKING · in under the stern" if lock.aft else "DOCKING · under the bow"
	elif lock.get("parked", false):
		status.text = "HOLDING POSITION · in front of the field" if lock.get("field") else "HOLDING POSITION · " + lock.name
	elif lock.get("auto", false):
		status.text = "AUTOPILOT · hold to take the controls"
	elif lock.get("field"):
		status.text = "LOCKED · double-tap to fly there"
	elif not scan_best.is_empty() and bearings.has(scan_best.id) and scan_strength > 0.2:
		status.text = "BEARING 1 OF 2 · move and sweep again"
	elif scan_strength > 0.25:
		status.text = "RETURN"
	else:
		status.text = "SWEEPING"
	sound.scanner(-1.0 if quiet else scan_strength)


func _fix_field(f: Dictionary) -> void:
	bearings.erase(f.id)
	lock = {"name": Debris.label_of(f), "pos": f.center, "stop_at": Debris.stand_off(f), "auto": false, "field": f}
	sound.chime()
	Voice.say("locked")
	_say("FIELD LOCKED\nScanner quiet. Double-tap to fly there.")


## FIELD CUE (Eric 10-11): while the stick is held, a faint glow on its rim shows which way the nearest uncleared field
## lies (as seen on screen), even out of sight and out of scanner range. Dead ahead, the whole rim glows.
func _field_cue(me: Array) -> void:
	var best := {}
	var bd := CUE_RANGE
	if holding and not docked and not (lock.get("field") or lock.get("dock", 0) > 0):
		for f in debris.fields:
			if f.cleared:
				continue
			var d := maxf(0.0, Solar.length(Solar.sub(f.center, me)) - f.rad)
			if d < bd:
				bd = d
				best = f
	if best.is_empty():
		cue.want = 0.0
		return
	var v: Vector3 = cam.global_basis.inverse() * Solar.vec(Solar.sub(best.center, me))   # into the camera's view
	cue.ahead = v.z < 0.0 and atan2(Vector2(v.x, v.y).length(), -v.z) < deg_to_rad(8.0)
	cue.angle = atan2(v.x, v.y)                  # 0 = top, clockwise
	cue.want = 0.25 + 0.5 * (1.0 - bd / CUE_RANGE)


## The pilot's true position in the ship's frame, 64-bit metres.
func _me() -> Array:
	return Solar.add(org, [cam.position.x, cam.position.y, cam.position.z])


# ── WARP (Eric 10-11): pick a destination and you're there in seconds. Rings: you arrive on the ring's line at your
#    current longitude. The route bends around the Sun if a straight line would pass too close.
const Solar := preload("res://scripts/solar.gd")
const Debris := preload("res://scripts/debris.gd")


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
	var warp_cost := FUEL_WARP / (1.0 + Session.skill("flight"))
	if fuel < warp_cost:
		_say("Not enough fuel to warp. Fly home, or wait for a tow.")
		return
	fuel -= warp_cost
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
	lock = {}
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
		var first: bool = work_ring == null
		work_ring = w.d.ring
		inara_t = 0.0
		Voice.say("warp%d" % Solar.RINGS.find(w.d.ring))
		if first:
			Voice.story(hud_root, "ring")
		_say("INARA\nDropping out in the " + w.d.ring.name + ". Debris all around you. Start sweeping.")
	elif w.d.key == "starship":
		cam.look_at(cam.position + Solar.vec(Solar.sub([0.0, 0.0, 0.0], _me())), Vector3.UP)     # turned to face her
		Voice.say("arrived")
		_say("ARRIVED\nThe Starship is ahead. Double-tap it to come aboard.")
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
		for c in get_parent().get_children():      # the HUD's buttons and words are in the way too (Eric 10-24)
			if c == self or not c.visible or c is Panel or not (c is Button or c is Label or c == bay.radar):
				continue
			if c is Label and (c as Label).text == "":
				continue
			var r: Rect2 = c.get_rect()
			if c == bay.thr_label:
				r.size = c.get_minimum_size()
			placed.append({"x": r.get_center().x, "y": r.get_center().y, "w": r.size.x, "h": r.size.y})
		var lms: Array = bay.sol.landmarks.duplicate()
		if not bay.band.is_empty() and bay.band.out > 1.0 and bay.warp.is_empty():   # outside the band: point the way back
			bay._band_node.position = bay.Solar.vec(bay.Solar.sub(bay.band.point, bay.org)).limit_length(300000.0)
			lms.append({"name": "Back to the " + bay.band.ring.name, "node": bay._band_node, "pos": bay.band.point, "rad": 0.0, "color": Color(1.0, 0.81, 0.42)})
		for l in lms:
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
			var hits := func(y: float) -> bool:
				for q in placed:
					if absf(q.x - px) < (w + q.w) / 2.0 + 8.0 and absf(q.y - y) < (h + q.h) / 2.0 + 3.0:
						return true
				return false
			var clear := false
			for k in range(1, 26):
				if not hits.call(py):
					clear = true
					break
				var step := ceili(k / 2.0) * (1 if k % 2 else -1)
				py = clampf(by + step * (h + 4.0), h / 2.0 + 6.0, H - h / 2.0 - 6.0)
			if not clear:                        # nowhere clear: stay where it belongs rather than land on a button
				py = clampf(by, h / 2.0 + 6.0, H - h / 2.0 - 6.0)
			placed.append({"x": px, "y": py, "w": w, "h": h})
			var c: Color = l.color
			var mc := Vector2(px, py - h / 2.0 + 8.0)
			# no ring over a body whose own disc is already bigger than the ring: the body shows itself
			var disc_px: float = l.rad / maxf(bay.sol.dist_to(l, me), 1.0) / th * H / 2.0
			if on and disc_px > 8.0:
				pass
			elif on:
				draw_arc(mc, 7.0, 0.0, TAU, 24, c, 2.5, true)
			else:
				var r := 8.0
				draw_polyline(PackedVector2Array([mc + Vector2(0, -r), mc + Vector2(r, 0), mc + Vector2(0, r), mc + Vector2(-r, 0), mc + Vector2(0, -r)]), c, 2.5, true)
			var base := Vector2(px - tw / 2.0, py + h / 2.0 - 6.0)
			draw_string(font, base + Vector2(0, 2), text, HORIZONTAL_ALIGNMENT_LEFT, -1, fs, Color(0, 0, 0, 0.85))
			draw_string(font, base, text, HORIZONTAL_ALIGNMENT_LEFT, -1, fs, c)
		# the lock (browser #lock): a green box on what's locked, with what the autopilot is doing
		var lk: Dictionary = bay.lock
		if not lk.is_empty() and bay.warp.is_empty():
			var p: Array = bay.Solar.sub(lk.get("aim", lk.pos), bay.org)
			var v: Vector3 = inv * bay.Solar.vec(p)
			if v.z < 0.0:
				var x := (v.x / -v.z) / (th * aspect)
				var y := (v.y / -v.z) / th
				if absf(x) < 1.0 and absf(y) < 1.0:
					var at := Vector2((x + 1.0) / 2.0 * W, (1.0 - y) / 2.0 * H)
					var g := Color("7fe0a8")
					draw_rect(Rect2(at - Vector2(31, 31), Vector2(62, 62)), g, false, 2.5)
					var t: String = ("AUTOPILOT · " if lk.get("auto", false) else ("HOLDING · " if lk.get("parked", false) else "LOCKED · ")) \
						+ lk.name + " · " + bay.Solar.fmt_dist(bay.Solar.length(bay.Solar.sub(lk.pos, me)))
					var tw2 := font.get_string_size(t, HORIZONTAL_ALIGNMENT_LEFT, -1, fs).x
					draw_string(font, at + Vector2(-tw2 / 2.0, 58), t, HORIZONTAL_ALIGNMENT_LEFT, -1, fs, Color(0, 0, 0, 0.85))
					draw_string(font, at + Vector2(-tw2 / 2.0, 56), t, HORIZONTAL_ALIGNMENT_LEFT, -1, fs, g)


## The stick (browser #stick, #knob) where you press, and on its rim the gold field cue (browser #cue).
class Stick extends Control:
	var bay: Node
	func _draw() -> void:
		if not bay.holding or bay.docked:
			return
		var c: Vector2 = bay.stick_from
		var R := 120.0
		draw_arc(c, R, 0.0, TAU, 64, Color(0.5, 0.69, 1.0, 0.35), 2.5, true)
		var k: Vector2 = (bay.stick_at - c).limit_length(bay.STICK_R) * (72.0 / bay.STICK_R)
		draw_circle(c + k, 48.0, Color(0.5, 0.69, 1.0, 0.25))
		draw_arc(c + k, 48.0, 0.0, TAU, 48, Color(0.5, 0.69, 1.0, 0.6), 2.5, true)
		var a: float = bay.cue.alpha
		if a < 0.01:
			return
		var gold := Color(1.0, 0.81, 0.42)
		if bay.cue.ahead:                        # dead ahead: the whole rim glows
			for i in 6:
				draw_arc(c, R + (i - 2.5) * 3.0, 0.0, TAU, 96, Color(gold, a * (0.45 - absf(i - 2.5) * 0.12)), 3.0, true)
			return
		# a soft gold glow on the rim, turned toward the field (0 = top, clockwise)
		draw_set_transform(c + Vector2(sin(bay.cue.angle), -cos(bay.cue.angle)) * R, bay.cue.angle, Vector2(1.0, 0.33))
		for i in 8:
			var r := 50.0 * (1.0 - i / 8.0)
			draw_circle(Vector2.ZERO, r, Color(gold, a * 0.18))
		draw_set_transform(Vector2.ZERO)


## A faint gold glow round the whole edge of the screen, slowly breathing, while something needs your attention.
class EdgeGlow extends Control:
	var on := false
	func _draw() -> void:
		if not on:
			return
		var a := 0.22 + 0.12 * sin(Time.get_ticks_msec() / 1000.0 * 2.4)
		var g := Color(1.0, 0.81, 0.42)
		for i in 10:                             # soft: ten thin bands fading inward
			var k := float(i) / 10.0
			var c := Color(g, a * pow(1.0 - k, 2))
			var d := i * 3.0
			draw_rect(Rect2(d, d, size.x - 2 * d, size.y - 2 * d), c, false, 3.0)


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
