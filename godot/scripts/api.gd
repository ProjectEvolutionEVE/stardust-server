extends Node
## Every call to the game server. Each call gets its own HTTPRequest, so screens can await them one at a time:
##   var r = await Api.call_api("GET", "/api/dfg/me")   ->  {ok, code, data, error}

const BASE_URL := "https://game-server-production-9863.up.railway.app"


func call_api(method: String, path: String, body: Dictionary = {}, auth: bool = true) -> Dictionary:
	var http := HTTPRequest.new()
	http.timeout = 15.0
	add_child(http)
	var headers := PackedStringArray(["Content-Type: application/json", "Accept: application/json"])
	if auth and Session.token != "":
		headers.append("Authorization: Bearer " + Session.token)
	var m := HTTPClient.METHOD_POST if method == "POST" else HTTPClient.METHOD_GET
	var err := http.request(BASE_URL + path, headers, m, JSON.stringify(body) if m == HTTPClient.METHOD_POST else "")
	if err != OK:
		http.queue_free()
		return {"ok": false, "code": 0, "data": {}, "error": "Couldn't start the request. Check your connection."}
	var res: Array = await http.request_completed
	http.queue_free()
	var result: int = res[0]
	var code: int = res[1]
	var parsed: Variant = JSON.parse_string((res[3] as PackedByteArray).get_string_from_utf8())
	var data: Dictionary = parsed if parsed is Dictionary else {}
	if result != HTTPRequest.RESULT_SUCCESS:
		return {"ok": false, "code": 0, "data": {}, "error": "Can't reach the Starship. Check your connection and try again."}
	if code >= 200 and code < 300:
		return {"ok": true, "code": code, "data": data, "error": ""}
	var msg := str(data.get("error", data.get("message", "")))
	if msg == "":
		msg = "Your sign-in has expired. Please sign in again." if code == 401 else "Something went wrong (%d). Please try again." % code
	return {"ok": false, "code": code, "data": data, "error": msg}


## A file from the server (Inara's recordings). Empty if it isn't there.
func get_bytes(path: String) -> PackedByteArray:
	var req := HTTPRequest.new()
	add_child(req)
	if req.request(BASE_URL + path) != OK:
		req.queue_free()
		return PackedByteArray()
	var res: Array = await req.request_completed
	req.queue_free()
	return res[3] if res[0] == HTTPRequest.RESULT_SUCCESS and res[1] == 200 else PackedByteArray()
