"""Ion Implantation and Surface Modification: ion beams, depth profiles, dose, lattice damage and applications to tools and seals."""
CODE = "engineering5_ion_implant"
BOOK = {
    "title": "Ion Implantation and Surface Modification",
    "subtitle": "Firing atoms into a surface to change it",
    "chapters": [
        ("Changing the surface, not the coating",
         "Ion implantation fires charged atoms into a surface with a high-energy beam. The atoms stop inside the material. Unlike a coating, nothing is added on top, so the surface does not peel."),
        ("Ion beams",
         "The beam is made by ionising a gas or vapour and accelerating the ions with electric fields. The energy of the beam sets how deep the ions go. Machines can scan the beam across a part evenly."),
        ("Depth profiles",
         "The ions do not all stop at the same depth. They form a profile, usually peaking a short distance below the surface. Engineers choose the energy to put the peak where the change is needed."),
        ("Dose",
         "Dose is the number of ions delivered per unit area. A higher dose changes the surface more. Too high a dose can damage it, so dose is set with care for each job."),
        ("Lattice damage",
         "The ions knock atoms out of their places in the crystal. This lattice damage is part of the process, and it can harden the surface. Heat treatment afterward can repair some of the damage if the design needs it."),
        ("Applications",
         "Ion implantation is used to harden tools and wear parts, and to improve surfaces such as seals that must resist wear. It costs more than many coatings, so it is chosen where a thin, well-bonded change is worth the price."),
    ],
    "test": [
        ("What does ion implantation do to the surface?",
         [("a", "It fires charged atoms into the material so they stop inside it"), ("b", "It paints a thick layer on top"), ("c", "It melts the part away"), ("d", "It sticks paper to the part")], "a"),
        ("What sets how deep the ions go?",
         [("a", "The colour of the part"), ("b", "The energy of the beam"), ("c", "The shape of the room"), ("d", "The name of the operator")], "b"),
        ("What is the dose in ion implantation?",
         [("a", "The weight of the part"), ("b", "The time of day"), ("c", "The number of ions delivered per unit area"), ("d", "The length of the cable")], "c"),
        ("What is lattice damage?",
         [("a", "A crack in the paint"), ("b", "A dent in the box"), ("c", "A fault in the wiring"), ("d", "Atoms knocked out of their places in the crystal")], "d"),
        ("Why is ion implantation chosen for some jobs?",
         [("a", "A thin, well-bonded change is worth its higher price there"), ("b", "It is always the cheapest coating"), ("c", "It needs no machine at all"), ("d", "It works only on plastic")], "a"),
    ],
}
