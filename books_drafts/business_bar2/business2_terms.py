"""Terms That Protect Both Sides (Broker, bar 2): what a good agreement says, and how it stays fair to both parties."""
CODE = "business2_terms"
BOOK = {
    "title": "Terms That Protect Both Sides",
    "subtitle": "What a good agreement says, and how it stays fair",
    "chapters": [
        ("What a good term says",
         "A term is one part of an agreement: what is to be done, what it costs, how much is needed, and by when. Most arguments start with a vague term. Write each one so that a reader can check it without asking anyone."),
        ("Measure what counts",
         "Say how a delivery will be measured. A term that asks for good ore gives nobody a number to check. A term that names a number of lots, measured in a way both sides agree, can be checked. Some services can even check the result against real chemistry."),
        ("Deadlines",
         "A deadline says when the work or the delivery is due. A good term also says what happens if the date is missed: who may cancel, and what they get back. Without that, a missed date becomes an argument."),
        ("Who holds the money",
         "When money is held by a neutral third party until the work is done, it is called escrow. The holder does not keep the money for itself while the deal is open. Escrow protects both sides, because neither has to trust the other. Aboard the Starship, the bank plays this role for services."),
        ("Settling a disagreement",
         "Every agreement needs a way to settle a disagreement before one starts. Name who checks the work, and how they check it. Then a dispute ends with a check, not a shouting match."),
        ("Keep a copy",
         "Keep a copy of every agreement, with its date and its code if it has one. A receipt is proof of what was done. A term you have written down is proof of what was agreed."),
    ],
    "test": [
        ("What is a term?",
         [("a", "A kind of ore"), ("b", "One part of an agreement, such as the price, the quantity or the deadline"), ("c", "A fee paid to the bank"), ("d", "The name of a player")], "b"),
        ("Which term is easiest to check?",
         [("a", "Good ore"), ("b", "A fair amount of metal"), ("c", "A stated number of lots, measured in a way both sides agree"), ("d", "Whatever the seller likes")], "c"),
        ("What is escrow?",
         [("a", "A fee on each sale"), ("b", "A neutral holder keeps the money until the work is done"), ("c", "A kind of auction"), ("d", "A type of receipt")], "b"),
        ("A deadline is missed. What should a good agreement say?",
         [("a", "Nothing, since deadlines do not matter"), ("b", "Who may cancel, and what they get back"), ("c", "The seller keeps all the money"), ("d", "The buyer must pay twice")], "b"),
        ("Why keep a copy of each agreement?",
         [("a", "It shows what was agreed, and it can be checked"), ("b", "It makes the agreement longer"), ("c", "Agreements expire after one day"), ("d", "The bank requires it to be burned")], "a"),
    ],
}
