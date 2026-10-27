"""High-Entropy Alloys: alloys with several main elements, and why mixing them can make them stable."""
CODE = "engineering5_high_entropy"
BOOK = {
    "title": "High-Entropy Alloys",
    "subtitle": "Alloys with several main elements, and why mixing them can make them stable",
    "chapters": [
        ("Several main elements",
         "High-entropy alloys mix five or more elements in roughly equal amounts. Traditional alloys have one main element with small additions of others."),
        ("Configurational entropy",
         "Mixing many elements at random raises the configurational entropy, which favours a simple solid solution. This is a central idea in their design."),
        ("Phase stability",
         "High entropy can stabilise a single solid solution at high temperature, although other phases may form at low temperature. Stability depends on the whole chemistry."),
        ("Property trade-offs",
         "Adding elements can raise strength but reduce ductility, or improve high-temperature behaviour while adding weight. Design means balancing these."),
        ("Alloy design rules",
         "Rules use measures such as mixing enthalpy, the atomic size difference and the valence electron count to predict the phase. They are guides, not guarantees."),
        ("Testing the prediction",
         "Each candidate must be made and tested, because the rules miss some phases. Real results decide the design."),
    ],
    "test": [
        ("How many main elements are in a classic high-entropy alloy?",
         [("a", "One"), ("b", "Two only"), ("c", "Five or more in roughly equal amounts"), ("d", "None")], "c"),
        ("What does configurational entropy favour?",
         [("a", "A simple solid solution"), ("b", "A paint film"), ("c", "A crack"), ("d", "A price")], "a"),
        ("What is a property trade-off?",
         [("a", "Gaining one property while losing another"), ("b", "A colour"), ("c", "A date"), ("d", "A price")], "a"),
        ("What do alloy design rules use?",
         [("a", "Colour"), ("b", "Mixing enthalpy, atomic size difference and valence electron count"), ("c", "Price"), ("d", "Music")], "b"),
        ("What must each candidate alloy be?",
         [("a", "Ignored"), ("b", "Judged by its colour"), ("c", "Sold"), ("d", "Made and tested, because rules miss some phases")], "d"),
    ],
}
