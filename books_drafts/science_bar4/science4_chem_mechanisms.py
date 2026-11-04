"""Reaction Mechanisms and Rate Laws: how chemists measure reaction rates, and how step-by-step mechanisms explain them."""
CODE = "science4_chem_mechanisms"
BOOK = {
    "title": "Reaction Mechanisms and Rate Laws",
    "subtitle": "Rates, orders, intermediates and the step-by-step path of a reaction",
    "chapters": [
        ("Rate laws and reaction order",
         "A rate law links the speed of a reaction to the concentrations of its reactants. The order with respect to a reactant is the power to which its concentration appears in the rate law. Orders must be found by experiment, not from the equation alone."),
        ("Reaction intermediates",
         "An intermediate is a species formed in one step and used up in a later step. It does not appear in the overall equation. Intermediates are often short-lived and hard to detect."),
        ("The steady-state approximation",
         "The steady-state approximation assumes that the concentration of an intermediate stays nearly constant while the reaction runs. It lets chemists write a simple rate law from a multi-step mechanism. It is a useful, though approximate, tool."),
        ("Elementary steps",
         "An elementary step is a single molecular event. Its rate law can be written directly from its molecularity, which is the number of molecules that collide in that step. The sum of elementary steps gives the overall mechanism."),
        ("Measuring rates",
         "Rates are measured by following a property that changes with time, such as absorbance, pressure or the amount of a product. Measuring at several starting concentrations reveals how the rate depends on each reactant."),
        ("Evidence for a mechanism",
         "A proposed mechanism must match the observed rate law, and it should predict other facts, such as the effect of temperature or the detection of an intermediate. A mechanism that fits all the evidence is a strong one, though never proven beyond doubt."),
    ],
    "test": [
        ("What does a rate law link?",
         [("a", "The colour of the reactants to the price of the products"), ("b", "The mass of the flask to the time of day"), ("c", "The speed of a reaction to the concentrations of its reactants"), ("d", "The volume of water to the temperature of the room")], "c"),
        ("What is a reaction intermediate?",
         [("a", "The final product of the reaction"), ("b", "A catalyst that never changes"), ("c", "The solvent of the reaction"), ("d", "A species that is formed in one step and used up in a later one")], "d"),
        ("What does the steady-state approximation assume?",
         [("a", "That the reaction never runs"), ("b", "That the intermediate is always the largest amount"), ("c", "That all steps are equally slow"), ("d", "That the intermediate concentration stays nearly constant")], "d"),
        ("What is an elementary step?",
         [("a", "The first lesson in a textbook"), ("b", "A single molecular event"), ("c", "A kind of solvent"), ("d", "A measure of pressure")], "b"),
        ("What must a proposed mechanism do?",
         [("a", "Ignore the rate law"), ("b", "Use only one step"), ("c", "Predict nothing at all"), ("d", "Match the observed rate law")], "d"),
    ],
}
