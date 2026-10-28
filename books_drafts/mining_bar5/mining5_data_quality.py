"""Data Quality in Exploration Databases: how errors creep into drill and survey records, and the checks that keep them trustworthy."""
CODE = "mining5_data_quality"
BOOK = {
    "title": "Data Quality in Exploration Databases",
    "subtitle": "Keeping drill and survey records trustworthy",
    "chapters": [
        ("Errors", "Errors creep into exploration data in many ways, from mistyped numbers to wrong units. A small error in a single hole can mislead a whole model. Good teams look for errors actively."),
        ("Coordinate systems", "Coordinates must be in a known system, such as a standard latitude and longitude or a local grid. Mixing systems can move a hole by hundreds of metres. Every record should state its system clearly."),
        ("Duplicate records", "The same drill hole can be entered twice under slightly different names. Duplicates make a deposit look bigger or change its averages. Regular checks find and remove them."),
        ("Validation rules", "Validation rules are automatic checks, such as a depth that cannot be negative or a grade within a sensible range. They catch many mistakes at the point of entry. Rules should be written down and reviewed."),
        ("Audit trails", "An audit trail records who changed a value, when and why. It makes errors traceable and keeps the database honest. Audit trails are a key part of trust."),
        ("Trust in data", "Trust in data comes from consistent checks, clear records and honest reporting of uncertainty. Decisions worth millions depend on it. A team that protects its data protects its investment."),
    ],
    "test": [
        ("Why must coordinate systems be stated clearly?",
         [("a", "They change the colour of the map"), ("b", "Mixing systems can move a hole by hundreds of metres"), ("c", "They make the data louder"), ("d", "They are never needed")], "b"),
        ("What is a validation rule?",
         [("a", "An automatic check, such as a depth that cannot be negative"), ("b", "A law about buying gold"), ("c", "A type of paint"), ("d", "A song for workers")], "a"),
        ("What problem do duplicate records cause?",
         [("a", "They make the moon brighter"), ("b", "They make rain fall"), ("c", "They have no effect"), ("d", "They can make a deposit look bigger or change its averages")], "d"),
        ("What does an audit trail record?",
         [("a", "The weather each day"), ("b", "The number of cups of tea"), ("c", "Who changed a value, when and why"), ("d", "The colour of the screen")], "c"),
        ("What builds trust in exploration data?",
         [("a", "Hiding all errors"), ("b", "Consistent checks, clear records and honest reporting of uncertainty"), ("c", "Guessing every number"), ("d", "Never writing anything down")], "b"),
    ],
}
