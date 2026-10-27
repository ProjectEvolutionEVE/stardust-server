"""Chemical Vapour Deposition of Coatings: precursor gases, growth rates, coating uniformity, coating cracks and the cost per coated part."""
CODE = "engineering5_cvd"
BOOK = {
    "title": "Chemical Vapour Deposition of Coatings",
    "subtitle": "Growing a thin hard layer from gas",
    "chapters": [
        ("Coating from a gas",
         "In chemical vapour deposition, or CVD, gases react on a heated surface and leave a solid film behind. The film builds up layer by layer. The method can coat complex shapes that a spray could not reach easily."),
        ("Precursor gases",
         "The gases that feed the reaction are called precursors. Their choice sets which coating forms and how pure it is. Precursors must be handled with care, because many are toxic or flammable."),
        ("Growth rate",
         "The coating grows at a rate set by temperature, pressure and gas flow. Faster growth saves time but can make the film rougher or less even. Engineers balance speed against quality."),
        ("Uniformity",
         "A good CVD coating is even in thickness over the whole part. Gas must reach every surface, so the layout of parts in the reactor matters. Uneven gas flow leaves thin spots that wear first."),
        ("Coating cracks",
         "When the coating and the base metal expand by different amounts, the coating can crack on cooling. Matching the expansion, or using a thinner layer, helps. Cracks are a common cause of coating failure."),
        ("Cost per coated part",
         "The cost of a CVD coating depends on gas, energy, time in the reactor and how many parts fit in one load. A full, well-packed load lowers the cost of each part. Engineers track the cost per part, not just the cost per run."),
    ],
    "test": [
        ("What happens in chemical vapour deposition?",
         [("a", "Gases react on a heated surface and leave a solid film"), ("b", "Metal is melted and poured"), ("c", "Wood is burned"), ("d", "Paint is sprayed on")], "a"),
        ("What are precursors?",
         [("a", "The finished coated parts"), ("b", "The gases that feed the reaction"), ("c", "The cooling fans"), ("d", "The workers on the floor")], "b"),
        ("Why does even gas flow matter in CVD?",
         [("a", "Gas flow changes the colour of the metal"), ("b", "Gas flow makes the part heavier"), ("c", "Uneven flow leaves thin spots that wear first"), ("d", "Gas flow has no effect")], "c"),
        ("Why can a CVD coating crack on cooling?",
         [("a", "The coating is too cold"), ("b", "The coating is painted"), ("c", "The coating is too thin to see"), ("d", "The coating and base metal expand by different amounts")], "d"),
        ("What is the best measure of CVD cost for planning?",
         [("a", "The cost per coated part"), ("b", "The colour of the reactor"), ("c", "The number of windows in the plant"), ("d", "The name of the gas")], "a"),
    ],
}
