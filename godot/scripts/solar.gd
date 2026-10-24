extends Node3D
## THE SOLAR SYSTEM around the flight, ported from the live browser game (static/debris-flight.js), number for number:
## true scale, 1 unit = 1 metre; the Sun, the four rings and the gas giants at their real distances; the wormhole 3 million
## km beyond Jupiter with the Starship parked 30 km off it, bow toward the Sun.
## The app keeps the Starship at the origin (bow +Z, Y up), so every world position is turned into the ship's frame.
## Positions are kept in full 64-bit precision on the CPU as [x, y, z] arrays and only small offsets reach the GPU: the
## scene's origin floats with the pilot (`org`, owned by the bay), so nothing shakes a billion kilometres out. Bodies far
## beyond the camera's range are drawn IMP_D metres away in their true direction at their true apparent size (placeFar).

const AU := 1.495978707e11
const SUN_R := 6.957e8
const RINGS := [ # where the four destroyed inner planets orbited: their true mean distances from the Sun (STORY-BIBLE.md)
	{"key": "mercury", "name": "Mercury ring", "au": 0.387},
	{"key": "venus", "name": "Venus ring", "au": 0.723},
	{"key": "earth", "name": "Earth ring", "au": 1.000},
	{"key": "mars", "name": "Mars ring", "au": 1.524}]
const BAND_HALF := 25000.0       # the debris band: 25 km either side of a ring's line, 6 km above and below
const BAND_THICK := 6000.0
const GIANTS := [ # true mean distances and radii; the angles just set where they are in the sky
	{"name": "Jupiter", "au": 5.204, "ang": 2.1, "rad": 6.9911e7, "color": Color("d2b08a")},
	{"name": "Saturn", "au": 9.583, "ang": 4.4, "rad": 5.8232e7, "color": Color("e0cc9c"), "ring": true}]
const WORMHOLE_R := 1500.0
const IMP_D := 200000.0
const SHIP_LIGHT := 1.8          # the app's sunlight at the Starship; it falls with the square of the distance from there

var sp: Array                    # the Starship's world position (browser STARSHIP_POS)
var ax: Array                    # the ship's axes in world coordinates (bow +Z faces the Sun)
var ay: Array
var az: Array
var sun_l: Array                 # positions in the ship's frame, metres, full precision
var giants_l: Array = []
var wh_w: Array
var wh_l: Array
var ship_sun_d: float

var landmarks: Array = []        # {name, pos (ship frame), node, rad, far, home, color}
var sun: Node3D
var glow: MeshInstance3D
var light: DirectionalLight3D
var wormhole: Node3D
var stars: MultiMeshInstance3D
var ship: Node3D


static func add(a: Array, b: Array) -> Array: return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]
static func sub(a: Array, b: Array) -> Array: return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]
static func mul(a: Array, s: float) -> Array: return [a[0] * s, a[1] * s, a[2] * s]
static func dot(a: Array, b: Array) -> float: return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
static func length(a: Array) -> float: return sqrt(dot(a, a))
static func norm(a: Array) -> Array: return mul(a, 1.0 / length(a))
static func cross(a: Array, b: Array) -> Array:
	return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]
static func vec(a: Array) -> Vector3: return Vector3(a[0], a[1], a[2])
static func vec3d(v: Vector3) -> Array: return [v.x, v.y, v.z]


func to_local_d(w: Array) -> Array:
	var d := sub(w, sp)
	return [dot(d, ax), dot(d, ay), dot(d, az)]


func to_world_d(l: Array) -> Array:
	return add(sp, add(mul(ax, l[0]), add(mul(ay, l[1]), mul(az, l[2]))))


func giant_w(g: Dictionary) -> Array:
	return mul([cos(g.ang), 0.0, sin(g.ang)], g.au * AU)


