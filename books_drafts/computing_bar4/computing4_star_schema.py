"""Star Schemas and Data Warehouses: organising data for reports."""
CODE = "computing4_star_schema"
BOOK = {
    "title": "Star Schemas and Data Warehouses",
    "subtitle": "Organising data for reports",
    "chapters": [
        ("Fact and dimension tables", "A star schema has a central fact table of measurable events, such as sales, with one row per event. Around it sit dimension tables that describe the who, what, where and when, such as customer or date. Each fact row points to its dimensions."),
        ("Grain", "The grain is what one fact row represents, such as one sale line on one day. Choosing the grain first keeps the design clear. Mixing grains in one table causes double counting."),
        ("Slowly changing dimensions", "A customer may move house or change a name. Slowly changing dimensions decide whether to overwrite the old value, keep history in new rows, or keep the old value in a separate column. Each choice answers a different reporting question."),
        ("Conformed dimensions", "A conformed dimension, such as one shared date table, is used by several fact tables. Shared dimensions let reports from different areas be compared fairly. They are a key part of building a warehouse in stages."),
        ("Building a warehouse", "Data is extracted from source systems, cleaned and loaded into the star schema. The load runs on a schedule, often nightly. Clear definitions of each measure help everyone agree on the numbers."),
        ("Reporting trade-offs", "Star schemas make reports simple and fast to write, at the cost of some repeated data. Normalised designs avoid repetition but need more joins. Many warehouses use star schemas because reports matter more than storage."),
    ],
    "test": [
        ("What does a fact table hold?",
         [("a", "Measurable events, one row per event"), ("b", "Only customer names"), ("c", "Pictures of the store"), ("d", "The weather for the year")], "a"),
        ("What is the grain of a fact table?",
         [("a", "The weight of the table"), ("b", "The colour of the labels"), ("c", "What one row represents"), ("d", "The number of tables in the database")], "c"),
        ("What do slowly changing dimensions decide?",
         [("a", "How bright the screen is"), ("b", "How to keep history when a description changes"), ("c", "When to switch off the server"), ("d", "Who wins a game")], "b"),
        ("What is a conformed dimension?",
         [("a", "A dimension with no rows"), ("b", "A paper form"), ("c", "A broken table"), ("d", "A shared dimension used by several fact tables")], "d"),
        ("What is the trade-off of a star schema?",
         [("a", "Simple, fast reports at the cost of some repeated data"), ("b", "No data can be stored"), ("c", "Reports are impossible"), ("d", "It needs no loading at all")], "a"),
    ],
}
