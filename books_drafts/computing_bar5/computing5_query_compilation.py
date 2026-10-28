"""Query compilation: interpretation overhead, compiling plans, vectorised execution, just-in-time compilation and its costs."""
CODE = 'computing5_query_compilation'
BOOK = {
    "title": 'Query Compilation',
    "subtitle": 'Turning a query into machine code, and why that can make it much faster',
    "chapters": [
        ('The interpreter cost',
         'A query engine can walk through a plan one step at a time, asking each step to do its work for every row. Each step adds overhead, and for big tables that overhead adds up.'),
        ('Compiling the plan',
         "Query compilation turns the plan into a small program written for that exact query. The program runs directly on the processor, with no need to re-check the plan's details for each row."),
        ('Vectorised execution',
         'A related idea processes batches of values from a column at a time, which suits modern processors well. The work is done in tight loops that the processor handles efficiently.'),
        ('Just in time',
         'Some databases compile a query when it arrives, using a just-in-time compiler. PostgreSQL offers this for expensive queries, using the LLVM compiler toolkit.'),
        ('The cost of compiling',
         'Compiling takes time, so it helps most on long-running analytical queries. For a quick lookup, the compile time can cost more than it saves.'),
        ('Benchmarks and balance',
         'Published benchmarks often show large speedups on scans and totals, but results depend on the workload. Engineers measure before deciding that compilation is worth the added complexity.'),
    ],
    "test": [
        ('What is the main problem with a step-by-step interpreter?',
         [('a', 'It needs no memory'), ('b', 'It cannot read numbers'), ('c', 'Each step adds overhead for every row'), ('d', 'It only works offline')], 'c'),
        ('What does query compilation produce?',
         [('a', 'A picture of the table'), ('b', 'A new table'), ('c', 'A printed report'), ('d', 'A small program written for that exact query')], 'd'),
        ('What does vectorised execution work on?',
         [('a', 'Single values one at a time'), ('b', 'Batches of values from a column'), ('c', 'Pictures of data'), ('d', "Users' names only")], 'b'),
        ('Which situation suits compilation best?',
         [('a', 'A long analytical query over lots of rows'), ('b', 'A single quick lookup'), ('c', 'Typing a password'), ('d', 'Sending an email')], 'a'),
        ('What is a just-in-time compiler in a database?',
         [('a', 'A compiler that runs when the query arrives'), ('b', 'A tool that prints bills'), ('c', 'A way to store backups'), ('d', 'A type of index')], 'a'),
    ],
}
