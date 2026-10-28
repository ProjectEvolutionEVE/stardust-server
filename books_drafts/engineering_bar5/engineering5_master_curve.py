"""Master Curves and Time-Temperature Shift: the WLF equation, shift factors, creep master curves, lifetime prediction for plastics and test planning."""
CODE = "engineering5_master_curve"
BOOK = {
    "title": "Master Curves and Time-Temperature Shift",
    "subtitle": "Predicting how a plastic behaves over years from short tests",
    "chapters": [
        ("Waiting for years",
         "A plastic under a steady load can creep slowly for years. Nobody can wait that long for a test result. Master curves let engineers predict long-term behaviour from short tests run at higher and lower temperatures."),
        ("The shift idea",
         "For many polymers, raising the temperature has the same effect as waiting longer. Test results taken at different temperatures can be slid along the time axis and joined into one smooth curve. That combined curve is the master curve."),
        ("Shift factors",
         "The amount each curve is slid is called the shift factor. It is found by matching the curves, and it depends on temperature. Good shift factors make the master curve trustworthy."),
        ("The WLF equation",
         "The Williams-Landel-Ferry, or WLF, equation describes how the shift factor changes with temperature near the glass transition. It is used for many amorphous polymers. It does not fit every material, so it must be checked."),
        ("Lifetime prediction",
         "Once the master curve is built, the engineer reads off the behaviour at a time far longer than the test. This gives an estimate of how much a plastic part will creep over its life. The estimate is only as good as the test range behind it."),
        ("Planning the tests",
         "Good planning picks a temperature range that covers the service conditions and overlaps well between curves. A short extra test can save a long, costly one later. Engineers always check the prediction against a real part where they can."),
    ],
    "test": [
        ("Why are master curves used for plastics?",
         [("a", "To predict long-term behaviour from shorter tests"), ("b", "To change the colour of a plastic"), ("c", "To make a plastic melt"), ("d", "To count the molecules by hand")], "a"),
        ("What does a shift factor give?",
         [("a", "The weight of the part"), ("b", "The amount to slide each test curve along the time axis"), ("c", "The number of colours available"), ("d", "The cost of a shipment")], "b"),
        ("What does the WLF equation describe?",
         [("a", "How fast a car drives"), ("b", "How metal is welded"), ("c", "How the shift factor changes with temperature near the glass transition"), ("d", "How many workers are needed")], "c"),
        ("Why must the WLF equation be checked before use?",
         [("a", "It is only written in a foreign language"), ("b", "It works only for metals"), ("c", "It has no numbers in it"), ("d", "It does not fit every material")], "d"),
        ("What makes a master curve trustworthy?",
         [("a", "Good shift factors and tests that overlap well"), ("b", "A single very short test"), ("c", "A very bright colour"), ("d", "A low price for the test")], "a"),
    ],
}
