"""Thermal-vacuum Testing: copying the cold, the heat and the empty dark on the ground before a craft flies."""
CODE = "flight5_s_thermal_vac"
BOOK = {
    "title": "Thermal-vacuum Testing",
    "subtitle": "Testing a craft in the cold, the heat and the empty dark",
    "chapters": [
        ("Why test in a vacuum",
         "In space there is no air to carry heat away. A craft is very hot in sunlight and very cold in shadow. Thermal-vacuum chambers copy those conditions on the ground before launch."),
        ("The chamber",
         "The chamber is a large sealed room pumped down to a very low pressure. Its walls can be cooled or heated, so the test craft meets the temperatures it will meet in flight."),
        ("Cycling",
         "Engineers run the craft through hot and cold cycles several times. This finds weak parts, poor joints and parts that drift out of shape."),
        ("Bake-out",
         "Before the final test, a craft is often heated in vacuum to drive off gases trapped in its materials. This stops those gases from later clouding lenses or coating sensors."),
        ("Apollo and later craft",
         "Apollo spacecraft and later space telescopes passed through tests like these. The largest telescopes need their own very big chambers."),
        ("Lessons",
         "A fault found on the ground is far cheaper than one found in orbit. Careful records of each cycle help teams decide when a craft is ready to fly."),
    ],
    "test": [
        ("Why do craft in space face wide temperature swings?",
         [("a", "Space is full of air"), ("b", "They never receive sunlight"), ("c", "They spin too fast"), ("d", "Sunlit parts heat up and shaded parts cool down, with no air to share the heat")], "d"),
        ("What does a thermal-vacuum chamber do?",
         [("a", "Launches rockets"), ("b", "Makes rain"), ("c", "Copies low pressure and space temperatures on the ground"), ("d", "Melts steel")], "c"),
        ("What is the purpose of bake-out?",
         [("a", "To drive off trapped gases before flight"), ("b", "To paint the outside"), ("c", "To make the craft lighter"), ("d", "To test the radio")], "a"),
        ("What is cycling in these tests?",
         [("a", "Riding a bicycle inside"), ("b", "Repeated hot and cold runs"), ("c", "Spinning in a circle"), ("d", "Switching the radio on and off")], "b"),
        ("Why is a fault found on the ground so valuable?",
         [("a", "It is more fun to fix"), ("b", "It makes the launch heavier"), ("c", "The craft cannot be repaired later"), ("d", "It is far cheaper than finding it in orbit")], "d"),
    ],
}
