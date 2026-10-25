extends Node3D
## DEBRIS FIELDS, ported from the live browser game (static/debris-flight.js, the DEBRIS block), roll for roll: fields are
## laid out in 3 km cells around the pilot, only inside a ring's band. Each cell's fields come from the session seed (the
## server's, from POST /api/dfg/session) and the cell's coordinates, so a cell is the same if you fly away and come
## back, and the server can tell what every piece is (fieldFacts and pieceMineral are the server's own rolls, minerals.py).
## Cells are in the solar system's own axes (world metres); rocks are stored relative to their field's centre, so only
## small numbers reach the GPU. Pieces wear NASA's Bennu (assets/asteroids/bennu.glb) instead of the browser's
## icosahedron; what a piece IS (its size, volume and mass) is still the browser's icosahedron numbers.

const CELL := 3000.0
const FIELD_GAP := 260.0
const SIZE_BIAS := 2.4           # >1 = many more small pieces than large ones
const FOG := 0.0009              # the browser's FogExp2: how far you can see the rocks
# Field types (Eric 10-11): n = how many pieces (range) · sc = piece scale range in metres · share = how often it occurs
const SIZE_KEYS := ["large", "medium", "small", "tiny"]
const SIZES := {
	"large": {"n": [400, 1200], "sc": [0.05, 4.0], "sight": 1100.0, "share": 0.25},
	"medium": {"n": [60, 250], "sc": [0.06, 2.0], "sight": 600.0, "share": 0.35},
	"small": {"n": [10, 20], "sc": [0.12, 1.2], "sight": 260.0, "share": 0.25},
	"tiny": {"n": [8, 20], "sc": [0.04, 0.35], "sight": 160.0, "share": 0.15}}
# Every piece is pure mineral (rules 25, 27): [key, name, density kg/m³, rarity band], in the browser's order.
const MATERIALS := [
	["basalt", "Basalt", 2900, "common"], ["iron-nickel", "Iron-nickel metal", 7900, "common"],
	["water-ice", "Water ice", 917, "common"], ["iron", "Iron ore (hematite)", 5300, "plentiful"],
	["magnetite", "Iron ore (magnetite)", 5150, "plentiful"], ["bauxite", "Aluminium ore (bauxite)", 2400, "plentiful"],
	["olivine", "Magnesium ore (olivine)", 3270, "plentiful"], ["quartz", "Quartz", 2650, "plentiful"],
	["copper", "Copper ore (chalcopyrite)", 4190, "ore"], ["ilmenite", "Titanium ore (ilmenite)", 4720, "ore"],
	["pentlandite", "Nickel ore (pentlandite)", 4800, "ore"], ["sphalerite", "Zinc ore (sphalerite)", 4050, "ore"],
	["galena", "Lead ore (galena)", 7600, "ore"], ["chromite", "Chromium ore (chromite)", 4790, "ore"],
	["pyrolusite", "Manganese ore (pyrolusite)", 5060, "ore"], ["apatite", "Phosphate (apatite)", 3190, "ore"],
	["graphite", "Graphite", 2250, "ore"], ["sulfur", "Native sulfur", 2070, "ore"],
	["spodumene", "Lithium ore (spodumene)", 3150, "ore"], ["silver", "Silver ore (acanthite)", 7300, "scarce"],
	["cobaltite", "Cobalt ore (cobaltite)", 6300, "scarce"], ["cassiterite", "Tin ore (cassiterite)", 6990, "scarce"],
	["wolframite", "Tungsten ore (wolframite)", 7300, "scarce"], ["molybdenite", "Molybdenum ore (molybdenite)", 4730, "scarce"],
	["monazite", "Rare-earth ore (monazite)", 5150, "scarce"], ["uraninite", "Uranium ore (uraninite)", 10950, "scarce"],
	["gold", "Native gold", 19300, "scarce"], ["diamond", "Industrial diamond", 3510, "scarce"],
	["platinum", "Native platinum", 21450, "rare"], ["palladium", "Native palladium", 12020, "rare"],
	["iridium", "Native iridium", 22560, "rare"], ["shocked-quartz", "Shocked quartz", 2650, "shock"],
	["impact-glass", "Impact glass", 2200, "shock"], ["maskelynite", "Maskelynite", 2550, "shock"],
	["coesite", "Coesite", 2920, "shock"], ["stishovite", "Stishovite", 4290, "shock-rare"],
	["ringwoodite", "Ringwoodite", 3900, "shock-rare"], ["lonsdaleite", "Lonsdaleite", 3520, "lonsdaleite"],
	["brownleeite", "Brownleeite", 5820, "brownleeite"]]
