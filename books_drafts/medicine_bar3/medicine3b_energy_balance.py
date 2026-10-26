"""Medicine, bar 3 (Senior Doctor), part B: Energy Balance. How food energy is measured, what each nutrient gives, where the body spends energy, and how a crew plans its food."""
CODE = "medicine3b_energy_balance"
BOOK = {
    "title": "Energy Balance",
    "subtitle": "Energy in, energy out: how food energy is measured and where the body spends it",
    "chapters": [
        ("Energy is measured",
         "Food energy is measured in kilocalories, often just called calories, or in kilojoules. One kilocalorie is the energy needed to warm one kilogram of water by one degree Celsius. Food labels usually show both kilojoules and kilocalories."),
        ("What each nutrient gives",
         "Carbohydrates and protein each give about 4 kilocalories per gram, and fat gives about 9. That is why fat is the most energy-dense nutrient. Water gives none, and fibre gives little."),
        ("Where the body spends energy",
         "Most energy goes on keeping the body alive: the heart, lungs, brain and liver, and keeping the body warm. This resting use is called the basal metabolic rate. Movement, digestion and growth add to it, and a hard day of work can use a large share."),
        ("Energy balance",
         "Energy balance is the energy taken in compared with the energy used. Taking in more than you use over time leads to weight gain, and taking in less leads to weight loss. A match keeps weight steady. Balance is only one part of health, because the quality of food matters too."),
        ("Why estimates are rough",
         "Energy needs vary from person to person, with body size, muscle, activity and sleep. Labels and calculators give estimates, not exact figures. Tracking weight over several weeks tells you more than a single day's numbers."),
        ("Energy on a ship",
         "A crew doing hard work needs enough food energy to match it, and too little shows up quickly as tiredness and poor focus. Feeding a crew costs money, so a careful planner compares the energy each meal gives with what it costs. Grains and pulses often give plenty of energy for the money, while small luxury items cost more per unit of energy."),
    ],
    "test": [
        ("About how much energy does fat give per gram?",
         [("a", "About 4 kilocalories"), ("b", "About 9 kilocalories"), ("c", "About 1 kilocalorie"), ("d", "About 20 kilocalories")], "b"),
        ("What is the basal metabolic rate?",
         [("a", "The energy the body uses at rest to keep vital work going"), ("b", "The speed of a ship"), ("c", "The rate at which food is bought"), ("d", "The number of meals in a day")], "a"),
        ("What is energy balance?",
         [("a", "Money spent compared with money saved"), ("b", "Water taken in compared with water lost"), ("c", "Energy taken in compared with energy used"), ("d", "Hours of sleep compared with hours awake")], "c"),
        ("Which statement about energy needs is right?",
         [("a", "Labels and calculators give estimates, and needs vary from person to person"), ("b", "Everyone needs exactly the same energy"), ("c", "Energy needs never change"), ("d", "Estimates are exact to the calorie")], "a"),
        ("Which tells you more about how food affects your weight?",
         [("a", "One day's numbers"), ("b", "A single meal"), ("c", "Guessing"), ("d", "Weight tracked over several weeks")], "d"),
    ],
}
