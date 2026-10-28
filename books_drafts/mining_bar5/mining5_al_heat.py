"""Aluminium Heat Treatment and Ageing: how solution treatment, quenching and ageing make aluminium alloys strong."""
CODE = "mining5_al_heat"
BOOK = {
    "title": "Aluminium Heat Treatment and Ageing",
    "subtitle": "Solution treatment, quenching and ageing, step by step",
    "chapters": [
        ("Dissolving the alloying atoms", "Solution treatment heats the alloy to a high temperature, often close to its melting point. At this heat, the added atoms, such as copper or magnesium, dissolve into the aluminium and spread evenly. The metal becomes one smooth mixture."),
        ("Quenching", "Next the metal is cooled very quickly, usually in water. The fast cooling traps the added atoms in place before they can gather together. The alloy is now soft, but it holds the seeds of its strength."),
        ("Natural ageing", "Some alloys left at room temperature slowly harden over days. The trapped atoms cluster into tiny groups called Guinier-Preston zones. These zones make the metal stronger without any extra heating."),
        ("Artificial ageing", "Heating the alloy gently, for hours at a lower temperature, speeds up the process. The clusters change into fine particles of a set shape, first a phase called double prime, then theta prime, and finally the stable phase. Hardness peaks at the in-between stages; the final stable phase is softer."),
        ("Overageing", "Heat or time past the peak makes the particles grow too large. The metal then softens again. Good practice is to stop at the peak, where the balance of strength and toughness is best."),
        ("Why it matters", "The same aluminium can be soft and easy to shape, or hard and strong, depending on the heat cycle. Makers of bike frames, aircraft skins and cooking pans all use these steps to get exactly the properties the job needs."),
    ],
    "test": [
        ("What does solution treatment do?",
         [("a", "It makes the metal rust"), ("b", "It turns the metal into powder"), ("c", "It dissolves the added atoms into the aluminium"), ("d", "It cools the metal very slowly")], "c"),
        ("Why is the alloy cooled very fast after solution treatment?",
         [("a", "To trap the added atoms in place"), ("b", "To make it lighter"), ("c", "To paint the surface"), ("d", "To melt it again")], "a"),
        ("What happens when an alloy is overaged?",
         [("a", "It becomes stronger without limit"), ("b", "It turns into glass"), ("c", "It dissolves in air"), ("d", "Its particles grow too large and it softens again")], "d"),
        ("What is natural ageing?",
         [("a", "Melting in a furnace"), ("b", "Hardening slowly at room temperature"), ("c", "Polishing with sand"), ("d", "Cutting into sheets")], "b"),
        ("What is the goal when you reach the peak of ageing?",
         [("a", "The softest metal possible"), ("b", "The lowest weight"), ("c", "The most colour"), ("d", "The best balance of strength and toughness")], "d"),
    ],
}
