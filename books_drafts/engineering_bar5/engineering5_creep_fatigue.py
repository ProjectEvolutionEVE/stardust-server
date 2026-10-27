"""Creep-Fatigue Interaction: how slow creep and repeated cycling combine to damage hot components, and how designers allow for both."""
CODE = "engineering5_creep_fatigue"
BOOK = {
    "title": "Creep-Fatigue Interaction",
    "subtitle": "Hold times, damage summation and designing hot parts",
    "chapters": [
        ("Two kinds of damage", "Creep is slow deformation under a steady load at high temperature. Fatigue is damage that builds from repeated load cycles. Hot parts can suffer both at once."),
        ("Hold times", "When a cycle holds the load for a long time at high temperature, creep adds to the fatigue damage. Long hold times can shorten life much more than fast cycling does."),
        ("Damage summation", "Engineers add up the damage from each mechanism, often with a simple linear rule, to estimate the life of a part. The sum must stay below a safe limit."),
        ("Cyclic creep", "Repeated loading can make creep strain build up cycle after cycle. The part can change shape slowly even when no single cycle seems large."),
        ("Life models", "Life models predict how many cycles a part can take at a given temperature and stress. They are fitted to test data and must be used within their range."),
        ("Designing hot parts", "Designers choose materials and limits so that both mechanisms stay within safe limits over the whole design life. Testing confirms the choice."),
    ],
    "test": [
        ("What is creep?", [("a", "Fast cutting of metal"), ("b", "A type of paint"), ("c", "A kind of sound"), ("d", "Slow deformation under steady load at high temperature")], "d"),
        ("What adds to fatigue damage when hold times are long?", [("a", "The colour of the material"), ("b", "The coolant used"), ("c", "Creep"), ("d", "Gravity alone")], "c"),
        ("What does damage summation do?", [("a", "Adds the damage from each mechanism to estimate life"), ("b", "Paints the part to protect it"), ("c", "Removes the load from the part"), ("d", "Makes the part heavier")], "a"),
        ("What is cyclic creep?", [("a", "A kind of bicycle used in test rigs"), ("b", "Creep strain that builds up cycle by cycle under repeated loads"), ("c", "A steel alloy with high carbon"), ("d", "A test lamp for furnaces")], "b"),
        ("What do life models predict?", [("a", "The number of cycles a part can take at a given temperature and stress"), ("b", "The colour of the metal"), ("c", "The weight of the box"), ("d", "The name of the operator")], "a"),
    ],
}
