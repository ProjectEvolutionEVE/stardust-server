"""Piezoelectric and Ferroelectric Materials: crystals whose built-in polarisation can be switched, and that turn force into charge."""
CODE = "science5_mat_piezo"
BOOK = {
    "title": "Piezoelectric and Ferroelectric Materials",
    "subtitle": "Crystals that turn pressure into electricity, and back again",
    "chapters": [
        ("Polarisation", "Some materials have built-in electric dipoles. These line up in regions called domains. The total polarisation depends on how the domains are arranged."),
        ("Domain switching", "An electric field can flip the direction of the domains. This switching is the basis of ferroelectric memory and some actuators. It is a clear example of a material responding to its environment."),
        ("Piezoelectric coefficients", "A piezoelectric material makes electric charge when it is squeezed or stretched. The coefficient measures how much charge results from each unit of stress. The reverse effect also holds."),
        ("Sensors and actuators", "Pressure sensors, microphones and small precise motors use these materials. A sensor turns force into a signal, and an actuator turns an electric field into motion. Both are used widely."),
        ("Lead-free options", "Many strong piezoelectric ceramics contain lead, which is toxic. Researchers study lead-free alternatives that still perform well. Finding a match is an active field."),
        ("Fatigue", "Repeated switching can wear a ferroelectric material out. Over many cycles its response can weaken. Fatigue sets the working life of a device."),
    ],
    "test": [
        ("What is polarisation in these materials?",
         [("a", "Bending of light"), ("b", "Noise"), ("c", "Colour"), ("d", "Built-in electric dipoles that can line up")], "d"),
        ("What does domain switching allow?",
         [("a", "Flipping the direction of polarisation with an electric field"), ("b", "Changing the colour of glass"), ("c", "Boiling water"), ("d", "Making a sound")], "a"),
        ("What do piezoelectric materials do?",
         [("a", "Glow in the dark"), ("b", "Change colour"), ("c", "Turn mechanical stress into electric charge, and the reverse"), ("d", "Dissolve in water")], "c"),
        ("Why do researchers study lead-free options?",
         [("a", "Lead is cheaper"), ("b", "Lead is toxic, so safer materials are wanted"), ("c", "Lead is too cold"), ("d", "Lead is too bright")], "b"),
        ("What can repeated switching cause?",
         [("a", "A longer working life"), ("b", "A nicer colour"), ("c", "Fatigue that wears the material out"), ("d", "Endless power")], "c"),
    ],
}
