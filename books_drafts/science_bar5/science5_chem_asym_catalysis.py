"""Asymmetric Catalysis: chiral catalysts that favour one mirror-image product, and how their selectivity is measured."""
CODE = "science5_chem_asym_catalysis"
BOOK = {
    "title": "Asymmetric Catalysis",
    "subtitle": "Chiral catalysts, enantioselective steps, ligand design and kinetic resolution",
    "chapters": [
        ("Catalysts that choose", "An asymmetric catalyst speeds a reaction and favours one mirror-image product over the other. This matters for medicines, because the two enantiomers of a drug can act very differently. The catalyst does not get used up in the reaction."),
        ("Enantioselective steps", "An enantioselective step gives mainly one enantiomer from a prochiral starting material. The catalyst creates a chiral environment that guides which face of the molecule reacts. Small changes in the catalyst can change the outcome."),
        ("Ligand design", "Many asymmetric catalysts are metal complexes with chiral ligands attached. The shape of the ligands sets the chiral space around the metal. Chemists design ligands and then test many variants."),
        ("Kinetic resolution", "In kinetic resolution, a chiral catalyst reacts with one enantiomer of a racemic mixture faster than the other. Left over is the slower-reacting enantiomer, enriched in purity. In the simplest case, the most that can be recovered as the unreacted enantiomer is half."),
        ("Industrial examples", "Asymmetric catalysis is used to make many drugs and fine chemicals. Some industrial processes make tonnes of a single enantiomer each year. These examples show the value of good selectivity."),
        ("Measuring selectivity", "Selectivity is measured by enantiomeric excess, which compares the amounts of the two products. Chiral chromatography and polarimetry are common tools. Careful measurement is needed to report reliable results."),
    ],
    "test": [
        ("What does an asymmetric catalyst favour?",
         [("a", "One of two mirror-image products"), ("b", "Both products equally every time"), ("c", "Only gases"), ("d", "Only metal salts")], "a"),
        ("Why does the chirality of a drug matter?",
         [("a", "It changes the colour of the tablet"), ("b", "It makes the drug heavier"), ("c", "Its two enantiomers can act very differently"), ("d", "It has no effect on the body")], "c"),
        ("What is a ligand in a catalyst?",
         [("a", "A type of tyre"), ("b", "A group bonded to a central metal that shapes the catalyst"), ("c", "A kind of paint for walls"), ("d", "A slow form of ice")], "b"),
        ("In simple kinetic resolution, what is the most of one enantiomer that can be recovered?",
         [("a", "Ten percent"), ("b", "All of it"), ("c", "Half"), ("d", "None at all")], "c"),
        ("How is selectivity measured?",
         [("a", "Enantiomeric hunger"), ("b", "Melting sound"), ("c", "Enantiomeric excess"), ("d", "Flask colour")], "c"),
    ],
}
