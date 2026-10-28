"""Transmission Electron Microscopy of Alloys: seeing dislocations and precipitates by passing electrons through a very thin metal foil."""
CODE = "mining5_tem"
BOOK = {
    "title": "Transmission Electron Microscopy of Alloys",
    "subtitle": "Seeing dislocations and precipitates through a metal foil",
    "chapters": [
        ("Electrons through metal", "In transmission electron microscopy, a beam of electrons passes through a very thin sample. The electrons that get through carry an image of the atoms and defects inside the metal."),
        ("A thin foil", "The sample must be about a hundred nanometres thick or less, so that electrons can pass through. Thinning is done by electropolishing or by ion milling."),
        ("Diffraction patterns", "Electrons scattered by crystal planes form a diffraction pattern of spots. Tilting the sample and reading the pattern gives the crystal orientation and the phases present."),
        ("Dislocations", "Dislocations are line defects that let metals bend. They can be imaged by choosing the right diffraction condition, which makes them show up as dark lines."),
        ("Precipitates", "Tiny precipitates, such as those formed in aluminium alloys, can be seen directly. Their size, shape and spacing decide how strong the alloy becomes."),
        ("Interpreting the image", "Images can mislead if the sample is tilted wrongly or the thickness changes. Experts check several views before they draw a conclusion."),
    ],
    "test": [
        ("What passes through the sample in transmission electron microscopy?",
         [("a", "Water"), ("b", "Sand"), ("c", "Wood chips"), ("d", "Electrons")], "d"),
        ("About how thick must the sample be?",
         [("a", "About a metre"), ("b", "About a hundred nanometres or less"), ("c", "About a kilometre"), ("d", "About a centimetre")], "b"),
        ("What do dislocations allow a metal to do?",
         [("a", "Bend"), ("b", "Glow"), ("c", "Float"), ("d", "Freeze instantly")], "a"),
        ("How are thin foils made?",
         [("a", "By baking them in bread"), ("b", "By freezing them in snow"), ("c", "By electropolishing or ion milling"), ("d", "By tearing them by hand")], "c"),
        ("What do precipitates decide in an alloy?",
         [("a", "How strong it becomes"), ("b", "What colour it is in shade"), ("c", "What shape its box has"), ("d", "Where it was bought")], "a"),
    ],
}
