"""Electron Microscopy for Failure Analysis: SEM imaging, fractography, EDS composition, TEM basics and sample preparation."""
CODE = "engineering5_em_methods"
BOOK = {
    "title": "Electron Microscopy for Failure Analysis",
    "subtitle": "Looking closely at what went wrong",
    "chapters": [
        ("Why use electrons",
         "Light cannot show detail finer than its own wavelength, but electrons have a much shorter one. An electron microscope uses a beam of electrons to show very small features. This makes it the tool of choice when a part has failed."),
        ("Scanning electron microscopy",
         "A scanning electron microscope, or SEM, moves a focused beam across the surface. Detectors pick up the electrons that bounce back or are knocked loose. The picture shows the shape of the surface in great depth and detail."),
        ("Fractography in the SEM",
         "Fractography is the study of fracture surfaces. The SEM shows the small marks left by how the metal broke. Those marks tell the engineer whether the break was sudden or built up over time."),
        ("Composition with EDS",
         "Energy-dispersive spectroscopy, or EDS, is a detector added to the SEM. When the beam hits an atom, the atom gives off X-rays with energies that are unique to each element. EDS reads those energies to tell which elements are present, such as a dirt particle or a wrong alloy."),
        ("Transmission microscopy",
         "A transmission electron microscope, or TEM, sends electrons through a sample that is thin enough to see through. It shows the arrangement of atoms and defects inside the grains. Making a TEM sample is slow and takes skill."),
        ("Preparing the sample",
         "A poor sample gives a poor answer. Parts are cut carefully to avoid heating the fracture, then cleaned and mounted. A non-conducting sample needs a thin conductive coating so the charge does not build up and blur the image."),
    ],
    "test": [
        ("Why do electron microscopes show finer detail than light microscopes?",
         [("a", "Electrons are brighter than light"), ("b", "The sample is always coloured"), ("c", "They use more lenses"), ("d", "Electrons have a much shorter wavelength")], "d"),
        ("What does an SEM use to build its picture?",
         [("a", "A beam scanned across the surface"), ("b", "A sound wave"), ("c", "A magnet only"), ("d", "A cold liquid")], "a"),
        ("What does EDS tell the engineer?",
         [("a", "The age of the part"), ("b", "The elements present, from the X-rays the sample gives off"), ("c", "The price of the metal"), ("d", "The speed of the crack")], "b"),
        ("What must a TEM sample be?",
         [("a", "Thick and solid"), ("b", "Painted white"), ("c", "Thin enough for electrons to pass through"), ("d", "Frozen in ice")], "c"),
        ("Why is a non-conducting sample given a thin conductive coating?",
         [("a", "So it becomes magnetic"), ("b", "So it will float"), ("c", "So it can be cut again"), ("d", "So charge does not build up and blur the image")], "d"),
    ],
}
