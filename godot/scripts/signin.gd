extends Control
## Sign-in (ported from the browser's showSignIn): your language, then phone or email, then a 6-digit code. No passwords
## (rule 3). The country list reads like the language list (flag, name, +code) and starts on the phone's own country, so
## nobody has to know their national prefix (Eric 11-02).

var channel := "email"
var countries: Array = []      # sorted by name, as shown
var langs: Array = []
var box: VBoxContainer
var lang: WheelPicker
var seg: HBoxContainer
var addr_label: Label
var region: WheelPicker
var address: LineEdit
var hint: Label
var code: LineEdit
var send: Button
var verify: Button
var keep: CheckBox
var status: Label
var retry: Button
var join: CheckBox            # offers to add a new sign-in to the SDID this phone knows (Eric 11-03)
var adding := false           # adding a phone or email to the signed-in SDID, not signing in


func _ready() -> void:
	box = Ui.screen(self)
	adding = Session.adding_contact
	if adding:
		box.add_child(Ui.label("Add a phone or email", 40, Ui.GOLD))
		box.add_child(Ui.label("A code proves it's yours. Then either one signs you in to your SDID.", 22, Ui.MUTED))
	else:
		box.add_child(Ui.label("Sign in", 44, Ui.GOLD))
		box.add_child(Ui.label("No passwords. A 6-digit code to your phone or email.", 22, Ui.MUTED))
	var lang_label := Ui.label("Your language", 22, Ui.MUTED)
	box.add_child(lang_label)
	lang = Ui.picker("Your language")
	lang.item_selected.connect(func(i):
		Session.set_pref("lang", str(langs[i].code))
		Ui.set_language(str(langs[i].code))
		get_tree().reload_current_scene())   # the whole page switches to the language at once (Eric 11-02)
	box.add_child(lang)
	lang_label.visible = not adding
	lang.visible = not adding
	seg = HBoxContainer.new()
	seg.add_theme_constant_override("separation", 12)
	for c in [["sms", "📱 Phone"], ["email", "✉️ Email"]]:
		var b := Ui.button(c[1], false)
		b.size_flags_horizontal = Control.SIZE_EXPAND_FILL
		b.set_meta("c", c[0])
		b.pressed.connect(func():
			if channel != c[0]:
				address.text = ""      # an email doesn't belong in the phone box, or the other way round
			_on_channel(c[0]))
		seg.add_child(b)
	box.add_child(seg)
	addr_label = Ui.label("", 22, Ui.MUTED)
	box.add_child(addr_label)
	region = Ui.picker("Your country")
	region.item_selected.connect(func(i): Session.set_pref("region", str(countries[i].iso)))
	box.add_child(region)
	address = Ui.field("")
	box.add_child(address)
	hint = Ui.label("", 20, Ui.MUTED)
	box.add_child(hint)
	keep = CheckBox.new()
	keep.text = tr("Remember my email or phone on this device")
	keep.add_theme_font_size_override("font_size", 22)
	keep.toggled.connect(func(on): if not on: Session.forget())
	box.add_child(keep)
	keep.visible = not adding
	var dev := Session.device()
	join = CheckBox.new()
	join.text = tr("If this phone or email is new, add it to my account %s") % str(dev.get("sdid", "")) \
		+ ("\n" + str(dev.title) if str(dev.get("title", "")) != "" else "")
	join.add_theme_font_size_override("font_size", 22)
	join.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	join.button_pressed = true
	join.visible = not adding and str(dev.get("key", "")) != ""
	box.add_child(join)
	send = Ui.button("")
	send.pressed.connect(_send)
	box.add_child(send)
	code = Ui.field("6-digit code")
	code.max_length = 6
	code.virtual_keyboard_type = LineEdit.KEYBOARD_TYPE_NUMBER   # the number pad: iOS then offers the code from Messages or Mail (ios/plugins/otc)
	code.text_changed.connect(_on_code)
	code.visible = false
	box.add_child(code)
	verify = Ui.button("Wake up")
	verify.visible = false
	verify.pressed.connect(_verify)
	box.add_child(verify)
	var saved := Session.remembered()
	if adding:
		var have := []
		for s in Session.me.get("sign_ins", []):
			have.append(s.channel)
		saved = {"channel": "sms" if "email" in have else "email"}   # offer the kind they haven't added yet
		var back := Ui.button("Back", false)
		back.pressed.connect(func():
			Session.adding_contact = false
			get_tree().change_scene_to_file(Session.after_contact))
		box.add_child(back)
	_on_channel(str(saved.get("channel", "email")))
	if not saved.is_empty():
		keep.button_pressed = true
		address.text = str(saved.get("address", ""))
	status = Ui.label("", 22, Ui.MUTED)
	box.add_child(status)
	box.move_child(status, 2)
	retry = Ui.button("Try again", false)
	retry.visible = false
	retry.pressed.connect(_load_lists)
	box.add_child(retry)
	box.move_child(retry, 3)
	var kept := Session.cached_options()      # lists kept on this phone: the screen fills at once
	if not kept.is_empty():
		_fill(kept)
	_load_lists()


