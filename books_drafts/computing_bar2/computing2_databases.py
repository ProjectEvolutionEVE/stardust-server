"""Databases and Tables: records kept in tables, keys that find them, links between tables, and transactions that keep changes together."""
CODE = "computing2_databases"
BOOK = {
    "title": "Databases and Tables",
    "subtitle": "Tables of records, keys that find them, links between them and transactions",
    "chapters": [
        ("A table is a grid",
         "A database keeps information in tables, which are like grids. Each row is one record, such as one player or one receipt, and each column is one kind of fact about it, such as a name or a date. Many tables together make up a database."),
        ("Keys",
         "Every row needs a key: a column whose value is unique to that row, so you can find exactly that record. Keys are often numbers that the database hands out automatically. Two people with the same name still get different keys."),
        ("Linking tables",
         "Tables link to each other through keys. A table of receipts can hold the key of the player it belongs to, rather than copying the player's details every time. The game's receipts table works this way, but the public receipt check never shows who owns a receipt."),
        ("Asking questions",
         "A query is a question put to a database, such as show me every receipt from this week. The database finds the rows that match and returns them. Good queries ask only for what is needed, so the answer comes back quickly."),
        ("All or nothing",
         "A transaction groups several changes so that they all happen, or none does. If a transfer of goods were recorded without its receipt, the two would no longer match. The game writes each transfer and its receipt together in one transaction, so both happen or neither does."),
        ("Indexes",
         "An index is an extra structure that lets the database find rows quickly, much like the index at the back of a book. It takes extra space and slows writes a little, so indexes go on the columns that are searched most."),
    ],
    "test": [
        ("In a database table, what does one row usually represent?",
         [("a", "One column"), ("b", "One kind of fact"), ("c", "One record, such as one player or one receipt"), ("d", "The whole database")], "c"),
        ("What is a key in a table?",
         [("a", "A value that is unique to each row, so the exact record can be found"), ("b", "A password for the database"), ("c", "A kind of column that is always empty"), ("d", "A copy of the whole table")], "a"),
        ("Why might one table hold the key of a record in another table, instead of copying its details?",
         [("a", "So the table prints faster"), ("b", "So each row is longer"), ("c", "So the database forgets the details"), ("d", "So a change to the details is made in one place, and the link still works")], "d"),
        ("What is a query?",
         [("a", "A power cable"), ("b", "A question put to a database that returns the matching rows"), ("c", "A kind of key"), ("d", "A copy of a backup")], "b"),
        ("What is a transaction?",
         [("a", "A payment made in coins"), ("b", "A list of prices"), ("c", "A group of changes that all happen, or none does"), ("d", "A type of network packet")], "c"),
    ],
}
