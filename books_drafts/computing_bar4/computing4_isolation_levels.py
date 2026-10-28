"""Isolation Levels and Anomalies: how much one transaction may see of another."""
CODE = "computing4_isolation_levels"
BOOK = {
    "title": "Isolation Levels and Anomalies",
    "subtitle": "How much one transaction may see of another",
    "chapters": [
        ("Dirty reads", "A dirty read sees a change from a transaction that has not yet committed. If that transaction is rolled back, the reader saw data that never really existed. Many systems prevent this even at their lowest level."),
        ("Non-repeatable reads", "A non-repeatable read happens when reading the same row twice gives different values, because another transaction changed and committed it between the two reads. Stronger levels prevent this."),
        ("Phantoms", "A phantom appears when a query returns a different set of rows the second time, because another transaction added or removed rows that match its condition. It is a problem about sets of rows, not single rows."),
        ("Write skew", "Write skew happens when two transactions read overlapping data, each makes a decision, and each writes to different rows. Both decisions may be fine alone but break a rule together. Serializable isolation prevents it."),
        ("The standard levels", "The standard levels are read uncommitted, read committed, repeatable read and serializable. Each stronger level prevents more anomalies, usually at a cost in speed or waiting. The exact behaviour varies between database systems."),
        ("Choosing a level for a workload", "Pick the weakest level that still keeps your rules safe. Reports may accept some anomalies, while money transfers may need the strictest level. Measure the cost before settling on a level."),
    ],
    "test": [
        ("What is a dirty read?",
         [("a", "Reading a dusty screen"), ("b", "Reading a backup"), ("c", "Reading a change from a transaction not yet committed"), ("d", "Reading a file with spelling errors")], "c"),
        ("What is a non-repeatable read?",
         [("a", "Reading nothing at all"), ("b", "Reading a row that never changes"), ("c", "Reading from a printer"), ("d", "Reading the same row twice and getting different values")], "d"),
        ("What is a phantom?",
         [("a", "A ghost on the screen"), ("b", "A changed set of rows that match a query, between reads"), ("c", "A row that never existed"), ("d", "A broken disk")], "b"),
        ("What is write skew?",
         [("a", "A slanted table"), ("b", "A slow printer"), ("c", "Two transactions each decide from overlapping reads and break a rule together"), ("d", "A bad screen colour")], "c"),
        ("Which level prevents the most anomalies?",
         [("a", "Serializable"), ("b", "Read uncommitted"), ("c", "No level"), ("d", "The lowest level")], "a"),
    ],
}
