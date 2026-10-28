"""Quasicrystals: ordered but never repeating structures, the discovery that changed crystallography, and what they can do."""
CODE = "mining5_quasi"
BOOK = {
    "title": "Quasicrystals",
    "subtitle": "Ordered atoms that never repeat, and the discovery that changed a science",
    "chapters": [
        ("Order without repeats", "For a long time, scientists believed that every solid with sharp diffraction spots had a repeating pattern. Quasicrystals break that rule. Their atoms are ordered, yet the pattern never repeats exactly over space."),
        ("A surprising discovery", "Dan Shechtman saw this in 1982 in a rapidly cooled aluminium and manganese alloy. Its diffraction showed five-fold symmetry, which was thought impossible for a crystal. He was awarded the Nobel Prize in Chemistry in 2011."),
        ("Icosahedral shapes", "Many quasicrystals have icosahedral symmetry, a shape with twenty triangular faces. Their atoms fit around this shape in layers that never line up in a simple repeat. This gives them unusual patterns when X-rays or electrons pass through."),
        ("Reading diffraction", "When an X-ray beam hits a quasicrystal, the pattern of spots shows its hidden order. Scientists read the spots to find the symmetry, and this is how the structure was first understood."),
        ("Properties", "Quasicrystals tend to be hard and brittle at room temperature, and they have low friction surfaces. They are poor conductors of heat compared with ordinary metals. These traits make them interesting for coatings and special tools."),
        ("What they teach", "Quasicrystals showed that the world of solids is wider than the crystal rules taught in schools. Their study has pushed chemists and physicists to rethink how atoms can organise themselves."),
    ],
    "test": [
        ("Which symmetry did Dan Shechtman observe?",
         [("a", "Two-fold"), ("b", "Three-fold"), ("c", "Five-fold"), ("d", "No symmetry at all")], "c"),
        ("In what year was the quasicrystal discovery made?",
         [("a", "1982"), ("b", "1882"), ("c", "1953"), ("d", "2011")], "a"),
        ("What is an icosahedron?",
         [("a", "A type of cloud"), ("b", "A liquid metal"), ("c", "A square box"), ("d", "A shape with twenty triangular faces")], "d"),
        ("What does a quasicrystal do that an ordinary crystal does not?",
         [("a", "It melts at room temperature"), ("b", "Its pattern never repeats exactly"), ("c", "It has no atoms"), ("d", "It floats in air")], "b"),
        ("What was the Nobel Prize awarded for this work?",
         [("a", "Physics in 1950"), ("b", "Peace in 1990"), ("c", "Medicine in 2000"), ("d", "Chemistry in 2011")], "d"),
    ],
}
