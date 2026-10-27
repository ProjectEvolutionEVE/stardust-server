"""MAX Phases: layered carbides and nitrides that combine metal and ceramic traits, and can be machined and resist damage."""
CODE = "mining5_max"
BOOK = {
    "title": "MAX Phases",
    "subtitle": "Layered materials that act like both metal and ceramic",
    "chapters": [
        ("What the name means", "MAX phases are layered compounds with the general formula M n+1 A X n. M is an early transition metal, A is an element from groups 13 or 14, and X is carbon or nitrogen. The layers stack in a fixed pattern."),
        ("A famous example", "Titanium silicon carbide, Ti3SiC2, is the best known MAX phase. Its structure is a stack of titanium carbide layers separated by layers of silicon."),
        ("Metal and ceramic together", "Ceramics are hard but brittle, and metals are tough but soft. MAX phases manage both. They conduct heat and electricity like metals, and keep high stiffness like ceramics."),
        ("Damage tolerance", "Under stress, cracks in MAX phases can bend and kink along their layers. This lets them absorb damage without shattering. Few ceramics can do this."),
        ("Oxidation resistance", "At high heat in air, these materials form a thin protective oxide layer, often of alumina or silica. The layer slows further attack, which is why they are studied for hot parts."),
        ("Making them", "MAX phases are made from powders by heating them under pressure or by sintering. The mix of elements must be chosen with care, because unwanted phases can form and weaken the result."),
    ],
    "test": [
        ("What does the letter X stand for in the MAX formula?",
         [("a", "Iron"), ("b", "Xenon"), ("c", "Oxygen only"), ("d", "Carbon or nitrogen")], "d"),
        ("What is titanium silicon carbide written as?",
         [("a", "SiO2"), ("b", "Ti3SiC2"), ("c", "Fe3C"), ("d", "NaCl")], "b"),
        ("What do MAX phases combine?",
         [("a", "Metal and ceramic traits"), ("b", "Glass and wood traits"), ("c", "Plastic and rubber traits"), ("d", "Gas and liquid traits")], "a"),
        ("What protective layer forms on MAX phases at high heat?",
         [("a", "A sugar coating"), ("b", "A layer of ice"), ("c", "An oxide layer"), ("d", "A film of oil")], "c"),
        ("Why can MAX phases absorb damage without shattering?",
         [("a", "Cracks can bend and kink along their layers"), ("b", "They contain no atoms"), ("c", "They are liquid inside"), ("d", "They are made of paper")], "a"),
    ],
}
