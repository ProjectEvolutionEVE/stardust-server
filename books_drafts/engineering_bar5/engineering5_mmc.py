"""Metal Matrix Composites and Their Processing: squeeze casting, powder routes, reinforcement particles, stiffness gains and machining difficulty."""
CODE = "engineering5_mmc"
BOOK = {
    "title": "Metal Matrix Composites and Their Processing",
    "subtitle": "Metals stiffened with hard particles or fibres",
    "chapters": [
        ("A metal with a hard partner",
         "A metal matrix composite is a metal, often aluminium, reinforced with a harder material such as ceramic particles or fibres. The result is stiffer and often wear-resistant, while staying a metal that can be joined and shaped."),
        ("Squeeze casting",
         "In squeeze casting, molten metal is poured into a die and pressed while it solidifies. The pressure drives the melt around the reinforcement and removes gas pockets. The method suits parts with a simple, repeatable shape."),
        ("Powder routes",
         "In a powder route, metal powder and reinforcement are mixed, pressed and sintered. Powder routes give good control over the mix, and they work with reinforcements that do not blend well when melted."),
        ("Reinforcement particles",
         "Common reinforcements include ceramic particles such as silicon carbide and alumina. Their size, shape and amount set the final behaviour. Too much reinforcement makes the metal brittle and hard to process."),
        ("Stiffness gains",
         "Adding particles raises the stiffness of the metal, often by a useful amount for a modest weight gain. Designers use this to cut deflection in parts such as brake discs or engine parts, where stiffness and wear matter."),
        ("Machining is harder",
         "Hard particles wear cutting tools quickly. Tool choice, cutting speed and coolant all need care. The machining cost is part of the true price of the composite, and it must be counted before a choice is made."),
    ],
    "test": [
        ("What is a metal matrix composite?",
         [("a", "A plastic with a metal coat"), ("b", "A metal reinforced with a harder material"), ("c", "A pure gold bar"), ("d", "A paper board")], "b"),
        ("What happens during squeeze casting?",
         [("a", "The metal is painted"), ("b", "The metal is frozen in ice"), ("c", "Molten metal is pressed in a die while it solidifies"), ("d", "The part is bent by hand")], "c"),
        ("Which reinforcement is commonly used in these composites?",
         [("a", "Ordinary sand"), ("b", "Dried leaves"), ("c", "Sugar"), ("d", "Silicon carbide particles")], "d"),
        ("What does adding a lot of reinforcement often cause?",
         [("a", "The metal becomes brittle and harder to process"), ("b", "The metal becomes softer and lighter"), ("c", "The metal stops conducting heat completely"), ("d", "Nothing changes")], "a"),
        ("Why is machining a metal matrix composite harder?",
         [("a", "The metal is too soft to cut"), ("b", "Hard particles wear cutting tools quickly"), ("c", "The parts are too small"), ("d", "The metal melts when touched")], "b"),
    ],
}
