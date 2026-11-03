"""Quantitative Trait Mapping and Genomic Selection. How breeders link genes to useful traits and select plants by DNA."""
CODE = "science5_bot_genomic_selection"
BOOK = {
    "title": "Quantitative Trait Mapping and Genomic Selection",
    "subtitle": "Using DNA markers to find and breed for useful traits",
    "chapters": [
        ("Traits with many genes",
         "Many useful traits, such as yield and height, are controlled by many genes at once. Such quantitative traits vary smoothly across a population, and the genes behind them are hard to see one by one."),
        ("QTL mapping",
         "QTL mapping looks for regions of the genome that are linked to a trait. Plants from a cross are scored for both DNA markers and the trait, and markers that travel with the trait point to a chromosome region that carries a QTL."),
        ("Marker-assisted selection",
         "Marker-assisted selection uses DNA markers linked to a wanted gene to pick plants early, without waiting to grow them to maturity. It speeds breeding and reduces the need to test every plant in the field."),
        ("Genomic prediction",
         "Genomic prediction uses markers across the whole genome to estimate a plant's breeding value. Thousands of markers are combined in one model, so even plants that have never been tested can be ranked."),
        ("Training populations",
         "A training population has both genotype and trait data, and it is used to build the prediction model. The larger and more closely related the training population is to the breeding lines, the more accurate the predictions tend to be."),
        ("Epistasis and breeding cycles",
         "Epistasis means that the effect of one gene depends on the presence of others. Breeding cycles repeat selection and crossing, and models must allow for epistasis to predict well."),
    ],
    "test": [
        ("What is a QTL?",
         [("a", "A type of fungus that grows on roots"), ("b", "A plant hormone"), ("c", "A sugar in pollen"), ("d", "A region of the genome linked to a trait")], "d"),
        ("What is genomic selection?",
         [("a", "Choosing plants by their colour alone"), ("b", "Letting the wind pick the seeds"), ("c", "Predicting breeding value from genome-wide markers"), ("d", "Cutting down plants that are too tall")], "c"),
        ("What is a training population?",
         [("a", "A group of animals in a barn"), ("b", "A crowd of gardeners"), ("c", "A bank of old seeds"), ("d", "A group with genotype and trait data used to build a prediction model")], "d"),
        ("What does epistasis mean?",
         [("a", "The effect of one gene depends on the presence of other genes"), ("b", "A gene that never changes"), ("c", "A type of soil"), ("d", "The shape of a leaf")], "a"),
        ("What does marker-assisted selection use to pick plants?",
         [("a", "The number of leaves"), ("b", "The length of the roots only"), ("c", "DNA markers linked to a wanted gene"), ("d", "The time of day the seed was planted")], "c"),
    ],
}
