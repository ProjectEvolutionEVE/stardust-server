"""Column Stores for Analytics: storing columns together for fast scans."""
CODE = "computing4_columnar"
BOOK = {
    "title": "Column Stores for Analytics",
    "subtitle": "Storing columns together for fast scans",
    "chapters": [
        ("Storing columns together", "A column store keeps each column's values together in one place, instead of storing each row whole. A query that needs three columns reads only those three. This suits questions that look across many rows but only a few columns."),
        ("Column compression", "Values in one column are often similar, so they compress well. Repeated values can be stored once, and sorted numbers can be stored as small differences. Less data means less reading from disk."),
        ("Vectorised scans", "The engine processes batches of column values together, rather than one row at a time. This makes better use of the processor's cache and its instructions. Scans of large tables become much faster."),
        ("Late materialisation", "The engine delays building full rows until it must. It filters on one column first, and fetches the other columns only for the matching positions. This saves work when the filters are selective."),
        ("Read-mostly workloads", "Column stores favour reads and bulk loads over many small updates. Changing one row may touch many column files. Systems often add a small write buffer and merge it in later."),
        ("Loading data", "Data is loaded in large batches, which are sorted and compressed as they arrive. Loading is planned, not done one record at a time. Good loading keeps queries fast and storage small."),
    ],
    "test": [
        ("What does a column store keep together?",
         [("a", "Each column's values"), ("b", "Each user's photo"), ("c", "The screen layout"), ("d", "The sound files")], "a"),
        ("Why do column values compress well?",
         [("a", "Columns hold no data"), ("b", "Compression is forbidden"), ("c", "Values in one column are often similar"), ("d", "They are all words")], "c"),
        ("What is a vectorised scan?",
         [("a", "Drawing vectors on screen"), ("b", "Processing batches of column values together"), ("c", "Scanning one row at a time"), ("d", "Deleting all columns")], "b"),
        ("What does late materialisation delay?",
         [("a", "Loading the screen"), ("b", "Saving the game"), ("c", "Choosing a ship"), ("d", "Building full rows until they are needed")], "d"),
        ("What workload do column stores favour?",
         [("a", "Read-mostly analysis and bulk loads"), ("b", "Many tiny updates every second"), ("c", "No reads at all"), ("d", "Printing paper reports")], "a"),
    ],
}
