"""Medicine, bar 3 (Senior Doctor), part A: Homeostasis. How the body keeps key values steady with set points, sensors and feedback loops."""
CODE = "medicine3a_homeostasis"
BOOK = {
    "title": "Homeostasis: Keeping the Inside Steady",
    "subtitle": "Set points, sensors and feedback loops that keep the body in balance",
    "chapters": [
        ("A steady inside",
         "The body works best within a narrow range for temperature, blood sugar, fluid, salts and oxygen. Keeping these values steady while the outside world changes is called homeostasis. It is ongoing work that never really stops."),
        ("Set points and sensors",
         "Each steady value has a set point, the level the body is aiming to keep it near. Sensors notice when a value moves away from that point. They send the information to control centres, mostly in the brain and in the endocrine glands."),
        ("Negative feedback",
         "Most control works by negative feedback. When a value rises, a response pushes it back down, and when it falls, a response pushes it back up. Sweating cools a body that has warmed up, and shivering warms one that has cooled. The response eases off once the value is back near the set point."),
        ("Positive feedback",
         "Positive feedback works the other way: a change triggers more of the same change. It is rare, and it suits short jobs that end on their own. Blood clotting is one example, because the clotting chain speeds itself up until a clot seals the damage."),
        ("Balance in the game",
         "In the game, three body bars, stamina, energy and mental focus, each run from 0 to 100. Below 50% a character's duties are impaired, and 65% is the lowest recommended level. Rest refills the bars, so keeping them in a healthy range is a small game version of the same idea."),
        ("Many controls at once",
         "No single control handles everything. Temperature, water, sugar and oxygen each have their own sensors and responses, and they affect one another. When one system is under strain, others must adjust, which is why illness often touches more than one part of the body."),
    ],
    "test": [
        ("What does homeostasis mean?",
         [("a", "A dramatic change in body temperature"), ("b", "Keeping key body values steady within a narrow range"), ("c", "The pause between two heartbeats"), ("d", "A type of white blood cell")], "b"),
        ("What is a set point?",
         [("a", "The highest speed the heart can beat"), ("b", "The number of bones in the arm"), ("c", "The level the body aims to keep a value near"), ("d", "A place where blood is stored")], "c"),
        ("Sweating to cool down is an example of which kind of control?",
         [("a", "Negative feedback"), ("b", "Positive feedback"), ("c", "Random action"), ("d", "No control at all")], "a"),
        ("Which best describes positive feedback?",
         [("a", "A change pushes the value back toward the set point"), ("b", "A change triggers more of the same change"), ("c", "The body ignores the change"), ("d", "The body stops all control")], "b"),
        ("In the game, what is the lowest recommended level for each body bar?",
         [("a", "20%"), ("b", "35%"), ("c", "65%"), ("d", "100%")], "c"),
    ],
}
