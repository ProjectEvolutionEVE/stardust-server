"""Electronics: real-world basics of circuits and the materials they're made from."""
CODE = "electronics"
BOOK = {
    "title": "Electronics",
    "subtitle": "Circuits, conductors and the materials that make them work",
    "chapters": [
        ("Electricity in one minute",
         "Electricity is a flow of tiny charged particles called electrons. Voltage is the push, measured in volts. "
         "Current is how much flows, measured in amps. Resistance is how hard the material makes it, measured in ohms."),
        ("The circuit",
         "Electricity only flows around a complete loop: from the power source, through the device, and back again. "
         "Break the loop anywhere and everything stops. A switch is simply a safe way to break the loop."),
        ("Ohm's law",
         "One simple rule ties it together: volts = amps × ohms. Double the push and, with the same resistance, you "
         "double the current. Too much current heats wires up, which is why circuits have fuses and breakers."),
        ("Conductors and insulators",
         "Conductors let electricity through easily. Silver is the best of all, and copper is a close second and far "
         "more common, so most wires are copper. Gold is used on connectors because it does not corrode. Insulators "
         "such as glass, ceramics and plastics block electricity and keep it where it belongs."),
        ("Semiconductors",
         "Silicon sits in between: a semiconductor. With a tiny bit of another element added, such as boron or "
         "phosphorus, it can be made to switch current on and off. Billions of these switches, called transistors, "
         "make up the chips in every computer, scanner and ship's console."),
        ("Electronics in space",
         "Space is hard on electronics. Radiation can flip bits and wear out chips, and there is no air to carry heat "
         "away, so heat has to be conducted out through metal and radiated into space. Space electronics are built "
         "tough and kept cool."),
        ("Electronics aboard",
         "Many raw materials in the catalogue go into electronics: copper, silver and gold, silicon, boron and "
         "phosphorus, and rare earths such as neodymium. A player designing a blueprint with electronic parts lists "
         "these materials and their amounts, like any other."),
    ],
    "test": [
        ("What is voltage?",
         [("a", "The push that drives electricity"), ("b", "A kind of wire"), ("c", "How heavy a battery is"), ("d", "A unit of heat")], "a"),
        ("What does electricity need in order to flow?",
         [("a", "Sunlight"), ("b", "A complete loop (circuit)"), ("c", "Water"), ("d", "A magnet")], "b"),
        ("Which metal are most wires made of?",
         [("a", "Iron"), ("b", "Lead"), ("c", "Copper"), ("d", "Titanium")], "c"),
        ("Which material is used to make computer chips?",
         [("a", "Silicon"), ("b", "Clay"), ("c", "Gold"), ("d", "Water ice")], "a"),
        ("Why is gold used on connectors?",
         [("a", "It is the lightest metal"), ("b", "It does not corrode"), ("c", "It is magnetic"), ("d", "It glows")], "b"),
    ],
}
