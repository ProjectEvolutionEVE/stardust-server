"""Radiometric Dating: using radioactive decay as a clock locked inside minerals, and planning the cost of lab work."""
CODE = 'science3a_radiometric'
BOOK = {
    "title": 'Radiometric Dating',
    "subtitle": 'Using radioactive decay as a clock locked inside minerals',
    "chapters": [
        ("A clock that ticks",
         "Some unstable atoms, called the parent isotope, decay at a fixed rate into a stable atom called the daughter isotope. Heat and pressure do not change that rate, so the decay can serve as a clock."),
        ("Reading the clock",
         "After one half-life, half of the parent atoms have decayed. By measuring the ratio of parent to daughter atoms in a mineral, scientists work out how long ago the mineral locked those atoms in place."),
        ("Zircon",
         "Zircon is a tough mineral that takes up uranium when it forms, but it rejects lead. So any lead found inside zircon came from the decay of uranium. That makes zircon one of the most trusted clocks in geology."),
        ("Very old grains",
         "Zircon grains from the Jack Hills in Western Australia are about 4.4 billion years old. They are among the oldest solid material ever found on Earth, and they tell us that the planet's crust had formed by then."),
        ("Carbon-14",
         "Carbon-14 has a half-life of about 5,730 years, so it dates once-living material such as wood and bone. It works only up to roughly 50,000 years, because after that too little carbon-14 remains to measure."),
        ("Planning lab work",
         "Lab dating costs money for each sample and each test. Before you order, list the samples you need, the tests and their costs, and what you will do if a result is unclear. A plan keeps the budget honest."),
    ],
    "test": [
        ("What is a daughter isotope?",
         [('a', 'The original unstable atom'), ('b', 'A type of mineral'), ('c', 'The stable atom that decay produces'), ('d', 'A kind of rock layer')], 'c'),
        ("After one half-life, what fraction of the parent atoms remain?",
         [('a', 'One quarter'), ('b', 'One half'), ('c', 'All of them'), ('d', 'None of them')], 'b'),
        ("Why is zircon useful for dating?",
         [('a', 'It melts at a very low temperature'), ('b', 'It floats in water'), ('c', 'It is always found on the Moon'), ('d', 'It takes up uranium and rejects lead')], 'd'),
        ("Which dating method suits material up to about 50,000 years old?",
         [('a', 'Carbon-14'), ('b', 'Uranium-lead'), ('c', 'Potassium-argon'), ('d', 'Lead-206 only')], 'a'),
        ("When planning a lab order, what should come first?",
         [('a', 'Pay the full fee in advance'), ('b', 'Choose the shiniest sample'), ('c', 'List the samples, the tests, their costs and what to do if a result is unclear'), ('d', 'Order every test in the lab')], 'c'),
    ],
}
