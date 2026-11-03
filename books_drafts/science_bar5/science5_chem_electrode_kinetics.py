"""Electrode Kinetics and Overpotential: how fast charge moves across an electrode interface, and why extra voltage is needed."""
CODE = "science5_chem_electrode_kinetics"
BOOK = {
    "title": "Electrode Kinetics and Overpotential",
    "subtitle": "The Butler-Volmer equation, charge transfer and sources of overpotential",
    "chapters": [
        ("Charge across an interface", "Electrode kinetics studies how fast electrons move across the boundary between an electrode and a solution. The rate depends on the voltage applied. Faster transfer means a bigger current."),
        ("Charge transfer", "Charge transfer is the step where an electron passes between the electrode and a species in solution. Its rate depends on the energy barrier for that step. The barrier is changed by the applied voltage."),
        ("Overpotential", "Overpotential is the extra voltage beyond the equilibrium voltage needed to drive a reaction at a useful rate. It is the difference between the applied potential and the equilibrium potential. Some overpotential is always needed in practice."),
        ("The Butler-Volmer equation", "The Butler-Volmer equation links current to overpotential through an exchange current and a transfer coefficient. It predicts how current rises steeply as overpotential grows. The transfer coefficient is often close to one half in simple systems."),
        ("Sources of overpotential", "Overpotential comes from several sources, including slow charge transfer, slow transport of reactants and resistance in the cell. Each source can be measured separately. Reducing them makes batteries and fuel cells more efficient."),
        ("Kinetic measurements", "Kinetic measurements use voltammetry and impedance to study electrode reactions. Tafel plots help find the exchange current and transfer coefficient. These measurements guide the choice of catalysts and electrode materials."),
    ],
    "test": [
        ("What is electrode kinetics about?",
         [("a", "How fast a ship sails across a lake"), ("b", "How fast a cloud moves across the sky"), ("c", "How fast charge moves across an electrode interface"), ("d", "How fast a plant grows in shade")], "c"),
        ("What is overpotential?",
         [("a", "The voltage of a battery fully charged"), ("b", "The voltage of a lightning strike"), ("c", "The extra voltage beyond equilibrium needed to drive a reaction at a useful rate"), ("d", "The voltage of a lamp in a room")], "c"),
        ("What does the Butler-Volmer equation link?",
         [("a", "Current to overpotential"), ("b", "Colour to taste"), ("c", "Height to weight of a box"), ("d", "Speed to the day of the week")], "a"),
        ("What is a typical value of the transfer coefficient in simple systems?",
         [("a", "Exactly one hundred"), ("b", "Close to zero for all cells"), ("c", "Close to one half"), ("d", "Exactly three")], "c"),
        ("Which of these is a source of overpotential?",
         [("a", "Sunlight falling on the desk"), ("b", "The shape of a mug"), ("c", "The sound of a kettle"), ("d", "Slow charge transfer at the electrode")], "d"),
    ],
}
