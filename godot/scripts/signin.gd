extends Control
## Sign-in: phone or email, then a 6-digit code. No passwords (rule 3).

var channel := "email"
var countries: Array = []
var box: VBoxContainer
var region: OptionButton
var address: LineEdit
var code: LineEdit
var send: Button
var verify: Button


func _ready() -> void:
	box = Ui.screen(self)
	box.add_child(Ui.label("Sign in", 44, Ui.GOLD))
	var pick := Ui.picker()
	pick.add_item("Email")
	pick.add_item("Phone (text message)")
	pick.item_selected.connect(_on_channel)
	box.add_child(pick)
	region = Ui.picker()
	region.visible = false
	box.add_child(region)
	address = Ui.field("Email address")
	box.add_child(address)
	send = Ui.button("Send my code")
	send.pressed.connect(_send)
	box.add_child(send)
	code = Ui.field("6-digit code")
	code.max_length = 6
	code.visible = false
	box.add_child(code)
	verify = Ui.button("Sign in")
	verify.visible = false
	verify.pressed.connect(_verify)
	box.add_child(verify)
	var r := await Api.call_api("GET", "/api/dfg/signup-options", {}, false)
	if r.ok:
		countries = r.data.get("countries", [])
		for c in countries:
			region.add_item("%s +%s" % [c.iso, str(c.dial).trim_prefix("+")])


func _on_channel(i: int) -> void:
	channel = "email" if i == 0 else "sms"
	region.visible = channel == "sms"
	address.placeholder_text = "Email address" if channel == "email" else "Phone number"


func _region() -> String:
	if channel != "sms" or region.selected < 0 or countries.is_empty():
		return ""
	return countries[region.selected].iso


func _send() -> void:
	if address.text.strip_edges() == "":
		Ui.error(self, "Enter your " + ("email address." if channel == "email" else "phone number."))
		return
	send.disabled = true
	var r := await Api.call_api("POST", "/api/dfg/auth/start",
		{"channel": channel, "address": address.text.strip_edges(), "region": _region()}, false)
	send.disabled = false
	if not r.ok:
		Ui.error(self, r.error)
		return
	code.visible = true
	verify.visible = true
	send.text = "Send a new code"


func _verify() -> void:
	verify.disabled = true
	var r := await Api.call_api("POST", "/api/dfg/auth/verify", {"channel": channel,
		"address": address.text.strip_edges(), "code": code.text.strip_edges(), "region": _region()}, false)
	verify.disabled = false
	if not r.ok:
		Ui.error(self, r.error)
		return
	Session.signed_in(r.data.token, r.data.me)
	Session.call_on_enter = "wake"
	get_tree().change_scene_to_file(Session.next_scene())
