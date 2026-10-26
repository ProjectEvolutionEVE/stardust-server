"""Common Attacks and Defences: phishing, guessing, reused logins, flooding and injection, and the layers that stop them."""
CODE = "computing3b_attacks_defences"
BOOK = {
    "title": "Common Attacks and Defences",
    "subtitle": "Phishing, guessing, flooding and injection, and the layers that stop them",
    "chapters": [
        ("The common attacks",
         "Most attacks are old and simple. Phishing tricks a person into giving away a code or a password by pretending to be a trusted sender. Guessing tries many passwords or codes. Flooding sends so many requests that a service slows down or stops."),
        ("Reused logins",
         "Credential stuffing takes lists of leaked logins from one site and tries them on another. It works because many people reuse the same password. Unique secrets, and one-time codes that cannot be reused, break the attack."),
        ("Injection",
         "Injection happens when a program mixes user input into a command, so the input becomes part of the command. The defence is to send input as a separate value, never as part of the command text. The game's database calls pass values in numbered slots, such as $1 and $2, for this reason."),
        ("Flooding",
         "A flood of requests can fill a server or run up its bill. Defences include limits per address and per network, such as the caps the game sets on codes, and waiting before retrying. A network provider can also absorb much of a flood before it reaches the server."),
        ("Layers, not one wall",
         "Defence in depth means several layers, so that one failure is not fatal. Encryption protects data on the wire, limits slow down guessing, hashes protect stored secrets, and separate accounts limit the damage if one is taken over."),
        ("Least privilege",
         "Give each account, program and person only the access it needs, and no more. A tool that only reads data should not be able to change it. If one account is taken over, the damage it can do stays small."),
    ],
    "test": [
        ("What is phishing?",
         [("a", "Fishing for free games"), ("b", "A trick that fakes a trusted sender to get someone to give away a code or password"), ("c", "A kind of backup"), ("d", "A kind of encryption")], "b"),
        ("Why does credential stuffing work?",
         [("a", "Because encryption has been turned off"), ("b", "Because hashes are reversed by the attacker"), ("c", "Because tokens never expire"), ("d", "Because many people reuse the same password on several sites")], "d"),
        ("What is the main defence against injection?",
         [("a", "Make the input longer"), ("b", "Print the command on the screen"), ("c", "Turn off the database"), ("d", "Send the input as a separate value, never as part of the command text")], "d"),
        ("What does least privilege mean?",
         [("a", "Giving everyone the same access"), ("b", "Keeping the number of players as low as possible"), ("c", "Giving each account only the access it needs"), ("d", "Lowering the price of access")], "c"),
        ("Why is defence in depth better than one strong wall?",
         [("a", "Because one layer failing is not fatal, since other layers still stand"), ("b", "Because walls are cheaper to build"), ("c", "Because layers remove the need for backups"), ("d", "Because one wall always fails")], "a"),
    ],
}
