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
