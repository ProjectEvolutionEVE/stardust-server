"""Indexes in Depth: how a database finds a row among millions, how a composite, partial or unique index helps, and what each index costs."""
CODE = "computing3b_indexes"
BOOK = {
    "title": "Indexes in Depth",
    "subtitle": "How a database finds one row among millions, and what each index costs",
    "chapters": [
        ("Searching without an index",
         "Without an index, a database may check every row to find the ones you want. That is called a full scan. It is fine for a small table, but it grows slower and slower as the table grows."),
        ("The sorted shortcut",
         "An index keeps a sorted copy of one or more columns, arranged in a tree called a B-tree. Each step down the tree cuts the search down a great deal, so even a very large table needs only a few steps to reach the right row."),
        ("Several columns in order",
         "A composite index covers several columns in a fixed order, such as item, then side, then price. It helps questions that match the first columns in that order. It cannot help much with a question that asks only for a later column."),
        ("Partial and unique indexes",
         "An index can cover only some rows, such as the open orders, which keeps it small and quick. A unique index also acts as a rule: the database refuses a second row with the same value. The game uses one of these to make sure each player has only one active ship."),
        ("Every index has a cost",
         "Each insert, update and delete must also update every index on that table. So indexes make reading faster and writing slower, and they take up disk space. Add an index for a question you ask often, not for every column."),
        ("Read the plan",
         "Most databases can show a query plan, which says whether the database will use an index or scan the whole table. When a query is slow, read the plan first, and then decide which index, if any, would help."),
    ],
    "test": [
        ("What is a full scan?",
         [("a", "A check of every row to find the matching ones"), ("b", "A backup of the whole database"), ("c", "A password check"), ("d", "A copy of the index")], "a"),
        ("What shape do many database indexes take?",
         [("a", "A circle"), ("b", "A list of colours"), ("c", "A ring of routers"), ("d", "A B-tree, a sorted tree of steps")], "d"),
        ("What does a composite index on item, then side, then price help with most?",
         [("a", "Printing receipts"), ("b", "Questions that match its first columns, in that order"), ("c", "Questions that only ask for the price"), ("d", "Encrypting the table")], "b"),
        ("What does a unique index do beyond speeding up searches?",
         [("a", "It deletes duplicate rows"), ("b", "It encrypts the column"), ("c", "It prints the table"), ("d", "It refuses a second row with the same value")], "d"),
        ("Why is an index not free?",
         [("a", "It costs the player credits to read"), ("b", "It has to be printed"), ("c", "It can only be used once"), ("d", "It must be updated on every insert, update and delete, and it takes up space")], "d"),
    ],
}
