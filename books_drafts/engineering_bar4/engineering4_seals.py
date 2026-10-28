"""Seals, O-Rings and Gaskets: squeeze and gap limits, fluid compatibility, lip seals, failure modes and installation."""
CODE = "engineering4_seals"
BOOK = {
    "title": "Seals, O-Rings and Gaskets",
    "subtitle": "Squeeze, compatibility, lip seals and failure",
    "chapters": [
        ("Squeeze and gap",
         "An O-ring must be squeezed enough to seal, but not so much that it is damaged. The gap it fills must be small enough that the seal cannot be pushed into it."),
        ("Compatibility",
         "A seal material must suit the fluid, the temperature and the pressure. Some fluids swell or harden rubber."),
        ("Lip seals",
         "A lip seal has a flexible lip that presses on a shaft. It holds fluid in and keeps dirt out."),
        ("Failure modes",
         "Seals fail by wear, hardening, extrusion into a gap, chemical attack or heat damage. Knowing the failure modes guides the choice of seal."),
        ("Choosing a seal material",
         "Compare the fluid, temperature, pressure, speed and cost, and check the supplier's data before deciding. Ask the supplier for test data on the exact fluid in use."),
        ("Installation",
         "Clean surfaces and correct fitting prevent many early leaks. Check the seal and its groove for damage before fitting."),
    ],
    "test": [
        ("Why must an O-ring be squeezed?",
         [("a", "So it seals without damage"), ("b", "So it glows"), ("c", "So it sings"), ("d", "So it is painted")], "a"),
        ("What does a lip seal do?",
         [("a", "Heats the shaft"), ("b", "Measures flow"), ("c", "Paints the shaft"), ("d", "Holds fluid in and keeps dirt out")], "d"),
        ("What can make a rubber seal harden or swell?",
         [("a", "Paint colour"), ("b", "Some fluids"), ("c", "Music"), ("d", "Sunlight in a box")], "b"),
        ("What is extrusion?",
         [("a", "A cake"), ("b", "A fuel"), ("c", "A seal pushed into a gap it should not fill"), ("d", "A paint")], "c"),
        ("What helps prevent early leaks?",
         [("a", "Clean surfaces and correct fitting"), ("b", "Dirty surfaces"), ("c", "Wrong fitting"), ("d", "Loud music")], "a"),
    ],
}