# Each band's share of pieces per field type, in the browser's order.
const MIX := {
	"large": [["common", 0.5515], ["plentiful", 0.25], ["ore", 0.14], ["scarce", 0.03], ["rare", 0.002], ["shock", 0.02], ["shock-rare", 0.006], ["lonsdaleite", 0.0005]],
	"medium": [["common", 0.4815], ["plentiful", 0.24], ["ore", 0.18], ["scarce", 0.06], ["rare", 0.005], ["shock", 0.025], ["shock-rare", 0.008], ["lonsdaleite", 0.0005]],
	"small": [["common", 0.402], ["plentiful", 0.22], ["ore", 0.22], ["scarce", 0.11], ["rare", 0.01], ["shock", 0.028], ["shock-rare", 0.009], ["lonsdaleite", 0.001]],
	"tiny": [["common", 0.3624], ["plentiful", 0.22], ["ore", 0.22], ["scarce", 0.14], ["rare", 0.016], ["shock", 0.03], ["shock-rare", 0.01], ["lonsdaleite", 0.0015], ["brownleeite", 0.0001]]}
const ICO_VOL := 2.536           # the browser's IcosahedronGeometry(1): volume, and half-extent of its box per axis
const ICO_HALF := 0.851
const ROCK_TONES := [Color("8a817a"), Color("6f6a66"), Color("9c8f80"), Color("7a6a5c"), Color("5d5a58"), Color("8b7765")]

const Solar := preload("res://scripts/solar.gd")
var HIDDEN := Transform3D(Basis.from_scale(Vector3.ZERO), Vector3.ZERO)   # a piece that's been taken

var seed_n := 0                  # the session seed (unsigned 32-bit)
var sol: Node3D
var fields: Array = []           # fields in the cells around the pilot right now
var cells := {}                  # "i,j,k" -> {fields, dust}
var memory := {}                 # field id -> {known, cleared}
var band_mats := {}
var rock_mesh: Mesh
var rock_fix: Transform3D        # centres Bennu and sizes it like the browser's icosahedron
var rock_mat: ShaderMaterial
var dust_mat: StandardMaterial3D
var w2l: Basis


# ── the browser's random numbers, bit for bit (mulberry32, FNV-1a, Math.imul) ──
static func imul(a: int, b: int) -> int:
	a &= 0xFFFFFFFF
	b &= 0xFFFFFFFF
	var al := a & 0xFFFF
	var ah := a >> 16
	return ((((ah * (b & 0xFFFF)) + (al * (b >> 16))) << 16) + al * (b & 0xFFFF)) & 0xFFFFFFFF


class Rng extends RefCounted:
	var a := 0
	func _init(s: int) -> void:
		a = s & 0xFFFFFFFF
	func next() -> float:
		a = (a + 0x6D2B79F5) & 0xFFFFFFFF
		var t := a
		t = Rng.mul(t ^ (t >> 15), t | 1)
		t = t ^ ((t + Rng.mul(t ^ (t >> 7), t | 61)) & 0xFFFFFFFF)
		return float((t ^ (t >> 14)) & 0xFFFFFFFF) / 4294967296.0
	static func mul(x: int, y: int) -> int:
		x &= 0xFFFFFFFF
		y &= 0xFFFFFFFF
		return (((((x >> 16) * (y & 0xFFFF)) + ((x & 0xFFFF) * (y >> 16))) << 16) + (x & 0xFFFF) * (y & 0xFFFF)) & 0xFFFFFFFF


