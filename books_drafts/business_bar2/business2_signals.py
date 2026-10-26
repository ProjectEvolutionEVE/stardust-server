"""Negotiation Without Words (Broker, bar 2): on the Starship, prices and quantities are the only message (rule 8)."""
CODE = "business2_signals"
BOOK = {
    "title": "Negotiation Without Words",
    "subtitle": "Prices are the only message on the Starship market",
    "chapters": [
        ("No talking, only prices",
         "On the Starship, players never talk to each other and never see each other's names. The only thing you can say to the market is a price and a quantity. Every bid, every ask and every trade is a message. So is a trade that does not happen."),
        ("Reading a bid as a message",
         "A bid tells you how much someone is willing to pay now. A rising series of bids tells you buyers want the item more than they did before. You do not know why, and you do not need to know why to act on it."),
        ("Orders are offers, not promises",
         "A limit order is an offer that waits, and it can be cancelled. So a price on the board shows what someone wants today, not what they will do tomorrow. Read the board as a set of offers that can change at any moment."),
        ("Make your offer clear",
         "Because only prices speak, a clear limit price is the best message you can send. Pick the price you will accept and post it plainly. Hoping someone will guess your meaning from a messy order is not a plan."),
        ("Taking the price on offer",
         "Buy now and Sell now accept the price already on the board. You are saying yes to someone else's offer, without a word. Taking it is a decision as much as a trade, so decide before you press the button."),
        ("Real-world signals",
         "Real markets are full of signals without words: a sold-out sign, a long queue, an empty shelf. Traders in every age have read these signs. The skill is to read them honestly, and to send only the signals you mean to send."),
    ],
    "test": [
        ("What can you tell the market, since players never talk?",
         [("a", "Long messages"), ("b", "Voice notes"), ("c", "Prices and quantities"), ("d", "Names")], "c"),
        ("What is a limit order, in plain words?",
         [("a", "A promise that cannot change"), ("b", "An offer that waits and can be cancelled"), ("c", "A payment that cannot be refunded"), ("d", "A receipt from the bank")], "b"),
        ("What does a rising series of bids tell you?",
         [("a", "Buyers want the item more than before"), ("b", "The seller has left the market"), ("c", "The floor is falling"), ("d", "The bank has stopped trading")], "a"),
        ("What do Buy now and Sell now do with the prices already on the board?",
         [("a", "Ignore them"), ("b", "Cancel them"), ("c", "Accept them, straight away"), ("d", "Post new bids that wait")], "c"),
        ("What is the clearest message to send with a limit order?",
         [("a", "A price you are prepared to accept, posted plainly"), ("b", "A price you hope no one notices"), ("c", "A price far above the floor that is never changed"), ("d", "No price at all")], "a"),
    ],
}
