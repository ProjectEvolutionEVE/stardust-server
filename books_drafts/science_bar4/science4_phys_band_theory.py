"""Band Theory of Solids: energy bands, conductors, insulators and semiconductors, and how to read a band diagram."""
CODE = "science4_phys_band_theory"
BOOK = {
    "title": "Band Theory of Solids",
    "subtitle": "Energy bands, conductors, insulators and semiconductors",
    "chapters": [
        ("Electrons in a crystal", "In a single atom, electrons sit at fixed energy levels. When many atoms pack together into a solid, those levels spread out into bands of closely spaced energies. Electrons move within these bands."),
        ("Allowed and forbidden energies", "Between the bands are gaps where no electron state exists. An electron cannot rest in a gap. The pattern of bands and gaps decides how a material carries electric current."),
        ("Conductors", "In a metal, the highest band is partly filled, or it overlaps the next band. Electrons there have empty states nearby to move into. A small voltage makes them drift and carry current."),
        ("Insulators and semiconductors", "In an insulator, the filled bands are separated from the empty band above by a large gap, so electrons almost never cross it. A semiconductor has a smaller gap. Heat or light can lift some electrons across it."),
        ("Doping", "Doping means adding a few foreign atoms to a semiconductor. Some dopants add extra electrons, and others leave extra empty spaces called holes. This control over the current is the basis of most electronic chips."),
        ("The Fermi level", "The Fermi level marks the energy up to which electron states are filled at absolute zero. In a band diagram, it shows where the electrons stop. Reading its position against the gap tells you whether a material is a metal, an insulator or a semiconductor."),
    ],
    "test": [
        ("What is an energy band in a solid?",
         [("a", "One fixed energy level of a single isolated atom"), ("b", "A wire that carries electric current"), ("c", "A range of closely spaced energy levels that electrons can occupy"), ("d", "The boundary of a crystal")], "c"),
        ("What is a band gap?",
         [("a", "A range of energies where no electron states exist"), ("b", "A hole drilled through a crystal"), ("c", "A magnetic field around a wire"), ("d", "The spacing between two neighbouring atoms")], "a"),
        ("In a metal, why can electrons carry current easily?",
         [("a", "They are stuck in fixed atomic orbits"), ("b", "The metal is wrapped in a layer of air"), ("c", "Gravity pulls them along the wire"), ("d", "The top band is partly filled, so empty states are nearby")], "d"),
        ("Why does an insulator carry almost no current?",
         [("a", "It has no electrons at all"), ("b", "A large gap separates the filled bands from the empty band above"), ("c", "It is always above its melting point"), ("d", "Its atoms are too close together")], "b"),
        ("What is doping in a semiconductor?",
         [("a", "Heating it until it melts"), ("b", "Adding a few foreign atoms to add extra electrons or holes"), ("c", "Coating it with metal"), ("d", "Cooling it to absolute zero")], "b"),
    ],
}
