"""Security Basics: passwords, hashing, encryption, and how the game keeps sign-in codes and tokens as hashes."""
CODE = "computing2_security"
BOOK = {
    "title": "Security Basics",
    "subtitle": "Passwords, hashing and encryption, and how the game uses them",
    "chapters": [
        ("Keeping secrets safe",
         "Security means keeping information and systems safe from people who should not have them. A basic rule is never to store a secret in a form that anyone who reads the storage can use. Good design also limits what an attacker can gain, even when something goes wrong."),
        ("Passwords and their weak points",
         "A password is only as safe as it is hard to guess. Short or common passwords can be tried by the millions in automated attacks. Long, unique passwords, and extra checks such as a code sent to your own phone, are much harder to break."),
        ("Hashing",
         "A hash is a one-way scramble of data: the same input always gives the same output, but the output cannot be turned back into the input. A server can check a code by comparing hashes, without keeping the code itself. SHA-256 is a widely used hash."),
        ("How the game uses hashing",
         "In the game, an email sign-in code is kept only as a hash, and so is each sign-in token. A leaked copy of the database therefore cannot be used to sign in. Sign-in codes are only six digits, so the server also limits the tries: five wrong tries end a code, and a code lasts ten minutes."),
        ("Encryption",
         "Encryption scrambles data so that only someone with the right key can read it. Unlike a hash, encrypted data can be turned back into the original, but only with the key. Secret-key encryption uses one key to lock and unlock, while public-key encryption uses a pair: one key can be shared, and the other is kept private."),
        ("Where you meet it",
         "A website that shows a padlock in the address bar is using encryption to protect what you send, such as passwords and payment details. Encryption also protects data kept on devices and in backups. Keeping keys secret matters as much as the encryption itself."),
    ],
    "test": [
        ("What is a hash?",
         [("a", "A way to make a password longer"), ("b", "A one-way scramble of data, where the same input always gives the same output"), ("c", "A key that unlocks encrypted data"), ("d", "A kind of network packet")], "b"),
        ("Why does the game keep sign-in tokens only as hashes?",
         [("a", "So the tokens can be printed on receipts"), ("b", "So the tokens load faster"), ("c", "So players can read their own tokens"), ("d", "So a leaked copy of the database cannot be used to sign in")], "d"),
        ("Why does the server limit the number of wrong tries for a six-digit code?",
         [("a", "Because there are only a million possible six-digit codes, so guessing could otherwise succeed"), ("b", "Because codes are too long"), ("c", "Because codes are hashed backwards"), ("d", "Because codes are printed in colour")], "a"),
        ("What is the difference between a hash and encryption?",
         [("a", "Hashes are always printed; encryption is not"), ("b", "Encryption is faster to type"), ("c", "A hash cannot be turned back, while encrypted data can be turned back with the right key"), ("d", "They are two names for the same thing")], "c"),
        ("What is public-key encryption?",
         [("a", "Encryption with no key at all"), ("b", "Encryption where every key is printed on the front of a book"), ("c", "Encryption that is only used in public libraries"), ("d", "Encryption that uses a pair of keys: one can be shared, and the other is kept private")], "d"),
    ],
}
