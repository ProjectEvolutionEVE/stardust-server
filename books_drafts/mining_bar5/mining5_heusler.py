"""Heusler Alloys: ordered metal compounds named after Friedrich Heusler, with half-metal, shape memory and spin properties."""
CODE = "mining5_heusler"
BOOK = {
    "title": "Heusler Alloys",
    "subtitle": "Ordered metal compounds with special magnetic and spin properties",
    "chapters": [
        ("A name from 1903", "Friedrich Heusler found in 1903 that an alloy of copper, manganese and aluminium is magnetic, even though none of its parts is strongly magnetic on its own. Alloys of this family are named after him."),
        ("Ordered structures", "Full Heusler alloys have a fixed ordered arrangement of three elements, often written X2YZ. The atoms sit in a neat pattern, which gives the alloy its special properties."),
        ("Half-metals", "Some Heusler alloys are half-metals. In theory, one electron spin type is metallic and the other is insulating. This makes them strong candidates for spintronic devices."),
        ("Shape memory", "Some Heusler alloys, such as nickel manganese gallium, change shape under a magnetic field. This magnetic shape memory effect is studied for actuators."),
        ("Making them", "Heusler alloys are often melted in an arc furnace, then annealed to set the ordered structure. Small changes in composition can shift their properties a great deal."),
        ("Uses", "Research looks at Heusler alloys for spin devices, sensors and actuators. They show how choosing a precise pattern of atoms can create useful behaviour."),
    ],
    "test": [
        ("Who discovered the magnetic Heusler alloy in 1903?",
         [("a", "Isaac Newton"), ("b", "Marie Curie"), ("c", "Friedrich Heusler"), ("d", "Galileo Galilei")], "c"),
        ("What is a half-metal?",
         [("a", "A material that is metallic for one spin type and insulating for the other"), ("b", "A metal that is half the weight of gold"), ("c", "A cut-in-half metal bar"), ("d", "A metal mixed with wood")], "a"),
        ("What is the typical formula of a full Heusler alloy?",
         [("a", "H2O"), ("b", "CO2"), ("c", "NaCl"), ("d", "X2YZ")], "d"),
        ("What is magnetic shape memory?",
         [("a", "Forgetting a name"), ("b", "Changing shape under a magnetic field"), ("c", "Melting when cold"), ("d", "Turning into paper")], "b"),
        ("How are Heusler alloys often made?",
         [("a", "Boiled in tea"), ("b", "Frozen in a bowl"), ("c", "Woven on a loom"), ("d", "Melted in an arc furnace and annealed")], "d"),
    ],
}
