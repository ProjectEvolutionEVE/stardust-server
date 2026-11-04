"""Genome Editing and Crop Design. How CRISPR tools change plant genes, and the checks a new crop must pass."""
CODE = "science5_bot_crop_editing"
BOOK = {
    "title": "Genome Editing and Crop Design",
    "subtitle": "Editing a plant's genes with care, from the lab to the field",
    "chapters": [
        ("Editing a gene",
         "CRISPR is a tool that uses a guide RNA to find a chosen sequence in DNA, where a protein cuts the strand. The cell then repairs the cut, and that repair can change the gene in a precise way."),
        ("Delivering the tools",
         "The editing tools must reach the cells that will form the next generation. Common methods include carrying them in with Agrobacterium bacteria, or firing coated particles into tissue, and each method suits different plants."),
        ("Off-target checks",
         "A guide can sometimes match DNA at places other than the target. Researchers search the genome for such off-target sites, sequence them and confirm that no unwanted change is present."),
        ("Trait design",
         "Good crop design starts with a clear trait, such as drought tolerance or disease resistance. Designers choose the edit that gives the trait and check that it does not harm yield or other features."),
        ("Regulatory steps",
         "Edited crops must meet the rules of each country before they are grown or sold. Rules differ widely, and some systems treat edits differently from older breeding methods."),
        ("Field trials",
         "A new variety is tested in the field over several seasons, in several places. Trials show how the crop performs in real weather, soil and pests, which the lab cannot copy."),
    ],
    "test": [
        ("What does CRISPR use to find a target sequence in DNA?",
         [("a", "A guide RNA that matches the sequence"), ("b", "A magnet placed in the soil"), ("c", "Sunlight focused by a lens"), ("d", "A sugar coating")], "a"),
        ("What are off-target sites?",
         [("a", "Places in the field where crops are sold"), ("b", "Wild flowers at the edge of a farm"), ("c", "Old seeds kept in a bank"), ("d", "DNA sites other than the intended target where a guide may match")], "d"),
        ("Which step is part of bringing an edited crop to farmers?",
         [("a", "Carving the seed into a shape"), ("b", "Freezing the crop in ice"), ("c", "Regulatory review and field trials"), ("d", "Printing the seed on paper")], "c"),
        ("What is one way editing tools are delivered into plant cells?",
         [("a", "Pouring them on the leaves as water"), ("b", "Burning them in a furnace"), ("c", "Playing them as sound"), ("d", "Carrying them in with Agrobacterium bacteria")], "d"),
        ("What does trait design aim for?",
         [("a", "A plant with no genes at all"), ("b", "A plant that never grows"), ("c", "A plant that is always the same colour"), ("d", "A plant with a useful and stable feature")], "d"),
    ],
}
