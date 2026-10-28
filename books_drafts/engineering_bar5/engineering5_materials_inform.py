"""Materials Informatics and Data Practice: property databases, data quality, machine learning on alloy data, uncertainty and sharing test results."""
CODE = "engineering5_materials_inform"
BOOK = {
    "title": "Materials Informatics and Data Practice",
    "subtitle": "Making good decisions from good data about materials",
    "chapters": [
        ("Data as a material",
         "Materials informatics treats past test results as a valuable resource. A property database holds the strength, the stiffness and the other numbers for each alloy and process. Good decisions start from good records."),
        ("Good data and bad data",
         "Data is only useful if it is right. Engineers check where each number came from, how it was measured, and whether the test followed a known standard. A number with no source is a guess, however neat it looks."),
        ("Learning from alloy data",
         "Machine learning finds patterns in many records at once. It can suggest which composition or heat treatment might give the strength a team needs. A model learns from its data, so it can only be as good as the records behind it."),
        ("Uncertainty in the numbers",
         "Every test has scatter. A careful team reports a range or a spread, not a single number. A model that ignores uncertainty can be confidently wrong, which is costly in a real part."),
        ("Checking the model",
         "A model must be tested on data it has not seen. Engineers keep some results back for that check. If the model fails on new results, it has learned the old records too closely."),
        ("Sharing test results",
         "Sharing results across a company, and with partners, saves repeated tests. Records must be clear about units, conditions and sample history, so that the next user can trust them. Shared data is worth most when it is kept in an orderly form."),
    ],
    "test": [
        ("What is a property database used for?",
         [("a", "To store office music"), ("b", "To hold the measured properties of materials and processes"), ("c", "To cut metal"), ("d", "To paint parts")], "b"),
        ("Why does an engineer check where a number came from?",
         [("a", "Because all numbers are the same"), ("b", "Because numbers change colour"), ("c", "Because a number with no source is only a guess"), ("d", "Because sources are always free")], "c"),
        ("What limits how good a machine learning model can be?",
         [("a", "The colour of the screen"), ("b", "The number of coffee breaks"), ("c", "The length of the name"), ("d", "The quality of the records it learns from")], "d"),
        ("Why should a team report a range rather than a single test number?",
         [("a", "Because every test has scatter"), ("b", "Because ranges are shorter"), ("c", "Because a single number is always wrong"), ("d", "Because ranges are cheaper to print")], "a"),
        ("Why keep some results back when checking a model?",
         [("a", "To give the results away"), ("b", "To test the model on data it has not seen"), ("c", "To lower the test cost to zero"), ("d", "To hide the units")], "b"),
    ],
}
