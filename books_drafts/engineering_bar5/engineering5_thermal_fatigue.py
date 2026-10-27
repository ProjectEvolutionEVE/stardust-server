"""Thermal Fatigue and Thermomechanical Cycling: how repeated heating and cooling cracks parts that are held in place."""
CODE = "engineering5_thermal_fatigue"
BOOK = {
    "title": "Thermal Fatigue and Thermomechanical Cycling",
    "subtitle": "How repeated heating and cooling cracks parts that are held in place",
    "chapters": [
        ("Heating and cooling",
         "Parts heat and cool in cycles, for example at each engine start and stop. Each cycle makes the material expand and contract."),
        ("Constrained expansion",
         "When a part is held in place, it cannot expand freely, so the thermal strain turns into stress. The stress rises as the temperature changes."),
        ("Strain range",
         "The key quantity is the strain range over a cycle, which is the total change in strain. A larger strain range shortens life."),
        ("Life models",
         "Life models relate the strain range, the temperature and the cycle count to failure. At high temperature they must combine fatigue with creep."),
        ("Cracking in hot parts",
         "Cracks often start at corners, holes or welds, where strain concentrates. Coatings and cooling holes can change where and when cracks appear."),
        ("Design around it",
         "Designers allow for free expansion, reduce constraint and choose materials that resist cycling. Testing under realistic cycles confirms the design."),
    ],
    "test": [
        ("What causes thermal fatigue?",
         [("a", "A paint drying"), ("b", "Sugar"), ("c", "Repeated heating and cooling of a part"), ("d", "A fixed cold temperature")], "c"),
        ("What happens when a held part tries to expand?",
         [("a", "Thermal strain turns into stress"), ("b", "Nothing happens"), ("c", "It shrinks to nothing"), ("d", "It turns to glass")], "a"),
        ("What is the strain range?",
         [("a", "A paint range"), ("b", "A price range"), ("c", "A colour range"), ("d", "The total change in strain over a cycle")], "d"),
        ("Where do cracks often start in hot parts?",
         [("a", "In open air"), ("b", "At corners, holes or welds"), ("c", "At the top of the sky"), ("d", "Nowhere")], "b"),
        ("What do life models combine at high temperature?",
         [("a", "Fatigue and creep"), ("b", "Paint and glue"), ("c", "Price and time"), ("d", "Sun and rain")], "a"),
    ],
}
