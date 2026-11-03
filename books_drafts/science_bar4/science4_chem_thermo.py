"""Thermodynamics of Reactions: enthalpy, entropy and Gibbs free energy, and what they say about whether a reaction will go."""
CODE = "science4_chem_thermo"
BOOK = {
    "title": "Thermodynamics of Reactions",
    "subtitle": "Heat, disorder and the energy that decides whether a reaction goes",
    "chapters": [
        ("Enthalpy",
         "Enthalpy is the heat content of a system at constant pressure. A reaction that releases heat has a negative enthalpy change and is called exothermic. A reaction that takes in heat is endothermic."),
        ("Entropy",
         "Entropy is a measure of disorder, or of the number of ways energy and matter can be arranged. Reactions that produce more gas or more separate particles usually raise the entropy of the system. Nature tends to move toward greater disorder."),
        ("Gibbs free energy",
         "The Gibbs free energy change combines enthalpy and entropy, weighted by temperature. It is written as delta G equals delta H minus T times delta S. It tells us the useful energy available from a reaction at constant temperature and pressure."),
        ("Spontaneity",
         "A reaction is spontaneous when its Gibbs free energy change is negative. This does not mean it is fast. Some spontaneous reactions are so slow that they seem not to happen at all, so kinetics matters as well."),
        ("Calorimetry",
         "A calorimeter measures heat by letting a reaction warm a known mass of water or another substance. The temperature rise, the mass and the specific heat give the heat of the reaction. Calorimetry is a simple way to measure enthalpy changes."),
        ("Hess's law",
         "Hess's law says the total enthalpy change of a reaction is the same however many steps it takes. This lets chemists add known enthalpy changes to find an unknown one. It works because enthalpy is a state function."),
    ],
    "test": [
        ("What does a negative enthalpy change mean?",
         [("a", "The reaction takes in heat"), ("b", "The reaction releases heat, which is exothermic"), ("c", "The reaction has no energy"), ("d", "The reaction makes no gas")], "b"),
        ("What is entropy a measure of?",
         [("a", "Disorder, or the number of ways energy and matter can be arranged"), ("b", "The mass of the reactants"), ("c", "The colour of the products"), ("d", "The price of the chemicals")], "a"),
        ("When is a reaction spontaneous?",
         [("a", "When its Gibbs free energy change is positive"), ("b", "When it is always fast"), ("c", "When its Gibbs free energy change is negative"), ("d", "When it is heated to boiling")], "c"),
        ("What does a calorimeter measure?",
         [("a", "The length of a bond"), ("b", "The heat of a reaction, from the temperature rise of a known mass"), ("c", "The colour of a flame"), ("d", "The density of a gas")], "b"),
        ("What does Hess's law say?",
         [("a", "The total enthalpy change is the same however many steps it takes"), ("b", "The enthalpy change depends on the route taken"), ("c", "Enthalpy never changes"), ("d", "Reactions must always be heated")], "a"),
    ],
}
