"""Molecular Evolution and the Neutral Theory: how most DNA changes drift by chance and how molecular clocks and selection tests follow from that."""
CODE = "science5_bio_neutral"
BOOK = {
    "title": "Molecular Evolution and the Neutral Theory",
    "subtitle": "Why most DNA changes drift by chance, and how scientists still find real selection",
    "chapters": [
        ("A surprising idea", "The neutral theory, proposed by Motoo Kimura in 1968, says that most changes in DNA have little or no effect on fitness. Such changes spread or disappear by chance, a process called genetic drift."),
        ("Neutral mutations", "A neutral mutation is one that neither helps nor harms the organism. Many mutations in non-coding DNA and in the third position of many codons are close to neutral."),
        ("Substitution rates", "A substitution is a mutation that has spread through a population until it is fixed. For neutral changes, the rate at which substitutions appear is about the same as the rate at which new mutations arise."),
        ("dN/dS ratios", "The dN/dS ratio compares changes that alter a protein with changes that do not. A ratio below one suggests that the protein is under purifying selection, while a ratio above one suggests positive selection."),
        ("Molecular clocks", "Because neutral changes arrive at a fairly steady rate, they can be used as a molecular clock. Counting differences between two species helps estimate how long ago they shared an ancestor, though the clock is never perfect."),
        ("Genome comparison", "Comparing whole genomes shows which regions have changed quickly and which have stayed nearly the same. Those patterns hint at where selection has acted, and where drift has been the main force."),
    ],
    "test": [
        ("What does the neutral theory say about most molecular changes?",
         [("a", "They are neutral and spread or vanish by chance"), ("b", "They are all harmful"), ("c", "They are all caused by sunlight"), ("d", "They are all helpful")], "a"),
        ("What does a dN/dS ratio below one usually suggest?",
         [("a", "Strong positive selection in every gene"), ("b", "No mutations at all"), ("c", "Purifying selection, which removes most changes that alter proteins"), ("d", "Gene duplication only")], "c"),
        ("What is a molecular clock?",
         [("a", "A device that counts DNA bases"), ("b", "A clock inside cells"), ("c", "A timer that stops at midnight"), ("d", "An estimate of time from the steady rate of neutral changes")], "d"),
        ("Why is genome comparison useful?",
         [("a", "It proves all genes are the same"), ("b", "It reveals regions that change quickly or stay the same, hinting at where selection acted"), ("c", "It removes all mutations"), ("d", "It replaces the need for fossils entirely")], "b"),
        ("What rate do neutral substitutions roughly follow?",
         [("a", "Zero"), ("b", "Set by the Sun"), ("c", "Roughly the neutral mutation rate"), ("d", "Faster than any mutation rate")], "c"),
    ],
}
