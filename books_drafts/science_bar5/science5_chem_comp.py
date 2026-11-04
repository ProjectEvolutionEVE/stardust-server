"""Computational Chemistry: Modelling Molecules: potential energy surfaces, basis sets, Hartree-Fock and density functional methods."""
CODE = "science5_chem_comp"
BOOK = {
    "title": "Computational Chemistry: Modelling Molecules",
    "subtitle": "Potential energy surfaces, basis sets, and checking computed results",
    "chapters": [
        ("Molecules on a computer", "Computational chemistry uses equations and computers to model molecules. It can predict shapes, energies and how fast reactions go. It works alongside experiments, not instead of them."),
        ("Potential energy surfaces", "A potential energy surface maps the energy of a molecule as its atoms move. Minima on the surface are stable shapes, and saddle points are the top of the barrier between them. Reactions can be understood as paths across this surface."),
        ("Basis sets", "A basis set is the group of mathematical functions used to describe electrons around atoms. Larger basis sets give more flexible and usually more accurate results. They also cost more computer time."),
        ("Hartree-Fock", "Hartree-Fock is a basic method that treats each electron as moving in the average field of the others. It misses some electron correlation, so its energies are approximate. It is the starting point for many better methods."),
        ("Density functional methods", "Density functional theory uses the electron density rather than the full wavefunction. Many functionals are used, and each suits some problems better than others. These methods are widely used because they balance cost and accuracy."),
        ("Geometry optimisation and checks", "Geometry optimisation moves the atoms until the energy reaches a minimum. Frequency calculations confirm whether a shape is a true minimum. Results should always be checked against experiment or a known benchmark."),
    ],
    "test": [
        ("What is a potential energy surface?",
         [("a", "A map of the ocean floor"), ("b", "A list of atomic weights"), ("c", "A diagram of a cell"), ("d", "A map of a molecule's energy as its atoms move")], "d"),
        ("What is a basis set?",
         [("a", "A set of laboratory glass"), ("b", "A group of mathematical functions used to describe electrons"), ("c", "A group of molecules in a flask"), ("d", "A list of safety rules")], "b"),
        ("What does Hartree-Fock treat each electron as doing?",
         [("a", "Moving in the average field of the other electrons"), ("b", "Standing still in one place"), ("c", "Turning into light"), ("d", "Leaving the molecule completely")], "a"),
        ("What does geometry optimisation search for?",
         [("a", "A minimum in the energy as atoms move"), ("b", "The highest possible energy only"), ("c", "The colour of the molecule"), ("d", "The price of the reagents")], "a"),
        ("Why should computed results be checked?",
         [("a", "Because computers never make any errors"), ("b", "Because chemistry does not need checking"), ("c", "Only to change their colour"), ("d", "Against experiment or a known benchmark")], "d"),
    ],
}