static func fnv1a(t: String) -> int:
	var h := 0x811C9DC5
	for i in t.length():
		h = imul(h ^ t.unicode_at(i), 0x01000193)
	return h


func field_facts(id: String) -> Array:
	var r := Rng.new(fnv1a("%d|%s|size" % [seed_n, id]))
	var v := r.next()
	var size := "tiny"
	for k in SIZE_KEYS:
		if v < SIZES[k].share:
			size = k
			break
		v -= SIZES[k].share
	var S: Dictionary = SIZES[size]
	return [size, S.n[0] + floori(r.next() * (S.n[1] - S.n[0] + 1))]


func piece_mineral(id: String, i: int, size: String) -> Array:
	var r := Rng.new(fnv1a("%d|%s|%d" % [seed_n, id, i]))
	var u := r.next()
	var acc := 0.0
	var band := "common"
	for b in MIX[size]:
		acc += b[1]
		if u < acc:
			band = b[0]
			break
	var ms: Array = band_mats[band]
	return ms[floori(r.next() * ms.size())]


static func field_rad(n: int, sc: Array) -> float:
	return roundf(3.0 * pow(n, 1.0 / 3.0) + 2.5 * sc[1])


func cell_seed(i: int, j: int, k: int) -> int:
	return (seed_n ^ imul(i, 73856093) ^ imul(j, 19349663) ^ imul(k, 83492791)) & 0xFFFFFFFF


static func label_of(f: Dictionary) -> String:
	return {"large": "Large field", "medium": "Field", "small": "Small field", "tiny": "Tiny field"}[f.size]


## Where the autopilot parks: in front of the field, outside it, so the whole field stays in view while you work it.
static func stand_off(f: Dictionary) -> float:
	return f.rad * 1.4 + {"tiny": 5.0, "small": 6.0, "medium": 15.0, "large": 30.0}[f.size]


func setup(the_sol: Node3D, s: int) -> void:
	sol = the_sol
	for m in MATERIALS:
		if not band_mats.has(m[3]):
			band_mats[m[3]] = []
		band_mats[m[3]].append(m)
	w2l = sol._w2l()
	# NASA's Bennu as the look of every piece, sized so its box matches the browser's icosahedron
	var bennu: Node = load("res://assets/asteroids/bennu.glb").instantiate()
	var mi: MeshInstance3D = bennu.find_children("*", "MeshInstance3D", true, false)[0]
	rock_mesh = mi.mesh
	var box := rock_mesh.get_aabb()
	var k := ICO_HALF / (maxf(box.size.x, maxf(box.size.y, box.size.z)) / 2.0)
	rock_fix = Transform3D(Basis.from_scale(Vector3.ONE * k), -box.get_center() * k)
	var tex: Texture2D = null
	var m0 := mi.get_active_material(0)
	if m0 is StandardMaterial3D:
		tex = (m0 as StandardMaterial3D).albedo_texture
	bennu.free()
	var sh := Shader.new()
	sh.code = """
shader_type spatial;
render_mode cull_back;
uniform sampler2D tex : source_color, filter_linear_mipmap;
uniform float fog_density = 0.0009;
void fragment() {
	ALBEDO = texture(tex, UV).rgb * COLOR.rgb;
	ROUGHNESS = 0.95;
	METALLIC = 0.08;
	float d = length(VERTEX) * fog_density;
	FOG = vec4(0.0, 0.0, 0.0, 1.0 - exp(-d * d));   // the browser's FogExp2: rocks fade into the dark with distance
}
"""
	rock_mat = ShaderMaterial.new()
	rock_mat.shader = sh
	rock_mat.set_shader_parameter("tex", tex)
	rock_mat.set_shader_parameter("fog_density", FOG)
	dust_mat = StandardMaterial3D.new()
	dust_mat.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	dust_mat.use_point_size = true
	dust_mat.point_size = 2.4
	dust_mat.albedo_color = Color(Color("9a8f84"), 0.6)
	dust_mat.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
	reset(s)


