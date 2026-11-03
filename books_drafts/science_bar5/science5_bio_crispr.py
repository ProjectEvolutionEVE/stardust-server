"""CRISPR and Gene Editing Mechanisms: how guide RNAs direct cutting enzymes, how cells repair the cuts and what to watch for."""
CODE = "science5_bio_crispr"
BOOK = {
    "title": "CRISPR and Gene Editing Mechanisms",
    "subtitle": "How guide RNA steers a cutting enzyme, how cells repair the cut, and the limits",
    "chapters": [
        ("A programmable scissors", "CRISPR systems came from a defence that bacteria use against viruses. Scientists adapted one of them, using a protein called Cas9, into a tool that can cut DNA at a chosen place."),
        ("Guide RNA design", "A guide RNA is a short piece of RNA that matches the DNA target. Designing a good guide means picking a sequence that is unique in the genome and sits next to the right short motif that Cas9 needs."),
        ("Cas nucleases", "The Cas protein is the enzyme that makes the cut. Different Cas proteins can cut in different ways or recognise different sequences, which gives researchers several tools to choose from."),
        ("Repair pathways", "After a cut, cells repair the break. One common route joins the ends back together and can leave small changes, while another uses a template to copy in a chosen sequence more precisely."),
        ("Off-target effects", "Guides can sometimes match and cut at places that are similar but not identical to the target. These off-target effects must be checked, because they can change genes that were not meant to change."),
        ("Base editing and ethics", "Base editors change a single DNA letter without a full double cut. Gene editing raises ethical and regulatory questions, since edits can affect people and future generations, so oversight matters."),
    ],
    "test": [
        ("What does the guide RNA do in a CRISPR system?",
         [("a", "It cuts proteins into small pieces"), ("b", "It makes the cell divide"), ("c", "It directs the Cas nuclease to a matching DNA sequence"), ("d", "It stores energy")], "c"),
        ("What is an off-target effect?",
         [("a", "A sound from a machine"), ("b", "The intended cut"), ("c", "A protein folding correctly"), ("d", "A cut or change at an unintended DNA site")], "d"),
        ("What do cells use to repair a cut made by Cas9?",
         [("a", "Natural DNA repair pathways such as end joining or template repair"), ("b", "Photosynthesis"), ("c", "Muscle contraction"), ("d", "Sound waves")], "a"),
        ("What is base editing?",
         [("a", "Printing new DNA on paper"), ("b", "Changing one DNA letter into another without a full cut through both strands"), ("c", "Adding a new cell wall"), ("d", "Removing all RNA")], "b"),
        ("Why do gene editing tools raise ethical and regulatory questions?",
         [("a", "Because they are very cheap"), ("b", "Because they only work on rocks"), ("c", "Because they have no effects at all"), ("d", "Because edits can affect people and future generations, so rules and oversight matter")], "d"),
    ],
}
