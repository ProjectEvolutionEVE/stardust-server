"""Numerical Modelling of Caving: computer models that predict how rock caves above an undercut, and how the draw of ore can be controlled."""
CODE = "mining5_cave_num"
BOOK = {
    "title": "Numerical Modelling of Caving",
    "subtitle": "Discrete elements, cave propagation, draw control and calibration",
    "chapters": [
        ("Rock that falls on purpose",
         "Block caving undercuts an ore body so that the rock above breaks and falls. The falling rock is then drawn off at the bottom. Computer models help predict how the cave will grow and where it will go."),
        ("Discrete elements",
         "Discrete element models treat the rock as many separate blocks or particles. They show how blocks break free, rotate and collide. This suits caving, where the rock falls apart."),
        ("Cave propagation",
         "A model can show how the cave spreads upward and outward over time. It helps predict how far the cave will reach and when it may reach the surface. Those predictions guide safety and planning."),
        ("Draw control",
         "The rate and location of drawing at the base controls how the cave moves. Drawing unevenly can leave pockets of ore or let waste flow in too early. Models test draw plans before they are used in the mine."),
        ("Mesh",
         "Some models use a mesh of cells to represent the rock. The mesh must be fine enough to capture key features, but not so fine that the run becomes too slow. Choosing the mesh is a balance of accuracy and time."),
        ("Calibration and predictions",
         "Models are calibrated against what has been observed in the mine, such as surface subsidence and cave shape. Once calibrated, they are used for predictions. Predictions are always checked against new observations."),
    ],
    "test": [
        ("What does block caving do to the ore body?",
         [("a", "It undercuts it so the rock above breaks and falls"), ("b", "It paints the ore red"), ("c", "It moves the ore to the sea"), ("d", "It stops all mining")], "a"),
        ("What do discrete element models treat rock as?",
         [("a", "One smooth sheet of glass"), ("b", "A cloud of gas"), ("c", "Many separate blocks or particles"), ("d", "A bowl of soup")], "c"),
        ("What does draw control affect?",
         [("a", "The colour of the office walls"), ("b", "The number of birds"), ("c", "The weather report"), ("d", "How the cave moves and where ore is left behind")], "d"),
        ("Why must a mesh be chosen with care?",
         [("a", "It must be as coarse as possible"), ("b", "It must be fine enough for key features but not too slow to run"), ("c", "It has no effect on results"), ("d", "It must be made of steel")], "b"),
        ("How are cave models calibrated?",
         [("a", "Against what has been observed in the mine"), ("b", "By guessing the answer"), ("c", "By using one picture only"), ("d", "By asking the cook")], "a"),
    ],
}
