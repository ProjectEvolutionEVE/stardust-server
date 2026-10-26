"""Magnetometers: Reading the Field. Sensing the magnetic field to find a rough heading, and the traps that make it less reliable than it looks."""
CODE = "navigation3c_magnetometers"
BOOK = {
    "title": "Magnetometers: Reading the Field",
    "subtitle": "Sensing the magnetic field for a rough heading, and the traps that make it less reliable than it looks",
    "chapters": [
        ("A compass that senses",
         "A magnetometer measures the strength and direction of a magnetic field. Earth has a magnetic field, so a magnetometer can give a rough heading. It does the job of the old compass needle, but it reads the field electronically."),
        ("How strong the field is",
         "At Earth's surface the field is roughly 25 to 65 microtesla, depending on where you are. A magnetometer must be sensitive enough to detect that, and it must know the field's expected value at its location."),
        ("Comparing with a model",
         "Navigators compare a reading with a model of the field, such as the International Geomagnetic Reference Field. The model gives the expected value at a place and time. The difference shows the local error, or warns that something nearby is disturbing the field."),
        ("Disturbances from the craft",
         "The craft makes magnetic fields of its own, from electric currents, motors and steel parts. A magnetometer is therefore mounted on a boom or away from the electronics, so the craft's own field does not confuse the reading."),
        ("Weaker away from home",
         "Far from Earth the field is much weaker, and it changes as the craft moves through the solar wind. A magnetometer in the wrong place may read a field that is weak, strong or twisted, which makes its heading less useful."),
        ("A helper, not a judge",
         "A magnetometer gives a rough check on heading, and it works best blended with other sensors. It is cheap and light. It cannot tell you where you are, and it is easily fooled near metal or electric currents."),
    ],
    "test": [
        ("What does a magnetometer measure?",
         [("a", "Sound"), ("b", "The strength and direction of a magnetic field"), ("c", "Air pressure"), ("d", "Light from stars")], "b"),
        ("Roughly what is Earth's magnetic field at the surface?",
         [("a", "About 25 to 65 microtesla"), ("b", "About 25 to 65 nanotesla"), ("c", "About 25 to 65 kilograms"), ("d", "About 25 to 65 metres")], "a"),
        ("What is the International Geomagnetic Reference Field used for?",
         [("a", "Making the hull shine"), ("b", "Setting the speed limit"), ("c", "Giving the expected field at a place and time, to compare with a reading"), ("d", "Measuring fuel")], "c"),
        ("Why is a magnetometer often mounted away from the craft's electronics?",
         [("a", "So it can see the stars"), ("b", "So it can run cooler"), ("c", "Because it needs sunlight"), ("d", "So the craft's own currents and steel do not disturb its reading")], "d"),
        ("What should a navigator do with a magnetometer's heading?",
         [("a", "Treat it as certain"), ("b", "Blend it with other sensors and check it"), ("c", "Throw it away"), ("d", "Use it only near steel")], "b"),
    ],
}
