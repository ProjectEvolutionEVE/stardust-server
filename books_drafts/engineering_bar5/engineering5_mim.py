"""Metal Injection Moulding: feedstock binders, moulding, debinding, sintering shrinkage and the cost of small parts."""
CODE = "engineering5_mim"
BOOK = {
    "title": "Metal Injection Moulding",
    "subtitle": "Moulding small, complex metal parts in large numbers",
    "chapters": [
        ("Plastic-like moulding for metal",
         "Metal injection moulding, or MIM, mixes very fine metal powder with a binder to make a feedstock. The feedstock is injected into a mould much like plastic. This makes small, complex metal parts in large numbers."),
        ("The feedstock",
         "The binder holds the powder together while the part is moulded. Its mix must flow well enough to fill the mould and hold the shape when it cools. A good feedstock is the base of a good part."),
        ("Moulding",
         "The feedstock is heated, injected under pressure and cooled in the mould. The green part comes out with the right shape but still holds binder. It is soft and fragile at this stage."),
        ("Debinding",
         "Debinding removes the binder, by heat or by solvent, before the part is sintered. Removing it too fast can crack or bloat the part. The debinding cycle is one of the most careful steps in the process."),
        ("Sintering shrinkage",
         "In sintering, the part is heated until the powder particles bond and the pores close. The part shrinks a great deal in the process. The mould must be made larger to allow for it, and the shrinkage must be predicted well."),
        ("The cost of small parts",
         "MIM suits small parts made in high volume, where machining each one would cost far more. Tooling is expensive, so the method pays off only with enough parts. The true cost is weighed against the number of parts the mould will make."),
    ],
    "test": [
        ("What is metal injection moulding?",
         [("a", "Pouring liquid steel into sand"), ("b", "Carving metal with a knife"), ("c", "Injecting metal powder mixed with a binder into a mould"), ("d", "Rolling sheets flat")], "c"),
        ("What does the binder do in the feedstock?",
         [("a", "It makes the part explode"), ("b", "It dyes the part blue"), ("c", "It cools the mould"), ("d", "It holds the powder together while the part is moulded")], "d"),
        ("What is debinding?",
         [("a", "Removing the binder before sintering"), ("b", "Adding a second binder"), ("c", "Polishing the finished part"), ("d", "Testing the part for strength")], "a"),
        ("Why must the mould be made larger than the final part?",
         [("a", "Because the mould must weigh more"), ("b", "Because the part shrinks a great deal during sintering"), ("c", "Because the part grows in the furnace"), ("d", "Because the powder is never used")], "b"),
        ("When does MIM pay off?",
         [("a", "For one huge part only"), ("b", "Only for paper parts"), ("c", "For small parts made in high volume"), ("d", "Only when the mould costs nothing")], "c"),
    ],
}
