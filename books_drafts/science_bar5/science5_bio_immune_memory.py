"""Immune Memory and T-Cell Responses: how T cells recognise antigens, are activated, form memory and inform vaccine design."""
CODE = "science5_bio_immune_memory"
BOOK = {
    "title": "Immune Memory and T-Cell Responses",
    "subtitle": "How the immune system learns a threat, keeps a memory and answers faster next time",
    "chapters": [
        ("Learning the enemy", "The immune system recognises invaders by their antigens, which are molecular shapes on their surface. Certain white blood cells learn to spot these shapes and respond."),
        ("Antigen presentation", "Antigen-presenting cells display fragments of proteins on MHC molecules, so T cells can inspect them. Without this display, a T cell cannot tell whether a threat is present."),
        ("T-cell activation", "A T cell needs to recognise an antigen on an antigen-presenting cell, and usually a second signal as well. With both signals, the T cell is activated and begins to divide."),
        ("Clonal selection", "Clonal selection means that the lymphocytes matching an antigen are chosen and expanded into a clone of many identical cells. Most of the clone fights the threat and then fades away."),
        ("Memory cells", "A few long-lived memory cells remain after the threat is gone. They remember the antigen and respond faster and more strongly if it returns."),
        ("Vaccine design and monitoring", "Vaccines train the immune system to build memory without the full disease. Immune monitoring measures T cells and their responses, which helps scientists judge whether a vaccine works."),
    ],
    "test": [
        ("What does a T cell need in order to be activated?",
         [("a", "Only sunlight"), ("b", "Water only"), ("c", "Sugar only"), ("d", "Recognition of an antigen displayed on an antigen-presenting cell")], "d"),
        ("What is antigen presentation?",
         [("a", "Giving a speech"), ("b", "Printing a sign"), ("c", "Showing a drawing"), ("d", "Displaying fragments of proteins on MHC molecules so T cells can see them")], "d"),
        ("What are memory cells?",
         [("a", "Long-lived cells that remember an antigen and respond faster next time"), ("b", "Cells that store phone numbers"), ("c", "Cells that make sugar"), ("d", "Cells on the Moon")], "a"),
        ("What does clonal selection mean?",
         [("a", "Selecting a plant for growth"), ("b", "Choosing a team"), ("c", "Lymphocytes that match an antigen are selected and expanded into a clone"), ("d", "Erasing DNA")], "c"),
        ("How do vaccines use immune memory?",
         [("a", "They train the immune system to build memory without the full disease"), ("b", "They remove memory"), ("c", "They stop cells from forming"), ("d", "They make the immune system sleep")], "a"),
    ],
}
