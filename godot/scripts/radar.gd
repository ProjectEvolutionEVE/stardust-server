extends Control
## THE LONG-RANGE SCANNER (Eric 10-24): a pull-down radar solar map, hidden at the top of the screen; the RADAR tab drops
## it down and pulls it back out of view. Transparent like the other instruments. A red sweep turns once every 12 s with
## a glow trailing 1 s behind it; what it passes lights up and fades through the turn, as a radar's returns do.
## Top-down onto the plane of the orbits, turned so straight up is the way your nose points. Tap it to change the range:
## nearby fields (5 km), the ring's band (75 km), the inner system (2 AU), the whole system out to Saturn (11 AU).

const Solar := preload("res://scripts/solar.gd")
const R := 190.0                                # the scope's radius on screen
const TURN := 12.0                              # seconds for one full sweep
const TRAIL := 1.0                              # the sweep's glow lingers this long behind it
const RED := Color(0.88, 0.16, 0.24)
const RANGES := [[5000.0, "5 km"], [75000.0, "75 km"], [2.0 * Solar.AU, "2 AU"], [11.0 * Solar.AU, "11 AU"]]

var bay: Node
var open := false
var range_i := 1
var tab: Button
var top_y := -440.0


func _ready() -> void:
	size = Vector2(440, 430)
	position = Vector2(140, top_y)
	mouse_filter = Control.MOUSE_FILTER_IGNORE
	visible = false


func toggle() -> void:
	open = not open
	if open:
		visible = true
		mouse_filter = Control.MOUSE_FILTER_STOP
	var tw := create_tween()
	tw.tween_property(self, "position:y", 124.0 if open else top_y, 0.3).set_trans(Tween.TRANS_CUBIC).set_ease(Tween.EASE_OUT)
	if not open:
		mouse_filter = Control.MOUSE_FILTER_IGNORE
		tw.tween_callback(func(): visible = open)


func _gui_input(ev: InputEvent) -> void:      # tap the scope: the next range
	if ev.device == InputEvent.DEVICE_ID_EMULATION:
		return    # on a phone each touch also arrives as a copied mouse event; counting both made one press a double-tap
	if ev is InputEventMouseButton and ev.pressed and ev.button_index == MOUSE_BUTTON_LEFT \
			or ev is InputEventScreenTouch and ev.pressed:
		range_i = (range_i + 1) % RANGES.size()
		accept_event()


func _process(_dt: float) -> void:
	if visible:
		queue_redraw()


