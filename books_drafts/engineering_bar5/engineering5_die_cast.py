"""Die Casting Alloys and Cold Chambers: alloy choice, cold and hot chamber machines, gate design, porosity and die life."""
CODE = "engineering5_die_cast"
BOOK = {
    "title": "Die Casting Alloys and Cold Chambers",
    "subtitle": "Forcing molten metal into steel dies at high speed",
    "chapters": [
        ("Fast casting in steel dies",
         "Die casting forces molten metal into a steel die under high pressure. The parts come out fast and with fine detail and smooth surfaces. The method is used for high-volume parts in many products."),
        ("Choosing the alloy",
         "Zinc, aluminium and magnesium alloys are common in die casting. Each has its own melting point, strength and cost. The alloy is chosen to match both the part's job and the machine that will cast it."),
        ("Hot and cold chambers",
         "In a hot chamber machine, the injection system sits in the molten metal, which suits zinc and magnesium. In a cold chamber machine, the metal is ladled into a separate shot chamber, which suits aluminium. The choice of machine follows the alloy."),
        ("Gate design",
         "The gate is the opening where metal enters the die. Its size and place control how smoothly the metal fills the cavity. A well-placed gate reduces turbulence and trapped air."),
        ("Porosity",
         "Trapped air and shrinkage can leave porosity inside a die cast part. Vents in the die let the air escape, and careful control of speed and pressure helps. Some parts are sealed or heat treated to be safe for pressure use."),
        ("Die life",
         "Dies wear and crack from heat and repeated shots. Die life is the number of good parts a die makes before it must be repaired or replaced. Die life is a major part of the cost per part, and it is tracked closely."),
    ],
    "test": [
        ("What does die casting do?",
         [("a", "It pours wax into sand"), ("b", "It forces molten metal into a steel die under high pressure"), ("c", "It rolls sheets flat"), ("d", "It spins clay on a wheel")], "b"),
        ("Which alloys are common in die casting?",
         [("a", "Wood and cloth"), ("b", "Glass and paper"), ("c", "Zinc, aluminium and magnesium alloys"), ("d", "Rubber and foam")], "c"),
        ("Which kind of machine suits aluminium?",
         [("a", "A paper press"), ("b", "A potter's wheel"), ("c", "A hand saw"), ("d", "A cold chamber machine")], "d"),
        ("What does the gate do in a die?",
         [("a", "It is the opening where metal enters the die"), ("b", "It holds the handle"), ("c", "It cools the room"), ("d", "It counts the shots")], "a"),
        ("What is die life?",
         [("a", "The age of the factory"), ("b", "The number of good parts a die makes before repair or replacement"), ("c", "The length of the power cable"), ("d", "The number of workers on shift")], "b"),
    ],
}
