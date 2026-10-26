"""Cyber Security for Craft: protecting the links that command a spacecraft, and lessons from real attacks."""
CODE = "flight5_s_cyber"
BOOK = {
    "title": "Cyber Security for Craft",
    "subtitle": "Protecting the links that command a craft",
    "chapters": [
        ("Why it matters",
         "A spacecraft is controlled by commands sent over radio links. If someone could forge those commands, they could cause real harm, so the links must be protected."),
        ("Threats",
         "Threats include stolen passwords, malicious software and attacks on ground systems. Each one needs its own defence."),
        ("Command links",
         "Commands are checked for authenticity before they are obeyed. Clear rules decide who may send them, and when."),
        ("Encryption",
         "Encryption scrambles data so that only the right receiver can read it. The keys that unlock it must be kept secret."),
        ("Software updates",
         "Updates fix weaknesses, but each one must be tested and checked before it is loaded. A careless update can open a new door to an attacker."),
        ("Lessons from Stuxnet",
         "The Stuxnet malware, found in 2010, damaged centrifuges in an industrial plant by manipulating their controls. It showed that a software attack can cause physical damage."),
    ],
    "test": [
        ("Why does a spacecraft need cyber security?",
         [("a", "To keep it cool"), ("b", "To make it lighter"), ("c", "Its commands travel over links that must be protected from forgery"), ("d", "To paint it")], "c"),
        ("What does encryption do?",
         [("a", "Makes data louder"), ("b", "Scrambles data so only the right receiver can read it"), ("c", "Erases data"), ("d", "Copies data")], "b"),
        ("What is essential before loading a software update?",
         [("a", "A coat of paint"), ("b", "A faster clock"), ("c", "Warm sunshine"), ("d", "Testing and checking it")], "d"),
        ("What did the Stuxnet malware show?",
         [("a", "A software attack can damage physical equipment"), ("b", "Radio links cannot be jammed"), ("c", "Computers never fail"), ("d", "Only paper is secure")], "a"),
        ("What must a command link check before a command is obeyed?",
         [("a", "The colour of the command"), ("b", "The music playing nearby"), ("c", "That the command is authentic"), ("d", "The weight of the sender")], "c"),
    ],
}
