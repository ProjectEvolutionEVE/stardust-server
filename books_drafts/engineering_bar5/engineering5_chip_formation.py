"""Chip Formation and the Shear Plane: the Merchant circle, shear angle, chip types, built-up edge and cutting force prediction."""
CODE = "engineering5_chip_formation"
BOOK = {
    "title": "Chip Formation and the Shear Plane",
    "subtitle": "What happens in the thin zone where a tool cuts metal",
    "chapters": [
        ("A cut is a shear",
         "When a cutting tool moves through metal, the metal does not simply split. It is pushed into a thin zone called the shear plane and sheared off as a chip. Most of the cutting energy is spent in that narrow zone."),
        ("The shear angle",
         "The shear angle is the angle of the shear plane to the cutting direction. A larger shear angle means a thinner chip and less force. Engineers adjust the rake angle and cutting conditions to move it."),
        ("The Merchant circle",
         "The Merchant circle is a force diagram that links the cutting force, the thrust force and the friction on the tool face. It helps predict the forces from simple measurements. It is a useful model, though it simplifies the real process."),
        ("Chip types",
         "Chips come in several forms. Continuous chips form in tough, ductile metals. Segmented chips form in harder or less ductile metals. Each type affects the surface and the safety of the cut."),
        ("Built-up edge",
         "Built-up edge is a small mass of work material that welds itself to the tool face. It changes the cut and can spoil the surface. Speed, cooling and the tool coating all influence how much forms."),
        ("Predicting the cutting force",
         "Cutting force is predicted from the shear strength of the metal, the chip thickness and the shear angle. Force sets the power the machine needs and the stress on the tool. A good prediction lets the engineer pick a machine and a tool with margin."),
    ],
    "test": [
        ("Where is most cutting energy spent?",
         [("a", "In the air above the tool"), ("b", "In the coolant tank"), ("c", "In the operator's hands"), ("d", "In the thin shear plane")], "d"),
        ("What does a larger shear angle usually give?",
         [("a", "A thinner chip and less force"), ("b", "A thicker chip and more force"), ("c", "A chip that never forms"), ("d", "No change at all")], "a"),
        ("What does the Merchant circle link?",
         [("a", "The price of the tool and the price of the metal"), ("b", "The cutting force, thrust force and friction on the tool face"), ("c", "The number of shifts and the number of workers"), ("d", "The colour of the chip and the room")], "b"),
        ("What is built-up edge?",
         [("a", "A raised ridge on the machine bed"), ("b", "A cutting oil label"), ("c", "A small mass of work material that welds to the tool face"), ("d", "A type of drill bit")], "c"),
        ("What is cutting force used for?",
         [("a", "Choosing the colour of the coolant"), ("b", "Counting the chips in the bin"), ("c", "Measuring the length of the shift"), ("d", "Setting the power the machine needs and the stress on the tool")], "d"),
    ],
}