func _init() -> void:
	var jup := giant_w(GIANTS[0])
	wh_w = add(jup, mul(norm(jup), 3.0e9))      # 3 million km beyond Jupiter, away from the Sun
	var out := norm(wh_w)
	var side := [-out[2], 0.0, out[0]]
	sp = add(add(add(wh_w, mul(side, 30000.0)), mul(out, -12000.0)), [0.0, 2500.0, 0.0])
	az = norm(mul(sp, -1.0))                    # three.js lookAt(Sun): +Z toward the Sun
	ax = norm(cross([0.0, 1.0, 0.0], az))
	ay = cross(az, ax)
	sun_l = to_local_d([0.0, 0.0, 0.0])
	for g in GIANTS:
		giants_l.append(to_local_d(giant_w(g)))
	wh_l = to_local_d(wh_w)
	ship_sun_d = length(sp)


func setup(the_ship: Node3D) -> void:
	ship = the_ship
	landmarks.append({"name": "Starship", "node": ship, "pos": [0.0, 0.0, 0.0], "rad": 140.0, "home": true, "color": Color("7fb0ff")})
	light = DirectionalLight3D.new()     # the Sun: the one light
	light.light_color = Color("fff1dc")
	add_child(light)
	sun = _sun()
	glow = _quad(_glow_tex([[0.0, Color(1, 0.94, 0.78, 1)], [0.18, Color(1, 0.84, 0.55, 0.55)],
		[0.45, Color(1, 0.67, 0.31, 0.12)], [1.0, Color(1, 0.55, 0.16, 0)]]), true, 1.0)
	for i in GIANTS.size():
		var g: Dictionary = GIANTS[i]
		var m := StandardMaterial3D.new()
		m.albedo_texture = load("res://assets/planets/%s.jpg" % g.name.to_lower())   # NASA maps (assets/SOURCES.md)
		m.emission_texture = m.albedo_texture
		m.roughness = 1.0
		m.metallic = 0.0
		m.emission_enabled = true
		m.emission = Color.WHITE
		m.emission_energy_multiplier = 0.07
		m.disable_fog = true
		var body := _sphere(m, 64)
		body.basis = _w2l()             # its poles on the solar system's own axis
		if g.get("ring", false):
			body.add_child(_saturn_ring())
		landmarks.append({"name": g.name, "node": body, "pos": giants_l[i], "rad": g.rad, "far": true, "color": Color("d9a441")})
	landmarks.append({"name": "Sun", "node": sun, "pos": sun_l, "rad": SUN_R, "far": true, "color": Color("d9a441")})
	_wormhole()
	landmarks.append({"name": "Wormhole", "node": wormhole, "pos": wh_l, "rad": WORMHOLE_R, "color": Color("b49cff")})
	_stars()


## Each frame: put every body where it belongs for a pilot at org + cam.position (ship frame, metres).
func place(org: Array, cam: Camera3D) -> void:
	var me := add(org, [cam.position.x, cam.position.y, cam.position.z])
	var to_sun := sub(sun_l, me)
	var d := length(to_sun)
	light.light_energy = minf(SHIP_LIGHT * pow(ship_sun_d / maxf(d, SUN_R * 30.0), 2), 6.0)
	light.basis = Basis.looking_at(-vec(norm(to_sun)), Vector3.UP)
	var s := _place_far(sun, sun_l, SUN_R, org, me, cam)
	glow.position = sun.position
	glow.scale = Vector3.ONE * maxf(s * 22.0, IMP_D * 0.012)   # a little more than the browser (Eric 10-24)
	for i in GIANTS.size():
		_place_far(landmarks[i + 1].node, giants_l[i], GIANTS[i].rad, org, me, cam)
	var near := func(n: Node3D, p: Array) -> void:
		var rel := sub(p, org)
		n.visible = length(rel) < 2.0e6
		if n.visible:
			n.position = vec(rel)
	near.call(ship, [0.0, 0.0, 0.0])
	near.call(wormhole, wh_l)
	stars.position = cam.position


func _place_far(n: Node3D, p: Array, r: float, org: Array, me: Array, cam: Camera3D) -> float:
	var tv := sub(p, me)
	var d := length(tv)
	if d < IMP_D:
		n.position = vec(sub(p, org))
		n.scale = Vector3.ONE * r
		return r
	n.position = cam.position + vec(mul(tv, IMP_D / d))
	n.scale = Vector3.ONE * (r * IMP_D / d)
	return r * IMP_D / d