## A new universe from a new seed (the server's, once signed in): lay it out afresh.
func reset(s: int) -> void:
	for key in cells.keys():
		_unload_cell(key)
	memory.clear()
	seed_n = s & 0xFFFFFFFF


func _make_field(id: String, ring: Dictionary, center_w: Array, size: String, n: int, r: Rng) -> Dictionary:
	var S: Dictionary = SIZES[size]
	var rad := field_rad(n, S.sc)
	var mem: Dictionary = memory.get(id, {})
	var mm := MultiMesh.new()
	mm.transform_format = MultiMesh.TRANSFORM_3D
	mm.use_colors = true
	mm.mesh = rock_mesh
	mm.instance_count = n
	var f := {"id": id, "ring": ring, "size": size, "center_w": center_w, "center": sol.to_local_d(center_w), "rad": rad,
		"sight": S.sight, "count": n, "pieces": [], "shown": false, "known": mem.get("known", false),
		"cleared": mem.get("cleared", false)}
	for i in n:
		var d := pow(r.next(), 0.6) * rad
		var v := Vector3(r.next() - 0.5, (r.next() - 0.5) * 0.6, r.next() - 0.5).normalized() * d
		var ex := r.next() * 6.3
		var ey := r.next() * 6.3
		var ez := r.next() * 6.3
		var rotb := Basis(Vector3.RIGHT, ex) * Basis(Vector3.UP, ey) * Basis(Vector3.BACK, ez)   # three.js Euler XYZ
		var s: float = S.sc[0] * pow(S.sc[1] / S.sc[0], pow(r.next(), SIZE_BIAS))   # log-spread sizes, weighted to small
		var sc := Vector3(s * (0.7 + r.next() * 0.6), s * (0.7 + r.next() * 0.6), s * (0.7 + r.next() * 0.6))
		var xf := Transform3D(rotb * Basis.from_scale(sc), v)
		var taken: bool = mem.get("taken", []).size() > i and mem.taken[i]
		mm.set_instance_transform(i, HIDDEN if taken else xf * rock_fix)
		var mat: Array = piece_mineral(id, i, size)
		var dims := [2 * ICO_HALF * sc.x, 2 * ICO_HALF * sc.y, 2 * ICO_HALF * sc.z]
		dims.sort()
		dims.reverse()
		var vol := ICO_VOL * sc.x * sc.y * sc.z
		f.pieces.append({"mat": mat[0], "dims": dims, "vol": vol, "box": dims[0] * dims[1] * dims[2], "mass": vol * mat[2], "taken": taken,
			"fid": id, "idx": i, "xf": xf})
		mm.set_instance_color(i, ROCK_TONES[floori(r.next() * ROCK_TONES.size())])
	var node := MultiMeshInstance3D.new()
	node.multimesh = mm
	node.material_override = rock_mat
	node.basis = w2l
	node.visible = false
	node.extra_cull_margin = rad
	add_child(node)
	f["node"] = node
	return f


