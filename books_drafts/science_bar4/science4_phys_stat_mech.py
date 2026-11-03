"""Statistical Mechanics and Entropy: how the behaviour of huge numbers of particles gives heat, entropy and the one-way direction of time."""
CODE = "science4_phys_stat_mech"
BOOK = {
    "title": "Statistical Mechanics and Entropy",
    "subtitle": "From countless particles to heat, entropy and the arrow of time",
    "chapters": [
        ("Microstates and macrostates",
         "A macrostate describes a system by a few large-scale quantities, such as temperature and volume. A microstate describes the exact position and motion of every particle. Many different microstates can give the same macrostate."),
        ("Boltzmann's entropy",
         "Boltzmann showed that entropy is S equals k times the logarithm of the number of microstates, where k is Boltzmann's constant. More microstates means more entropy. This links disorder to counting and gives entropy a clear meaning."),
        ("Ensembles",
         "An ensemble is a large collection of imagined copies of a system, each in a possible microstate. Averages over an ensemble give the properties we measure. Different ensembles suit different conditions, such as fixed energy or fixed temperature."),
        ("Heat capacity",
         "Heat capacity is the amount of heat needed to raise a system’s temperature by one degree. It depends on how the energy of the particles is shared among their motions. Measuring heat capacity gives clues to the internal structure of matter."),
        ("Equipartition",
         "The equipartition theorem says that, at a given temperature, each independent way a particle can store energy holds on average half a unit of thermal energy per degree of freedom, measured in units of k times T. It explains many simple heat capacities."),
        ("The arrow of time",
         "Systems tend to move from less likely macrostates to more likely ones, so entropy usually rises. This gives time a direction, even though the basic laws of motion work in both directions. The arrow of time is a statistical fact about large systems."),
    ],
    "test": [
        ("What does a microstate describe?",
         [("a", "The average colour of a room"), ("b", "The total price of a gas"), ("c", "The exact position and motion of every particle"), ("d", "The number of walls")], "c"),
        ("What is Boltzmann's formula for entropy?",
         [("a", "S equals k times the logarithm of the number of microstates"), ("b", "S equals the mass times the speed"), ("c", "S equals force times time"), ("d", "S equals zero always")], "a"),
        ("What is an ensemble?",
         [("a", "A type of choir"), ("b", "A single particle"), ("c", "A large collection of imagined copies of a system in possible microstates"), ("d", "A chemical bond")], "c"),
        ("What does heat capacity measure?",
         [("a", "The colour of a flame"), ("b", "The heat needed to raise a system’s temperature by one degree"), ("c", "The speed of sound"), ("d", "The weight of an atom")], "b"),
        ("Why does entropy give time a direction?",
         [("a", "Because clocks always run backward"), ("b", "Because systems tend to move to more likely macrostates"), ("c", "Because particles never move"), ("d", "Because time is a colour")], "b"),
    ],
}
