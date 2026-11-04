"""X-ray Diffraction in Materials: reading the atomic arrangement of a crystal from its X-ray pattern."""
CODE = "science4_mat_xrd"
BOOK = {
    "title": "X-ray Diffraction in Materials",
    "subtitle": "Reading a crystal's fingerprint with X-rays",
    "chapters": [
        ("What XRD does", "X-ray diffraction, or XRD, shines X-rays on a material and records the directions where they bounce back strongly. Crystals send X-rays off in clear directions, so the pattern tells us about the atoms inside. It is one of the most used tools in materials science."),
        ("Bragg's law", "Bragg's law says that n times lambda equals two times d times the sine of theta. Here lambda is the X-ray wavelength, d is the spacing between atomic planes, and theta is the angle. A strong reflection appears when this rule is met, so the angle reveals the spacing."),
        ("Reading a pattern", "A diffraction pattern plots intensity against angle, and each peak marks one set of planes. The positions of the peaks match a crystal structure, like a fingerprint. Peak height and width carry further information about the sample."),
        ("Phase identification", "To identify a material, analysts compare its peaks with reference patterns in a database. A match means the same crystal phase is present. A mixture of phases shows peaks from each one, so this method can reveal impurities."),
        ("Crystallite size", "Very small crystals make the peaks broader. The Scherrer equation links the peak width to an estimated crystallite size. The method works best for crystals in the nanometre range, and strain can also broaden peaks."),
        ("Sample preparation", "Good results need a fine, flat powder, packed well and spread at random orientations, so that all the crystals show their planes. Large grains or a preferred orientation can distort the peak heights. A careful sample is as important as a careful instrument."),
    ],
    "test": [
        ("What does XRD mainly reveal about a material?",
         [("a", "Its taste"), ("b", "Its price"), ("c", "Its weight in grams"), ("d", "The arrangement of atoms in its crystals")], "d"),
        ("In Bragg's law, what does d represent?",
         [("a", "The detector distance"), ("b", "The spacing between atomic planes"), ("c", "The X-ray dose"), ("d", "The sample's density")], "b"),
        ("How is a phase usually identified in XRD?",
         [("a", "By tasting the sample"), ("b", "By weighing the sample"), ("c", "By matching peak positions to a reference database"), ("d", "By measuring its colour")], "c"),
        ("What does a broad diffraction peak often suggest?",
         [("a", "Very small crystallites"), ("b", "A very large single crystal only"), ("c", "A perfectly clean glass"), ("d", "A sample that is too heavy")], "a"),
        ("Why must a powder sample be fine and randomly oriented?",
         [("a", "So it dissolves in water"), ("b", "So all crystal planes can show up in the pattern"), ("c", "So it reflects light"), ("d", "So it stays warm")], "b"),
    ],
}
