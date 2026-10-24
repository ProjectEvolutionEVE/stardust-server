extends Node
## Inara's RECORDED lines (rules 14, 15: never live speech). Files come from the game server: /voice/<voice_set>/<ID>.mp3.
## An incoming call (Eric 10-20, 10-23): chime, an opener ("Is this a good moment?"), then Answer / Not now; Answer plays
## the line. Ids match static/debris-flight.js.

const OPEN := ["INARA-CALL-001", "INARA-CALL-002", "INARA-CALL-003", "INARA-CALL-004", "INARA-CALL-005"]
const OPEN_CPT := ["INARA-CALL-006", "INARA-CALL-007", "INARA-CALL-008", "INARA-CALL-009", "INARA-CALL-010"]
# Her short lines for moments, as the browser's MOMENTS (static/debris-flight.js). TWR-036 and 039 are SOURCE lines whose
# voice use Eric has not approved yet: left out of the takes.
const MOMENTS := {"bay": ["INARA-TWR-001", "INARA-TWR-002", "INARA-TWR-003"],
	"launch": ["INARA-TOWER-001", "INARA-TWR-004", "INARA-TWR-005", "INARA-TWR-006"],
	"ring0": ["INARA-RING-001", "INARA-TWR-007"], "ring1": ["INARA-RING-002", "INARA-TWR-008"],
	"ring2": ["INARA-RING-003", "INARA-TWR-009"], "ring3": ["INARA-RING-004", "INARA-TWR-010"],
	"warp0": ["INARA-RING-005"], "warp1": ["INARA-RING-006"], "warp2": ["INARA-RING-007"], "warp3": ["INARA-RING-008"],
	"drift0": ["INARA-RING-013"], "drift1": ["INARA-RING-014"], "drift2": ["INARA-RING-015"], "drift3": ["INARA-RING-016"],
	"ret": ["INARA-TOWER-002", "INARA-TWR-011", "INARA-TWR-012"], "bearing": ["INARA-TWR-013", "INARA-TWR-014"],
	"locked": ["INARA-TOWER-003", "INARA-TWR-015", "INARA-TWR-016", "INARA-TWR-017"],
	"parked": ["INARA-TWR-018", "INARA-TWR-019", "INARA-TWR-020"], "toobig": ["INARA-TOWER-004", "INARA-TWR-021"],
	"firstpiece": ["INARA-TWR-022", "INARA-TWR-023"], "cleared": ["INARA-TWR-024", "INARA-TWR-025"],
	"diamond": ["INARA-TWR-026", "INARA-TWR-027"], "full": ["INARA-TOWER-005", "INARA-TWR-028", "INARA-TWR-029"],
	"home": ["INARA-TWR-030", "INARA-TWR-031"], "arrived": ["INARA-TWR-032"], "approach": ["INARA-TOWER-006"],
	"docked": ["INARA-TOWER-007", "INARA-TWR-033", "INARA-TWR-034"], "unloaded": ["INARA-TWR-035"],
	"low65": ["INARA-TWR-037", "INARA-TWR-038"], "low50": ["INARA-TWR-040", "INARA-TWR-041"],
	"wake": ["INARA-TWR-042", "INARA-TWR-043"], "sleep": ["INARA-TWR-044", "INARA-TWR-045"],
	"pass": ["INARA-TWR-049"], "fail": ["INARA-TWR-050"], "order": ["INARA-TWR-051"], "submitted": ["INARA-TWR-053"]}
# Story beats (each heard once, after a call she asks first), as the browser's BEATS.
const BEATS := {"library": ["INARA-STORY-003", "INARA-STORY-004"], "test": ["INARA-STORY-005", "INARA-STORY-006"],
	"blueprint": ["INARA-STORY-007"], "launch": ["INARA-STORY-008", "INARA-STORY-009"],
	"ring": ["INARA-STORY-010", "INARA-STORY-011"], "piece": ["INARA-STORY-012"], "unload": ["INARA-STORY-013"],
	"diamond": ["INARA-STORY-016"]}
# Tower lines heard aboard the ship get the chime first; every other TWR, RING and TOWER line comes over the flight radio
# and gets no chime and no opener.
const ABOARD := ["INARA-TWR-042", "INARA-TWR-043", "INARA-TWR-044", "INARA-TWR-045", "INARA-TWR-049", "INARA-TWR-050",
	"INARA-TWR-051", "INARA-TWR-053"]
const WELCOME := ["INARA-WELCOME-001", "INARA-WELCOME-002", "INARA-STORY-001", "INARA-STORY-002", "INARA-WELCOME-003"]

var player: AudioStreamPlayer
var busy := false
var muted := false               # the flight's sound toggle silences her too
var last := {}                   # the take last played for each moment: never the same twice in a row


func _ready() -> void:
	player = AudioStreamPlayer.new()
	add_child(player)


