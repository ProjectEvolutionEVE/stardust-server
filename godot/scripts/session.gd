extends Node
## The sign-in token and the latest player record (GET /api/dfg/me). The token is kept in an encrypted file tied to this
## device. Before the store release this moves to the phone's own secure storage (Keychain / Keystore).

const SAVE_PATH := "user://session.dat"

var token := ""
var me: Dictionary = {}


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


## Where a signed-in player goes next: setup until their name and language are chosen, then their quarters.
func next_scene() -> String:
	return "res://scenes/setup.tscn" if me.get("needs_setup", true) else "res://scenes/quarters.tscn"


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
