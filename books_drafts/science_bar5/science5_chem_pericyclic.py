"""Pericyclic Reactions and the Woodward-Hoffmann Rules: concerted reactions, frontier orbitals and selection rules."""
CODE = "science5_chem_pericyclic"
BOOK = {
    "title": "Pericyclic Reactions and the Woodward-Hoffmann Rules",
    "subtitle": "Concerted reactions, frontier orbitals, electrocyclic reactions and selection rules",
    "chapters": [
        ("Reactions in one step", "Pericyclic reactions happen in a single concerted step. Bonds break and form together around a ring of electrons. No intermediate is formed along the way."),
        ("Frontier orbitals", "Frontier orbitals are the highest occupied and lowest unoccupied molecular orbitals. In many pericyclic reactions, the main action is between these two orbitals. Their shape and symmetry decide what can happen."),
        ("Electrocyclic reactions", "An electrocyclic reaction closes or opens a ring by forming or breaking one sigma bond at the ends of a conjugated chain. The stereochemical outcome depends on whether the ends rotate in the same or opposite directions. Heat or light can drive the reaction."),
        ("Cycloadditions", "A cycloaddition joins two unsaturated molecules to make a ring. The Diels-Alder reaction is a famous example, combining a diene and an alkene. It is a very reliable way to build six-membered rings."),
        ("Stereochemical outcomes", "Pericyclic reactions often give a very predictable three-dimensional result. The stereochemistry follows from the symmetry of the frontier orbitals. Chemists use this to plan syntheses."),
        ("Selection rules", "The Woodward-Hoffmann rules state which pericyclic reactions are allowed under heat or light. They are based on orbital symmetry and count electrons in the reacting system. Reactions that break the rules are slow or do not happen in one step."),
    ],
    "test": [
        ("What is a pericyclic reaction?",
         [("a", "A reaction that happens in two separate steps only"), ("b", "A reaction that happens only in water"), ("c", "A reaction that never forms bonds"), ("d", "A concerted reaction in one step, with bonds forming and breaking together")], "d"),
        ("What are frontier orbitals?",
         [("a", "The highest occupied and lowest unoccupied molecular orbitals"), ("b", "The outer walls of a flask"), ("c", "The orbits of planets"), ("d", "The shells of a nuclear reactor")], "a"),
        ("What does a Diels-Alder reaction make?",
         [("a", "A long wire of metal"), ("b", "A gas that smells sweet"), ("c", "A six-membered ring from a diene and an alkene"), ("d", "A solid crystal of salt")], "c"),
        ("What do the Woodward-Hoffmann rules describe?",
         [("a", "Which pericyclic reactions are allowed under heat or light, based on orbital symmetry"), ("b", "Which colours are safe to mix"), ("c", "Which soils grow tea"), ("d", "Which metals are shiny")], "a"),
        ("What decides the stereochemical outcome of many pericyclic reactions?",
         [("a", "The price of the solvent"), ("b", "The symmetry of the frontier orbitals"), ("c", "The name of the chemist"), ("d", "The time of day")], "b"),
    ],
}