## The pilot's true distance from a landmark, metres.
func dist_to(l: Dictionary, me: Array) -> float:
	return length(sub(l.pos, me))


func ring_of(me_world: Array) -> Variant:
	var rxy := Vector2(me_world[0], me_world[2]).length()
	for rg in RINGS:
		if absf(rxy - rg.au * AU) < BAND_HALF and absf(me_world[1]) < BAND_THICK:
			return rg
	return null


static func fmt_dist(m: float) -> String:
	if m < 1000.0:
		return "%d m" % roundi(m)
	if m < 1e6:
		return ("%.1f km" if m < 1e5 else "%.0f km") % (m / 1000.0)
	if m < 0.05 * AU:
		return _commas(roundi(m / 1000.0)) + " km"
	return "%.2f AU" % (m / AU)


static func _commas(n: int) -> String:
	var s := str(n)
	var out := ""
	while s.length() > 3:
		out = "," + s.substr(s.length() - 3) + out
		s = s.substr(0, s.length() - 3)
	return s + out


# ── the bodies ──
func _unlit(c: Color) -> StandardMaterial3D:
	var m := StandardMaterial3D.new()
	m.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	m.albedo_color = c
	m.disable_fog = true
	return m


func _sphere(m: Material, seg: int) -> MeshInstance3D:
	var sm := SphereMesh.new()
	sm.radius = 1.0
	sm.height = 2.0
	sm.radial_segments = seg
	sm.rings = seg * 5 / 8
	var mi := MeshInstance3D.new()
	mi.mesh = sm
	mi.material_override = m
	add_child(mi)
	return mi


## A camera-facing square (the browser's THREE.Sprite), 1 m wide before scaling.
func _quad(tex: Texture2D, additive: bool, opacity: float, parent: Node = self) -> MeshInstance3D:
	var m := StandardMaterial3D.new()
	m.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	m.billboard_mode = BaseMaterial3D.BILLBOARD_ENABLED
	m.billboard_keep_scale = true
	m.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
	if additive:
		m.blend_mode = BaseMaterial3D.BLEND_MODE_ADD
	m.depth_draw_mode = BaseMaterial3D.DEPTH_DRAW_DISABLED
	m.albedo_texture = tex
	m.albedo_color = Color(1, 1, 1, opacity)
	m.disable_fog = true
	var q := QuadMesh.new()
	q.size = Vector2.ONE
	var mi := MeshInstance3D.new()
	mi.mesh = q
	mi.material_override = m
	parent.add_child(mi)
	return mi


## The browser's glowTex: a radial gradient on a 256 square.
func _glow_tex(stops: Array) -> Texture2D:
	var g := Gradient.new()
	g.offsets = PackedFloat32Array(stops.map(func(s): return s[0]))
	g.colors = PackedColorArray(stops.map(func(s): return s[1]))
	var t := GradientTexture2D.new()
	t.gradient = g
	t.width = 256
	t.height = 256
	t.fill = GradientTexture2D.FILL_RADIAL
	t.fill_from = Vector2(0.5, 0.5)
	t.fill_to = Vector2(1.0, 0.5)
	return t


