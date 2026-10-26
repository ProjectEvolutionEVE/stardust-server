"""Hashing in Depth: salts, slow hashes and collisions, and why a hash is only as good as the way it is used."""
CODE = "computing3b_hashing_depth"
BOOK = {
    "title": "Hashing in Depth",
    "subtitle": "Salts, slow hashes and collisions: why a hash is only as good as its use",
    "chapters": [
        ("A fingerprint of data",
         "A hash turns data of any length into a fixed-length fingerprint. SHA-256, for example, always gives 256 bits. The same input always gives the same fingerprint, and a tiny change to the input gives a completely different one. That makes a hash a good way to spot a changed file."),
        ("Collisions",
         "A good hash makes it very hard to find two different inputs with the same fingerprint. Such a pair is called a collision. Hashes that were once trusted have been broken this way, so systems move to newer hashes when that happens."),
        ("Guessing is the weak point",
         "A password or a six-digit code has only a few possible values. An attacker can hash every guess and compare the results, and a plain hash is fast to run. So a plain hash of a short secret is weak, even though the hash itself is sound."),
        ("Salt",
         "A salt is a random value added to each item before it is hashed. Each user gets a different salt, so two people with the same password end up with different stored hashes. A salt also stops one ready-made table of hashes from working on everyone at once."),
        ("Slow on purpose",
         "Password hashing functions such as bcrypt, scrypt and Argon2 are built to be slow, and some use a lot of memory. One check is barely noticed by a person, but billions of guesses become very costly to run."),
        ("Hashes check, they do not hide",
         "A hash cannot be reversed, but it can be checked. Store only the hash, hash each new attempt, and compare. A hash of a short code is only safe when other limits, such as a cap on tries, apply as well."),
    ],
    "test": [
        ("What does a hash function produce from any input?",
         [("a", "A fixed-length fingerprint"), ("b", "A key that can be reversed"), ("c", "A list of every input it has seen"), ("d", "A new random number each time")], "a"),
        ("What is a collision in hashing?",
         [("a", "Two different inputs that give the same fingerprint"), ("b", "A hash that is too long to store"), ("c", "A password that is too short"), ("d", "A server that stops working")], "a"),
        ("What does a salt do?",
         [("a", "It makes the password shorter"), ("b", "It encrypts the hash with a public key"), ("c", "It sends the hash to the browser"), ("d", "It adds a random value to each item, so the same secret gives different hashes")], "d"),
        ("Why are password hashes made slow on purpose?",
         [("a", "So the server uses less electricity"), ("b", "So users wait less time for their pages"), ("c", "So a huge number of guesses becomes expensive to try"), ("d", "So a hash can be reversed more easily")], "c"),
        ("Why is a plain hash alone a weak defence for a six-digit code?",
         [("a", "Because there are only a million codes, so every one can be hashed and checked"), ("b", "Because hashes cannot be stored"), ("c", "Because six digits is too long to hash"), ("d", "Because codes are sent in colour")], "a"),
    ],
}
