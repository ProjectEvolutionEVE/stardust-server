"""Hydrogen embrittlement: how hydrogen enters steel, high-strength bolt failures, baking and coatings, and testing for it."""
CODE = "engineering4_hydrogen_embrittle"
BOOK = {
    "title": "Hydrogen Embrittlement",
    "subtitle": "How hydrogen enters steel and how to prevent it",
    "chapters": [
        ("Hydrogen in steel",
         "Hydrogen can enter steel during pickling, plating or welding, and from damp service. Once inside, it can make the steel brittle. The effect is worst in high-strength steels."),
        ("High-strength bolt failures",
         "High-strength bolts can fail suddenly under load, sometimes long after they were fitted. Hydrogen picked up in plating is a common cause. A bolt can break with little warning and little plastic bending."),
        ("Baking to remove hydrogen",
         "Baking is heating plated parts to drive hydrogen out of the steel. It is usually done soon after plating and must be done at a set temperature for a set time. Skipping the bake leaves hydrogen trapped in the part."),
        ("Coatings and protection",
         "Coatings can keep hydrogen out or limit how much enters. The choice of coating and the plating process both matter. Protection works best when the whole process is controlled from start to finish."),
        ("Testing for hydrogen",
         "Engineers test for hydrogen sensitivity with tests that load notched samples in a damp or charged condition. Other tests measure the hydrogen content of the steel. These tests show whether the process gives a safe result."),
        ("Designing against the risk",
         "Designers choose a steel that is less sensitive to hydrogen when the part is high-strength. They also control the process so that hydrogen is not introduced. The aim is a part that is safe through its whole life."),
    ],
    "test": [
        ("Where can hydrogen enter steel?", [("a", "From bright sunshine"), ("b", "During pickling, plating or welding, and from damp service"), ("c", "From the paint colour"), ("d", "From the wind")], "b"),
        ("Why are high-strength bolts at risk?", [("a", "They are always painted"), ("b", "They are too light"), ("c", "They can fail suddenly from trapped hydrogen, sometimes after a long time"), ("d", "They never carry load")], "c"),
        ("What is baking in this context?", [("a", "Drying paint in the sun"), ("b", "Cooking food in a kiln"), ("c", "Heating plated parts to drive hydrogen out of the steel"), ("d", "Freezing the steel")], "c"),
        ("What does a coating do for hydrogen risk?", [("a", "Keeps hydrogen out or limits how much enters"), ("b", "Adds hydrogen to the steel"), ("c", "Has no effect"), ("d", "Melts the steel")], "a"),
        ("Why does a sudden failure matter in a high-strength bolt?", [("a", "It cannot happen"), ("b", "It always bends first, so no warning is needed"), ("c", "It is only a cosmetic problem"), ("d", "It can break with little warning and little plastic bending")], "d"),
    ],
}
