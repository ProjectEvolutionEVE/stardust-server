"""Symmetric Encryption: one shared secret key that locks and unlocks the data, and how modern ciphers such as AES use it."""
CODE = "computing3b_symmetric_encryption"
BOOK = {
    "title": "Symmetric Encryption",
    "subtitle": "One shared secret key, and how modern ciphers use it",
    "chapters": [
        ("One key, both ways",
         "In symmetric encryption, the same secret key locks and unlocks the data. Both sides must hold that key. The method is quick, which makes it the usual choice for large amounts of data, such as files, backups and the main body of a web session."),
        ("Ciphers and keys",
         "The method that does the scrambling is called a cipher. The standard in wide use today is AES, which works with keys of 128 or 256 bits. A key that long has so many possible values that guessing it is out of reach."),
        ("The key is the secret",
         "A strong cipher with a leaked key protects nothing. The hard part is getting the key to the right people and keeping it from everyone else. A key should be random, long, and stored apart from the data it protects."),
        ("Modes and fresh values",
         "A cipher works on fixed-size blocks, so a mode of operation says how the blocks are chained. Each message also needs its own fresh random value, often called a nonce. Reusing a nonce with the same key can weaken the protection badly."),
        ("Checking for tampering",
         "Encryption alone hides data but does not prove it was left alone. Modern modes add an authentication tag, a short check value made from the data and the key. If anything has changed, the tag fails and the data is rejected. This is called authenticated encryption."),
        ("Where you meet it",
         "Symmetric encryption protects files on a disk, backups, and the data in a session once a key has been agreed. Public-key methods are used mainly to agree the shared key in the first place."),
    ],
    "test": [
        ("In symmetric encryption, how many keys are used?",
         [("a", "None at all"), ("b", "Two, one public and one private"), ("c", "One shared secret key for both locking and unlocking"), ("d", "One new key printed for each message")], "c"),
        ("What is a cipher?",
         [("a", "A type of router"), ("b", "A method that scrambles data using a key"), ("c", "A password manager"), ("d", "A kind of backup")], "b"),
        ("Why is symmetric encryption often used for large amounts of data?",
         [("a", "It is quick"), ("b", "It cannot be broken"), ("c", "It needs no key at all"), ("d", "It only works on text")], "a"),
        ("What does authenticated encryption add to ordinary encryption?",
         [("a", "A tag that shows whether the data was changed"), ("b", "A printed copy of the data"), ("c", "A faster network connection"), ("d", "A longer file name")], "a"),
        ("Why must a nonce be fresh for each message?",
         [("a", "So the same message never looks the same twice, which keeps the protection strong"), ("b", "So each message is shorter"), ("c", "So the key can be printed on the screen"), ("d", "So a router can read the message")], "a"),
    ],
}
