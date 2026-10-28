"""Solidification Modelling and Chvorinov's Rule: heat extraction, freezing time, mould modulus, shrink risk and casting design."""
CODE = "engineering5_solidification"
BOOK = {
    "title": "Solidification Modelling and Chvorinov's Rule",
    "subtitle": "How long molten metal takes to freeze, and why it matters",
    "chapters": [
        ("Heat leaves through the mould",
         "When molten metal is poured into a mould, heat flows out through the mould walls. The metal freezes from the outside in. The speed of freezing decides much of the casting's quality."),
        ("Freezing time",
         "Chvorinov's rule says the time to freeze depends on the square of the mould modulus. The modulus is the volume of the casting divided by the area that cools. A bigger, chunkier section takes much longer to freeze."),
        ("Mould modulus",
         "A thin section has a small modulus and freezes fast. A thick section has a large modulus and freezes slowly. Engineers compare the modulus of each section to see where the casting will freeze last."),
        ("Shrink risk",
         "Most metals shrink as they freeze. If a thick section freezes last with no molten metal left to feed it, a shrink cavity forms there. Knowing the freezing order warns the engineer where the cavity will be."),
        ("Modelling the freeze",
         "Computer models simulate heat flow and show the freezing pattern. They point to the hot spots before any metal is poured. Engineers test the model against a real casting to be sure it is right."),
        ("Designing the casting",
         "A good casting design evens out the section sizes and lets the metal freeze from the far end toward the feed. Changes at the drawing stage cost little. Changes after the mould is made cost much more."),
    ],
    "test": [
        ("What does Chvorinov's rule relate?",
         [("a", "The price of metal to the colour"), ("b", "Freezing time to the mould modulus"), ("c", "The number of workers to the shift length"), ("d", "The weight of paint to the room size")], "b"),
        ("What is the mould modulus?",
         [("a", "The weight of the mould"), ("b", "The cost of the mould"), ("c", "The volume of the casting divided by the area that cools"), ("d", "The number of gates")], "c"),
        ("What does a thick section do in a casting?",
         [("a", "It freezes instantly"), ("b", "It never freezes"), ("c", "It freezes faster than thin parts"), ("d", "It freezes more slowly, because its modulus is larger")], "d"),
        ("Why does a last-freezing section risk a shrink cavity?",
         [("a", "No molten metal is left to feed it as it shrinks"), ("b", "It has too much molten metal"), ("c", "It is painted too early"), ("d", "It is always the smallest part")], "a"),
        ("When are design changes cheapest?",
         [("a", "After the mould is made"), ("b", "At the drawing stage, before the mould is made"), ("c", "After the part is sold"), ("d", "Never, they cost the same")], "b"),
    ],
}
