"""Phylogenetic Trees and Molecular Clocks: tree building, character states, tree support, molecular clocks, divergence dating and the limits of trees."""
CODE = "science4_bio_phylogeny"
BOOK = {
    "title": "Phylogenetic Trees and Molecular Clocks",
    "subtitle": "Tree building, molecular clocks and divergence dates",
    "chapters": [
        ("Building a tree", "A phylogenetic tree shows the evolutionary relationships among species. Each branch point represents a common ancestor shared by the groups that split from it."),
        ("Character states", "Trees are built from characters, such as the shape of a bone or the sequence of a gene. Each character can take different states in different species."),
        ("Tree support", "Scientists test how well the data support each branch, often by resampling the characters many times. Strong support means a branch is more likely to be correct."),
        ("Molecular clocks", "A molecular clock uses the roughly steady rate of DNA change to estimate when two lineages split. Rates can vary, so the clock must be calibrated."),
        ("Divergence dating", "Scientists date splits using fossils and known rates of change. A fossil sets a minimum date for a split, which helps calibrate the clock."),
        ("The limits of trees", "A tree is a hypothesis, and it can change as new data arrive. Gene transfer between microbes can make a simple tree misleading."),
    ],
    "test": [
        ("What does a phylogenetic tree show?",
         [("a", "Evolutionary relationships among species"), ("b", "Weather patterns"), ("c", "How tall plants grow"), ("d", "The shape of mountains")], "a"),
        ("What is a character in tree-building?",
         [("a", "An actor in a play"), ("b", "A planet's name"), ("c", "A trait or sequence that can take different states in different species"), ("d", "A type of fossil bed")], "c"),
        ("What is a molecular clock?",
         [("a", "A watch made of molecules"), ("b", "A way to estimate when lineages split using a steady rate of DNA change"), ("c", "A sundial"), ("d", "A laboratory timer")], "b"),
        ("Why do molecular clocks need calibration?",
         [("a", "Because they are always exact"), ("b", "Because they run on electricity"), ("c", "Because they measure colour"), ("d", "Because DNA change rates can vary")], "d"),
        ("What role do fossils play in divergence dating?",
         [("a", "They are useless"), ("b", "They make trees colourful"), ("c", "They set a minimum date for a split and help calibrate the clock"), ("d", "They replace DNA")], "c"),
    ],
}
