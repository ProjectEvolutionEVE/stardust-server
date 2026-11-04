"""Mineral Stability and Phase Diagrams: how minerals settle into stable groups as pressure and temperature change."""
CODE = "science4_geo_phase_rules"
BOOK = {
    "title": "Mineral Stability and Phase Diagrams",
    "subtitle": "Pressure, temperature and the minerals that rocks settle into",
    "chapters": [
        ("Why minerals change",
         "A mineral is stable only under certain conditions. When pressure or temperature changes, a rock may rearrange its minerals into new ones. Geologists use phase diagrams to show which minerals are stable at which conditions."),
        ("The Gibbs phase rule",
         "The Gibbs phase rule links the number of components, the number of phases and the degrees of freedom: F = C minus P plus 2. Here C is the number of components, P the number of phases, and F the number of conditions you may change freely. The rule tells you how much a system can vary before a phase must appear or disappear."),
        ("Pressure temperature diagrams",
         "A pressure temperature diagram plots the conditions under which different mineral groups are stable. Lines on the diagram are reaction boundaries, where two sets of minerals can exist side by side. Crossing a boundary means the rock is likely to change its minerals."),
        ("Metamorphic facies",
         "A metamorphic facies is a group of rocks formed under similar pressure and temperature. Each facies is marked by a characteristic set of minerals. Geologists read a facies from the minerals in a rock, then estimate the conditions it saw."),
        ("Reading an equilibrium diagram",
         "To read a diagram, find the point that matches the rock you are studying. Then look at which minerals are stable there and which boundaries lie nearby. A rock that shows a mineral set outside its expected field tells you the rock has not fully reached equilibrium."),
        ("Where the simple model fails",
         "Phase diagrams assume the rock has had time to reach equilibrium, and that the chemistry is simple. Real rocks often hold on to older minerals because reactions are slow, and they may contain fluids that change the picture. Good geologists use phase diagrams as a guide, then check them against the rock they see."),
    ],
    "test": [
        ("In the Gibbs phase rule, F = C minus P plus 2, what does P stand for?",
         [("a", "The pressure only"), ("b", "The number of phases present"), ("c", "The number of minerals in a rock"), ("d", "The freedom of temperature")], "b"),
        ("What does a reaction boundary on a pressure temperature diagram show?",
         [("a", "The speed at which a rock cools"), ("b", "Where two sets of minerals can exist side by side"), ("c", "The colour of the minerals"), ("d", "The depth of the ocean floor")], "b"),
        ("What is a metamorphic facies?",
         [("a", "A type of volcano"), ("b", "The shape of a fold in a rock"), ("c", "A group of rocks formed under similar pressure and temperature"), ("d", "A kind of fossil")], "c"),
        ("A system has one component and two phases. What is F?",
         [("a", "0"), ("b", "2"), ("c", "3"), ("d", "1")], "d"),
        ("Where does the simple equilibrium model of minerals most often fail?",
         [("a", "When the rock is heated"), ("b", "When water is present"), ("c", "When reactions are too slow for a rock to reach equilibrium"), ("d", "It never fails")], "c"),
    ],
}
