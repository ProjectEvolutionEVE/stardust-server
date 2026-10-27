"""Relational Algebra: the mathematics behind database queries."""
CODE = "computing4_relational_algebra"
BOOK = {
    "title": "Relational Algebra",
    "subtitle": "The mathematics behind database queries",
    "chapters": [
        ("Selection, projection and join", "Selection keeps the rows that match a condition. Projection keeps only some of the columns. Join combines rows from two tables where their keys match. These three operations build most ordinary queries."),
        ("Set operations", "Union, intersection and difference treat tables as sets of rows. The tables must have the same shape for these to work. Union gathers rows from both, and difference removes the rows found in the other table."),
        ("Composing queries", "Operations can be nested, with the output of one feeding the next. A query becomes a tree of such steps. Writing it this way makes the order of work clear."),
        ("Equivalence rules", "Some rewrites give the same result, such as applying a selection before a join. These rules let an optimiser choose a cheaper plan. Equivalence is checked by reasoning about what each step means."),
        ("How SQL maps onto algebra", "A SELECT with WHERE, FROM and a join maps onto the matching operators. SQL adds extras, such as duplicate rows and nulls, that the pure algebra leaves out. Knowing the mapping helps you predict results."),
        ("Reasoning about correctness", "A query is correct when it returns exactly the rows its meaning requires. Writing the question in algebra makes it easier to check. Small algebraic steps can catch mistakes before they reach the data."),
    ],
    "test": [
        ("What does selection do?",
         [("a", "Keeps the rows that match a condition"), ("b", "Removes every column"), ("c", "Sorts the tables by colour"), ("d", "Copies the database to a phone")], "a"),
        ("What does projection keep?",
         [("a", "Only the first row"), ("b", "Nothing"), ("c", "Only some columns"), ("d", "Every table in the database")], "c"),
        ("What must two tables share for union to work?",
         [("a", "The same colour"), ("b", "The same owner"), ("c", "The same name for the game"), ("d", "The same shape")], "d"),
        ("Why is applying a selection before a join useful?",
         [("a", "It changes the answer"), ("b", "It gives the same answer and can be cheaper"), ("c", "It deletes the join"), ("d", "It stops the database")], "b"),
        ("What does SQL add beyond pure algebra?",
         [("a", "Extras such as duplicate rows and nulls"), ("b", "Nothing, ever"), ("c", "A paint tool"), ("d", "A map")], "a"),
    ],
}
