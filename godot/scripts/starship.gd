extends Node3D
## THE STARSHIP, WSC Alexander von Humboldt (rule 9: the Starship is the truth). Built from the same numbers as the live
## browser game (static/debris-flight.js, the ship block), line for line, so both look the same: the sleek hull with no
## fins or wings, the raised spine on top, the Tower (bridge) under the bow, the belly docking bay open at both ends with
## its level deck, the original hangar door in the bay's ceiling, the oval exhaust, and the guide lights.
## Ship axes as in the browser: bow toward +Z, Y up, metres.

const SKIN := 2.2
const EDGE_K := 3.0
const ROUND_L := 6.0
const MAIN := [[0, 130], [7, 90], [15, 30], [19, -40], [20, -100], [14, -130]]
const MAIN_FLARE := 1.2
const RIDGE := [[0, 70], [6, 30], [10, -40], [11, -110], [8, -126]]
const RIDGE_Y := 12.0
const BAY := {"zf": 66.0, "za": -118.0, "cy": -11.6, "a": 15.75, "b": 13.5, "pOut": 2.6, "ocy": -14.3, "hw": 13.5,
	"hh": 8.1, "pTop": 2.4, "pBot": 4.0, "rake": 1.2, "lip": 12.0, "sweep": 16.0}
const DOCK := {"approach": Vector3(0, -17, 215), "mouth": Vector3(0, -15, -35),
	"aftApproach": Vector3(0, -17, -285), "aftMouth": Vector3(0, -15, -60)}

var hull_mat: StandardMaterial3D
var guide: Array = []          # [mesh, t] pairs, pulsed toward the ship


func _ready() -> void:
	hull_mat = _mat(Color("5a606b"), 0.5, 0.35)
	_mesh(_dagger(MAIN, 14, 20, 130, MAIN_FLARE, Vector2(12, 12 * 0.42)), hull_mat)
	var ridge := _mesh(_dagger(RIDGE, 8, 0, 70, 0.0, Vector2.ZERO), hull_mat)
	ridge.position.y = RIDGE_Y
	_bay()
	_exhaust()
	_tower()
	_name()
	_door()
	_portholes()
	_lights()


func _process(delta: float) -> void:
	var t := Time.get_ticks_msec() / 1000.0
	for g in guide:                # the lane pulses in sequence toward the ship
		var ph := fposmod(t * 0.6 - g[1], 1.0)
		var k := pow(1.0 - ph, 6)
		(g[0].material_override as StandardMaterial3D).emission = Color(0.25 + 0.25 * k, 0.45 + 0.5 * k, 0.35 + 0.4 * k)


# ── helpers ──
func _mat(c: Color, rough: float, metal: float) -> StandardMaterial3D:
	var m := StandardMaterial3D.new()
	m.albedo_color = c
	m.roughness = rough
	m.metallic = metal
	m.cull_mode = BaseMaterial3D.CULL_DISABLED
	return m


func _glow(c: Color) -> StandardMaterial3D:
	var m := StandardMaterial3D.new()
	m.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	m.albedo_color = c
	m.emission_enabled = true
	m.emission = c
	m.cull_mode = BaseMaterial3D.CULL_DISABLED
	return m


func _mesh(am: ArrayMesh, m: Material) -> MeshInstance3D:
	var mi := MeshInstance3D.new()
	mi.mesh = am
	mi.material_override = m
	add_child(mi)
	return mi


