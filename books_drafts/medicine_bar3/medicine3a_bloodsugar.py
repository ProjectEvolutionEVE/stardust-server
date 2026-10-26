"""Medicine, bar 3 (Senior Doctor), part A: Blood Sugar. How insulin, glucagon, the liver and stress hormones keep fuel steady."""
CODE = "medicine3a_bloodsugar"
BOOK = {
    "title": "Blood Sugar: A Balancing Act",
    "subtitle": "How hormones and the liver keep fuel levels steady between meals",
    "chapters": [
        ("Why blood sugar matters",
         "Glucose is a simple sugar and the main fuel for the brain and most body cells. The blood carries glucose from the gut and the liver to where it is used. Keeping its level in a healthy range is one of the body's most important balancing acts."),
        ("After a meal",
         "After food is digested, glucose enters the blood and its level rises. The pancreas releases insulin, a hormone that helps cells take glucose in and store the extra for later. The level then settles back toward its set point."),
        ("Between meals",
         "When no food has been eaten for a while, glucose levels begin to fall. The pancreas releases glucagon, which signals the liver to release its stored glucose. The liver acts as a store that keeps the supply steady between meals."),
        ("A pair of opposing hormones",
         "Insulin and glucagon work against each other, which is a clear example of negative feedback. One lowers the level when it is high, and the other raises it when it is low. Both are needed for a steady supply."),
        ("Stress and fuel",
         "Stress hormones such as adrenaline can release extra glucose quickly, so muscles have fuel for a sudden effort. This helps in a short emergency. Long periods of stress strain the same systems over time, which is why steady routines matter."),
        ("Steady fuel from food",
         "Foods that break down slowly, with fibre and protein, release glucose more gradually than a large amount of sugar eaten alone. This is general healthy eating, not a treatment. A health professional can advise anyone with a specific condition."),
    ],
    "test": [
        ("What is the main job of insulin?",
         [("a", "To make the body hot"), ("b", "To help cells take glucose in from the blood"), ("c", "To break down bones"), ("d", "To carry oxygen")], "b"),
        ("Which organ releases stored glucose between meals?",
         [("a", "The lungs"), ("b", "The skin"), ("c", "The liver"), ("d", "The heart")], "c"),
        ("How do insulin and glucagon work together?",
         [("a", "As positive feedback that never ends"), ("b", "As random action"), ("c", "As no control at all"), ("d", "As negative feedback that keeps the level near its set point")], "d"),
        ("Why can adrenaline help in a short emergency?",
         [("a", "It can release extra glucose quickly for a burst of effort"), ("b", "It stops glucose from being used"), ("c", "It turns off the heart"), ("d", "It fills the lungs with water")], "a"),
        ("Which kind of food gives glucose to the blood more gradually?",
         [("a", "Large amounts of sugar eaten alone"), ("b", "Food that contains fibre and protein"), ("c", "Plain water"), ("d", "Strong drinks")], "b"),
    ],
}
