"""Logging: what a system should record so that problems can be found later, what must never be written down, and how long logs are kept."""
CODE = "computing3b_logging"
BOOK = {
    "title": "Logs That Help, Not Harm",
    "subtitle": "What to record to find problems later, and what must never be written down",
    "chapters": [
        ("What a log is for",
         "A log is a record of what a system did: when a request came in, what happened, and whether it worked. Good logs help you find a fault after the event, when nobody was watching the screen."),
        ("Levels of detail",
         "Logs use levels, such as debug, info, warning and error. Debug detail is useful while building a system, but it is noisy when the system runs every day. Errors need attention, so they should always be recorded."),
        ("Never log secrets",
         "A log must never hold a password, a live sign-in code, a token or a private key. Logs are copied around, read by many people and kept for months, so a secret written there is leaked. The game's failed text-message calls, for example, log only the kind of error, never the code."),
        ("Leave out personal details",
         "Logs often need an identifier to link related events. Prefer an internal random id over a name or an email address, and do not write personal data unless the job really needs it. Record what happened, not everything there is to know about the person."),
        ("Logs as evidence",
         "Some logs form an audit trail, a record that shows who did what and when, such as a change to a balance. An audit trail must be complete, and the people it checks must not be able to edit it quietly. A gap in an audit trail is a finding in itself."),
        ("Keep them for a fair time",
         "Logs are useful for a while, and after that they become a privacy and cost burden. Decide how long each kind is kept, and remove older logs on a schedule, unless the law or an audit requires otherwise."),
    ],
    "test": [
        ("What is a log?",
         [("a", "A record of what a system did, when, and whether it worked"), ("b", "A kind of cable"), ("c", "A type of ship"), ("d", "A bank account")], "a"),
        ("Why should a log never hold a live sign-in code?",
         [("a", "Because codes are too long to read"), ("b", "Because codes are always wrong"), ("c", "Because logs cannot store numbers"), ("d", "Because anyone who can read the log could use the code to sign in")], "d"),
        ("What does a debug level of logging usually contain?",
         [("a", "Only the price of food"), ("b", "Only the passwords"), ("c", "Only the year"), ("d", "Fine detail that is useful while building, but noisy when the system runs every day")], "d"),
        ("What is an audit trail?",
         [("a", "A map of every planet"), ("b", "A decorative border on a page"), ("c", "A route for ships"), ("d", "A record that shows who did what and when, and cannot be quietly edited")], "d"),
        ("Why is it good to prefer an internal random id over an email address in a log?",
         [("a", "Because random ids are longer"), ("b", "Because email addresses make logs run slower"), ("c", "Because the log can still link related events without revealing personal details"), ("d", "Because email addresses cannot be typed")], "c"),
    ],
}
