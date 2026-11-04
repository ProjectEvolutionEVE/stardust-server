"""Population Genetics and Natural Selection: allele frequencies, Hardy-Weinberg equilibrium, genetic drift, selection coefficients, mutation and gene flow, and measuring selection."""
CODE = "science4_bio_pop_gen"
BOOK = {
    "title": "Population Genetics and Natural Selection",
    "subtitle": "Allele frequencies, drift, selection and mutation",
    "chapters": [
        ("Allele frequencies", "An allele is a version of a gene. The allele frequency is the fraction of gene copies in a population that carry a given allele."),
        ("Hardy-Weinberg equilibrium", "Without selection, mutation, migration, drift or non-random mating, allele frequencies stay the same from one generation to the next. This steady state is the Hardy-Weinberg equilibrium, and it gives a baseline for comparison."),
        ("Genetic drift", "Genetic drift is random change in allele frequencies, caused by chance in which parents' genes are passed on. It is strongest in small populations."),
        ("Selection coefficients", "A selection coefficient measures how much an allele changes an individual's chance of survival or reproduction. Larger values mean stronger selection."),
        ("Mutation and gene flow", "Mutations add new alleles to a population. Gene flow moves alleles between populations through migration. Both can change allele frequencies."),
        ("Measuring selection", "Scientists measure selection by tracking how allele frequencies change across generations. Comparing the observed changes with expectations shows where selection is acting."),
    ],
    "test": [
        ("What is an allele?",
         [("a", "A type of cell"), ("b", "A rock layer"), ("c", "A planet"), ("d", "A version of a gene")], "d"),
        ("What does Hardy-Weinberg equilibrium describe?",
         [("a", "A way to measure a planet's gravity"), ("b", "A steady state where allele frequencies stay constant without selection, mutation, migration, drift or non-random mating"), ("c", "A type of star"), ("d", "A species of fish")], "b"),
        ("What is genetic drift?",
         [("a", "The movement of ocean currents"), ("b", "Planned breeding"), ("c", "A drug used in farming"), ("d", "Random change in allele frequencies from chance, strongest in small populations")], "d"),
        ("What does a selection coefficient measure?",
         [("a", "How much an allele changes survival or reproduction chances"), ("b", "The number of cells in a body"), ("c", "The speed of a planet"), ("d", "The number of chromosomes")], "a"),
        ("What adds new alleles to a population?",
         [("a", "Mutation"), ("b", "Hardy-Weinberg equilibrium"), ("c", "Sunlight"), ("d", "Gravity")], "a"),
    ],
}