## Saturn's ring (three.js RingGeometry 1.35..2.3 in the XY plane, tilted PI/2.4 about the world X axis).
func _saturn_ring() -> MeshInstance3D:
	var st := SurfaceTool.new()
	st.begin(Mesh.PRIMITIVE_TRIANGLES)
	var n := 96
	for i in n:
		var a0 := TAU * i / n
		var a1 := TAU * (i + 1) / n
		var p := [Vector3(cos(a0) * 1.35, sin(a0) * 1.35, 0), Vector3(cos(a0) * 2.3, sin(a0) * 2.3, 0),
			Vector3(cos(a1) * 2.3, sin(a1) * 2.3, 0), Vector3(cos(a1) * 1.35, sin(a1) * 1.35, 0)]
		for k in [0, 1, 2, 0, 2, 3]:
			st.set_normal(Vector3.BACK)
			st.add_vertex(p[k])
	var m := StandardMaterial3D.new()
	m.albedo_color = Color(Color("cdb892"), 0.75)
	m.emission_enabled = true          # a little light of its own, so the ring reads past the planet's edge (Eric 10-24)
	m.emission = Color("cdb892")
	m.emission_energy_multiplier = 0.3
	m.roughness = 1.0
	m.cull_mode = BaseMaterial3D.CULL_DISABLED
	m.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
	m.disable_fog = true
	var mi := MeshInstance3D.new()
	mi.mesh = st.commit()
	mi.material_override = m
	# the tilt is in the solar system's own axes, so turn it into the ship's frame
	mi.basis = Basis(Vector3.RIGHT, PI / 2.4)      # Saturn itself is already turned into the solar system's axes
	return mi


func _w2l() -> Basis:
	return Basis(Vector3(ax[0], ay[0], az[0]), Vector3(ax[1], ay[1], az[1]), Vector3(ax[2], ay[2], az[2]))


## The Sun: NASA's Solar Dynamics Observatory photograph of its disc (HMI, visible light), always facing the camera.
## The photo's disc fills 478/512 of the picture; everything outside it (black sky, the caption) is cut away.
func _sun() -> Node3D:
	var n := Node3D.new()
	add_child(n)
	var sh := Shader.new()
	sh.code = """
shader_type spatial;
render_mode unshaded, cull_disabled, depth_draw_never, fog_disabled;
uniform sampler2D tex : source_color, filter_linear_mipmap;
void vertex() {
	MODELVIEW_MATRIX = VIEW_MATRIX * mat4(INV_VIEW_MATRIX[0], INV_VIEW_MATRIX[1], INV_VIEW_MATRIX[2], MODEL_MATRIX[3]);
	MODELVIEW_MATRIX = MODELVIEW_MATRIX * mat4(vec4(length(MODEL_MATRIX[0].xyz), 0, 0, 0), vec4(0, length(MODEL_MATRIX[1].xyz), 0, 0), vec4(0, 0, length(MODEL_MATRIX[2].xyz), 0), vec4(0, 0, 0, 1));
}
void fragment() {
	float r = length(UV - 0.5) * 2.0;
	ALBEDO = texture(tex, UV).rgb;
	ALPHA = 1.0 - smoothstep(0.925, 0.94, r);
}
"""
	var m := ShaderMaterial.new()
	m.shader = sh
	m.set_shader_parameter("tex", load("res://assets/planets/sun_sdo_hmi.jpg"))
	m.render_priority = 2              # drawn over its own glow, so the photo shows
	var q := QuadMesh.new()
	q.size = Vector2.ONE * 2.0 * 512.0 / 478.0
	var mi := MeshInstance3D.new()
	mi.mesh = q
	mi.material_override = m
	n.add_child(mi)
	return n


