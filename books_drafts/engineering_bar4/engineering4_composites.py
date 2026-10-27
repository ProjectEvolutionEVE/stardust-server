"""Fibre composites: carbon, glass and aramid fibres, matrices, layup, the rule of mixtures, damage and cost against metal."""
CODE = "engineering4_composites"
BOOK = {
    "title": "Fibre Composites: Carbon, Glass and Aramid",
    "subtitle": "Fibres, matrices, layup and the rule of mixtures",
    "chapters": [
        ("Fibres in a matrix",
         "A fibre composite combines strong fibres with a matrix, usually a resin, that holds them in place. The fibres carry most of the load along their length. The matrix spreads the load between fibres and protects them."),
        ("Carbon, glass and aramid",
         "Carbon fibre is very stiff and light, glass fibre is cheaper and more widely used, and aramid fibre is tough and resists impact. Each fibre suits different jobs. The choice depends on stiffness, toughness, weight and cost."),
        ("Layup and fibre direction",
         "Layup is the process of placing layers of fibre in a chosen pattern. Fibre direction sets where the part is strongest and stiffest. Engineers align the fibres with the main loads in the part."),
        ("The rule of mixtures",
         "The rule of mixtures gives a rough estimate of a composite's stiffness from the fibre and matrix properties and their share by volume. More fibre gives more stiffness along the fibre direction. The rule is a simple guide, not an exact result."),
        ("Types of damage",
         "Composites can fail by fibre breakage, matrix cracking, delamination between layers, and fibre pull-out. Damage can be hidden inside the part even when the surface looks sound. Inspection methods help find it."),
        ("Composites against metal",
         "Composites often cost more per kilogram than metal, but they can be much lighter for the same stiffness. The total cost depends on the part, the number made and how it is manufactured. A fair comparison looks at the whole life of the part."),
    ],
    "test": [
        ("What is the job of the matrix in a fibre composite?", [("a", "To make the part magnetic"), ("b", "To carry all the load alone"), ("c", "To hold the fibres in place and spread the load between them"), ("d", "To cool the part")], "c"),
        ("Which fibre is known for being very stiff and light?", [("a", "Wool"), ("b", "Cotton"), ("c", "Carbon fibre"), ("d", "Paper")], "c"),
        ("What does the rule of mixtures estimate?", [("a", "A rough stiffness from the fibre and matrix properties and their volume share"), ("b", "The colour of a composite"), ("c", "The number of workers needed"), ("d", "The price of the paint")], "a"),
        ("What is delamination?", [("a", "Cutting a fibre to length"), ("b", "Painting a surface"), ("c", "Melting a metal"), ("d", "Separation between layers of a composite")], "d"),
        ("What does the lifetime cost of a composite part depend on?", [("a", "Only the colour of the resin"), ("b", "The part, the number made and how it is manufactured"), ("c", "Nothing but the weight"), ("d", "The name of the factory")], "b"),
    ],
}
