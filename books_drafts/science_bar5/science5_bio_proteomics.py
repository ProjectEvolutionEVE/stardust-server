"""Proteomics and Protein Interaction Networks: identifying proteins, finding their partners and reading their chemical tags."""
CODE = "science5_bio_proteomics"
BOOK = {
    "title": "Proteomics and Protein Interaction Networks",
    "subtitle": "Identifying proteins, finding their partners and reading their chemical tags",
    "chapters": [
        ("The protein toolkit", "Proteomics studies the full set of proteins in a cell or tissue. Because proteins do most of the work in cells, their identities and amounts tell a rich story."),
        ("Protein identification", "Proteins are cut into peptides and measured in a mass spectrometer. The masses of the fragments are matched against databases to identify which proteins were present."),
        ("Quantitative proteomics", "Labels or label-free methods measure how much of each protein is present in different samples. Careful controls make it possible to compare those amounts fairly."),
        ("Affinity purification", "In affinity purification, a bait protein is used to pull out the proteins that bind to it. The catch is then identified by mass spectrometry, revealing likely partners."),
        ("Interaction maps and modifications", "Partners found across many experiments are drawn as interaction maps, or networks. Post-translational modifications, such as phosphate tags, add another layer that can switch proteins on or off."),
        ("Data quality", "False identifications can mislead an analysis, so scientists set a false discovery rate to limit them. Good data quality depends on controls, replicates and careful statistics."),
    ],
    "test": [
        ("What does mass spectrometry measure in proteomics?",
         [("a", "The mass-to-charge of peptide fragments used to identify proteins"), ("b", "The colour of cells"), ("c", "The age of a tissue"), ("d", "The weight of a cell")], "a"),
        ("What is an affinity purification?",
         [("a", "Cleaning a glass slide"), ("b", "Using a bait protein to pull out its binding partners"), ("c", "Filtering air"), ("d", "Freezing a sample")], "b"),
        ("What are post-translational modifications?",
         [("a", "Changes to DNA before the cell divides"), ("b", "Changes to the cell's colour"), ("c", "Chemical changes added to proteins after they are made, such as phosphate tags"), ("d", "Changes to the Moon")], "c"),
        ("What does a protein interaction map show?",
         [("a", "The weather"), ("b", "The sizes of planets"), ("c", "The colours of tissues"), ("d", "Which proteins are known or likely to bind one another")], "d"),
        ("Why does data quality matter in proteomics?",
         [("a", "It does not"), ("b", "Because false identifications can mislead, so false discovery rates are used to control them"), ("c", "Because proteins never change"), ("d", "Because mass spectrometers are always silent")], "b"),
    ],
}
