"""Zinc and Lead Ores: sphalerite and galena, two heavy sulfide ores, and the metals they give."""
CODE = 'mining2_zinc_lead'
BOOK = {
    "title": "Zinc and Lead Ores",
    "subtitle": "Sphalerite and galena: two heavy sulfide ores, and what zinc and lead are used for",
    "chapters": [
        ("Two sulfide ores",
         "Sphalerite (ZnS) is the main zinc ore, and galena (PbS) is the main lead ore. Both are sulfides, with sulfur joined to one metal. Both sit in the ore band, so they turn up in many fields."),
        ("Sphalerite",
         "Sphalerite is often brown, yellow or black, and its streak is pale. Its shine is closer to resin or glass than to metal. Most of the world's zinc comes from ores like it."),
        ("What zinc is for",
         "Zinc protects steel from rust. Steel coated with zinc is called galvanised, and the zinc wears away first to protect the iron underneath. Zinc is also mixed with copper to make brass."),
        ("Galena",
         "Galena is a heavy, shiny grey mineral that often splits into neat cubes. That cube shape is the easiest way to know it. It is one of the heaviest common ores in our fields."),
        ("What lead is for",
         "People have used lead for thousands of years, for pipes, roofing and weights. Today lead is still used in car batteries, because it stores and gives back electricity well. Lead is poisonous to people, so lead ore and lead dust are handled with care."),
        ("Yields in the game",
         "Each piece is pure ore mineral, so the formula gives the share by weight. Sphalerite gives 67.10 per cent zinc, and galena gives 86.60 per cent lead. The rest of each piece goes to slag."),
    ],
    "test": [
        ("Which mineral is the main zinc ore?",
         [("a", "Sphalerite"), ("b", "Pentlandite"), ("c", "Bauxite"), ("d", "Cobaltite")], "a"),
        ("What does galvanising do to steel?",
         [("a", "Makes it see-through"), ("b", "Protects it from rust with a zinc coating"), ("c", "Makes it magnetic"), ("d", "Turns it into lead")], "b"),
        ("What shape does galena often split into?",
         [("a", "Needles"), ("b", "Feathers"), ("c", "Spheres"), ("d", "Cubes")], "d"),
        ("In the game, how much lead does galena give by weight?",
         [("a", "8.66 per cent"), ("b", "6.6 per cent"), ("c", "86.6 per cent"), ("d", "100 per cent")], "c"),
        ("Why are lead ore and lead dust handled with care?",
         [("a", "Lead is poisonous to people"), ("b", "It explodes in air"), ("c", "It is always hot"), ("d", "It is radioactive")], "a"),
    ],
}
