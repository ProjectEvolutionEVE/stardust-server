"""Adaptive query processing: optimiser estimates, mid-query re-planning, feedback loops and plan stability."""
CODE = 'computing5_adaptive_query'
BOOK = {
    "title": 'Adaptive Query Processing',
    "subtitle": 'Plans that change while a query runs, when the first guesses turn out wrong',
    "chapters": [
        ('Guessing before running',
         'A query optimiser guesses how many rows each step will return, then picks a plan. Those guesses come from statistics, which can be out of date or miss patterns between columns.'),
        ('When the guess is wrong',
         'If a step returns far more or fewer rows than expected, the chosen plan may be slow. A join that suits a hundred rows can struggle with a million.'),
        ('Changing mid-query',
         'Adaptive query processing lets the engine notice this during the run. It can switch join methods or re-plan the rest of the query using the real row counts it has just seen.'),
        ('Feedback loops',
         'Some systems record the real results and use them next time. Over many runs, the estimates improve and fewer surprises occur.'),
        ('Robustness and stability',
         'Changing plans can make results less predictable, since the same query may take different routes on different days. Engineers weigh speed against stability.'),
        ('A worked idea',
         'Imagine a query that joins a customer table to orders. If the engine finds early that a filter matched far fewer customers than guessed, it can switch to a method suited to a small input. The answer stays the same, only the route changes.'),
    ],
    "test": [
        ('Where do the row estimates used by the optimiser come from?',
         [('a', "The user's mood"), ('b', 'Statistics about the data'), ('c', 'The weather'), ('d', 'A random number')], 'b'),
        ('What can go wrong when an estimate is far off?',
         [('a', 'The data is deleted'), ('b', 'The result becomes a picture'), ('c', 'The plan may be slow for the real data'), ('d', 'The table gains an extra column')], 'c'),
        ('What can adaptive processing change during a run?',
         [('a', 'The colour of the results'), ('b', 'The name of the database'), ('c', 'The date on the server'), ('d', 'The join method or the rest of the plan')], 'd'),
        ('What do feedback loops do?',
         [('a', 'Record real results so later estimates improve'), ('b', 'Delete old statistics'), ('c', 'Stop all queries'), ('d', 'Print the plan')], 'a'),
        ('What is the trade-off of changing plans?',
         [('a', 'Queries get longer text'), ('b', 'Speed may be weighed against predictability'), ('c', 'Storage becomes free'), ('d', 'Users must log out')], 'b'),
    ],
}
