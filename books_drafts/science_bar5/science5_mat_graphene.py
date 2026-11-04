"""Graphene and Two-Dimensional Materials: a single layer of carbon atoms, its unusual electrons, and how layers are stacked."""
CODE = "science5_mat_graphene"
BOOK = {
    "title": "Graphene and Two-Dimensional Materials",
    "subtitle": "A single sheet of carbon atoms, and what it can do",
    "chapters": [
        ("One atom thick", "Graphene is a single layer of carbon atoms arranged in a honeycomb pattern. It is only one atom thick. It is one of the thinnest materials ever made."),
        ("Dirac electrons", "Electrons in graphene behave as if they have no mass near certain points in their energy map. They are called Dirac electrons. This gives graphene very high electron mobility."),
        ("Making graphene", "Exfoliation peels thin layers from graphite, the same stuff as pencil lead. Chemical vapour deposition grows large sheets on a metal surface. Each method suits different uses."),
        ("Transport", "Graphene conducts electricity and heat very well. Electrons move through it with little scattering. These properties make it of interest for electronics."),
        ("Defects", "Missing atoms and the edges of a sheet change its properties. Defects can open an energy gap or scatter electrons. Controlling defects is important for applications."),
        ("Van der Waals stacks", "Two-dimensional layers can be stacked on one another and held by weak van der Waals forces. Stacks of different layers create new combinations. This lets designers build devices layer by layer."),
    ],
    "test": [
        ("What is graphene?",
         [("a", "A metal"), ("b", "A single layer of carbon atoms in a honeycomb pattern"), ("c", "A glass"), ("d", "A gas")], "b"),
        ("What is a Dirac electron in graphene?",
         [("a", "A type of cloud"), ("b", "A kind of battery"), ("c", "A fish"), ("d", "An electron that behaves as if it has no mass near certain points")], "d"),
        ("How can large graphene sheets be grown?",
         [("a", "By freezing water"), ("b", "By baking clay"), ("c", "By chemical vapour deposition"), ("d", "By weaving wool")], "c"),
        ("What holds the layers of a van der Waals stack together?",
         [("a", "Weak forces"), ("b", "Strong glue"), ("c", "Nails"), ("d", "Screws")], "a"),
        ("What can missing atoms or edges do in graphene?",
         [("a", "Nothing at all"), ("b", "Make it heavier"), ("c", "Change its properties"), ("d", "Turn it into sand")], "c"),
    ],
}