## Rings, and plays `ids` only if the player answers. `beat` (a story beat) is marked heard on the server once answered.
func ring(parent: Control, ids: Array, beat := "") -> void:
	var me: Dictionary = Session.me
	if busy or muted or ids.is_empty() or str(me.get("voice_set", "")) == "":
		return
	if beat != "":
		var r := await Api.call_api("POST", "/api/dfg/voice/heard", {"beat": beat})
		if not r.ok or not r.data.get("play", false):
			return
	busy = true
	await _chime()
	await _play((OPEN_CPT if me.get("rank") == "Captain" else OPEN).pick_random())
	if await _ask(parent):
		if beat != "":
			await Api.call_api("POST", "/api/dfg/voice/heard", {"beat": beat, "accepted": true})
		for id in ids:
			await _play(id)
	busy = false


## A short line for a moment, played at once with no call (as the browser's VOICE.say); skipped while she's busy, so
## one line at a time. Lines heard aboard get the chime first; flight radio lines don't.
func say(m: String) -> void:
	if busy or muted or not MOMENTS.has(m) or str(Session.me.get("voice_set", "")) == "":
		return
	var ids: Array = MOMENTS[m]
	var c: Array = ids.filter(func(i): return i != last.get(m, "")) if ids.size() > 1 else ids
	var id: String = c.pick_random()
	last[m] = id
	busy = true
	if aboard(id):
		await _chime()
	await _play(id)
	busy = false


static func aboard(id: String) -> bool:
	return ABOARD.has(id) or not (id.begins_with("INARA-TWR-") or id.begins_with("INARA-RING-") or id.begins_with("INARA-TOWER-"))


## A story beat (as the browser's VOICE.story): she calls first and plays it only if answered; the server keeps it heard.
func story(parent: Control, beat: String) -> void:
	if BEATS.has(beat) and Session.token != "":
		ring(parent, BEATS[beat], beat)


## The sound toggle: silences her at once and keeps her quiet until it's turned back on.
func set_muted(m: bool) -> void:
	muted = m
	if m and player.playing:
		player.stop()
		player.finished.emit()     # let whatever was waiting on the line carry on


func moment(m: String) -> Array:
	return [MOMENTS[m].pick_random()] if MOMENTS.has(m) else []


func _play(id: String) -> void:
	var path := "/voice/%s/%s.mp3" % [Session.me.get("voice_set", ""), id]
	var r := await Api.get_bytes(path)
	if r.is_empty() or muted:
		return   # missing or offline: carry on silently
	var s := AudioStreamMP3.new()
	s.data = r
	player.stream = s
	player.volume_db = -1.5
	player.play()
	await player.finished


## Our own three-note rising bell, made in code (the same notes as the browser's).
func _chime() -> void:
	var rate := 22050
	var data := PackedByteArray()
	data.resize(int(rate * 0.95) * 2)
	for n in [[659.25, 0.0], [987.77, 0.14], [1318.5, 0.28]]:
		var start := int(n[1] * rate)
		for i in int(0.6 * rate):
			var t := float(i) / rate
			var v := sin(TAU * n[0] * t) * 0.18 * exp(-t * 9.0) * minf(1.0, t / 0.01)
			var k := (start + i) * 2
			var cur := data.decode_s16(k)
			data.encode_s16(k, clampi(cur + int(v * 32767), -32768, 32767))
	var w := AudioStreamWAV.new()
	w.format = AudioStreamWAV.FORMAT_16_BITS
	w.mix_rate = rate
	w.data = data
	player.stream = w
	player.play()
	await player.finished


## The call panel: Answer / Not now. No answer in 20 s ends the call quietly.
func _ask(parent: Control) -> bool:
	var panel := PanelContainer.new()
	var s := StyleBoxFlat.new()
	s.bg_color = Ui.PANEL
	s.border_color = Ui.GOLD
	s.set_border_width_all(2)
	s.set_corner_radius_all(14)
	s.set_content_margin_all(20)
	panel.add_theme_stylebox_override("panel", s)
	panel.custom_minimum_size = Vector2(560, 0)
	var center := CenterContainer.new()          # centred on the screen, whatever its size
	center.set_anchors_preset(Control.PRESET_FULL_RECT)
	center.mouse_filter = Control.MOUSE_FILTER_IGNORE
	center.add_child(panel)
	var box := VBoxContainer.new()
	box.add_theme_constant_override("separation", 14)
	panel.add_child(box)
	box.add_child(Ui.label("INARA · Incoming call", 26, Ui.GOLD))
	var row := HBoxContainer.new()
	row.add_theme_constant_override("separation", 14)
	box.add_child(row)
	var yes := Ui.button("Answer")
	var no := Ui.button("Not now", false)
	for b in [yes, no]:
		b.size_flags_horizontal = Control.SIZE_EXPAND_FILL
		row.add_child(b)
	parent.add_child(center)
	var result := {"v": null}
	yes.pressed.connect(func(): result.v = true)
	no.pressed.connect(func(): result.v = false)
	var waited := 0.0
	while result.v == null and waited < 20.0:
		await get_tree().process_frame
		waited += get_process_delta_time()
	center.queue_free()
	return result.v == true