func _draw() -> void:
	var c := Vector2(size.x / 2.0, R + 8.0)
	var font := get_theme_default_font()
	var t := Time.get_ticks_msec() / 1000.0
	var sweep := fposmod(t / TURN, 1.0) * TAU    # 0 = straight up, clockwise
	# the scope: transparent, red rings
	draw_circle(c, R, Color(0, 0, 0, 0.28))
	for k in [1.0, 0.66, 0.33]:
		draw_arc(c, R * k, 0.0, TAU, 96, Color(RED, 0.55 if k == 1.0 else 0.22), 1.5 if k == 1.0 else 1.0, true)
	draw_line(c - Vector2(R, 0), c + Vector2(R, 0), Color(RED, 0.15), 1.0)
	draw_line(c - Vector2(0, R), c + Vector2(0, R), Color(RED, 0.15), 1.0)
	# the trailing glow: a wedge behind the sweep, fading over TRAIL seconds
	var steps := 24
	for i in steps:
		var a0 := sweep - TAU * TRAIL / TURN * float(i) / steps
		var a1 := sweep - TAU * TRAIL / TURN * float(i + 1) / steps
		var al := 0.32 * (1.0 - float(i) / steps)
		draw_colored_polygon(PackedVector2Array([c, c + _dir(a0) * R, c + _dir(a1) * R]), Color(RED, al))
	draw_line(c, c + _dir(sweep) * R, Color(RED, 0.95), 2.0, true)
	# what's on it
	var rng: float = RANGES[range_i][0]
	var k := R / rng
	var me_w: Array = bay.sol.to_world_d(bay._me())
	var center: Array = [0.0, 0.0, 0.0] if rng > 1e9 else me_w     # the system maps are centred on the Sun
	var f: Vector3 = -bay.cam.global_basis.z
	var fw := Solar.add(Solar.add(Solar.mul(bay.sol.ax, f.x), Solar.mul(bay.sol.ay, f.y)), Solar.mul(bay.sol.az, f.z))
	var fv := Vector2(fw[0], fw[2])
	fv = fv.normalized() if fv.length() > 1e-6 else Vector2(1, 0)
	var to_scope := func(p: Array) -> Vector2:   # world point -> scope (nose up)
		var d := Vector2(p[0] - center[0], p[2] - center[2])
		return Vector2(-d.x * fv.y + d.y * fv.x, -(d.x * fv.x + d.y * fv.y)) * k
	var glow := func(v: Vector2) -> float:       # a return is brightest just after the sweep passes it
		var since := fposmod(sweep - fposmod(atan2(v.x, -v.y), TAU), TAU) / TAU * TURN
		return clampf(1.0 - since / TURN, 0.25, 1.0)
	# the rings: their bands up close, their orbits from far
	for rg in Solar.RINGS:
		var rr: float = rg.au * Solar.AU
		var lines: Array = [rr] if rng > 1e9 else [rr - bay.sol.BAND_HALF, rr + bay.sol.BAND_HALF]
		var lon := atan2(me_w[2], me_w[0])
		var span := PI if rng > 1e9 else minf(PI, rng * 1.6 / rr)
		for L in lines:
			var prev = null
			for i in 97:
				var th := lon - span + 2.0 * span * i / 96.0
				var v: Vector2 = to_scope.call([cos(th) * L, 0.0, sin(th) * L])
				if prev != null and v.length() < R and prev.length() < R:
					draw_line(c + prev, c + v, Color(0.5, 0.88, 0.66, 0.35), 1.0, true)
				prev = v
	# debris fields (gold), the locked one ringed
	if rng < 1e6:
		for fl in bay.debris.fields:
			if fl.cleared:
				continue
			var v: Vector2 = to_scope.call(fl.center_w)
			if v.length() > R:
				continue
			var big: float = {"large": 4.0, "medium": 3.0, "small": 2.2, "tiny": 1.6}[fl.size]
			draw_circle(c + v, big, Color(1.0, 0.81, 0.42, glow.call(v)))
			if bay.lock.get("field") and bay.lock.field.id == fl.id:
				draw_arc(c + v, big + 5.0, 0.0, TAU, 24, Color("7fe0a8"), 1.5, true)
	# landmarks; past the edge they wait on the rim
	var marks := [[tr("Sun"), [0.0, 0.0, 0.0], Color("ffcf6b")], [tr("Starship"), bay.sol.sp, Color("7fb0ff")],
		[tr("Wormhole"), bay.sol.wh_w, Color("b49cff")]]
	for g in Solar.GIANTS:
		marks.append([tr(g.name), bay.sol.giant_w(g), Color("d9a441")])
	if rng > 1e9:
		marks.append([tr("You"), me_w, Color("7fe0a8")])
	var placed: Array = []
	for m in marks:
		var v: Vector2 = to_scope.call(m[1])
		var on := v.length() <= R
		if not on:
			if rng < 1e6 and m[0] != tr("Starship"):
				continue                         # up close, only the Starship points the way home from the rim
			v = v.normalized() * R
		var col: Color = m[2]
		draw_circle(c + v, 3.5 if on else 2.5, Color(col, glow.call(v) if on else 0.6))
		var at := c + v + Vector2(6, -4)
		for q in placed:                         # names that would sit on each other step down a line
			if absf(q.x - at.x) < 70.0 and absf(q.y - at.y) < 12.0:
				at.y = q.y + 13.0
		placed.append(at)
		draw_string(font, at, m[0], HORIZONTAL_ALIGNMENT_LEFT, -1, 12, Color(col, 0.85))
	if rng < 1e9:                                # you, at the centre, nose up
		draw_colored_polygon(PackedVector2Array([c + Vector2(0, -7), c + Vector2(5, 5), c + Vector2(-5, 5)]), Color("7fe0a8"))
	var txt := tr("RANGE %s · tap to change") % RANGES[range_i][1]
	var tw := font.get_string_size(txt, HORIZONTAL_ALIGNMENT_LEFT, -1, 13).x
	draw_string(font, Vector2(c.x - tw / 2.0, c.y + R + 22.0), txt, HORIZONTAL_ALIGNMENT_LEFT, -1, 13, Color(RED, 0.9))


static func _dir(a: float) -> Vector2:
	return Vector2(sin(a), -cos(a))