## Build a mesh from the browser's vertex list and triangles. Normals are worked out in the browser's winding, then the
## triangles are reversed, because Godot treats clockwise as the front where three.js treats counter-clockwise.
func _build(pos: PackedVector3Array, idx: PackedInt32Array) -> ArrayMesh:
	var nrm := PackedVector3Array()
	nrm.resize(pos.size())
	for i in range(0, idx.size(), 3):
		var a := pos[idx[i]]
		var n := (pos[idx[i + 1]] - a).cross(pos[idx[i + 2]] - a)
		for k in 3:
			nrm[idx[i + k]] += n
	for i in nrm.size():
		nrm[i] = nrm[i].normalized()
	var rev := PackedInt32Array()
	rev.resize(idx.size())
	for i in range(0, idx.size(), 3):
		rev[i] = idx[i]
		rev[i + 1] = idx[i + 2]
		rev[i + 2] = idx[i + 1]
	var arr := []
	arr.resize(Mesh.ARRAY_MAX)
	arr[Mesh.ARRAY_VERTEX] = pos
	arr[Mesh.ARRAY_NORMAL] = nrm
	arr[Mesh.ARRAY_INDEX] = rev
	var am := ArrayMesh.new()
	am.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, arr)
	return am


## A hull section at z: half-width and half-height (the browser's section()).
func _sec(pts: Array, height: float, tf: float, tt: float, z: float) -> Vector2:
	var z_tip: float = pts[0][1]
	var z_last: float = pts[pts.size() - 1][1]
	var w: float = pts[pts.size() - 1][0] + SKIN
	if z > z_last:
		for i in range(1, pts.size()):
			var a: Array = pts[i - 1]
			var b: Array = pts[i]
			if z <= a[1] and z >= b[1]:
				var t: float = (a[1] - z) / float(a[1] - b[1])
				w = a[0] + (b[0] - a[0]) * t + SKIN * minf(1.0, (z_tip - z) / 10.0)
				break
	var t2 := clampf((z - tf) / (tt - tf), 0.0, 1.0)
	return Vector2(maxf(0.0, w), height * 0.85 * (1.0 - 0.85 * t2))


func main_sec(z: float) -> Vector2:
	return _sec(MAIN, 14, 20, 130, z)


func _ring(a: float, w: float, h: float, flare: float, wo: float) -> Vector2:
	var c := cos(a)
	var s := sin(a)
	return Vector2(c * w + signf(c) * (flare * wo + (wo - w)) * pow(1.0 - absf(s), EDGE_K), s * h)


func _dagger(pts: Array, height: float, tf: float, tt: float, flare: float, hole: Vector2) -> ArrayMesh:
	var N := 128
	var S := 120
	var z_tip: float = pts[0][1]
	var z_end: float = pts[pts.size() - 1][1] - SKIN
	var pos := PackedVector3Array()
	var idx := PackedInt32Array()
	var zs: Array = []
	for j in S + 1:
		var z := z_tip - (z_tip - z_end) * j / float(S)
		if z > z_end + ROUND_L:
			zs.append(z)
	for j in 11:
		zs.append(z_end + ROUND_L * (1.0 - j / 10.0))
	var D := minf(3.0, 0.35 * _sec(pts, height, tf, tt, z_end).y)
	for z in zs:
		var k := _sec(pts, height, tf, tt, z)
		var u := maxf(0.0, 1.0 - (z - z_end) / ROUND_L)
		var d := D * (1.0 - sqrt(1.0 - u * u))
		for i in N:
			var r := _ring(i / float(N) * TAU, k.x - d, k.y - d, flare, k.x)
			pos.append(Vector3(r.x, r.y, z))
	for j in zs.size() - 1:
		for i in N:
			var a := j * N + i
			var b := j * N + (i + 1) % N
			idx.append_array([a, a + N, b, b, a + N, b + N])
	var ci := pos.size()
	var ke := _sec(pts, height, tf, tt, z_end)
	for i in N:
		var r := _ring(i / float(N) * TAU, ke.x - D, ke.y - D, flare, ke.x)
		pos.append(Vector3(r.x, r.y, z_end))
	if hole != Vector2.ZERO:
		for i in N:
			var a := i / float(N) * TAU
			pos.append(Vector3(cos(a) * hole.x, sin(a) * hole.y, z_end))
		for i in N:
			var o := ci + i
			var o1 := ci + (i + 1) % N
			var n := ci + N + i
			var n1 := ci + N + (i + 1) % N
			idx.append_array([n, o1, o, n, n1, o1])
	else:
		var c := pos.size()
		pos.append(Vector3(0, 0, z_end))
		for i in N:
			idx.append_array([c, ci + (i + 1) % N, ci + i])
	return _build(pos, idx)


