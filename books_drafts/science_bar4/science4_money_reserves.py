"""Contingency Funds and Risk Reserves: risk registers, contingency sizing, expected loss and reserve rules."""
CODE = "science4_money_reserves"
BOOK = {
    "title": "Contingency Funds and Risk Reserves",
    "subtitle": "Keeping money aside for the things that go wrong",
    "chapters": [
        ("Risk registers", "A risk register lists what could go wrong, how likely it is and what it would cost. Writing risks down makes them easier to plan for. The register should be reviewed as the project moves on."),
        ("Contingency sizing", "A contingency is money set aside for risks that are likely but not certain. Its size depends on the risks listed and their possible cost. A contingency that is too small leaves a project exposed."),
        ("Expected loss", "Expected loss is the chance of a problem multiplied by its cost. A one in ten chance of a 5,000 unit loss gives an expected loss of 500 units. Expected loss helps decide how large a reserve should be."),
        ("Reserve rules", "A reserve rule is a clear policy on how much to keep and when to use it. For example, a group may keep a fixed share of its annual budget. Written rules stop reserves being spent on routine costs."),
        ("Using reserves", "Reserves should be used only for the risks they were set aside for. Each use should be approved and recorded. Recording use shows whether the reserve is the right size."),
        ("Reporting reserves", "Reports should show how much reserve is held, what it is for and how much has been used. Funders and leaders need this to judge the health of a project. Open reporting builds trust."),
    ],
    "test": [
        ("What does a risk register list?",
         [("a", "Lunch menus"), ("b", "Lab colours"), ("c", "Journal names only"), ("d", "What could go wrong, how likely it is and what it would cost")], "d"),
        ("What is a contingency?",
         [("a", "Money set aside for likely but uncertain risks"), ("b", "A fee for a conference"), ("c", "The weight of a sample"), ("d", "A type of microscope")], "a"),
        ("What is expected loss?",
         [("a", "The total budget"), ("b", "The price of a new lab"), ("c", "The chance of a problem multiplied by its cost"), ("d", "The number of staff leaving")], "c"),
        ("What is a reserve rule?",
         [("a", "A rule about lab noise"), ("b", "A clear policy on how much to keep and when to use it"), ("c", "A rule about paper size"), ("d", "A fee for parking")], "b"),
        ("Why should each use of a reserve be recorded?",
         [("a", "To hide the spending"), ("b", "To make the reserve bigger"), ("c", "To stop all research"), ("d", "To show whether the reserve is the right size and used for its purpose")], "d"),
    ],
}
