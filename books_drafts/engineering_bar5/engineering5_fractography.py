"""Fractography: Reading Fracture Surfaces. Beach marks, striations, dimples, cleavage, and tracing a crack back to its origin."""
CODE = "engineering5_fractography"
BOOK = {
    "title": "Fractography: Reading Fracture Surfaces",
    "subtitle": "What a broken part can tell you about how it broke",
    "chapters": [
        ("A broken part is a record",
         "Every break leaves a surface that tells its own story. By reading that surface, an engineer can often tell how the part failed, and sometimes why. This reading is called fractography."),
        ("Beach marks",
         "Beach marks are curved ridges on a fatigue surface. They look like the lines left on a sandy shore by the tide. Each mark shows where the crack paused or grew in a new stage of loading."),
        ("Striations",
         "Striations are very fine lines on a fatigue surface, one for each load cycle in many metals. Their spacing can show how fast the crack grew. Striations point the engineer toward the crack's direction of travel."),
        ("Dimples and overload",
         "A surface full of small cup-shaped dimples means the metal stretched a lot before it broke. This is ductile fracture, often from a single overload. Dimples are a sign that the metal had some give before it failed."),
        ("Cleavage and brittle breaks",
         "Cleavage gives flat, shiny facets where the crystal planes split apart. It shows a brittle break, with little stretching before failure. Brittle breaks can happen suddenly, which makes them dangerous."),
        ("Following the crack back",
         "Chevron marks, the arrow-like ridges on many breaks, point back toward where the crack began. Following them to the origin tells the engineer where to look for the cause, such as a notch, a flaw or a surface scratch."),
    ],
    "test": [
        ("What do beach marks on a fatigue surface look like?",
         [("a", "Curved ridges, like lines left by the tide on a shore"), ("b", "Bright round dots"), ("c", "Square holes"), ("d", "Blue patches")], "a"),
        ("What does each striation on many metals stand for?",
         [("a", "One year of service"), ("b", "One load cycle"), ("c", "One gram of weight"), ("d", "One weld pass")], "b"),
        ("What does a surface full of dimples usually mean?",
         [("a", "The metal never bent at all"), ("b", "The part was painted"), ("c", "The metal stretched a lot before it broke"), ("d", "The part was new")], "c"),
        ("What does cleavage show?",
         [("a", "A soft, stretched lip"), ("b", "A weld bead"), ("c", "A layer of rust"), ("d", "A flat, shiny facet where crystal planes split")], "d"),
        ("What do chevron marks help the engineer find?",
         [("a", "The origin of the crack"), ("b", "The weight of the part"), ("c", "The date of manufacture"), ("d", "The colour of the paint")], "a"),
    ],
}
