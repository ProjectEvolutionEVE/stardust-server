"""Ship Maintenance & Repair: real-world basics of keeping machines and spacecraft working. Background knowledge."""
CODE = "maintenance"
BOOK = {
    "title": "Ship Maintenance & Repair",
    "subtitle": "Keeping a ship healthy, and fixing it when it isn't",
    "chapters": [
        ("Why maintenance matters",
         "Every machine wears out. Maintenance is looking after it before it breaks; repair is fixing it after. In "
         "space there is no roadside help, so good crews look after their ship every day."),
        ("Look, listen, check",
         "Most trouble shows up early: a new noise, a warm part, a reading that creeps up, a loose fitting. Regular "
         "inspections catch small problems while they are still small and cheap to fix."),
        ("What wears a ship out",
         "• Moving parts rub and wear, so they need checking and replacing.\n"
         "• Heat and cold: swinging between sunlight and shadow makes metal grow and shrink, over and over.\n"
         "• Radiation slowly wears down electronics and some materials.\n"
         "• Tiny specks of dust and debris, called micrometeoroids, hit the hull at very high speed. Flying through "
         "debris fields makes this a real concern."),
        ("Fix the cause, not just the symptom",
         "A blown fuse is a symptom; the short circuit that blew it is the cause. Replace the fuse without finding "
         "the cause and it blows again. Good repair asks why it failed, fixes that, then tests that it works."),
        ("Safety first",
         "Before working on anything, switch it off and make sure it stays off. Never work alone on something "
         "dangerous without the right equipment. In a sealed ship, air is precious: a leak is always the first "
         "thing to deal with."),
        ("Spares and records",
         "Keep the right spare parts, and write down what was checked, what was fixed and when. Records show which "
         "parts fail often, so they can be improved."),
        ("Maintenance aboard",
         "Aboard the Starship, better parts begin as blueprints. A designer can submit an upgrade or a newer version "
         "of Starship standard equipment or of an approved design, naming what it builds on and what's different. "
         "Knowing what wears out is the best way to know what to improve."),
    ],
    "test": [
        ("What is the difference between maintenance and repair?",
         [("a", "There is none"), ("b", "Maintenance is before it breaks, repair is after"), ("c", "Repair is cheaper"), ("d", "Maintenance is only for engines")], "b"),
        ("What are micrometeoroids?",
         [("a", "Tiny specks hitting the hull at high speed"), ("b", "Small planets"), ("c", "A kind of fuel"), ("d", "Ship computers")], "a"),
        ("A fuse keeps blowing. What should you do?",
         [("a", "Use a bigger fuse"), ("b", "Ignore it"), ("c", "Find and fix the cause"), ("d", "Remove the fuse")], "c"),
        ("What should you do before working on a machine?",
         [("a", "Switch it off and make sure it stays off"), ("b", "Run it faster"), ("c", "Nothing"), ("d", "Paint it")], "a"),
        ("How does a designer improve Starship equipment?",
         [("a", "By chatting with other players"), ("b", "By submitting an upgrade blueprint"), ("c", "By buying it at the market"), ("d", "It can't be improved")], "b"),
    ],
}
