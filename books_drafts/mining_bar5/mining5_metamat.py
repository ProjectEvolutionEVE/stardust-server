"""Mechanical Metamaterials: structures whose designed lattice gives unusual stiffness, negative Poisson ratio and energy absorption."""
CODE = "mining5_metamat"
BOOK = {
    "title": "Mechanical Metamaterials",
    "subtitle": "Designing the shape of a material to give it new behaviour",
    "chapters": [
        ("Shape as material", "A mechanical metamaterial gets its behaviour mainly from its designed structure, not from its chemistry alone. A repeating lattice of struts and joints can act like a material with unusual properties."),
        ("Lattice design", "Engineers choose the cell shape, the strut thickness and the joint layout. Small changes in these choices can shift stiffness, strength and weight."),
        ("Negative Poisson ratio", "Most materials get thinner sideways when stretched. Some lattices do the opposite and get fatter. This negative Poisson ratio makes them auxetic."),
        ("Energy absorption", "Some lattices crush in a controlled way and absorb energy without a sudden break. This is useful in padding, helmets and crash structures."),
        ("Printing", "Complex lattices are often made by additive manufacturing, which builds a part layer by layer. Printing makes shapes that would be hard or impossible to cut."),
        ("Uses", "Metamaterials are studied for shoe soles, protective gear, lightweight parts and vibration control. They show that a clever shape can do work that heavy material would otherwise do."),
    ],
    "test": [
        ("What mainly gives a mechanical metamaterial its behaviour?",
         [("a", "Its designed structure"), ("b", "Its colour"), ("c", "Its smell"), ("d", "Its name")], "a"),
        ("What is a negative Poisson ratio?",
         [("a", "Getting heavier when cooled"), ("b", "Turning a different colour"), ("c", "Getting fatter sideways when stretched"), ("d", "Making a sound")], "c"),
        ("What is an auxetic material?",
         [("a", "A material that floats"), ("b", "A material with a negative Poisson ratio"), ("c", "A material that burns"), ("d", "A material made of sugar")], "b"),
        ("How can some lattices help protect people?",
         [("a", "By glowing in the dark"), ("b", "By making a loud noise"), ("c", "By dissolving in rain"), ("d", "By absorbing energy in a controlled crush")], "d"),
        ("Which manufacturing method is often used for complex lattices?",
         [("a", "Boiling in tea"), ("b", "Additive manufacturing"), ("c", "Hand weaving only"), ("d", "Freezing in ice")], "b"),
    ],
}
