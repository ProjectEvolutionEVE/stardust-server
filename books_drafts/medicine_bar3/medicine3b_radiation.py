"""Medicine, bar 3 (Senior Doctor), part B: Radiation and the Body. Types of radiation, what it does to cells, how doses are measured, and how crews limit exposure."""
CODE = "medicine3b_radiation"
BOOK = {
    "title": "Radiation and the Body",
    "subtitle": "Ionising and other radiation, what it does to cells, and how dose and shielding are measured",
    "chapters": [
        ("Two kinds of radiation",
         "Radiation is energy that travels through space or through matter. Some kinds, such as visible light and radio waves, carry too little energy to change atoms. Ionising radiation, such as X-rays, gamma rays and fast particles, carries enough energy to knock electrons out of atoms."),
        ("What it does to a cell",
         "When ionising radiation passes through a cell, it can damage the DNA, which is the cell's instruction book. Cells have repair systems, and most damage is put right. Damage that cannot be repaired may cause a cell to die, and in rare cases a cell may change in a way that matters over time."),
        ("Measuring a dose",
         "The energy absorbed by the body is measured in grays. The sievert takes account of the type of radiation and the tissue it reaches, so it describes the effect on the body. A sievert is a large amount, so everyday doses are usually counted in millisieverts, which are thousandths of a sievert."),
        ("Radiation on Earth",
         "Everyone receives some background radiation from rocks, soil, the sky and some building materials. On average it adds up to a few millisieverts a year. Flying and living at high altitude add a little more, because the air above is thinner."),
        ("Time, distance and shielding",
         "Three simple ideas limit a dose: spend less time near a source, stay further from it, and put more material between the source and the person. Dense materials such as water, stored supplies and thick walls can absorb some of the energy. Each of these ideas costs something in space, mass or planning, so designers weigh them together."),
        ("Radiation in space",
         "Beyond Earth's magnetic field and air, crews receive more radiation from the Sun and from cosmic rays. A solar storm can raise the dose for a short time, so crews may spend those hours in the most shielded parts of the ship. Monitoring and careful planning keep exposure within the limits set by safety bodies."),
    ],
    "test": [
        ("Which kind of radiation carries enough energy to knock electrons out of atoms?",
         [("a", "Radio waves"), ("b", "Visible light"), ("c", "Ionising radiation, such as X-rays"), ("d", "Warm air")], "c"),
        ("What does ionising radiation most often damage inside a cell?",
         [("a", "The cell's outer wall only"), ("b", "The DNA, the cell's instruction book"), ("c", "The colour of the cell"), ("d", "The cell's water supply")], "b"),
        ("What does the sievert measure?",
         [("a", "The speed of a solar storm"), ("b", "The number of cells in a crew member"), ("c", "The mass of a shield"), ("d", "The effect of a dose on the body, adjusted for the type of radiation and the tissue")], "d"),
        ("Roughly how much background radiation does a person on Earth receive each year, on average?",
         [("a", "A few millisieverts"), ("b", "Several thousand sieverts"), ("c", "None at all"), ("d", "Only during flights")], "a"),
        ("Which set lists the three simple ways to limit a radiation dose?",
         [("a", "Bright light, loud noise and cold air"), ("b", "More time, closer distance and less shielding"), ("c", "Less time, more distance and more shielding"), ("d", "Fresh air, sweet food and more light")], "c"),
    ],
}
