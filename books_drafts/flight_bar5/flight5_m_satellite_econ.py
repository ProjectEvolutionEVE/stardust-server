"""Satellite Business Models: capital, revenue, satellite life, replacement, constellations and failures such as Iridium."""
CODE = "flight5_m_satellite_econ"
BOOK = {
    "title": "Satellite Business Models",
    "subtitle": "Big upfront costs, long payback, and what can go wrong",
    "chapters": [
        ("Capital first",
         "A satellite business spends heavily before earning anything. Building, launching and insuring a satellite can cost a great deal. Investors must wait years for their money back, so the model depends on long-term funding."),
        ("Where revenue comes from",
         "Satellites earn money from services, such as television, communications, navigation, weather data and images of Earth. Each service needs customers willing to pay enough to cover the costs."),
        ("Satellite life",
         "A satellite has a limited life, set by its fuel, its electronics and its orbit. When it runs low on fuel or fails, it stops earning. Operators must plan carefully for each satellite's working years."),
        ("Replacement",
         "Because satellites wear out, operators must pay to replace them. A business that plans replacement early can keep its service running. One that does not may find its revenue fading."),
        ("Constellations",
         "A constellation is a group of many satellites working together to cover the globe. Large constellations need many launches and large budgets. They can offer fast service, but the cost of building and replacing them is very high."),
        ("Failures",
         "The satellite phone firm Iridium built a large constellation in the 1990s and filed for bankruptcy in 1999. Its costs were high and its customers were fewer than expected. Such cases show how fragile these businesses can be."),
    ],
    "test": [
        ("Why do satellite businesses need long-term funding?",
         [("a", "They spend heavily before earning, and wait years for returns"), ("b", "They never spend money"), ("c", "They earn money on the first day"), ("d", "They have no costs")], "a"),
        ("What limits a satellite's working life?",
         [("a", "The colour of its paint"), ("b", "The weather on Earth"), ("c", "Its fuel, its electronics and its orbit"), ("d", "The number of stars")], "c"),
        ("What is a constellation in this sense?",
         [("a", "A type of star chart"), ("b", "A group of many satellites working together"), ("c", "A single large satellite"), ("d", "A map of cities")], "b"),
        ("What happened to the satellite phone firm Iridium?",
         [("a", "It doubled its customers at once"), ("b", "It was never built"), ("c", "It moved to the Moon"), ("d", "It filed for bankruptcy in 1999")], "d"),
        ("Why does replacement matter for a satellite business?",
         [("a", "Satellites never wear out"), ("b", "Replacement is always free"), ("c", "Satellites wear out, and revenue fades if they are not replaced"), ("d", "It is banned")], "c"),
    ],
}
