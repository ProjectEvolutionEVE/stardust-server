extends Node
## The sign-in token and the latest player record (GET /api/dfg/me). The token is kept in an encrypted file tied to this
## device. Before the store release this moves to the phone's own secure storage (Keychain / Keystore).

const SAVE_PATH := "user://session.dat"

var token := ""
var me: Dictionary = {}:
	set(v):
		me = v
		if str(v.get("language", "")) != "":
			Ui.set_language(str(v.language))   # everything on screen follows the player's language (Eric 11-02)


func _ready() -> void:
	if FileAccess.file_exists(SAVE_PATH):
		var f := FileAccess.open_encrypted_with_pass(SAVE_PATH, FileAccess.READ, _key())
		if f:
			token = f.get_as_text().strip_edges()


func signed_in(new_token: String, new_me: Dictionary) -> void:
	token = new_token
	me = new_me
	var f := FileAccess.open_encrypted_with_pass(SAVE_PATH, FileAccess.WRITE, _key())
	if f:
		f.store_string(token)


func clear() -> void:
	token = ""
	me = {}
	if FileAccess.file_exists(SAVE_PATH):
		DirAccess.remove_absolute(SAVE_PATH)


## Where a signed-in player goes next: setup until their name and language are chosen, then their quarters; or their
## cockpit, if they signed out there (Eric 10-24).
## The skill bonus (a fraction) for a job of this career, counted only while its uniform is worn (rule 32):
## mining collects faster, flight stretches fuel (Eric 10-26).
func skill(career: String) -> float:
	var c: Dictionary = me.get("career", {}) if me.get("career") is Dictionary else {}
	return float(c.get("skill_pct", 0.0)) / 100.0 if c.get("code") == career else 0.0


## A Science uniform with its fifth bar in gold lets the miner pick which raw material to collect (Eric 10-26).
func can_pick_material() -> bool:
	var c: Dictionary = me.get("career", {}) if me.get("career") is Dictionary else {}
	var bars: Array = c.get("bars", [])
	return c.get("code") == "science" and bars.size() >= 5 and bars[4] is Dictionary and bars[4].get("medal") == "gold"


func next_scene() -> String:
	if me.get("needs_setup", true):
		return "res://scenes/setup.tscn"
	return "res://scenes/bay.tscn" if me.get("parked") else "res://scenes/quarters.tscn"


func _key() -> String:
	var id := OS.get_unique_id()
	return "stardust:" + (id if id != "" else OS.get_name())

## What Inara rings about when the quarters open: "wake" after signing in, "welcome" after first setup.
var call_on_enter := ""


## "Remember me" (Eric 10-24): the player may keep their email or phone on this device, encrypted with the same device key,
## so sign-in starts filled in. Off unless they tick it; unticking erases it.
const REMEMBER_PATH := "user://remember.dat"


func remembered() -> Dictionary:
	if not FileAccess.file_exists(REMEMBER_PATH):
		return {}
	var f := FileAccess.open_encrypted_with_pass(REMEMBER_PATH, FileAccess.READ, _key())
	if not f:
		return {}
	var d: Variant = JSON.parse_string(f.get_as_text())
	return d if d is Dictionary else {}


func remember(channel: String, address: String, region: String) -> void:
	var f := FileAccess.open_encrypted_with_pass(REMEMBER_PATH, FileAccess.WRITE, _key())
	if f:
		f.store_string(JSON.stringify({"channel": channel, "address": address, "region": region}))


func forget() -> void:
	if FileAccess.file_exists(REMEMBER_PATH):
		DirAccess.remove_absolute(REMEMBER_PATH)

## Which quarters tab opens next, e.g. "Desk" when coming back from the Market terminal.
var quarters_tab := ""


## The language and country picked on the sign-in screen, kept on this device (not personal: the browser keeps them too).
const PREFS_PATH := "user://prefs.cfg"


func pref(key: String, default: String = "") -> String:
	var c := ConfigFile.new()
	return str(c.get_value("signin", key, default)) if c.load(PREFS_PATH) == OK else default


func set_pref(key: String, value: String) -> void:
	var c := ConfigFile.new()
	c.load(PREFS_PATH)
	c.set_value("signin", key, value)
	c.save(PREFS_PATH)


## The sign-up lists (languages, countries, names) kept on this device, so sign-in fills at once even when the Starship is
## slow to answer; refreshed from the server each time it does.
const OPTIONS_PATH := "user://signup-options.json"


func cached_options() -> Dictionary:
	if not FileAccess.file_exists(OPTIONS_PATH):
		return {}
	var d: Variant = JSON.parse_string(FileAccess.get_file_as_string(OPTIONS_PATH))
	return d if d is Dictionary else {}


func cache_options(d: Dictionary) -> void:
	var f := FileAccess.open(OPTIONS_PATH, FileAccess.WRITE)
	if f:
		f.store_string(JSON.stringify(d))


## The lists: from this device at once if kept, else from the server (waiting up to 45 s: it can be slow to wake).
func signup_options() -> Dictionary:
	var r := await Api.call_api("GET", "/api/dfg/signup-options", {}, false, 45.0)
	if r.ok:
		cache_options(r.data)
		return r.data
	return cached_options()
