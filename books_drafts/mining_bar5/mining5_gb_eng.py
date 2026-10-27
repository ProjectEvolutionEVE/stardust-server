"""Grain Boundary Engineering: choosing special grain boundaries that resist corrosion, and how they are measured and made."""
CODE = "mining5_gb_eng"
BOOK = {
    "title": "Grain Boundary Engineering",
    "subtitle": "Choosing the best boundaries between grains to fight corrosion",
    "chapters": [
        ("Boundaries matter", "Between each pair of grains is a boundary, a thin zone where the atoms do not line up. Boundaries are often where corrosion, cracking and wear begin. Changing the boundaries can change how a metal lasts."),
        ("Special boundaries", "Some boundaries have a neat, low energy arrangement. These are called special boundaries. A common type is the coherent twin boundary, which has a mirror arrangement of atoms across it."),
        ("Why twins help", "In certain stainless steels, special boundaries resist sensitisation, the chromium loss that lets corrosion spread along boundaries. A high share of these boundaries makes the steel more resistant."),
        ("Processing", "Makers use cycles of cold working and annealing to increase the share of special boundaries. The annealing temperature and time are set carefully so the new boundaries form."),
        ("Measuring boundaries", "Electron backscatter diffraction is the main tool. It shows each grain orientation, and from that the type of each boundary. Engineers then report the share of special boundaries."),
        ("Alloys in use", "Grain boundary engineering is used for some nickel alloys and austenitic stainless steels. It is an example of making a metal better by designing its internal structure, not only its chemistry."),
    ],
    "test": [
        ("Where does corrosion often start in a metal?",
         [("a", "In the centre of the sky"), ("b", "On the surface paint only"), ("c", "At grain boundaries"), ("d", "In wood fibres")], "c"),
        ("What is a coherent twin boundary?",
         [("a", "A boundary with a mirror arrangement of atoms"), ("b", "A type of paint"), ("c", "A gas bubble"), ("d", "A glass window")], "a"),
        ("What is sensitisation?",
         [("a", "Making a metal sound louder"), ("b", "Turning metal into powder"), ("c", "Freezing the metal in ice"), ("d", "Chromium loss along boundaries that lets corrosion spread")], "d"),
        ("Which tool is the main way to measure boundary types?",
         [("a", "A kitchen scale"), ("b", "Electron backscatter diffraction"), ("c", "A ruler"), ("d", "A thermometer in water")], "b"),
        ("What do makers use to raise the share of special boundaries?",
         [("a", "Adding water to the metal"), ("b", "Leaving it in salt"), ("c", "Painting it red"), ("d", "Cold working and annealing cycles")], "d"),
    ],
}
