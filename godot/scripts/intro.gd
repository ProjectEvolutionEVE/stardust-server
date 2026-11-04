extends Control
## The intro: Inara's backstory, played at every sign-in before the game (Eric 10-27).
## - A small Skip in the corner, there the whole time.
## - At the end, a Launch now button takes the player in; if they don't tap, the game goes on by itself.
## The video is the approved cut (~/Desktop/Stardust-Inara/intro-video/Stardust-Intro.mp4), converted to Ogg Theora,
## the one video format Godot plays: video/intro.ogv, 960x540.

const VIDEO := "res://video/intro.ogv"
## The same film narrated in the player's voice language where it's recorded (Eric 11-04: Arabic and Hindi first):
## video/intro-<voice set>.ogv, built by make_intro_video.py <lang>. Everyone else sees the English.
const VOICED_INTROS := ["ar", "hi"]
const AUTO_GO := 8.0        # seconds after the end before the game goes on by itself

var player: VideoStreamPlayer
var skip: Button
var launch: Button
var leaving := false


func _ready() -> void:
	var bg := ColorRect.new()
	bg.color = Color.BLACK
	bg.set_anchors_preset(Control.PRESET_FULL_RECT)
	add_child(bg)
	player = VideoStreamPlayer.new()
	var vset := str(Session.me.get("voice_set", ""))
	var own := "res://video/intro-%s.ogv" % vset
	player.stream = load(own if VOICED_INTROS.has(vset) and ResourceLoader.exists(own) else VIDEO)
	player.expand = true
	# 16:9 picture, as wide as the screen, centred (sizes from the viewport: this Control isn't laid out yet)
	var vs := get_viewport_rect().size
	var h := vs.x * 9.0 / 16.0
	player.size = Vector2(vs.x, h)
	player.position = Vector2(0, (vs.y - h) / 2.0)
	player.finished.connect(_ended)
	add_child(player)

	skip = Button.new()
	skip.text = tr("Skip ›")
	skip.flat = true
	skip.add_theme_font_size_override("font_size", 22)
	skip.add_theme_color_override("font_color", Color(1, 1, 1, 0.55))
	skip.position = Vector2(vs.x - 130, 28)
	skip.pressed.connect(_go)
	add_child(skip)

	launch = Ui.button("Launch now")
	launch.custom_minimum_size = Vector2(360, 84)
	launch.position = Vector2((vs.x - 360) / 2.0, player.position.y + h + 60)
	launch.visible = false
	launch.pressed.connect(_go)
	add_child(launch)

	if player.stream == null:   # no video in this build: straight on
		_go()
		return
	player.play()


func _ended() -> void:
	skip.visible = false
	launch.visible = true
	launch.grab_focus()
	await get_tree().create_timer(AUTO_GO).timeout
	_go()


func _go() -> void:
	if leaving:
		return
	leaving = true
	if player:
		player.stop()
	get_tree().change_scene_to_file(Session.next_scene())
