"""Belt and Chain Drives: belt tension, pulley sizing, chain wear, timing belts, drive efficiency and maintenance costs."""
CODE = "engineering4_belts_chains"
BOOK = {
    "title": "Belt and Chain Drives",
    "subtitle": "Tension, pulleys, chain wear and timing belts",
    "chapters": [
        ("Belt tension",
         "A belt must be tight enough to grip the pulleys, but not so tight that it overloads the bearings and shortens the belt's life. Engineers set the tension using the maker's guide and check it again after the first run."),
        ("Pulley sizing",
         "Pulley sizes set the speed ratio and how far the belt wraps around each pulley. Small pulleys bend the belt more, so it wears faster."),
        ("Chain wear",
         "Chains stretch as their pins and bushes wear. A worn chain rides up the teeth, which causes noise and early failure."),
        ("Timing belts",
         "Timing belts have teeth that mesh with the pulleys, so the timing stays exact with no slip. They suit engines and machines that need precise timing."),
        ("Drive efficiency",
         "Belt and chain drives are efficient, with losses from flexing and friction. Efficiency falls when belts are loose or misaligned."),
        ("Maintenance costs",
         "Regular checks of tension, alignment and wear keep costs low. Replacing a chain early costs far less than a failure in service."),
    ],
    "test": [
        ("What goes wrong if a belt is too tight?",
         [("a", "It overloads the bearings and shortens belt life"), ("b", "It becomes cheaper"), ("c", "It is painted"), ("d", "It becomes quiet")], "a"),
        ("What do pulley sizes set?",
         [("a", "Colour"), ("b", "Music"), ("c", "Weather"), ("d", "The speed ratio and how far the belt wraps")], "d"),
        ("What happens to a worn chain?",
         [("a", "It gets brighter"), ("b", "It rides up the teeth and causes noise"), ("c", "It stops all drive"), ("d", "It grows")], "b"),
        ("What lets a timing belt avoid slip?",
         [("a", "Paint"), ("b", "Wings"), ("c", "Sails"), ("d", "Teeth that mesh with the pulleys")], "d"),
        ("What are the main losses in belt and chain drives?",
         [("a", "Flexing and friction"), ("b", "Light and heat"), ("c", "Music only"), ("d", "Colour")], "a"),
    ],
}
