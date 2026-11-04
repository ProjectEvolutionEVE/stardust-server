"""Epigenetics and Chromatin Regulation: chemical marks on DNA and histones that switch genes on and off without changing the letters."""
CODE = "science5_bio_epigenetics"
BOOK = {
    "title": "Epigenetics and Chromatin Regulation",
    "subtitle": "How chemical marks on DNA and its packaging switch genes up or down",
    "chapters": [
        ("Beyond the letters", "Every cell in your body has the same DNA, yet a skin cell and a nerve cell look and act very differently. Epigenetic marks help explain how one set of instructions gives rise to many cell types."),
        ("DNA methylation", "Methyl groups can be added to some DNA bases, most often where a C is followed by a G. Methylation in regulatory regions usually makes a gene harder to read."),
        ("Histone modifications", "DNA is wrapped around proteins called histones. Chemical tags added to histones can loosen or tighten that wrapping, making genes easier or harder to reach."),
        ("Chromatin states", "The combination of DNA marks and histone marks forms a chromatin state. Cells use these states to define which regions are open and active, and which are packed and quiet."),
        ("Epigenetic inheritance", "Some epigenetic marks survive cell division, so daughter cells keep the pattern of their parents. In a few cases, marks can even pass between generations, though this is not common."),
        ("Reprogramming and measurement", "Early embryos and stem cells can erase and reset many marks, a process called reprogramming. Methods such as bisulfite sequencing show which DNA bases carry methyl groups."),
    ],
    "test": [
        ("What does DNA methylation do in gene regulatory regions?",
         [("a", "It changes the letters of the DNA sequence"), ("b", "It breaks the DNA apart"), ("c", "It turns DNA into protein"), ("d", "It can change how genes are read without changing the DNA letters")], "d"),
        ("What is a histone modification?",
         [("a", "A chemical tag on the proteins around which DNA is wrapped"), ("b", "A type of cell membrane"), ("c", "A mineral in rock"), ("d", "A kind of virus")], "a"),
        ("What is epigenetic inheritance?",
         [("a", "Changes passed down only through the DNA letters"), ("b", "Some marks passed on through cell division and, in some cases, between generations"), ("c", "The passing on of eye colour"), ("d", "A rule about the speed of light")], "b"),
        ("What does reprogramming refer to?",
         [("a", "Writing new computer code"), ("b", "A computer restart"), ("c", "Erasing and resetting epigenetic marks, as in early embryos and when stem cells are made"), ("d", "Fixing broken bones")], "c"),
        ("How are DNA methylation patterns often measured?",
         [("a", "With methods such as bisulfite sequencing that show which bases are methylated"), ("b", "By listening to cells"), ("c", "By weighing cells"), ("d", "By counting planets")], "a"),
    ],
}