## Fetch the lists (the server can take a while to wake); say so while waiting, and offer a retry if it doesn't answer.
func _load_lists() -> void:
	retry.visible = false
	if langs.is_empty():
		status.text = tr("Contacting the Starship…")
	var r := await Api.call_api("GET", "/api/dfg/signup-options", {}, false, 45.0)
	if r.ok:
		Session.cache_options(r.data)
		status.text = ""
		if langs.is_empty():
			_fill(r.data)
	elif langs.is_empty():
		status.text = tr("The Starship isn't answering. Check your connection, then try again.")
		retry.visible = true


func _fill(d: Dictionary) -> void:
	_fill_languages(d.get("languages", []))
	_fill_countries(d.get("countries", []), str(Session.remembered().get("region", "")))


func _fill_languages(list: Array) -> void:
	langs = list
	var want := Session.pref("lang", OS.get_locale_language())   # last choice, else the phone's own language
	var pick := -1
	for i in langs.size():
		var l: Dictionary = langs[i]
		var name := "%s %s" % [l.get("flag", ""), l.get("native", l.name)]
		if l.get("native", "") != l.get("name", ""):
			name += " · " + str(l.name)
		lang.add_item(name + ("" if l.supported else " · " + tr("coming soon")))
		lang.set_item_disabled(i, not l.supported)
		if l.supported and (l.code == want or (pick < 0 and l.code == "en")):
			pick = i
	if pick >= 0:
		lang.select(pick)
		Session.set_pref("lang", str(langs[pick].code))


## Flag, the country's name and its dialling code, in name order; starts on the remembered country, else the phone's own.
func _fill_countries(list: Array, saved: String) -> void:
	countries = list.duplicate()
	for c in countries:
		c["name"] = tr(TranslationServer.get_country_name(str(c.iso)))   # country names are in the translation table too
		if c.name == "":
			c.name = str(c.iso)
	countries.sort_custom(func(a, b): return str(a.name).naturalnocasecmp_to(str(b.name)) < 0)
	var want := saved if saved != "" else Session.pref("region", OS.get_locale().get_slice("_", 1).to_upper())
	if want == "":
		want = "US"
	for i in countries.size():
		var c: Dictionary = countries[i]
		region.add_item("%s %s +%d" % [_flag(str(c.iso)), c.name, int(str(c.dial).trim_prefix("+"))])
		if c.iso == want:
			region.select(i)
	if region.selected < 0 and not countries.is_empty():
		region.select(0)
	_on_channel(channel)


func _flag(iso: String) -> String:
	if iso.length() != 2:
		return ""
	return String.chr(0x1F1A5 + iso.unicode_at(0)) + String.chr(0x1F1A5 + iso.unicode_at(1))


func _on_channel(c: String) -> void:
	channel = c
	var ph := channel == "sms"
	for b in seg.get_children():
		var on: bool = b.get_meta("c") == channel
		var s := StyleBoxFlat.new()
		s.bg_color = Ui.GOLD if on else Ui.PANEL
		s.border_color = Ui.GOLD
		s.set_border_width_all(2)
		s.set_corner_radius_all(14)
		for st in ["normal", "hover", "pressed", "focus"]:
			b.add_theme_stylebox_override(st, s)
		for k in ["font_color", "font_hover_color", "font_pressed_color", "font_focus_color"]:
			b.add_theme_color_override(k, Ui.BG if on else Ui.GOLD)
	addr_label.text = tr("Mobile number") if ph else tr("Email address")
	region.visible = ph
	hint.visible = ph
	var dial := 1
	if region.selected >= 0 and not countries.is_empty():
		dial = int(str(countries[region.selected].dial).trim_prefix("+"))
	hint.text = tr("Type it the way it's saved in your phone. Spaces, dashes or a leading %s are all fine.") % ("1" if dial == 1 else "0")
	address.placeholder_text = "5745550123" if ph else "you@example.com"
	address.virtual_keyboard_type = LineEdit.KEYBOARD_TYPE_PHONE if ph else LineEdit.KEYBOARD_TYPE_EMAIL_ADDRESS
	send.text = tr("Text me a code") if ph else tr("Email me a code")


