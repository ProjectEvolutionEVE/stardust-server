"""Mould Filling and Flow Simulation: predicting how melt fills a mould before any steel is cut."""
CODE = 'engineering4_mould_flow'
BOOK = {
    "title": "Mould Filling and Flow Simulation",
    "subtitle": "Predicting how melt fills a mould, before any steel is cut",
    "chapters": [
        ("How melt fills a mould",
         "Molten plastic flows through the cavity from the gate outward. The flow front moves faster in some places than in others. Understanding this pattern shows where the part will fill well and where it may not."),
        ("Weld lines",
         "When two flow fronts meet, they can form a weld line, a weak line that may show on the surface. Moving the gate can change where the flow fronts meet, and so where the weld line falls."),
        ("Air traps",
         "If air cannot escape as the melt fills the cavity, it can be trapped. Trapped air leaves burn marks or a short fill. Vents cut into the mould let the air out as the melt advances."),
        ("Warpage",
         "Uneven cooling makes a part bend or twist out of shape. Flow and cooling simulation helps show where warpage is likely, so the design can be changed before the mould is cut."),
        ("Simulation before steel",
         "Flow software predicts the fill, the pressure and the cooling on a computer. Finding a problem on screen costs far less than finding it in a cut mould. The simulation is checked against real trials."),
        ("The cost of mould changes",
         "Changing a mould after it has been cut can cost weeks of work and a great deal of money. Testing the design early keeps those changes rare. Early checks protect the schedule as well as the budget."),
    ],
    "test": [
        ("What is a weld line?",
         [("a", "A line of paint"), ("b", "A welded metal joint in the mould"), ("c", "A weak line where two flow fronts meet"), ("d", "A line printed on the part")], "c"),
        ("What can trap air in a mould?",
         [("a", "Melt that fills the cavity faster than air can escape"), ("b", "Cold water"), ("c", "A bright surface"), ("d", "Slow cooling")], "a"),
        ("What causes warpage?",
         [("a", "Very fast injection of the melt"), ("b", "Painting the part"), ("c", "Using a steel mould"), ("d", "Uneven cooling")], "d"),
        ("Why run flow simulation before cutting steel?",
         [("a", "To make the steel stronger"), ("b", "To find problems on a computer, which costs much less than changing a cut mould"), ("c", "To delete the design"), ("d", "To speed up the cutting")], "b"),
        ("What does a vent in a mould do?",
         [("a", "Lets trapped air escape"), ("b", "Heats the melt"), ("c", "Holds the part"), ("d", "Cools the steel")], "a"),
    ],
}