# ── the docking bay (Eric 10-23) ──
func _pw(v: float, e: float) -> float:
	return signf(v) * pow(absf(v), e)


func _inside_outer(x: float, y: float) -> bool:
	var s := (y - BAY.cy) / BAY.b
	if absf(s) > 1.0:
		return false
	var p: float = BAY.pOut if s < 0 else 2.0
	return absf(x) <= BAY.a * pow(1.0 - pow(absf(s), p), 1.0 / p)


func _bay_inner(t: float) -> Vector2:
	var c := cos(t)
	var s := sin(t)
	var p: float = BAY.pTop if s >= 0 else BAY.pBot
	var r := 1.0 / pow(pow(absf(c) / BAY.hw, p) + pow(absf(s) / BAY.hh, p), 1.0 / p)
	return Vector2(c * r, BAY.ocy + s * r)


func _bay_outer(t: float) -> Vector2:
	var c := cos(t)
	var s := sin(t)
	var lo := 0.0
	var hi := 60.0
	for k in 40:
		var m := (lo + hi) / 2.0
		if _inside_outer(c * m, BAY.ocy + s * m):
			lo = m
		else:
			hi = m
	return Vector2(c * lo, BAY.ocy + s * lo)


func _rake(z: float, y: float, x := 0.0) -> float:
	var zm: float = (BAY.zf + BAY.za) / 2.0
	var half: float = (BAY.zf - BAY.za) / 2.0
	return z - ((z - zm) / half) * (BAY.rake * (BAY.cy + BAY.b - y) + BAY.sweep * pow(x / BAY.a, 2))


