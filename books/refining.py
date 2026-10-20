"""Refining & Chemistry (10-20): the real chemistry behind getting metal out of ore."""
import minerals as MN

CODE = "refining"
_H, _B = MN.MINERALS["iron"], MN.MINERALS["bauxite"]

BOOK = {
    "title": "Refining & Chemistry",
    "subtitle": "The chemistry that takes metal out of ore",
    "chapters": [
        ("Elements and compounds",
         "Everything is made of elements: iron (Fe), oxygen (O), sulfur (S) and so on. An ore is a compound, an "
         "element locked together with others. A formula like Fe₂O₃ says two iron atoms for every three oxygen. "
         "Refining is the work of unlocking the metal."),
        ("Oxides: take the oxygen away",
         f"Many ores are oxides, like {_H['name'].lower()} ({_H['formula']}). Heated with carbon, the carbon grabs "
         "the oxygen and leaves as carbon monoxide or dioxide gas, and metal is left behind. That is called "
         "reduction, and it is how a blast furnace makes iron."),
        ("Sulfides: roast first",
         "Ores like chalcopyrite (CuFeS₂) and galena (PbS) are sulfides. On Earth they are usually roasted in air "
         "first, which drives the sulfur off as gas, and then reduced like an oxide."),
        ("Electricity for stubborn metals",
         f"Some metals hold on too tightly for carbon. Aluminium from {_B['name'].lower()} is made with electricity: "
         "the oxide is dissolved in a molten salt and a strong current pulls the aluminium out. This is called "
         "electrolysis."),
        ("Slag",
         "Whatever is not the metal ends up as slag. Aboard, every ore piece yields exactly its metal's share by "
         "weight from its formula, and the rest is slag. 100 kg of chalcopyrite gives 34.6 kg of copper and 65.4 kg "
         "of slag."),
        ("What the game does today",
         "The game uses this chemistry for smelting yields (see Metallurgy). The furnaces themselves are designed by "
         "players as blueprints. The steps in this book are real-world background: the game does not yet model "
         "roasting, reduction or electrolysis one by one."),
    ],
    "test": [
        ("What does the formula Fe₂O₃ tell you?",
         [("a", "Two iron atoms for every three oxygen"), ("b", "Its price"), ("c", "It is gold"), ("d", "Its weight is 23 kg")], "a"),
        ("What does carbon do in reduction?",
         [("a", "It melts the ship"), ("b", "It takes the oxygen away, leaving metal"), ("c", "It adds sulfur"), ("d", "Nothing")], "b"),
        ("What is usually done to a sulfide ore first?",
         [("a", "Freezing"), ("b", "Painting"), ("c", "Roasting in air"), ("d", "Selling")], "c"),
        ("How is aluminium made?",
         [("a", "With electricity (electrolysis)"), ("b", "By hammering"), ("c", "It is found pure"), ("d", "From ice")], "a"),
        ("Aboard, what is left over after the metal's share?",
         [("a", "Diamonds"), ("b", "Slag"), ("c", "Credits"), ("d", "Water")], "b"),
    ],
}
