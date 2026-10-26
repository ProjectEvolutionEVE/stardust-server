"""Doing It Twice Safely: idempotent actions, and the key that stops a repeat from doing harm."""
CODE = "computing3c_idempotency"
BOOK = {
    "title": "Doing It Twice Safely",
    "subtitle": "Idempotent actions, and the key that stops a repeat from doing harm",
    "chapters": [
        ("What idempotent means",
         "An action is idempotent when doing it again leaves the same result as doing it once. Setting a balance to 50 is idempotent, because setting it again still leaves 50. Adding 10 to a balance is not, because each repeat adds again."),
        ("Why it matters",
         "Retries and duplicate messages are common, as the last book showed. If an action is idempotent, a repeat is harmless. If it is not, a repeat can charge a card twice or give a reward twice."),
        ("Idempotency keys",
         "A common fix is an idempotency key, a unique code sent with the request. The server remembers the key and the result. If the same key arrives again, the server returns the saved result and does not repeat the work."),
        ("Keep the key with the work",
         "The server must store the key and the outcome somewhere that survives a crash. It must check the key and do the work as one safe step. Otherwise two copies of the same request can both slip through."),
        ("Designing actions",
         "Design actions to name the result, not the change. Set the balance to 50 is safer than add 10. When you must add, attach a key, so a repeat can be caught."),
        ("Money and trust",
         "A duplicate charge or a double reward costs real money and erodes trust. Careful design takes a little thought at the start. It saves far more later."),
    ],
    "test": [
        ("What does idempotent mean?",
         [("a", "Doing the action again always doubles the result"), ("b", "It needs a printer"), ("c", "Doing the action again gives the same result as doing it once"), ("d", "It can only happen on a Monday")], "c"),
        ("Which action is idempotent?",
         [("a", "Add 10 to a balance"), ("b", "Set a balance to 50"), ("c", "Charge a card one more time"), ("d", "Give one more reward each time")], "b"),
        ("Why does a repeated add 10 cause trouble?",
         [("a", "It adds again on each repeat, so the total grows"), ("b", "It is too quick"), ("c", "It is stored in red"), ("d", "It needs no server")], "a"),
        ("What is an idempotency key?",
         [("a", "A key to open a door"), ("b", "A key on a keyboard"), ("c", "A key that deletes the server"), ("d", "A unique code sent with a request, so the server can spot and skip a repeat")], "d"),
        ("What must a server do with an idempotency key?",
         [("a", "Ignore it"), ("b", "Print it"), ("c", "Share it with other players"), ("d", "Store the key and its result, and return the saved result if the same key comes back")], "d"),
    ],
}
