"""One-Time Codes: how a short code sent to a phone or an email proves that you can receive messages there, and how systems stop guessing."""
CODE = "computing3b_one_time_codes"
BOOK = {
    "title": "One-Time Codes",
    "subtitle": "How a short code proves you can receive messages, and how systems stop guessing",
    "chapters": [
        ("Something you can receive",
         "A one-time code proves that you can receive messages at an address you chose. The system sends a short code, and you type it back. Because a code works once and then expires, a copy of an old code does nothing."),
        ("Kinds of proof",
         "Proof of identity comes in kinds: something you know, such as a password, something you have, such as a phone, and something you are, such as a fingerprint. The game uses no passwords, so its sign-in rests on proof that you can receive a code at your phone or your email."),
        ("Why codes expire",
         "A code that lasted for ever would be a standing key for anyone who saw it. The game's codes last ten minutes, long enough to read a message and type the code, and short enough that an old code is useless."),
        ("Guessing is the threat",
         "A six-digit code has one million possible values, so trying codes at random could eventually succeed. A cap on wrong tries closes that gap. In the game, five wrong tries use up the code."),
        ("Limiting requests too",
         "Attackers may also flood a system with requests, to run up its costs or to fish for codes across many addresses. The game allows five codes per address and twenty per network address each hour. Each text message costs money, so these limits protect the bill as well as the sign-in."),
        ("Keeping codes safe",
         "Phone codes are checked by Twilio's service, which holds them. Email codes are kept on the game's server only as a hash, so someone who reads the database cannot see a live code. The record of attempts is kept in the database too, so the limits still apply after a restart."),
    ],
    "test": [
        ("Why does a one-time code stop working after one use?",
         [("a", "So a printer can reuse it"), ("b", "So a copy of an old code cannot be used again"), ("c", "So it becomes a password"), ("d", "So it can be sent by post")], "b"),
        ("How many values can a six-digit code take?",
         [("a", "Ten"), ("b", "One thousand"), ("c", "One hundred thousand"), ("d", "One million")], "d"),
        ("What does the game's rule of five wrong tries do?",
         [("a", "Gives the player five more guesses"), ("b", "Deletes the player's account"), ("c", "Sends a warning to a bank"), ("d", "Ends that code, so guessing it becomes much harder")], "d"),
        ("Why does the game cap how many codes can be requested each hour?",
         [("a", "So players sign in faster"), ("b", "Because codes are sent in colour"), ("c", "To stop anyone running up the text-message bill or fishing for codes"), ("d", "Because the codes grow longer each hour")], "c"),
        ("Why are email codes kept only as a hash?",
         [("a", "So the player can read the code back later"), ("b", "So someone who reads the database cannot use a live code"), ("c", "So the code is printed on receipts"), ("d", "So the code never expires")], "b"),
    ],
}