func _region() -> String:
	if channel != "sms" or region.selected < 0 or countries.is_empty():
		return ""
	return countries[region.selected].iso


## Keep only the digits (a pasted "123 456" or "Your code is 123456" still works); once all 6 are in, the keypad goes away.
func _on_code(t: String) -> void:
	var digits := ""
	for ch in t:
		if ch >= "0" and ch <= "9":
			digits += ch
	digits = digits.left(6)
	if digits != t:
		code.text = digits
		code.caret_column = digits.length()
	if digits.length() == 6:
		_hide_keypad()


func _hide_keypad() -> void:
	var f := get_viewport().gui_get_focus_owner()
	if f:
		f.release_focus()
	DisplayServer.virtual_keyboard_hide()


## A tap anywhere outside the box being typed in puts the keypad away (Eric 11-03).
func _input(e: InputEvent) -> void:
	if e.device == InputEvent.DEVICE_ID_EMULATION:
		return
	if (e is InputEventScreenTouch or e is InputEventMouseButton) and e.pressed:
		var f := get_viewport().gui_get_focus_owner()
		if f is LineEdit and not f.get_global_rect().has_point(e.position):
			_hide_keypad()


func _send() -> void:
	_hide_keypad()
	if address.text.strip_edges() == "":
		Ui.error(self, "Enter your email address." if channel == "email" else "Enter your mobile number.")
		return
	send.disabled = true
	send.text = tr("Sending…")
	var r := await Api.call_api("POST", "/api/dfg/me/contact/start" if adding else "/api/dfg/auth/start",
		{"channel": channel, "address": address.text.strip_edges(), "region": _region()}, adding, 45.0)
	_on_channel(channel)
	send.disabled = false
	if not r.ok:
		Ui.error(self, r.error)
		return
	code.visible = true
	verify.visible = true
	send.text = tr("Send a new code")
	code.grab_focus()


func _verify() -> void:
	_hide_keypad()
	verify.disabled = true
	if adding:
		var a := await Api.call_api("POST", "/api/dfg/me/contact/verify", {"channel": channel,
			"address": address.text.strip_edges(), "code": code.text.strip_edges(), "region": _region()}, true, 45.0)
		verify.disabled = false
		if not a.ok:
			Ui.error(self, a.error)
			return
		Session.me = a.data
		Session.adding_contact = false
		get_tree().change_scene_to_file(Session.after_contact)
		return
	var dev := Session.device()
	var r := await Api.call_api("POST", "/api/dfg/auth/verify", {"channel": channel,
		"address": address.text.strip_edges(), "code": code.text.strip_edges(), "region": _region(),
		"device_key": str(dev.get("key", "")), "link": join.visible and join.button_pressed}, false, 45.0)
	verify.disabled = false
	if not r.ok:
		Ui.error(self, r.error)
		return
	Session.set_device(str(r.data.get("device_key", "")), str(r.data.me.get("sdid", "")), str(r.data.me.get("title", "")))
	if keep.button_pressed:
		Session.remember(channel, address.text.strip_edges(), _region())
	else:
		Session.forget()
	Session.signed_in(r.data.token, r.data.me)
	var picked := Session.pref("lang", "")
	if picked != "" and not r.data.me.get("needs_setup", false) and picked != str(r.data.me.get("language", "")):
		var ch := await Api.call_api("POST", "/api/dfg/me/language", {"language": picked}, true, 45.0)
		if ch.ok:
			Session.me = ch.data          # a returning player's account follows the language picked here (Eric 11-02)
	Session.call_on_enter = "wake"
	get_tree().change_scene_to_file("res://scenes/intro.tscn")   # the intro plays at every sign-in (Eric 10-27)