func _load_cell(i: int, j: int, k: int) -> void:
	var key := "%d,%d,%d" % [i, j, k]
	if cells.has(key):
		return
	var cell := {"fields": [], "dust": null}
	cells[key] = cell
	var o := [i * CELL, j * CELL, k * CELL]
	var ring = sol.ring_of(Solar.add(o, [CELL / 2, CELL / 2, CELL / 2]))
	if ring == null:
		return
	var r := Rng.new(cell_seed(i, j, k))
	# beginners first (Eric 10-11): plenty of large, easy-to-hear fields of common material
	var u := r.next()
	var n := 0 if u < 0.3 else (1 if u < 0.8 else 2)
	for fi in n:
		r.next()
		var facts := field_facts(key + "#" + str(fi))       # size and piece count: the server's roll
		var S: Dictionary = SIZES[facts[0]]
		var m := field_rad(S.n[1], S.sc)                       # room for the biggest it could be
		var c := [o[0] + m + r.next() * (CELL - 2 * m), o[1] + m + r.next() * (CELL - 2 * m), o[2] + m + r.next() * (CELL - 2 * m)]
		if sol.ring_of(c) == null:
			continue
		var clash := false
		for g in cell.fields:
			if Solar.length(Solar.sub(g.center_w, c)) < g.rad + m + FIELD_GAP:
				clash = true
		if clash:
			continue
		var f := _make_field(key + "#" + str(fi), ring, c, facts[0], facts[1], r)
		cell.fields.append(f)
		fields.append(f)
	# a thin haze of dust, so the band reads as a place even between fields
	var pts := PackedVector3Array()
	for d in 140:
		pts.append(Vector3(r.next() * CELL, r.next() * CELL, r.next() * CELL))
	var am := ArrayMesh.new()
	var arr := []
	arr.resize(Mesh.ARRAY_MAX)
	arr[Mesh.ARRAY_VERTEX] = pts
	am.add_surface_from_arrays(Mesh.PRIMITIVE_POINTS, arr)
	var dust := MeshInstance3D.new()
	dust.mesh = am
	dust.material_override = dust_mat
	dust.basis = w2l
	add_child(dust)
	cell.dust = {"node": dust, "o": sol.to_local_d(o)}


func _unload_cell(key: String) -> void:
	var cell: Dictionary = cells[key]
	cells.erase(key)
	for f in cell.fields:
		memory[f.id] = {"known": f.known, "cleared": f.cleared, "taken": f.pieces.map(func(q): return q.taken)}
		f.node.queue_free()
		for x in fields.size():
			if fields[x].id == f.id:
				fields.remove_at(x)
				break
	if cell.dust:
		cell.dust.node.queue_free()


## Cells around the pilot (me_l: the pilot in the ship's frame); also which fields are close enough to be seen.
func update_cells(me_l: Array) -> void:
	var w: Array = sol.to_world_d(me_l)
	var ci := floori(w[0] / CELL)
	var cj := floori(w[1] / CELL)
	var ck := floori(w[2] / CELL)
	for key in cells.keys():
		var p: PackedStringArray = key.split(",")
		if absi(int(p[0]) - ci) > 2 or absi(int(p[1]) - cj) > 2 or absi(int(p[2]) - ck) > 2:
			_unload_cell(key)
	for a in range(-1, 2):
		for b in range(-1, 2):
			for c in range(-1, 2):
				_load_cell(ci + a, cj + b, ck + c)
	for f in fields:     # per-field visibility by its size class; the fog then fades what is shown with distance
		f.shown = not f.cleared and Solar.length(Solar.sub(f.center, me_l)) - f.rad < f.sight
		f.node.visible = f.shown


## Draw piece i of field f at `xf` (field-local, world axes; before Bennu's own fix), or hide it.
func show_piece(f: Dictionary, i: int, xf = null) -> void:
	f.node.multimesh.set_instance_transform(i, HIDDEN if xf == null else xf * rock_fix)


func material(key: String) -> Array:
	for m in MATERIALS:
		if m[0] == key:
			return m
	return [key, key, 1.0, ""]


## Each frame: put the fields and dust where they are, relative to the floating origin.
func place(org: Array) -> void:
	for f in fields:
		if f.shown:
			f.node.position = Solar.vec(Solar.sub(f.center, org))
	for key in cells:
		var cell: Dictionary = cells[key]
		if cell.dust:
			var rel := Solar.sub(cell.dust.o, org)
			cell.dust.node.visible = Solar.length(rel) < 20000.0
			if cell.dust.node.visible:
				cell.dust.node.position = Solar.vec(rel)
