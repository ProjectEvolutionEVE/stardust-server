"""Tokens and Sessions: how a signed-in player keeps access without typing a code at every step, and how a token is kept safe."""
CODE = "computing3b_tokens_sessions"
BOOK = {
    "title": "Tokens and Sessions",
    "subtitle": "How a signed-in player keeps access without a new code each time",
    "chapters": [
        ("Why a token exists",
         "Once you have proved who you are, the server needs a way to recognise you on the next request without asking for a code again. It gives you a token, a long random string that your device sends with each request."),
        ("Random and long",
         "A good token comes from a strong source of randomness, and it is long enough that nobody can guess it. The game's tokens are 32 random bytes, which is 256 bits. No guesser could try that many values."),
        ("Keep only a hash",
         "The server keeps only a hash of each token, not the token itself. When a device sends a token, the server hashes it and looks for the match. A leaked list of hashes cannot be used to sign in, because the real tokens are not in it."),
        ("Sending it along",
         "The game's requests carry the token in an Authorization header, with the word Bearer in front of it. Whoever holds the token is treated as the player, so a token must travel only over an encrypted connection."),
        ("Expiry and last seen",
         "A token stops working after a period without use. In the game, a token expires after thirty days without a visit, and each visit restarts that clock. A token that is revoked, for example at sign-out, stops working at once."),
        ("Sessions",
         "A session is the time a token covers, from sign-in to sign-out. Ending a session early means revoking its token, which is the right step when a device is lost or a token may have leaked. The player then signs in again to start a new one."),
    ],
    "test": [
        ("What is a token for?",
         [("a", "To print a receipt"), ("b", "To let the server recognise you on later requests without a new code"), ("c", "To pay for a ship"), ("d", "To store the game's images")], "b"),
        ("Why is a good token made from random bytes?",
         [("a", "So it can be guessed easily"), ("b", "So it is shorter to type"), ("c", "So it can be printed on paper"), ("d", "So it is long and cannot be guessed")], "d"),
        ("Why does the server keep only a hash of each token?",
         [("a", "So any administrator can read the tokens"), ("b", "So tokens run faster"), ("c", "So a leaked list of hashes cannot be used to sign in"), ("d", "So tokens never expire")], "c"),
        ("Why must a bearer token travel only over an encrypted connection?",
         [("a", "Because it is too large to send otherwise"), ("b", "Because the server cannot read it"), ("c", "Because it is written in colour"), ("d", "Because anyone who sees it can act as its holder")], "d"),
        ("What happens to a game token that goes thirty days without use?",
         [("a", "It doubles in length"), ("b", "It is sent to the player's email"), ("c", "It becomes a permanent key"), ("d", "It expires, and the player must sign in again")], "d"),
    ],
}
