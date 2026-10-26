"""Public-Key Encryption and Signatures: key pairs, sharing a public key safely, and signatures that show who signed a message."""
CODE = "computing3b_public_key"
BOOK = {
    "title": "Public-Key Encryption and Signatures",
    "subtitle": "Key pairs, sharing without a secret, and signatures that prove who signed",
    "chapters": [
        ("A matched pair",
         "Public-key cryptography uses two keys that are mathematically linked. Anything locked with the public key can be opened only with the matching private key. The public key can be shared with anyone. The private key never leaves its owner."),
        ("Sharing without a secret",
         "Two people who have never met can still send each other a secret. The sender locks the message with the receiver's public key, and only the receiver's private key can open it. This solves the old problem of getting a shared key to someone safely."),
        ("Signatures prove origin",
         "A digital signature works the other way round. The sender uses the private key to sign, and anyone with the public key can check the signature. A valid signature shows that the holder of the private key signed the message, and that it has not changed since."),
        ("Why the maths is hard to reverse",
         "The key pairs rely on mathematics that is easy to do in one direction and extremely hard to undo at real sizes. Multiplying two large prime numbers is quick. Finding those two primes from their product is not. That gap is what keeps the private key safe."),
        ("Slow and fast together",
         "Public-key methods are slow for large data, so in practice they handle small jobs: agreeing a key, or signing. The large data then travels under fast symmetric encryption, using the key that was agreed."),
        ("Guarding the private key",
         "The whole system fails if a private key leaks, because anyone holding it can sign as its owner. Keep private keys in few places, limit who can reach them, and replace a key at once if it may have been exposed."),
    ],
    "test": [
        ("In public-key encryption, which key is kept private?",
         [("a", "The public key"), ("b", "The private key"), ("c", "The message"), ("d", "The router's address")], "b"),
        ("How can someone send you a secret without first sharing a secret key?",
         [("a", "Lock it with your public key, which only your private key can open"), ("b", "Send it twice"), ("c", "Print it on a receipt"), ("d", "Write it in capital letters")], "a"),
        ("What does a valid digital signature show?",
         [("a", "The message is short"), ("b", "The message was read by everyone who received it"), ("c", "The sender has a fast network connection"), ("d", "The message was signed with the private key and has not changed since")], "d"),
        ("Why is public-key maths trusted to keep the private key safe?",
         [("a", "Its numbers are printed in every textbook"), ("b", "It is easy to do one way and extremely hard to reverse at real sizes"), ("c", "Nobody has ever tried to break it"), ("d", "It uses the same key for everything")], "b"),
        ("Why do real systems combine public-key and symmetric encryption?",
         [("a", "Symmetric encryption cannot lock anything"), ("b", "Public keys are only for printing"), ("c", "Two systems cost less than one"), ("d", "Public-key methods are slow for large data, so they agree a key that fast symmetric encryption then uses")], "d"),
    ],
}