func _bay() -> void:
	var N := 96
	var inner: Array = []
	var outer: Array = []
	for i in N:
		inner.append(_bay_inner(i / float(N) * TAU))
		outer.append(_bay_outer(i / float(N) * TAU))
	var rings: Array = []
	var add_ring := func(pts: Array, z: float):
		var r: Array = []
		for p in pts:
			r.append(Vector3(p.x, p.y, _rake(z, p.y, p.x)))
		rings.append(r)
	var lip := func(u: float, z_end: float, dir: float):
		var k := sin(u * PI / 2)
		var pts: Array = []
		for i in N:
			pts.append(inner[i] + (outer[i] - inner[i]) * k)
		add_ring.call(pts, z_end - dir * BAY.lip * (1.0 - cos(u * PI / 2)))
	var LS := 10
	var OS := 40
	for j in LS + 1:
		lip.call(j / float(LS), BAY.zf, 1.0)
	for j in range(1, OS):
		add_ring.call(outer, BAY.zf - BAY.lip - (BAY.zf - BAY.za - 2 * BAY.lip) * j / float(OS))
	for j in range(LS, -1, -1):
		lip.call(j / float(LS), BAY.za, -1.0)
	for j in range(1, OS):
		add_ring.call(inner, BAY.za + (BAY.zf - BAY.za) * j / float(OS))
	var pos := PackedVector3Array()
	var idx := PackedInt32Array()
	for r in rings:
		for v in r:
			pos.append(v)
	var R := rings.size()
	for j in R:
		var k := (j + 1) % R
		for i in N:
			var a := j * N + i
			var b := j * N + (i + 1) % N
			var c := k * N + i
			var d := k * N + (i + 1) % N
			idx.append_array([a, c, b, b, c, d])
	_mesh(_build(pos, idx), hull_mat)
	# the deck: a level landing pad the full length of the tunnel
	var deck_y: float = BAY.ocy - BAY.hh * 0.75
	var dw: float = BAY.hw * pow(1.0 - pow(0.75, BAY.pBot), 1.0 / BAY.pBot) - 0.05
	var dz0 := _rake(BAY.zf, deck_y, dw) - 1.0
	var dz1 := _rake(BAY.za, deck_y, dw) + 1.0
	var deck := MeshInstance3D.new()
	var pm := PlaneMesh.new()
	pm.size = Vector2(2 * dw, dz0 - dz1)
	deck.mesh = pm
	deck.material_override = _mat(Color("3a3f47"), 0.8, 0.2)
	deck.position = Vector3(0, deck_y, (dz0 + dz1) / 2.0)
	add_child(deck)
	# ceiling lights on the hull's underside, and a blue strip along each side of the deck
	var lm := _glow(Color("dfe8ff"))
	for x in [-8.0, 8.0]:
		for i in 22:
			var z: float = BAY.za + 14 + i * (BAY.zf - BAY.za - 28) / 21.0
			var q := MeshInstance3D.new()
			var qm := PlaneMesh.new()
			qm.size = Vector2(1.6, 3.2)
			q.mesh = qm
			q.material_override = lm
			q.position = Vector3(x, -main_sec(z).y - 0.3, z)
			add_child(q)
	for sd in [-1.0, 1.0]:
		var s := MeshInstance3D.new()
		var bm := BoxMesh.new()
		bm.size = Vector3(0.05, 0.5, dz0 - dz1 - 10)
		s.mesh = bm
		s.material_override = _glow(Color("7fb0ff"))
		s.position = Vector3(sd * (dw - 0.3), deck_y + 0.6, (dz0 + dz1) / 2.0)
		add_child(s)
	for z in [0.0, -46.0, -92.0]:     # work-lights inside the hangar
		var l := OmniLight3D.new()
		l.light_color = Color("bfd4ff")
		l.light_energy = 1.2
		l.omni_range = 40
		l.position = Vector3(0, -main_sec(0).y - 4, z)
		add_child(l)


# ── engine: an oval exhaust set into the stern ──
func _exhaust() -> void:
	var OV := 0.42
	var zs: float = MAIN[MAIN.size() - 1][1] - SKIN
	var well := MeshInstance3D.new()
	var cm := CylinderMesh.new()
	cm.top_radius = 12
	cm.bottom_radius = 12
	cm.height = 6
	cm.cap_top = false
	cm.cap_bottom = false
	well.mesh = cm
	well.material_override = _mat(Color("23272d"), 0.6, 0.4)
	well.rotation.x = PI / 2
	well.scale = Vector3(1, 1, OV)
	well.position.z = zs + 3
	add_child(well)
	var core := MeshInstance3D.new()
	var qm := QuadMesh.new()
	qm.size = Vector2(24, 24 * OV)
	core.mesh = qm
	core.material_override = _glow(Color("ffb060"))
	core.position.z = zs + 5.8
	core.rotation.y = PI
	add_child(core)
	var el := OmniLight3D.new()
	el.light_color = Color("ff9c4a")
	el.light_energy = 2.0
	el.omni_range = 120
	el.position.z = -160
	add_child(el)


