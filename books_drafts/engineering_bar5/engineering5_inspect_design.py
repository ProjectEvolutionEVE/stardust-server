"""Designing Parts for Inspectability: how design choices decide whether a part can be checked quickly and reliably."""
CODE = "engineering5_inspect_design"
BOOK = {
    "title": "Designing Parts for Inspectability",
    "subtitle": "Probe access, datums and designs that are easy to check",
    "chapters": [
        ("Design for inspection", "The easiest parts to inspect are designed with inspection in mind from the start. Adding inspection later is always harder and more costly."),
        ("Probe access", "Inspection probes need room to reach the surface. A design that blocks access can hide defects, so the inspector may never see them."),
        ("Measurement datums", "A datum is a fixed reference that all measurements start from. Naming datums early lets readings from different people and machines be compared."),
        ("Testability", "A part that can be tested quickly and reliably saves time at every stage, from the first prototype to the last production run."),
        ("The money side", "Inspection uses machine time and people's time. Designs that need less of each save money on every part made."),
        ("Design rules", "Keep surfaces reachable, name datums early, and leave room for probes and sensors. These rules cost little at the drawing board and save much later."),
    ],
    "test": [
        ("What is a datum?", [("a", "A kind of bolt"), ("b", "A colour used on drawings"), ("c", "A type of seal"), ("d", "A fixed reference that measurements start from")], "d"),
        ("Why must probes have access to the part?", [("a", "To reach the surface and see defects"), ("b", "To make the part heavier"), ("c", "To change the colour of the part"), ("d", "To remove the datum")], "a"),
        ("What does design for inspection aim to do?", [("a", "Add weight to the part"), ("b", "Remove all datums"), ("c", "Make parts easy to test reliably"), ("d", "Hide the surfaces from view")], "c"),
        ("Why does inspection time cost money?", [("a", "It changes the datum"), ("b", "It uses machine and people's time"), ("c", "It adds sound to the factory"), ("d", "It uses only paint")], "b"),
        ("What happens when a design blocks probe access?", [("a", "The part gets lighter"), ("b", "The colour changes"), ("c", "The datum moves by itself"), ("d", "Defects can be hidden")], "d"),
    ],
}
