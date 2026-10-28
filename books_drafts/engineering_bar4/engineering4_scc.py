"""Stress corrosion cracking: the joint action of stress and environment, chloride cracking, brass and stainless examples, prevention and inspection."""
CODE = "engineering4_scc"
BOOK = {
    "title": "Stress Corrosion Cracking",
    "subtitle": "Stress and environment acting together",
    "chapters": [
        ("Two causes together",
         "Stress corrosion cracking happens when a tensile stress and a corrosive environment act together. Either one alone may cause no harm. Together they can crack a metal that looked sound."),
        ("Chloride cracking",
         "Chlorides can cause cracking in some stainless steels, especially at high temperature and under tensile stress. The crack often runs through the metal in a branching pattern. Designers limit chlorides and stress in these service conditions."),
        ("Brass examples",
         "Brass once suffered season cracking, which was linked to ammonia and stress in some components. The cracks formed in the metal after it was cold worked. Stress relief annealing reduced the problem."),
        ("Stainless examples",
         "Some austenitic stainless steels crack in hot chloride water. The crack starts small and can grow through a thick section. Choosing a steel with better resistance and reducing residual stress help prevent it."),
        ("Prevention",
         "Prevention involves reducing tensile stress, removing the corrosive agent, choosing a resistant material or applying a protective coating. Stress relief heat treatment can lower residual stress from welding or forming. Each step is chosen for the service conditions."),
        ("Inspection",
         "Inspection looks for cracks in regions of high stress and in places where the environment collects. Methods include visual checks, dye penetrant and ultrasonic testing. Regular inspection helps catch cracking before it becomes a failure."),
    ],
    "test": [
        ("What two things must act together for stress corrosion cracking?", [("a", "Paint and wind"), ("b", "Heat and sunlight"), ("c", "Tensile stress and a corrosive environment"), ("d", "Sand and gravel")], "c"),
        ("What environment is linked to chloride cracking?", [("a", "Pure oxygen"), ("b", "Clean dry air only"), ("c", "Chlorides, which can crack some stainless steels under tensile stress"), ("d", "Vacuum")], "c"),
        ("What is one way to prevent stress corrosion cracking?", [("a", "Reducing tensile stress"), ("b", "Adding more tensile stress"), ("c", "Leaving the part wet"), ("d", "Removing all inspections")], "a"),
        ("What does stress relief heat treatment do?", [("a", "Changes the colour of the part"), ("b", "Adds more stress"), ("c", "Melts the metal"), ("d", "Lowers residual stress from welding or forming")], "d"),
        ("Where should inspectors look first for stress corrosion cracks?", [("a", "Only the paint on the back"), ("b", "Regions of high stress and places where the environment collects"), ("c", "Nowhere in the part"), ("d", "Only the packaging")], "b"),
    ],
}
