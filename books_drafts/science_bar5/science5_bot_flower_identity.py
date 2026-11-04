"""Floral Organ Identity and Development: how flower parts are placed and what the genes behind them do."""
CODE = "science5_bot_flower_identity"
BOOK = {
    "title": "Floral Organ Identity and Development",
    "subtitle": "The ABC model, floral meristems and how flower parts are set",
    "chapters": [
        ("Flowers are arranged parts", "A typical flower has four whorls, or rings, of organs. From the outside in, these are sepals, petals, stamens and carpels. The pattern is very consistent across many species."),
        ("Floral meristems", "A floral meristem is a small group of growing cells that makes a flower instead of a leaf. It is set up by earlier signals in the shoot. Once it begins, the meristem produces its organs in order."),
        ("The ABC model", "The ABC model explains how gene activity sets organ identity. Class A genes alone give sepals. Classes A and B together give petals, B and C together give stamens, and C alone gives carpels. The model was built from mutant studies in model plants."),
        ("Organ identity genes", "Organ identity genes are transcription factors. They switch on other genes that build each organ's shape and tissue. A change in one identity gene can turn one organ into another."),
        ("Flower evolution", "Flowers appeared and diversified over time, and their genes can be compared across plant groups. Similar gene families often shape flowers in very different species. Comparing these genes helps scientists rebuild how flower forms changed."),
        ("Developmental mutants", "Mutants that lack or change a flower gene show the gene's role clearly. A mutant with missing stamens, for example, points to a loss of class B or C activity. Such mutants are a key tool for testing the model."),
    ],
    "test": [
        ("How many whorls of organs does a typical flower have?",
         [("a", "Four"), ("b", "Two"), ("c", "Six"), ("d", "Nine")], "a"),
        ("In the ABC model, which classes together give petals?",
         [("a", "Classes B and C"), ("b", "Class C alone"), ("c", "Classes A and C"), ("d", "Classes A and B")], "d"),
        ("What is a floral meristem?",
         [("a", "A small group of growing cells that makes a flower instead of a leaf"), ("b", "A kind of root hair"), ("c", "A type of seed coat"), ("d", "A fruit that grows under water")], "a"),
        ("What are organ identity genes?",
         [("a", "Transcription factors that switch on other genes for each organ"), ("b", "Genes that only colour the petals"), ("c", "Genes that stop all growth"), ("d", "Genes found only in animals")], "a"),
        ("What can a mutant with missing stamens show?",
         [("a", "That the flower has no roots"), ("b", "That the plant can fly"), ("c", "A loss of class B or C gene activity"), ("d", "That the soil is too wet")], "c"),
    ],
}
