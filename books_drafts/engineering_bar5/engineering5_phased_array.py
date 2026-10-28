"""Phased Array Ultrasonic Testing: steering and focusing an ultrasonic beam electronically, to image and size flaws in a part."""
CODE = "engineering5_phased_array"
BOOK = {
    "title": "Phased Array Ultrasonic Testing",
    "subtitle": "Beam steering, focal laws, imaging and coverage plans",
    "chapters": [
        ("Many elements, one beam", "A phased array probe has many small elements, each pulsed on its own timing. Together they make one beam that can be shaped and aimed."),
        ("Beam steering", "By changing the timing of the pulses, the combined beam can be steered to an angle without moving the probe. This makes scanning fast and repeatable."),
        ("Focal laws", "The set of timing delays used for a given angle or focus is called a focal law. Each inspection uses a set of these laws, chosen for the part."),
        ("Imaging", "Scanning the beam over many angles builds an image of the inside of the part. The image shows where reflections come from."),
        ("Sizing flaws", "The shape of the echo and the spread of the beam help estimate how big a flaw is. This is needed to judge whether it is acceptable."),
        ("Coverage plans", "An inspection plan shows which angles and scans cover each part of the weld or component. Gaps in coverage must be found on paper before the inspection."),
    ],
    "test": [
        ("What lets a phased array steer its beam?", [("a", "A can of paint"), ("b", "A water pump"), ("c", "A permanent magnet"), ("d", "The timing of pulses from many elements")], "d"),
        ("What is a focal law?", [("a", "The set of timing delays for a given angle or focus"), ("b", "A court ruling on fair trade"), ("c", "A rule for mixing paint"), ("d", "A type of tax")], "a"),
        ("What does an inspection image show?", [("a", "The inside of a part"), ("b", "The price of the probe"), ("c", "The operator's name"), ("d", "The room temperature")], "a"),
        ("What can the shape of an echo help with?", [("a", "Showing the brand of the probe"), ("b", "Setting the room light"), ("c", "Estimating how big a flaw is"), ("d", "Telling the time")], "c"),
        ("What does a coverage plan show?", [("a", "The cost of coffee in the lab"), ("b", "Which angles and scans cover each part of the component"), ("c", "The weather in the shop"), ("d", "The name of the designer")], "b"),
    ],
}
