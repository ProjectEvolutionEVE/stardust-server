"""Crystallisation and Polymorph Control: nucleation, crystal growth, supersaturation, polymorphic forms and seeding."""
CODE = "science5_chem_polymorph"
BOOK = {
    "title": "Crystallisation and Polymorph Control",
    "subtitle": "Nucleation, supersaturation, polymorphs and process control",
    "chapters": [
        ("Making solid crystals", "Crystallisation turns a dissolved substance into solid crystals. It is used to purify chemicals and to make products with the right form. The final crystal form matters for how a product behaves."),
        ("Nucleation", "Nucleation is the start of a new crystal from a solution. It needs a small cluster of molecules to form first. Nucleation can be spontaneous or triggered by a surface or seed."),
        ("Crystal growth", "After nucleation, the crystal grows as more molecules join its surface. The growth rate depends on supersaturation and on how the surface attaches molecules. Controlled growth gives larger and more uniform crystals."),
        ("Supersaturation", "Supersaturation means the solution holds more dissolved substance than it would at equilibrium. It is the driving force for both nucleation and growth. Too much supersaturation can give many small crystals and poor purity."),
        ("Polymorphic forms", "Polymorphs are different crystal forms of the same molecule. Each form can have a different solubility, stability or appearance. Choosing and keeping the right polymorph is a key task in manufacturing."),
        ("Seeding and process control", "Seeding adds small crystals of the desired form to start growth in that form. Process control keeps temperature, cooling rate and supersaturation steady. Good control gives a reproducible product."),
    ],
    "test": [
        ("What is nucleation?",
         [("a", "The melting of ice into water"), ("b", "The breaking of a window"), ("c", "The start of a new crystal from a solution"), ("d", "The cooling of a kettle")], "c"),
        ("What is supersaturation?",
         [("a", "Holding less water than a sponge"), ("b", "Holding more dissolved substance than equilibrium allows"), ("c", "Being exactly at equilibrium"), ("d", "Being frozen solid")], "b"),
        ("What are polymorphs?",
         [("a", "Different crystal forms of the same molecule"), ("b", "Different molecules with the same name"), ("c", "Crystals made of glass"), ("d", "Crystals that never grow")], "a"),
        ("What does seeding do?",
         [("a", "Makes the solution boil"), ("b", "Starts growth in a chosen crystal form"), ("c", "Removes all crystals"), ("d", "Makes the flask bigger")], "b"),
        ("Why does the right polymorph matter in manufacturing?",
         [("a", "Polymorphs always look the same"), ("b", "Polymorphs weigh nothing"), ("c", "Different forms can differ in solubility and stability"), ("d", "Polymorphs cannot be made")], "c"),
    ],
}
