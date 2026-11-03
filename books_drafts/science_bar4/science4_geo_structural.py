"""Structural Geology: Folds and Faults: how rocks bend and break under stress, and how geologists read those changes in the field."""
CODE = "science4_geo_structural"
BOOK = {
    "title": "Structural Geology: Folds and Faults",
    "subtitle": "Stress, strain, folds, faults and the history they record",
    "chapters": [
        ("Stress and strain",
         "Stress is force divided by the area it acts on. Strain is the change in shape or size that the stress produces. Rocks respond to stress in different ways depending on temperature, pressure and time."),
        ("Fold geometry",
         "A fold is a bend in layered rock. Geologists name its parts: the hinge is the bend itself, and the limbs are the sides. An anticline arches upward, and a syncline dips down in the middle."),
        ("Fault mechanics",
         "A fault is a break along which rock blocks have moved. Normal faults form when the crust is pulled apart. Reverse faults form when the crust is squeezed together. Strike-slip faults form when blocks slide past each other."),
        ("Strike and dip",
         "Strike is the compass direction of a horizontal line drawn on a layer. Dip is the steepest angle the layer makes with the horizontal, measured down from the surface. Together they describe how a layer is tilted in space."),
        ("Mapping structures in the field",
         "Field geologists measure strike and dip at many points and mark them on a map. Where the layers repeat or cut across each other, the pattern shows folds and faults. A good map lets a reader picture the structure below the ground."),
        ("Reconstructing a deformation history",
         "The order in which folds and faults formed can be worked out from which structure cuts another. A fault that cuts through a fold must be younger than the fold. Piece by piece, the sequence tells a story of the rock’s past."),
    ],
    "test": [
        ("What is strike in a layer of rock?",
         [("a", "The compass direction of a horizontal line on the layer"), ("b", "The amount of rock that has been eroded"), ("c", "The depth of the layer under the ocean"), ("d", "The colour of the layer")], "a"),
        ("What does dip describe?",
         [("a", "How much rock is in a mountain"), ("b", "The steepest angle a layer makes with the horizontal"), ("c", "How many fossils a layer holds"), ("d", "How fast a river runs")], "b"),
        ("What is stress, as a geologist uses the word?",
         [("a", "The temperature of a rock"), ("b", "Force divided by the area it acts on"), ("c", "The age of a fault"), ("d", "The number of layers in a fold")], "b"),
        ("What is strain?",
         [("a", "The weight of a rock"), ("b", "The speed of an earthquake"), ("c", "The change in shape or size that stress produces"), ("d", "The distance between two faults")], "c"),
        ("What kind of stress forms a normal fault?",
         [("a", "Squeezing together"), ("b", "Sliding sideways"), ("c", "Pulling apart"), ("d", "Heating up")], "c"),
    ],
}
