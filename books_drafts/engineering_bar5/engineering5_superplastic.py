"""Superplasticity and Superplastic Forming: stretching fine-grained metal very far at high temperature, and forming it into shape."""
CODE = "engineering5_superplastic"
BOOK = {
    "title": "Superplasticity and Superplastic Forming",
    "subtitle": "Stretching fine-grained metal very far at high temperature, and forming it into shape",
    "chapters": [
        ("Stretching very far",
         "Superplastic metals can stretch by hundreds of percent before breaking, when held at the right temperature and strain rate. Ordinary metals neck down and break much sooner."),
        ("The fine-grain requirement",
         "Superplasticity needs very fine and stable grains, usually a few micrometres across. Grain boundary sliding carries much of the deformation."),
        ("Strain rate sensitivity",
         "The metal must be sensitive to strain rate, so that it resists local necking. Forming must be slow enough for this effect to act."),
        ("Forming temperatures",
         "Forming happens at high temperature, often above half the melting point, which keeps the grains stable. If the metal is too cold, the effect is lost."),
        ("Cavitation",
         "Tiny voids can grow at grain boundaries during forming, which is called cavitation. It limits how far a part can be stretched."),
        ("Aerospace panels",
         "Superplastic forming makes complex one-piece panels from a sheet, with less joining. Titanium alloys and some aluminium alloys are formed this way."),
    ],
    "test": [
        ("How far can superplastic metals stretch?",
         [("a", "Not at all"), ("b", "Only one percent"), ("c", "Hundreds of percent before breaking"), ("d", "Only in water")], "c"),
        ("What grain size does superplasticity need?",
         [("a", "Very fine and stable, a few micrometres across"), ("b", "Huge boulders"), ("c", "Sand"), ("d", "Paint")], "a"),
        ("What is the role of strain rate sensitivity?",
         [("a", "It sets the price"), ("b", "It paints the metal"), ("c", "It counts grains"), ("d", "It resists local necking")], "d"),
        ("What is cavitation?",
         [("a", "A cave"), ("b", "A paint type"), ("c", "Tiny voids growing at grain boundaries"), ("d", "A sugar rush")], "c"),
        ("What is an aerospace use of superplastic forming?",
         [("a", "Making one-piece panels from a sheet"), ("b", "Paint"), ("c", "Sugar"), ("d", "Mud")], "a"),
    ],
}
