"""Galileo Navigation Message Authentication: how signed navigation data help a receiver reject fake signals."""
CODE = "navigation5_osnma"
BOOK = {
    "title": "Galileo Navigation Message Authentication",
    "subtitle": "Checking that a satellite message is genuine",
    "chapters": [
        ("Why authenticate", "Satellite signals can be faked, a problem called spoofing. Authentication lets a receiver check that a message really came from the satellite."),
        ("Message signing", "OSNMA, the Galileo navigation message authentication service, adds tags to the navigation data. Receivers check these tags against trusted keys."),
        ("Keys and timing", "Keys are released on a fixed schedule, so a message can be checked only after its key is public. This timing stops an attacker from using a key too early."),
        ("Verification", "A receiver stores a trusted root key and checks the chain of keys one step at a time. Once the chain is verified, the data can be trusted."),
        ("Spoofing resistance", "OSNMA helps stop fake signals from being accepted as genuine. It does not stop every kind of attack."),
        ("Adoption", "Authentication takes time to roll out, because receivers, chips and services must all support it. It arrives in stages."),
    ],
    "test": [
        ("What problem does authentication address?",
         [("a", "Paper jams"), ("b", "Rain"), ("c", "A low battery"), ("d", "Spoofing of satellite signals")], "d"),
        ("What does OSNMA do with navigation data?",
         [("a", "Deletes it"), ("b", "Adds tags that receivers check"), ("c", "Prints it"), ("d", "Sells it")], "b"),
        ("Why are keys released on a schedule?",
         [("a", "To slow the satellite"), ("b", "To hide the sky"), ("c", "So an attacker cannot use a key before it is public"), ("d", "To make a map")], "c"),
        ("What does a receiver start from when it verifies the keys?",
         [("a", "A trusted root key"), ("b", "A random number"), ("c", "A photograph"), ("d", "A printed page")], "a"),
        ("Which statement is NOT true of OSNMA?",
         [("a", "It helps against fake signals"), ("b", "It lets a receiver verify data"), ("c", "It protects against every type of attack"), ("d", "It uses keys")], "c"),
    ],
}