# ── THE TOWER (the bridge): a long pod under the bow, level, sinking into the hull aft ──
func _tower() -> void:
	var T := {"zc": 88.0, "L": 11.3, "W": 3.7, "H": 2.0, "p": 2.5, "gap": 1.5}
	var yc: float = -main_sec(T.zc - T.L).y + T.H - 0.5
	var half_w := func(z: float) -> float:
		var u := minf(1.0, absf(z - T.zc) / T.L)
		return T.W * pow(1.0 - pow(u, T.p), 1.0 / T.p)
	var N := 40
	var zs: Array = []
	for j in 49:
		var t := -1.0 + 2.0 * j / 48.0
		zs.append(T.zc + T.L * signf(t) * pow(absf(t), 0.8))
	var pos := PackedVector3Array()
	var idx := PackedInt32Array()
	for z in zs:
		var w: float = half_w.call(z)
		var h: float = T.H * w / T.W
		for i in N:
			var a := i / float(N) * TAU
			pos.append(Vector3(cos(a) * w, yc + sin(a) * h, z))
	for j in zs.size() - 1:
		for i in N:
			var a := j * N + i
			var b := j * N + (i + 1) % N
			idx.append_array([a, b, a + N, b, b + N, a + N])
	_mesh(_build(pos, idx), hull_mat)
	# windows all the way round except the aft end; a lower row tilted to look down on the approach
	var wm := _glow(Color("ffd9a0"))
	var outline: Array = []
	for i in 721:
		var th := i / 720.0 * TAU
		outline.append(Vector2(T.W * _pw(cos(th), 2.0 / T.p), T.zc + T.L * _pw(sin(th), 2.0 / T.p)))
	for r in [[-0.2, 1.0, 1.2, 0.0], [-1.15, 0.9, 0.7, 0.55]]:
		var k := sqrt(maxf(0.0, 1.0 - pow(r[0] / T.H, 2)))
		var run := 0.0
		for i in range(1, outline.size()):
			var p0: Vector2 = outline[i - 1]
			var p1: Vector2 = outline[i]
			run += p0.distance_to(p1)
			if run < T.gap:
				continue
			run = 0.0
			if p1.y < T.zc - T.L * 0.55:
				continue
			var yaw := atan2(p1.x - p0.x, p1.y - p0.y) + PI / 2
			var q := MeshInstance3D.new()
			var qm := QuadMesh.new()
			qm.size = Vector2(r[1], r[2])
			q.mesh = qm
			q.material_override = wm
			q.basis = Basis(Vector3.UP, yaw) * Basis(Vector3.RIGHT, r[3])
			q.position = Vector3(p1.x * k + sin(yaw) * 0.12, yc + r[0], p1.y + cos(yaw) * 0.12)
			add_child(q)


# ── the name on both sides of the spine, starting 40 m aft of amidships (rule 9 / Eric 10-11) ──
func _name() -> void:
	for sd in [-1.0, 1.0]:
		var l := Label3D.new()
		l.text = "WSC  ALEXANDER  VON  HUMBOLDT"
		l.font_size = 160
		l.pixel_size = 3.4 / 160.0
		l.modulate = Color("eef1f5")
		l.horizontal_alignment = HORIZONTAL_ALIGNMENT_LEFT if sd > 0 else HORIZONTAL_ALIGNMENT_RIGHT
		l.rotation.y = sd * PI / 2
		l.position = Vector3(sd * 12.9, RIDGE_Y + 2, -40)
		add_child(l)


