"""Exergy: Where Energy Quality Is Lost. Energy is never lost in amount, but its quality can be wasted."""
CODE = 'engineering4_exergy'
BOOK = {
    "title": "Exergy: Where Energy Quality Is Lost",
    "subtitle": "Energy is never lost in amount, but its quality can be wasted",
    "chapters": [
        ("Energy quality",
         "Energy comes in different qualities. Hot fuel or electricity can do useful work, while warm water near room temperature can do very little."),
        ("Exergy",
         "Exergy is the part of an energy supply that can do useful work. It is the measure of energy quality, and it is what engineers try to save."),
        ("Exergy destruction",
         "Every irreversible step destroys some exergy. The exergy destroyed is a measure of avoidable waste in the process."),
        ("Waste heat",
         "Waste heat often still holds some exergy, and sometimes it can be reused. Low-grade heat is harder to put to use than high-grade heat."),
        ("Where to fix a system first",
         "Find the steps that destroy the most exergy. Fixing those steps often gives the biggest gain for the effort."),
        ("The value of recovered heat",
         "Recovering heat that can be reused saves fuel and money. Its value depends on how useful it is to the process."),
    ],
    "test": [
        ("What is exergy?",
         [("a", "The part of energy that can do useful work"), ("b", "The weight of a tank"), ("c", "The colour of heat"), ("d", "The price of power")], "a"),
        ("What is exergy destruction?",
         [("a", "A broken window"), ("b", "Painting a surface"), ("c", "Exergy lost in irreversible steps"), ("d", "The end of a shift")], "c"),
        ("Why is warm water near room temperature low quality?",
         [("a", "It is too wet"), ("b", "It is too heavy"), ("c", "It is too bright"), ("d", "It can do very little useful work")], "d"),
        ("Where should you look first to improve a system?",
         [("a", "The paint"), ("b", "The steps that destroy the most exergy"), ("c", "The office"), ("d", "The car park")], "b"),
        ("What does recovered heat save?",
         [("a", "Fuel and money"), ("b", "Paint"), ("c", "Time for lunch"), ("d", "The sky")], "a"),
    ],
}
