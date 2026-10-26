"""Corrosion: how metal rots, why some metals speed it up, and how craft are protected."""
CODE = "flight5_s_corrosion"
BOOK = {
    "title": "Corrosion",
    "subtitle": "How metal rots, and how to stop it",
    "chapters": [
        ("What rust is",
         "Rust is iron combining with oxygen and water, slowly turning solid metal into flaky oxide. Other metals corrode in their own ways, but the damage is always a loss of material."),
        ("Galvanic action",
         "When two different metals touch in damp conditions, one of them can corrode faster. This is galvanic corrosion. The metals and the moisture between them act like a tiny battery."),
        ("Stress corrosion",
         "A metal under steady stress can crack in a corrosive place, even when the corrosion itself looks slight. This is called stress corrosion cracking, and it can be sudden."),
        ("Ships and aircraft",
         "Ships spend their lives in salt water, which speeds corrosion. Aircraft meet salt spray, moisture and grime, so their hidden areas need regular checks."),
        ("Protection",
         "Paint, coatings and sealants keep water and air away from metal. Sacrificial metals such as zinc can be fitted so that they corrode first and guard the main part."),
        ("Checking and fixing",
         "Inspectors look for bubbling paint, white powder and dark stains. Catching corrosion early keeps repairs small and cheap."),
    ],
    "test": [
        ("What is rust?",
         [("a", "Metal getting shiny"), ("b", "A paint colour"), ("c", "Glass cracking"), ("d", "Iron combining with oxygen and water")], "d"),
        ("What causes galvanic corrosion?",
         [("a", "Two identical metals in sunlight"), ("b", "Two different metals touching in damp conditions"), ("c", "Dry air alone"), ("d", "Heavy rain on glass")], "b"),
        ("What is a sacrificial metal?",
         [("a", "A metal used only for coins"), ("b", "A metal that is too expensive to use"), ("c", "A metal that corrodes first to protect the main part"), ("d", "A metal that never rusts")], "c"),
        ("Why do ships corrode quickly?",
         [("a", "Salt water speeds corrosion"), ("b", "The waves are too cold"), ("c", "Their engines are heavy"), ("d", "Their paint is too bright")], "a"),
        ("Which is a sign of possible corrosion?",
         [("a", "A bright shine"), ("b", "Bubbling paint and white powder"), ("c", "A clean surface"), ("d", "A fresh coat of paint")], "b"),
    ],
}