# ── the original hangar door (10-11), now in the bay's ceiling ──
func _door() -> void:
	var D := {"x": 11.0, "z0": -58.0, "z1": -8.0}
	var belly := func(x: float, z: float) -> float:
		var k := main_sec(z)
		return -k.y * sqrt(maxf(0.0, 1.0 - pow(x / k.x, 2)))
	var patch := func(x0: float, x1: float, z0: float, z1: float, off: float, m: Material):
		var nx := 12
		var nz := 20
		var pos := PackedVector3Array()
		var idx := PackedInt32Array()
		for j in nz + 1:
			for i in nx + 1:
				var x := x0 + (x1 - x0) * i / float(nx)
				var z := z0 + (z1 - z0) * j / float(nz)
				pos.append(Vector3(x, belly.call(x, z) - off, z))
		for j in nz:
			for i in nx:
				var a := j * (nx + 1) + i
				idx.append_array([a, a + 1, a + nx + 1, a + 1, a + nx + 2, a + nx + 1])
		_mesh(_build(pos, idx), m)
	var door := _mat(Color("40454e"), 0.6, 0.4)
	var frame := _mat(Color("7a808b"), 0.4, 0.5)
	var seam := _glow(Color("0b0d10"))
	var F := 1.4
	patch.call(-D.x, D.x, D.z0, D.z1, 0.12, door)
	patch.call(-D.x - F, D.x + F, D.z0 - F, D.z0, 0.3, frame)
	patch.call(-D.x - F, D.x + F, D.z1, D.z1 + F, 0.3, frame)
	patch.call(-D.x - F, -D.x, D.z0, D.z1, 0.3, frame)
	patch.call(D.x, D.x + F, D.z0, D.z1, 0.3, frame)
	patch.call(-0.25, 0.25, D.z0, D.z1, 0.2, seam)
	var z: float = D.z0 + 10
	while z < D.z1 - 1:
		patch.call(-D.x, -0.25, z - 0.15, z + 0.15, 0.18, seam)
		patch.call(0.25, D.x, z - 0.15, z + 0.15, 0.18, seam)
		z += 10
	var lamp := _glow(Color("ffb347"))
	for c in [[-1, D.z0 - F / 2], [1, D.z0 - F / 2], [-1, D.z1 + F / 2], [1, D.z1 + F / 2]]:
		var x: float = c[0] * (D.x + F / 2)
		var m := MeshInstance3D.new()
		var sm := SphereMesh.new()
		sm.radius = 0.6
		sm.height = 1.2
		m.mesh = sm
		m.material_override = lamp
		m.position = Vector3(x, belly.call(x, c[1]) - 0.5, c[1])
		add_child(m)


# ── scattered lit portholes along the flanks ──
func _portholes() -> void:
	var mm := MultiMesh.new()
	mm.transform_format = MultiMesh.TRANSFORM_3D
	var qm := QuadMesh.new()
	qm.size = Vector2(1.1, 0.55)
	mm.mesh = qm
	mm.instance_count = 420
	var rng := RandomNumberGenerator.new()
	rng.seed = 1011
	for i in 420:
		var z := -125 + rng.randf() * 215
		var side := -1.0 if rng.randf() < 0.5 else 1.0
		var y := -3 + rng.randf() * 8 * (0.4 if z > 60 else 1.0)
		var k := main_sec(z)
		var r := _ring(asin(clampf(y / k.y, -1, 1)), k.x, k.y, MAIN_FLARE, k.x)
		mm.set_instance_transform(i, Transform3D(Basis(Vector3.UP, side * PI / 2), Vector3(side * (r.x + 0.15), y, z)))
	var mi := MultiMeshInstance3D.new()
	mi.multimesh = mm
	mi.material_override = _glow(Color("ffcf8a"))
	add_child(mi)


# ── floodlights, and the guide lanes into both ends of the bay ──
func _lights() -> void:
	for f in [[0, 45, -20, 6.0, "c8d4ff"], [0, -75, 60, 3.0, "ffe0b0"], [60, 0, -60, 4.0, "c8d4ff"], [-60, 0, -60, 4.0, "c8d4ff"]]:
		var l := OmniLight3D.new()
		l.light_color = Color(f[4])
		l.light_energy = f[3]
		l.omni_range = 260
		l.position = Vector3(f[0], f[1], f[2])
		add_child(l)
	for lane in [[DOCK.approach, DOCK.mouth], [DOCK.aftApproach, DOCK.aftMouth]]:
		for i in 16:
			var t := i / 15.0
			var p: Vector3 = lane[0].lerp(lane[1], t)
			for s in [-1.0, 1.0]:
				var m := MeshInstance3D.new()
				var sm := SphereMesh.new()
				sm.radius = 0.9
				sm.height = 1.8
				m.mesh = sm
				m.material_override = _glow(Color("7fe0a8"))
				m.position = Vector3(s * 9, p.y - 4, p.z)
				add_child(m)
				guide.append([m, t])
