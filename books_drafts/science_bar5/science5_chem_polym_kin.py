"""Polymerisation Kinetics and Chain Growth: step and chain growth, kinetic chain length, molecular weight and living polymerisation."""
CODE = "science5_chem_polym_kin"
BOOK = {
    "title": "Polymerisation Kinetics and Chain Growth",
    "subtitle": "Step versus chain growth, molecular weight distributions and living systems",
    "chapters": [
        ("Building long molecules", "Polymers are long chains made of repeating units called monomers. The way the chain grows affects its length, structure and properties. Kinetics explains how fast that growth happens."),
        ("Step versus chain growth", "In step growth, any two molecules can react, and chains build up slowly through many steps. In chain growth, a reactive centre adds one monomer after another very quickly. The two routes give very different molecular weights over time."),
        ("Kinetic chain length", "The kinetic chain length is the average number of monomers added to each active centre before it stops. It depends on the rates of propagation and termination. A high ratio of propagation to termination gives long chains."),
        ("Initiation and termination", "Chain growth starts with initiation, which creates the reactive centre. It ends by termination, when two active centres combine or when a transfer step stops growth. Each step affects the final product."),
        ("Molecular weight distributions", "Real polymers contain chains of many different lengths, so they have a distribution of molecular weights. The polydispersity index compares the average weights and measures how broad the distribution is. Narrow distributions often give more predictable properties."),
        ("Living polymerisation", "In living polymerisation, chains keep growing as long as monomer is supplied, because termination is absent. This gives polymers with very narrow distributions and control over length. It is a powerful way to design polymer structures."),
    ],
    "test": [
        ("What is a polymer built from?",
         [("a", "Single atoms of gold"), ("b", "Bubbles of air"), ("c", "Grains of sand"), ("d", "Repeating units called monomers")], "d"),
        ("What is a key difference between step and chain growth?",
         [("a", "Step growth is always much faster"), ("b", "Chain growth never makes long molecules"), ("c", "There is no difference at all"), ("d", "In chain growth a reactive centre adds monomers one after another quickly")], "d"),
        ("What is kinetic chain length?",
         [("a", "The length of a metal pipe"), ("b", "The average number of monomers added to each active centre before it stops"), ("c", "The distance a polymer travels in air"), ("d", "The time a polymer sits on a shelf")], "b"),
        ("What is the polydispersity index a measure of?",
         [("a", "How hot a polymer is"), ("b", "How much a polymer weighs in a bag"), ("c", "How broad the distribution of chain lengths is"), ("d", "How many colours a polymer has")], "c"),
        ("What is a feature of living polymerisation?",
         [("a", "Chains shrink to nothing"), ("b", "Chains turn into stone"), ("c", "Chains are never formed"), ("d", "Chains keep growing because termination is absent")], "d"),
    ],
}
