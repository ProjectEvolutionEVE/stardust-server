"""Sedimentology and Depositional Environments: reading rocks made of sediment to rebuild the rivers, deltas and seas where they formed."""
CODE = "science4_geo_sedimentology"
BOOK = {
    "title": "Sedimentology and Depositional Environments",
    "subtitle": "Grain size, layers and the places sediment came from",
    "chapters": [
        ("Grain size and sorting",
         "Sediment grains range from clay to boulders. Grain size tells you how fast the water or wind was moving when the grains settled. Sorting describes how alike the grains are: well sorted sediment has grains of similar size."),
        ("Facies recognition",
         "A facies is a body of rock with particular features that show how it formed. Geologists look at layers, colours, grain sizes and fossils. Together these features point to a particular environment."),
        ("River and delta deposits",
         "Rivers leave channel sands and gravels, and their floodplains leave finer silt and clay. Where a river meets a standing body of water, a delta builds out, with layers that slope in a characteristic way."),
        ("Turbidity currents",
         "A turbidity current is a fast-moving flow of sediment-laden water that runs down a slope. It deposits graded beds, where the coarse grains settle first and the finer ones settle above them. Graded beds are a strong clue to deep-water settings."),
        ("Sedimentary sequences",
         "Layers are stacked in order, with the oldest at the bottom in undisturbed rock. The way one facies changes into another, from one layer to the next, records how an environment shifted over time. A sequence can show a sea advancing or retreating."),
        ("Reconstructing an environment from a core",
         "A core is a cylinder of rock or sediment drilled from the ground. Geologists log each interval, note grain size and structures, and match the facies to known environments. The result is a picture of the place that existed when the sediment was laid down."),
    ],
    "test": [
        ("What does sorting describe in sediment?",
         [("a", "How much water the sediment holds"), ("b", "How old the sediment is"), ("c", "How alike the grains are in size"), ("d", "The number of fossils present")], "c"),
        ("What is a turbidity current?",
         [("a", "A fast flow of sediment-laden water running down a slope"), ("b", "A slow wind that blows across a desert"), ("c", "A crack in a glacier"), ("d", "A current of warm air above a lake")], "a"),
        ("What does a graded bed show?",
         [("a", "Only one size of grain"), ("b", "Fine grains settled first, with coarser ones above"), ("c", "Coarse grains settled first, with finer ones above"), ("d", "A layer of ice")], "c"),
        ("What environment is most often linked to a delta?",
         [("a", "A river meeting a standing body of water"), ("b", "The top of a mountain"), ("c", "A dry desert with no water"), ("d", "The middle of a glacier")], "a"),
        ("In undisturbed rock, which layer is the oldest?",
         [("a", "The top layer"), ("b", "The layer in the middle"), ("c", "The youngest layer"), ("d", "The bottom layer")], "d"),
    ],
}
