"""Organometallic Chemistry and Catalytic Cycles: metal-carbon bonds and the steps that let metals drive reactions."""
CODE = "science5_chem_organometallic"
BOOK = {
    "title": "Organometallic Chemistry and Catalytic Cycles",
    "subtitle": "Metal-carbon bonds, key steps and the way catalysts wear out",
    "chapters": [
        ("Metal-carbon bonds", "Organometallic compounds contain at least one bond between a metal and a carbon atom. These bonds give metals the power to make and break carbon-carbon links. Many important industrial processes depend on them."),
        ("Oxidative addition", "In oxidative addition, a molecule such as H-H or C-X adds across a metal centre. The metal's oxidation state rises by two. The number of ligands around the metal often rises as well."),
        ("Reductive elimination", "Reductive elimination is the reverse of oxidative addition. Two groups leave the metal together as a new bond, and the metal's oxidation state falls by two. This step releases the product from the catalyst."),
        ("Insertion", "In migratory insertion, a group on the metal moves to a neighbouring ligand, such as an alkene. A new metal-carbon bond forms in the process. Insertion builds up the carbon chain step by step."),
        ("Catalytic cycles", "A catalytic cycle links these steps into a loop. The catalyst is used again and again, and the product leaves at one step. Drawing the cycle helps chemists see what each step must achieve."),
        ("Catalyst deactivation", "Catalysts can lose activity over time. They may decompose, bind too strongly to a product or be poisoned by impurities. Understanding deactivation helps chemists design more robust catalysts."),
    ],
    "test": [
        ("What is an organometallic compound?",
         [("a", "A compound made only of gases"), ("b", "A compound with no metal at all"), ("c", "A compound with at least one bond between a metal and a carbon atom"), ("d", "A sugar with no carbon")], "c"),
        ("What happens to the metal's oxidation state in oxidative addition?",
         [("a", "It falls by two"), ("b", "It stays exactly the same"), ("c", "It rises by two"), ("d", "It becomes zero forever")], "c"),
        ("What is reductive elimination?",
         [("a", "A metal turning into a solid cube"), ("b", "A catalyst being added to water"), ("c", "A sample being heated in a flame"), ("d", "Two groups leave the metal together and form a new bond")], "d"),
        ("What is migratory insertion?",
         [("a", "Metal atoms being melted into powder"), ("b", "A group on the metal moves onto a neighbouring ligand"), ("c", "A bottle being filled with gas"), ("d", "A ball falling down a slope")], "b"),
        ("Why do catalysts lose activity?",
         [("a", "They grow larger every day"), ("b", "They change into sugar"), ("c", "They can decompose, bind too strongly or be poisoned"), ("d", "They become lighter in colour only")], "c"),
    ],
}
