"""Process Safety and Reaction Hazards: exotherms, thermal runaway, adiabatic temperature rise, calorimetry and hazard controls."""
CODE = "science5_chem_process_safety"
BOOK = {
    "title": "Process Safety and Reaction Hazards",
    "subtitle": "Exotherm screening, runaway reactions and lessons from incidents",
    "chapters": [
        ("Heat is the main hazard", "Many chemical reactions give off heat. If that heat builds up faster than it can be removed, the reaction can run away. Process safety is the discipline that prevents this."),
        ("Exotherm screening", "Exotherm screening checks a reaction for heat release before it is scaled up. Scientists measure how much heat is released and how fast. Early screening catches hazards while changes are still cheap."),
        ("Thermal runaway", "Thermal runaway is a cycle where rising temperature speeds the reaction, which releases more heat still. It can lead to boiling, pressure build-up and vessel failure. Cooling capacity must always exceed the heat released."),
        ("Adiabatic temperature rise", "The adiabatic temperature rise is how much the temperature would climb if no heat escaped. It is found from the reaction heat, the concentration and the heat capacity of the mixture. A large value signals a serious hazard."),
        ("Calorimetry data", "Reaction calorimetry measures heat flow during a reaction at lab scale. Its data give the heat released and the rate of heat release. These data feed safety calculations for larger plants."),
        ("Hazard controls and lessons", "Hazards are controlled with cooling, dosing controls, emergency quench systems and pressure relief. Past incidents show what happens when these controls fail. Each incident teaches a lesson that improves future plant design."),
    ],
    "test": [
        ("What is thermal runaway?",
         [("a", "A cycle where rising temperature speeds the reaction, which releases more heat"), ("b", "A cool room getting colder"), ("c", "A reaction that stops by itself"), ("d", "A slow walk to the lab")], "a"),
        ("What does the adiabatic temperature rise show?",
         [("a", "The colour of the mixture"), ("b", "The weight of the flask"), ("c", "How much the temperature would climb if no heat escaped"), ("d", "The number of chemists present")], "c"),
        ("What does reaction calorimetry measure?",
         [("a", "The sound of stirring"), ("b", "The brightness of the lamp"), ("c", "Heat flow during a reaction"), ("d", "The height of the fume hood")], "c"),
        ("What must cooling capacity always do?",
         [("a", "Be smaller than zero"), ("b", "Stay exactly the same as the room"), ("c", "Never be checked"), ("d", "Exceed the heat being released")], "d"),
        ("What is exotherm screening?",
         [("a", "Checking a reaction for heat release before scaling up"), ("b", "Painting the reactor red"), ("c", "Counting the chairs in the lab"), ("d", "Checking the price of the solvent")], "a"),
    ],
}
