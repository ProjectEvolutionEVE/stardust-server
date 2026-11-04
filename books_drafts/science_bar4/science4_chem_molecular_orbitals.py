"""Molecular Orbitals and Bond Order: how atomic orbitals combine into molecular ones, and how bond order and magnetism follow."""
CODE = "science4_chem_molecular_orbitals"
BOOK = {
    "title": "Molecular Orbitals and Bond Order",
    "subtitle": "How atomic orbitals combine to make molecules",
    "chapters": [
        ("Orbital combination",
         "When atomic orbitals overlap, they combine to form molecular orbitals that span the whole molecule. Two orbitals always give two molecular orbitals: one lower in energy and one higher. Electrons fill them from the lowest energy upward."),
        ("Bonding and antibonding orbitals",
         "A bonding orbital has electron density between the nuclei and holds the atoms together. An antibonding orbital has a node between the nuclei and weakens the bond. Filling antibonding orbitals reduces the strength of a bond."),
        ("Bond order",
         "Bond order is half the difference between the number of bonding electrons and the number of antibonding electrons. A bond order of one is a single bond, two is a double bond, and zero means no stable bond forms."),
        ("Magnetism of molecules",
         "A molecule with unpaired electrons is paramagnetic and is drawn into a magnetic field. A molecule with all electrons paired is diamagnetic and is weakly pushed away. Molecular orbital theory explains the magnetism of oxygen, which has two unpaired electrons."),
        ("Simple Hückel ideas",
         "Hückel theory is a simple way to treat the pi electrons of conjugated molecules. It assigns energies to molecular orbitals across the system. The method gives a clear picture of which molecules are especially stable."),
        ("Aromatic stability",
         "Aromatic molecules, such as benzene, have a ring of pi electrons that fills bonding orbitals completely. This gives extra stability. Chemists use molecular orbital ideas to explain why aromatic rings resist change."),
    ],
    "test": [
        ("What is a bonding molecular orbital?",
         [("a", "One that has no electrons at all"), ("b", "One that pushes atoms apart"), ("c", "One that has electron density between the nuclei and holds atoms together"), ("d", "One that is always empty")], "c"),
        ("How is bond order calculated?",
         [("a", "The number of atoms in the molecule"), ("b", "Half the difference between bonding and antibonding electrons"), ("c", "The total mass of the electrons"), ("d", "The number of protons")], "b"),
        ("What does a bond order of zero mean?",
         [("a", "A double bond"), ("b", "A triple bond"), ("c", "No stable bond forms"), ("d", "The molecule is a metal")], "c"),
        ("Why is oxygen attracted to a magnetic field?",
         [("a", "It is made of iron"), ("b", "It has no electrons"), ("c", "It is always heated"), ("d", "It has unpaired electrons, so it is paramagnetic")], "d"),
        ("Why is benzene considered aromatic and stable?",
         [("a", "It has no electrons"), ("b", "Its ring of pi electrons fills bonding orbitals completely"), ("c", "It is always a gas"), ("d", "It contains no carbon")], "b"),
    ],
}
