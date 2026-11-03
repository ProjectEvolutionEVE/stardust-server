"""Cosmogenic Nuclides and Surface Exposure Dating. How cosmic rays leave a clock in the rocks at the surface."""
CODE = "science5_geo_exposure_dating"
BOOK = {
    "title": "Cosmogenic Nuclides and Surface Exposure Dating",
    "subtitle": "Dating how long a rock surface has been exposed to space",
    "chapters": [
        ("Cosmic rays",
         "Cosmic rays from space strike the upper atmosphere and send a shower of particles down to the ground. Some of these particles strike atoms in surface rock and make rare new atoms, called cosmogenic nuclides."),
        ("Nuclide accumulation",
         "The longer a rock surface stays exposed, the more cosmogenic nuclides build up in its minerals. Measuring the amount and knowing the production rate gives an exposure age for the surface."),
        ("Erosion correction",
         "If the surface erodes, it removes some of the nuclides and the age comes out too young. Scientists must estimate erosion from the landscape and correct for it, or state clearly the range of possible ages."),
        ("Moraine dating",
         "When a glacier retreats, it leaves boulders on its moraine. Dating the boulder surfaces with cosmogenic nuclides shows when the ice left them, which helps reconstruct past glacier changes."),
        ("Burial dating",
         "Some rocks are buried quickly after exposure, and their nuclides decay during burial. Comparing two nuclides with different decay rates can reveal how long a sediment has been buried."),
        ("Sampling strategy",
         "Good sampling chooses flat, stable surfaces, records the shielding by nearby terrain and collects several samples. Agreement among samples builds confidence in the age."),
    ],
    "test": [
        ("What are cosmogenic nuclides?",
         [("a", "Fossils of tiny sea animals"), ("b", "Rare atoms made when cosmic rays strike rock at the surface"), ("c", "Sugar molecules from plants"), ("d", "Magnetic minerals from volcanoes")], "b"),
        ("What happens to the amount of cosmogenic nuclides as a surface stays exposed?",
         [("a", "It falls to zero within a year"), ("b", "It builds up over time"), ("c", "It stays exactly the same forever"), ("d", "It depends only on the colour of the rock")], "b"),
        ("What effect does erosion have on an exposure age?",
         [("a", "It makes the age too old"), ("b", "It has no effect at all"), ("c", "It removes nuclides, so the age comes out too young"), ("d", "It makes the rock melt")], "c"),
        ("What do dated boulders on a moraine help reconstruct?",
         [("a", "Past glacier changes"), ("b", "The number of volcanoes in Africa"), ("c", "Ocean salinity"), ("d", "The speed of light")], "a"),
        ("Why should several samples be collected in exposure dating?",
         [("a", "Agreement among samples builds confidence in the age"), ("b", "Each sample must be from a different continent"), ("c", "Samples must be heated in a furnace first"), ("d", "Only one sample ever gives a true age")], "a"),
    ],
}
