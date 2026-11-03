"""Magnetotellurics and Electrical Imaging. Using natural electromagnetic fields to image rock conductivity underground."""
CODE = "science5_geo_magnetotellurics"
BOOK = {
    "title": "Magnetotellurics and Electrical Imaging",
    "subtitle": "Mapping underground electrical conductivity with natural fields",
    "chapters": [
        ("Natural electric and magnetic fields",
         "The Sun and lightning produce natural electromagnetic fields that reach the ground. Magnetotellurics measures these fields at the surface and uses them to image the electrical structure of the rock below."),
        ("Apparent resistivity",
         "Apparent resistivity is a measure of how strongly the ground resists the flow of electric current, calculated from the electric and magnetic fields. It is called apparent because it reflects the average response of many layers."),
        ("Impedance tensors",
         "The impedance tensor links the electric and magnetic fields at each frequency. Its values show how the ground responds, and they help separate the effects of different directions of structure."),
        ("Resistivity imaging",
         "Measurements at many frequencies and stations are combined into a resistivity model. Low resistivity often marks fluids, clays, graphite or melt, while high resistivity marks dry, solid rock."),
        ("Fluid and melt detection",
         "Water-rich rock and partly molten rock are more conductive than dry rock. Magnetotelluric surveys have been used to look for fluids in fault zones and melt beneath volcanoes."),
        ("Inversion limits",
         "Converting measured data into a model is an inversion, and many different models can fit the same data. Scientists test how well the model is constrained and state the limits of what the image can show."),
    ],
    "test": [
        ("What natural sources drive the fields used in magnetotellurics?",
         [("a", "Ocean waves and tides only"), ("b", "The Sun and lightning"), ("c", "Volcanic ash"), ("d", "Earthquake slip")], "b"),
        ("What does apparent resistivity measure?",
         [("a", "How easily the ground carries electric current"), ("b", "How high a mountain stands"), ("c", "How fast a river flows"), ("d", "How heavy a rock is")], "a"),
        ("What does low resistivity often indicate underground?",
         [("a", "Fluids, clays, graphite or melt"), ("b", "Pure dry granite"), ("c", "Hard quartz with no water"), ("d", "Open air in a cave")], "a"),
        ("Why is an inversion limited?",
         [("a", "Only one model can ever fit data"), ("b", "Inversions are done with a camera"), ("c", "Inversions need no data at all"), ("d", "Many different models can fit the same data")], "d"),
        ("Which underground feature is detected by magnetotelluric surveys?",
         [("a", "Melt beneath volcanoes"), ("b", "The colour of tree leaves"), ("c", "Ocean salinity at the surface"), ("d", "Radio stations in the sky")], "a"),
    ],
}
