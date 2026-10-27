"""Query Optimisers: choosing a good plan before a query runs."""
CODE = "computing4_query_optimiser"
BOOK = {
    "title": "Query Optimisers",
    "subtitle": "Choosing a good plan before a query runs",
    "chapters": [
        ("Many possible plans", "A query can often be answered in many ways, such as scanning a table or using an index, and joining tables in different orders. The optimiser's job is to pick a plan that is cheap to run. The choice can change the time by a large factor."),
        ("Cardinality estimates", "To judge a plan, the optimiser estimates how many rows each step will produce. These estimates are called cardinalities. Good estimates lead to good plans, and poor ones lead to slow queries."),
        ("Cost models", "A cost model turns each plan into a number based on reads, memory and processing. The optimiser compares these numbers and picks the lowest. The model is an approximation, not a stopwatch."),
        ("Join order search", "With several tables, the number of possible join orders grows quickly. Optimisers search a limited set of orders, often using dynamic programming. They skip routes they expect to be costly."),
        ("Statistics refresh", "Optimisers rely on statistics about the data, such as value counts and ranges. These must be refreshed as the data changes. Stale statistics produce wrong estimates."),
        ("Why plans go wrong", "A plan can go wrong when estimates are far off, for example when values are linked in ways the statistics miss. A small change in the data can then cause a large slowdown. Checking the plan the database chose is a normal part of tuning."),
    ],
    "test": [
        ("What does a query optimiser choose?",
         [("a", "The colour of the result"), ("b", "The name of the user"), ("c", "The size of the monitor"), ("d", "A cheap plan for running the query")], "d"),
        ("What are cardinality estimates?",
         [("a", "Prices of goods"), ("b", "Guesses of how many rows each step produces"), ("c", "Lists of players"), ("d", "Sound levels")], "b"),
        ("What does a cost model produce?",
         [("a", "A picture of a plan"), ("b", "A new table"), ("c", "A number that compares plans"), ("d", "A password")], "c"),
        ("Why does join order search need limits?",
         [("a", "The number of join orders grows quickly"), ("b", "Joins cannot be done"), ("c", "Tables have no rows"), ("d", "Plans are always the same")], "a"),
        ("Why do stale statistics cause trouble?",
         [("a", "They make the disk spin"), ("b", "They give wrong estimates"), ("c", "They remove the indexes"), ("d", "They stop all queries")], "b"),
    ],
}