## THE WORMHOLE (STORY-BIBLE): a throat onto another universe, ringed with light. Through the throat you see ANOTHER
## universe (Eric 10-20: black reads as a black hole): its stars are a different colour, denser and brighter than ours.
func _wormhole() -> void:
	wormhole = Node3D.new()
	add_child(wormhole)
	var img := Image.create(512, 512, false, Image.FORMAT_RGBA8)
	img.fill(Color(0, 0, 0, 0))
	# the browser hands this canvas to the GPU as linear colour, which shows it brighter than drawn: do the same here
	_disc(img, 256, 256, 256, Color("030308").linear_to_srgb(), 1.0)
	var r := [12345]                 # (a lambda captures locals by value, so the seed lives in an array)
	var rnd := func() -> float:
		r[0] = (r[0] * 16807) % 2147483647
		return float(r[0]) / 2147483647.0
	var tints := [Color("ffd9a0"), Color("a0fff0"), Color("ffb3e6"), Color("d8c8ff"), Color("ffffff")]
	for i in 450:
		var a: float = rnd.call() * TAU
		var d: float = sqrt(rnd.call()) * 256.0
		var k := 1.0 - d / 256.0 * 0.7
		var s := 2.2 if rnd.call() < 0.06 else (1.3 if rnd.call() < 0.3 else 0.8)
		_disc(img, 256 + cos(a) * d, 256 + sin(a) * d, s, (tints[i % tints.size()] as Color).linear_to_srgb(), 0.55 + 0.45 * k, 256.0)
	for i in 33:                     # 33 brighter stars (Eric 10-20): same size, more intense
		var a: float = rnd.call() * TAU
		var d: float = sqrt(rnd.call()) * 240.0
		_disc(img, 256 + cos(a) * d, 256 + sin(a) * d, 1.3, Color.WHITE, 1.0, 256.0)
	img.generate_mipmaps()
	var core := _quad(ImageTexture.create_from_image(img), false, 1.0, wormhole)
	core.scale = Vector3.ONE * 1.54  # fills right up to the ring (its bright band sits at radius 0.8)
	(core.material_override as StandardMaterial3D).render_priority = 0
	var ring_tex := _glow_tex([[0.0, Color(0, 0, 0, 0)], [0.44, Color(0, 0, 0, 0)], [0.475, Color8(120, 90, 255, 89)],
		[0.5, Color8(190, 220, 255, 255)], [0.525, Color8(120, 90, 255, 89)], [0.7, Color8(80, 50, 200, 38)], [1.0, Color8(40, 20, 120, 0)]])
	var rq := _quad(ring_tex, true, 0.9, wormhole)
	rq.scale = Vector3.ONE * 3.2
	(rq.material_override as StandardMaterial3D).render_priority = 1
	wormhole.scale = Vector3.ONE * WORMHOLE_R


## A soft-edged filled circle, blended over what's there (clipped to the wormhole's disc when clip > 0).
func _disc(img: Image, cx: float, cy: float, rad: float, c: Color, alpha: float, clip := 0.0) -> void:
	for y in range(floori(cy - rad - 1), ceili(cy + rad + 1) + 1):
		for x in range(floori(cx - rad - 1), ceili(cx + rad + 1) + 1):
			if x < 0 or y < 0 or x >= img.get_width() or y >= img.get_height():
				continue
			if clip > 0.0 and Vector2(x + 0.5 - 256, y + 0.5 - 256).length() > clip:
				continue
			var cov := clampf(rad + 0.5 - Vector2(x + 0.5 - cx, y + 0.5 - cy).length(), 0.0, 1.0) * alpha
			if cov <= 0.0:
				continue
			var dst := img.get_pixel(x, y)
			var a := cov + dst.a * (1.0 - cov)
			var rgb := (Color(c.r, c.g, c.b) * cov + Color(dst.r, dst.g, dst.b) * dst.a * (1.0 - cov)) / maxf(a, 1e-6)
			img.set_pixel(x, y, Color(rgb.r, rgb.g, rgb.b, a))


## The starfield rides with the camera: the stars are too far for anything you do to move them.
func _stars() -> void:
	var mm := MultiMesh.new()
	mm.transform_format = MultiMesh.TRANSFORM_3D
	var qm := QuadMesh.new()
	qm.size = Vector2(200, 200)
	mm.mesh = qm
	mm.instance_count = 2500
	var rng := RandomNumberGenerator.new()
	rng.seed = 7
	for i in mm.instance_count:
		var d := Vector3(rng.randfn(), rng.randfn(), rng.randfn()).normalized()
		var p := d * 300000.0
		var b := Basis.looking_at(-d, Vector3.UP if absf(d.y) < 0.99 else Vector3.RIGHT)
		mm.set_instance_transform(i, Transform3D(b.scaled(Vector3.ONE * rng.randf_range(0.4, 1.4)), p))
	stars = MultiMeshInstance3D.new()
	stars.multimesh = mm
	var m := _unlit(Color("dfe6ff"))
	m.billboard_mode = BaseMaterial3D.BILLBOARD_ENABLED
	stars.material_override = m
	stars.extra_cull_margin = 400000.0
	add_child(stars)
