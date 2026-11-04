"""Metagenomics and Environmental DNA: reading the DNA of whole communities, and finding species from the traces they leave."""
CODE = "science5_bio_metagenomics"
BOOK = {
    "title": "Metagenomics and Environmental DNA",
    "subtitle": "Reading the DNA of a whole community at once",
    "chapters": [
        ("Reading all the DNA", "Shotgun sequencing breaks DNA into many short fragments and reads them all. Metagenomics applies this to a whole community of organisms at once. The result is a huge pile of sequence to sort."),
        ("Genome reconstruction", "Overlapping fragments are assembled by computer into longer stretches. Careful work can rebuild near-complete genomes of microbes from a mixed sample. This shows what each organism could do."),
        ("Environmental DNA", "Organisms shed DNA into water, soil and air through skin, waste and other traces. This environmental DNA, or eDNA, can show which species were present without catching them."),
        ("Species detection", "eDNA is useful for finding rare or hidden species. A water sample may reveal a fish that is hard to see. Results need careful checking, because a trace shows presence, not number."),
        ("Contamination control", "DNA is easy to pick up by accident, so careful handling matters. Scientists use blank control samples and clean equipment. These checks stop false results from creeping in."),
        ("Biodiversity surveys", "Sampling many places over time maps the life of an area. Metagenomics and eDNA together give a broad picture of biodiversity. They are fast and cover many species at once."),
    ],
    "test": [
        ("What does shotgun sequencing do?",
         [("a", "Fires a gun at samples"), ("b", "Breaks DNA into many fragments and reads them"), ("c", "Counts stars in the sky"), ("d", "Freezes soil")], "b"),
        ("What is environmental DNA?",
         [("a", "DNA made only in a laboratory"), ("b", "The DNA of a human fossil"), ("c", "DNA shed by organisms into their surroundings"), ("d", "DNA found in rock")], "c"),
        ("How can eDNA help a survey?",
         [("a", "It can detect a species without catching it"), ("b", "It replaces all fieldwork"), ("c", "It turns water into soil"), ("d", "It stops all contamination")], "a"),
        ("Why do scientists use blank control samples?",
         [("a", "To keep samples cold"), ("b", "To paint the laboratory"), ("c", "To make results bigger"), ("d", "To check whether contamination created false results")], "d"),
        ("What does a biodiversity survey aim to show?",
         [("a", "The price of land"), ("b", "Which species live in an area"), ("c", "The age of the Sun"), ("d", "The weight of rain")], "b"),
    ],
}
