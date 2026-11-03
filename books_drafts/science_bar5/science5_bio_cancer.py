"""Cancer Biology: Mutations and Growth Control: the driver mutations, oncogenes and tumour suppressors that let cells escape control."""
CODE = "science5_bio_cancer"
BOOK = {
    "title": "Cancer Biology: Mutations and Growth Control",
    "subtitle": "How changes in a cell's genes can release it from normal growth control",
    "chapters": [
        ("Growth that goes wrong", "Cancer begins when cells gain changes that let them grow and divide without the usual limits. Most of these changes are acquired during a person's life, not inherited."),
        ("Driver mutations", "A driver mutation gives a cell a growth advantage and helps push it toward cancer. Other mutations come along for the ride and do not help the cancer grow."),
        ("Oncogenes", "Oncogenes are genes that push cells toward growth and division when they are overactive. A single change that switches a growth gene on can be enough to start a problem."),
        ("Tumour suppressors", "Tumour suppressors restrain cell growth, help repair damaged DNA and remove cells that are too damaged. When both copies of such a gene are lost, the brake is gone."),
        ("Clonal evolution", "Cells inside a tumour keep gaining new mutations, and those that grow best are selected. This clonal evolution means a tumour changes over time and can become harder to treat."),
        ("The tumour microenvironment", "The tumour microenvironment is the set of cells and signals around a tumour. These neighbours can help the tumour grow or hinder it, depending on the balance of signals."),
    ],
    "test": [
        ("What is a driver mutation?",
         [("a", "A mutation in a car"), ("b", "A mutation that gives a cell a growth advantage and helps drive cancer"), ("c", "A mutation that never matters"), ("d", "A kind of sunlight")], "b"),
        ("What do oncogenes do when overactive?",
         [("a", "Slow every cell down"), ("b", "Repair DNA"), ("c", "Push cells toward growth and division"), ("d", "Make cells invisible")], "c"),
        ("What do tumour suppressors do?",
         [("a", "Restrain cell growth and help repair or remove damaged cells"), ("b", "Make tumours bigger"), ("c", "Turn off all genes"), ("d", "Produce light")], "a"),
        ("What is clonal evolution in a tumour?",
         [("a", "A single tumour that never changes"), ("b", "A tumour that becomes a plant"), ("c", "A type of blood test"), ("d", "Cells in a tumour gaining new mutations and being selected, so the tumour changes over time")], "d"),
        ("What is the tumour microenvironment?",
         [("a", "The cells and signals around a tumour that can help or hinder it"), ("b", "The weather near a tumour"), ("c", "A kind of microscope"), ("d", "A tumour's name")], "a"),
    ],
}
