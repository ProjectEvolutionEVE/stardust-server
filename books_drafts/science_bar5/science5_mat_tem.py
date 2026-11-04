"""Electron Microscopy of Materials: how electron beams reveal structure, composition and crystal orientation in materials."""
CODE = "science5_mat_tem"
BOOK = {
    "title": "Electron Microscopy of Materials",
    "subtitle": "Seeing inside materials with a beam of electrons",
    "chapters": [
        ("Why electrons", "Electrons have a much shorter wavelength than visible light. That lets an electron microscope resolve much finer detail than a light microscope. It is the main tool for seeing structure at the nanometre scale."),
        ("Beam interactions", "The electron beam interacts with the sample in several ways. Electrons scatter, and X-rays are emitted. Detectors record these signals to build images and analyse the material."),
        ("Imaging modes", "A transmission electron microscope, or TEM, forms images from electrons that pass through a thin sample. Bright-field and dark-field images show different features. A scanning electron microscope, or SEM, forms images from electrons emitted from the surface."),
        ("Diffraction patterns", "When the beam passes through a crystal, it forms a diffraction pattern of spots. The pattern reveals the crystal structure and how the crystal is oriented. It is a fingerprint of the material."),
        ("EDS analysis", "Energy-dispersive X-ray spectroscopy, or EDS, identifies elements from the characteristic X-rays they emit. It tells us which elements are present and roughly how much. It is often paired with imaging."),
        ("Sample preparation and resolution", "TEM samples must be very thin so the beam can pass through. Preparing them takes skill and can introduce artefacts. The resolution limit depends on the lens quality, the sample and the instrument's alignment."),
    ],
    "test": [
        ("Why can an electron microscope see finer detail than a light microscope?",
         [("a", "Electrons are bigger"), ("b", "Electrons have a much shorter wavelength"), ("c", "Electrons are colder"), ("d", "Electrons are slower")], "b"),
        ("What does a diffraction pattern reveal?",
         [("a", "The weight of a sample"), ("b", "The taste of a sample"), ("c", "The smell of a sample"), ("d", "Crystal structure and orientation")], "d"),
        ("What does EDS analysis identify?",
         [("a", "Which elements are present, from their characteristic X-rays"), ("b", "The price of a sample"), ("c", "The taste of a sample"), ("d", "The history of a sample")], "a"),
        ("Why must a TEM sample be very thin?",
         [("a", "So it fits in a box"), ("b", "So it cools quickly"), ("c", "So the electron beam can pass through it"), ("d", "So it glows")], "c"),
        ("What limits the resolution of an electron microscope?",
         [("a", "The colour of the sample"), ("b", "Factors such as lens quality and the sample"), ("c", "Background music in the lab"), ("d", "The weather outside")], "b"),
    ],
}
