"""Three-Dimensional Induced Polarisation: sending current into the ground through arrays of electrodes to image chargeable sulphide bodies in depth."""
CODE = "mining5_ip3d"
BOOK = {
    "title": "Three-Dimensional Induced Polarisation",
    "subtitle": "Electrode arrays, inversion, sulphide shells and depth",
    "chapters": [
        ("Current into the ground",
         "Induced polarisation sends an electric current into the ground through electrodes. When the current is switched off, some materials hold a charge for a short time. This delayed response is called chargeability."),
        ("Electrode arrays",
         "In three dimensions, electrodes are laid out as grids rather than single lines. A grid sees the ground in many directions. More electrodes give more data, but also need more time and care in laying them out."),
        ("Inversion",
         "Raw measurements are turned into a three-dimensional model of chargeability by inversion. The computer adjusts the model until it matches the measured data. The result is a volume, not a single cross-section."),
        ("Sulphide shells",
         "Sulphide minerals are very chargeable. Some deposits form shells of sulphide around an intrusion, and the shells show up clearly in the model. Geologists then test the shells with drilling."),
        ("Acquisition and depth",
         "Depth of view depends on the spacing and length of the electrode layout. Deep targets need wider layouts and stronger current. Good acquisition plans balance depth against detail."),
        ("Data handling",
         "Three-dimensional surveys produce large data sets. Careful checks remove bad readings before inversion. Records of each step keep the work open to review."),
    ],
    "test": [
        ("What does induced polarisation measure?",
         [("a", "How long a material holds a charge after current is switched off"), ("b", "The colour of the sky"), ("c", "The speed of wind"), ("d", "The number of birds")], "a"),
        ("Why are electrodes laid out as grids in three-dimensional surveys?",
         [("a", "To keep the cables warm"), ("b", "To make the field smaller"), ("c", "To see the ground in many directions"), ("d", "To avoid collecting any data")], "c"),
        ("What is inversion?",
         [("a", "Turning a line of readings upside down"), ("b", "Painting the electrodes"), ("c", "Turning off the power for good"), ("d", "Adjusting a model until it matches the measured data")], "d"),
        ("Why do sulphide minerals show up strongly?",
         [("a", "They are always invisible"), ("b", "They are very chargeable"), ("c", "They are made of water"), ("d", "They are always very cold")], "b"),
        ("What controls how deep a survey can see?",
         [("a", "The spacing and length of the electrode layout"), ("b", "The colour of the cable"), ("c", "The name of the surveyor"), ("d", "The time of day only")], "a"),
    ],
}
