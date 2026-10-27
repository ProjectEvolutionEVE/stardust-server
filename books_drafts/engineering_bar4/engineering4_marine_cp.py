"""Cathodic Protection in Seawater: galvanic anodes, impressed current, coatings, monitoring and lifetime cost."""
CODE = "engineering4_marine_cp"
BOOK = {
    "title": "Cathodic Protection in Seawater",
    "subtitle": "Anodes, impressed current, coatings and monitoring",
    "chapters": [
        ("Corrosion in seawater",
         "Seawater conducts electricity, so steel in it can corrode in an electrical way. Corrosion is worst where dissimilar metals touch, or where a coating has been damaged."),
        ("Galvanic anodes",
         "A galvanic anode is a block of a more reactive metal, such as zinc, aluminium or magnesium, fixed to the hull. It corrodes in place of the steel, so the steel is protected."),
        ("Impressed current systems",
         "An impressed current system uses a power supply and long-lasting anodes to push a current onto the hull. It can supply more current than sacrificial anodes, which suits large ships."),
        ("Coatings",
         "Paint keeps most of the steel dry, and so reduces the current the protection must supply. The coating does most of the work, and the protection covers the gaps the coating leaves."),
        ("Monitoring",
         "Reference electrodes measure the hull's electrical potential, so the crew can tell whether protection is working. Readings should stay within the set range."),
        ("Lifetime cost",
         "Anodes are used up and must be replaced. The true cost includes the materials, the dry-docking and the labour over the life of the ship."),
    ],
    "test": [
        ("Why does seawater cause corrosion?",
         [("a", "It is sweet"), ("b", "It conducts electric current, so it acts as an electrolyte"), ("c", "It is dry"), ("d", "It is cold")], "b"),
        ("What is a galvanic anode made from?",
         [("a", "Gold"), ("b", "Glass"), ("c", "A more reactive metal such as zinc"), ("d", "Wood")], "c"),
        ("What does an impressed current system use?",
         [("a", "A power supply"), ("b", "Only paint"), ("c", "Sunlight"), ("d", "Sails")], "a"),
        ("What does a coating do for cathodic protection?",
         [("a", "Adds weight"), ("b", "Makes the steel heavier"), ("c", "Heats the hull"), ("d", "Keeps most of the steel dry and cuts the current needed")], "d"),
        ("What does monitoring with reference electrodes show?",
         [("a", "The colour of the hull"), ("b", "Whether protection is working"), ("c", "The crew size"), ("d", "The fuel use")], "b"),
    ],
}
