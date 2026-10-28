"""Normal Forms and Their Trade-offs: designing tables that stay consistent."""
CODE = "computing4_normal_forms"
BOOK = {
    "title": "Normal Forms and Their Trade-offs",
    "subtitle": "Designing tables that stay consistent",
    "chapters": [
        ("Functional dependencies", "A functional dependency says that one set of columns decides another. For example, a product code decides its name and price. Finding these dependencies is the first step in good table design."),
        ("First to third normal forms", "First normal form asks each cell to hold one value. Second and third normal forms remove columns that depend only on part of a key, or on another non-key column. Each step cuts repetition further."),
        ("Anomalies that normalisation removes", "Anomalies are problems when inserting, updating or deleting data. If a product's price is stored in many rows, one update may miss some of them. Normalising stores each fact once, so the update is safe."),
        ("Denormalising for speed", "Sometimes a team copies data on purpose to avoid expensive joins. This is denormalising. It speeds up reads, but the copies must then be kept in step."),
        ("Keeping data consistent", "When data is copied, the application or database must update every copy together. Constraints and transactions help. Without them, the copies drift apart."),
        ("Choosing a design", "Normalised designs suit systems where correctness matters most. Denormalised designs suit heavy reading where speed matters more. Many systems use both: normalised for the source, and copies for reports."),
    ],
    "test": [
        ("What does a functional dependency say?",
         [("a", "Two tables must never meet"), ("b", "One set of columns decides another"), ("c", "Every column is a key"), ("d", "Rows have no order")], "b"),
        ("What is first normal form about?",
         [("a", "Every table has a picture"), ("b", "No columns are allowed"), ("c", "Each cell holds one value"), ("d", "Tables must be sorted by colour")], "c"),
        ("What is an anomaly in a table?",
         [("a", "A problem when inserting, updating or deleting data"), ("b", "A normal row"), ("c", "A very fast query"), ("d", "A paper report")], "a"),
        ("What is denormalising?",
         [("a", "Deleting all keys"), ("b", "Removing the database"), ("c", "Making every cell empty"), ("d", "Copying data on purpose to speed up reads")], "d"),
        ("Why must copies be kept in step?",
         [("a", "So they can be printed"), ("b", "Otherwise they drift apart and give conflicting answers"), ("c", "So the screen is brighter"), ("d", "They are never needed")], "b"),
    ],
}
