"""Transcriptomics and RNA Sequencing: how sequencing reads of RNA reveal which genes are active, and how to compare them fairly."""
CODE = "science5_bio_rnaseq"
BOOK = {
    "title": "Transcriptomics and RNA Sequencing",
    "subtitle": "Reading which genes are active, and comparing them fairly between samples",
    "chapters": [
        ("Reading the active genes", "RNA sequencing reads the RNA molecules in a sample, which shows which genes are switched on and how strongly. This set of RNA is called the transcriptome."),
        ("Library preparation", "Before sequencing, RNA is converted into DNA and cut into fragments. Each fragment is tagged with short adapter sequences, forming a sequencing library ready to be read."),
        ("Read alignment", "The machine produces millions of short reads. Alignment software matches each read to its place in a reference genome or transcriptome, and the number of matches shows how much each gene is expressed."),
        ("Differential expression", "Differential expression compares gene activity between conditions, such as diseased and healthy tissue. Statistical tests then decide which changes are large enough and consistent enough to trust."),
        ("Normalisation", "Samples differ in how deeply they were sequenced and in their RNA content. Normalisation adjusts the counts so that samples can be compared fairly."),
        ("Single-cell RNA sequencing", "Single-cell RNA sequencing measures expression in individual cells instead of a mixed sample. It reveals cell types and states that a bulk sample would blur together, and good experimental design, with enough replicates, makes the results reliable."),
    ],
    "test": [
        ("What is a sequencing library?",
         [("a", "A book about sequencing"), ("b", "A prepared set of DNA fragments ready to be read"), ("c", "A list of cells"), ("d", "A computer folder")], "b"),
        ("What does read alignment do?",
         [("a", "Makes reads longer"), ("b", "Stops the sequencing machine"), ("c", "Matches each short read to its place in a reference genome or transcriptome"), ("d", "Dyes the RNA")], "c"),
        ("What is differential expression?",
         [("a", "Gene sequences that never change"), ("b", "A type of microscope"), ("c", "Only the number of cells in a sample"), ("d", "Comparing how much each gene is expressed between conditions")], "d"),
        ("Why is normalisation needed?",
         [("a", "To make counts from different samples comparable"), ("b", "To make RNA heavier"), ("c", "To remove all genes"), ("d", "To stop the machine")], "a"),
        ("What does single-cell RNA sequencing add?",
         [("a", "A single sample of blood only"), ("b", "Only one gene"), ("c", "Expression profiles for individual cells"), ("d", "A picture of the cell wall")], "c"),
    ],
}
