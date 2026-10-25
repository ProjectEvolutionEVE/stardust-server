extends Node
## THE SCANNER'S SOUND (spec §5, Eric's design), made in code as the browser does: a soft hiss while nothing is in the
## sweep; a calm tone rises out of it, higher and clearer as you aim closer and get nearer; dead centre the static falls
## away. Silent once locked. Plus the browser's ping (bearing taken) and two-note chime (field locked).
## The browser builds it from Web Audio nodes; here the same recipe is computed sample by sample into a generator.

const RATE := 22050.0
const MASTER := 0.55

var player: AudioStreamPlayer
var pb: AudioStreamGeneratorPlayback
var hiss := PackedFloat32Array()  # 2 s of pink noise through the browser's band-pass (1400 Hz, Q 0.6), looped
var hi := 0
var hiss_g := 0.0                 # current and target levels (the browser's setTargetAtTime)
var hiss_t := 0.0
var tone_g := 0.0
var tone_t := 0.0
var freq := 200.0
var freq_t := 200.0
var ph1 := 0.0
var ph2 := 0.0
var lp := 0.0
var blips: Array = []             # [frequency, start sample, length, volume, phase]
var clock := 0
var muted := false               # the flight's sound toggle


func _ready() -> void:
	_make_hiss()
	var gen := AudioStreamGenerator.new()
	gen.mix_rate = RATE
	gen.buffer_length = 0.15
	player = AudioStreamPlayer.new()
	player.stream = gen
	player.volume_db = 0.0
	add_child(player)
	player.play()
	pb = player.get_stream_playback()


func _make_hiss() -> void:
	var n := int(RATE * 2.0)
	hiss.resize(n)
	var b0 := 0.0
	var b1 := 0.0
	var b2 := 0.0
	# RBJ band-pass, constant 0 dB peak gain, as the browser's BiquadFilter 'bandpass'
	var w0 := TAU * 1400.0 / RATE
	var alpha := sin(w0) / (2.0 * 0.6)
	var a0 := 1.0 + alpha
	var c := [alpha / a0, 0.0, -alpha / a0, -2.0 * cos(w0) / a0, (1.0 - alpha) / a0]
	var x1 := 0.0
	var x2 := 0.0
	var y1 := 0.0
	var y2 := 0.0
	for i in n:
		var w := randf() * 2.0 - 1.0
		b0 = 0.99765 * b0 + w * 0.099
		b1 = 0.963 * b1 + w * 0.2965
		b2 = 0.57 * b2 + w * 1.0526
		var x := (b0 + b1 + b2 + w * 0.1848) * 0.12
		var y: float = c[0] * x + c[1] * x1 + c[2] * x2 - c[3] * y1 - c[4] * y2
		x2 = x1
		x1 = x
		y2 = y1
		y1 = y
		hiss[i] = y


## s < 0: silent (locked, docking or docked); 0..1: how strong the return is.
func scanner(s: float) -> void:
	if s < 0.0 or muted:
		hiss_t = 0.0
		tone_t = 0.0
		return
	hiss_t = 0.05 * (1.0 - minf(1.0, s * 1.25))
	freq_t = 200.0 + 620.0 * s
	tone_t = 0.0 if s < 0.06 else 0.11 * pow(s, 1.2)


func ping(f := 660.0) -> void:
	_blip(f, 0.25, 0.12, 0.0)


func chime() -> void:
	_blip(660.0, 0.35, 0.12, 0.0)
	_blip(990.0, 0.5, 0.1, 0.14)


func _blip(f: float, dur: float, vol: float, delay: float) -> void:
	if muted:
		return
	blips.append([f, clock + int(delay * RATE), int(dur * RATE), vol, 0.0])


func _process(_dt: float) -> void:
	if pb == null:
		return
	var n := pb.get_frames_available()
	if n <= 0:
		return
	var buf := PackedVector2Array()
	buf.resize(n)
	# per-sample smoothing toward the targets (time constants 0.08 s, 0.06 s, 0.05 s, as the browser)
	var kh := 1.0 - exp(-1.0 / (0.08 * RATE))
	var kt := 1.0 - exp(-1.0 / (0.06 * RATE))
	var kf := 1.0 - exp(-1.0 / (0.05 * RATE))
	var klp := 1.0 - exp(-TAU * 1600.0 / RATE)    # the browser's low-pass on the tone
	var hn := hiss.size()
	for i in n:
		hiss_g += (hiss_t - hiss_g) * kh
		tone_g += (tone_t - tone_g) * kt
		freq += (freq_t - freq) * kf
		ph1 = fmod(ph1 + freq / RATE, 1.0)
		ph2 = fmod(ph2 + 2.0 * freq / RATE, 1.0)
		var tri := 4.0 * absf(ph2 - 0.5) - 1.0
		var tone := sin(ph1 * TAU) + 0.25 * tri
		lp += (tone - lp) * klp
		var v := hiss[hi] * hiss_g + lp * tone_g
		hi = (hi + 1) % hn
		for b in blips:
			var t: int = clock - b[1]
			if t >= 0 and t < b[2]:
				var e := minf(1.0, t / (0.01 * RATE)) * exp(-6.9 * t / float(b[2]))   # up in 10 ms, down to nothing
				b[4] += b[0] / RATE
				v += sin(b[4] * TAU) * b[3] * e
		buf[i] = Vector2.ONE * v * MASTER
		clock += 1
	pb.push_buffer(buf)
	blips = blips.filter(func(b): return clock - b[1] < b[2])
