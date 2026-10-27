"""Compliant Mechanisms and Flexure Hinges: flexure hinges, stress limits, precision motion, compliance modelling and fatigue life."""
CODE = "engineering5_compliant"
BOOK = {
    "title": "Compliant Mechanisms and Flexure Hinges",
    "subtitle": "Motion from bending, with no sliding parts",
    "chapters": [
        ("Motion from bending",
         "A compliant mechanism moves because its parts flex, rather than because they slide or turn on pins. A single solid piece can carry the whole motion. This removes many of the parts that normally wear out."),
        ("Flexure hinges",
         "A flexure hinge is a thin, narrowed section that bends to act as a joint. It is made in one piece with the parts around it. Its motion is smooth and predictable, because there are no sliding surfaces."),
        ("Stress limits",
         "Bending puts stress into the flexure. Stress is highest at the thinnest section, and it must stay below the level the material can take. Designers keep the flexure's shape and size within safe limits."),
        ("Precision motion",
         "Without friction or backlash from sliding joints, a flexure can give very fine and repeatable motion. This makes flexures useful in precision tools, optical mounts and sensors. The motion is usually small, but very controlled."),
        ("Compliance modelling",
         "Engineers model how much a flexure deflects under a given load. The model is checked against tests, because small errors in the shape can change the result. A good model lets the designer predict the motion before building."),
        ("Fatigue life",
         "A flexure bends back and forth many times over its life, and this cycling can cause cracks. Fatigue life is the number of cycles the part can take before it fails. Designers set the stress low enough that the part lasts the planned number of cycles."),
    ],
    "test": [
        ("What is a flexure hinge?",
         [("a", "A hinge made by bending a thin section of one solid piece"), ("b", "A door hinge with pins"), ("c", "A chain link"), ("d", "A bolt")], "a"),
        ("What makes compliant mechanisms attractive for precision?",
         [("a", "They are noisy"), ("b", "They are painted"), ("c", "They have no friction or backlash from sliding joints"), ("d", "They use glue")], "c"),
        ("What is the main stress concern in a flexure?",
         [("a", "Colour"), ("b", "Stress concentrates at the thin section, which may limit its life"), ("c", "Sound"), ("d", "Price")], "b"),
        ("What is fatigue life in flexure design?",
         [("a", "Time spent painting"), ("b", "Time spent heating"), ("c", "Time spent in meetings"), ("d", "The number of flex cycles before cracking")], "d"),
        ("What must compliance modelling predict?",
         [("a", "How much the mechanism deflects under a load"), ("b", "The paint colour"), ("c", "The designer's name"), ("d", "The price")], "a"),
    ],
}
