"""Computed Tomography of Rock Samples: X-ray scanning of cores and samples to see density, pores and cracks inside them."""
CODE = "mining5_ct"
BOOK = {
    "title": "Computed Tomography of Rock Samples",
    "subtitle": "X-ray scanning, density maps, pore networks and core scanning",
    "chapters": [
        ("Seeing inside a sample",
         "A computed tomography scanner passes X-rays through a rock sample from many angles. A computer combines the images into a three-dimensional picture of the inside. Cracks, pores and dense grains all show up without cutting the sample open."),
        ("X-ray scanning",
         "Dense material absorbs more X-rays, so it looks brighter on the image. Empty pores look dark. By reading the brightness, the scanner shows how the material is spread through the sample."),
        ("Density maps",
         "The brightness can be turned into a density map, with numbers for each small volume of the sample. Density maps help match a sample to its place in the core and to the ore it came from."),
        ("Pore networks",
         "Scans can show the pores and how they connect. The connected pore space controls how easily fluid flows through rock. Engineers use this to estimate porosity and permeability."),
        ("Core scanning",
         "Whole cores can be scanned on a fast machine, and the results sit beside the drill log. This keeps every sample linked to its depth. Scanning before cutting protects the core for later tests."),
        ("Resolution and storage",
         "A bigger sample gives a coarser picture, and a smaller sample gives a finer one. The files are very large, so storage and backup need careful planning. Good labels keep each scan linked to its sample for years."),
    ],
    "test": [
        ("What does a computed tomography scan of a rock sample show?",
         [("a", "The colour of the sample only"), ("b", "The weight of the drill bit"), ("c", "A three-dimensional picture of the inside of the sample"), ("d", "The price of the core")], "c"),
        ("Why does dense material look brighter on an X-ray scan?",
         [("a", "It is painted white"), ("b", "It is closer to the sun"), ("c", "It is always warm"), ("d", "It absorbs more X-rays")], "d"),
        ("What do pore networks help engineers estimate?",
         [("a", "The number of workers"), ("b", "Porosity and permeability"), ("c", "The name of the drill company"), ("d", "The age of the miner")], "b"),
        ("What is an advantage of scanning core before cutting it?",
         [("a", "The core is protected for later tests"), ("b", "The core becomes lighter"), ("c", "The core turns into metal"), ("d", "The core needs no label")], "a"),
        ("What trade-off comes with sample size in CT scanning?",
         [("a", "A bigger sample gives a coarser picture and a smaller one a finer one"), ("b", "A bigger sample always gives a clearer picture"), ("c", "Sample size has no effect on the picture"), ("d", "Only tiny samples can be scanned")], "a"),
    ],
}
