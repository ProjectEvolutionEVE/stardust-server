"""Directional Solidification and Single-Crystal Growth: gradient control, grain selection, withdrawal rates and turbine blade casting."""
CODE = "engineering5_directional"
BOOK = {
    "title": "Directional Solidification and Single-Crystal Growth",
    "subtitle": "Growing a metal part so it freezes in one direction",
    "chapters": [
        ("Freezing in one direction",
         "In directional solidification, the mould is slowly drawn through a temperature gradient so the metal freezes from one end to the other. Grains grow in a single direction, which makes the casting stronger where it is loaded."),
        ("Gradient control",
         "The gradient is the difference in temperature from the hot end to the cold end. A steep, steady gradient keeps the freezing front smooth. The gradient is controlled by the furnace and the pull rate."),
        ("Grain selection",
         "In a single-crystal casting, a selector at the start lets only one grain grow across the part. Other grains are blocked out. The result is one crystal over the whole casting, with no grain boundaries to weaken it."),
        ("Withdrawal rates",
         "The withdrawal rate is how fast the mould is pulled out of the hot zone. Too fast and the front becomes unstable; too slow and the grain structure coarsens. The rate is picked for each alloy and each part."),
        ("Turbine blades",
         "Turbine blades in jet engines are a main use of this process. They run very hot and under heavy load, and grain boundaries are the first place they fail. Removing those boundaries gives the blade its high-temperature strength."),
        ("The cost of a single crystal",
         "The process is slow and the furnaces are costly, so the parts cost much more than ordinary castings. The price is worth paying where failure is not an option. Yield is also watched closely, because scrapped blades waste a great deal of effort."),
    ],
    "test": [
        ("What happens in directional solidification?",
         [("a", "The metal freezes from one end to the other in a single direction"), ("b", "The metal is spun in a circle"), ("c", "The metal is painted in layers"), ("d", "The metal is cooled in ice")], "a"),
        ("What does the gradient control?",
         [("a", "The colour of the mould"), ("b", "The freezing front stays smooth as the metal solidifies"), ("c", "The number of bolts"), ("d", "The length of the shift")], "b"),
        ("What does a grain selector do in a single-crystal casting?",
         [("a", "It paints the grains red"), ("b", "It cuts the part in two"), ("c", "It lets only one grain grow across the part"), ("d", "It melts the grains away")], "c"),
        ("What happens if the withdrawal rate is too fast?",
         [("a", "The part gets heavier"), ("b", "The part turns to glass"), ("c", "Nothing at all"), ("d", "The freezing front becomes unstable")], "d"),
        ("Why are turbine blades cast this way?",
         [("a", "Removing grain boundaries gives high-temperature strength"), ("b", "The blades must be transparent"), ("c", "The blades must float"), ("d", "The blades must be made from paper")], "a"),
    ],
}
