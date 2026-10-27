"""Abstract Interpretation: checking what a program can do by running it on simplified summaries."""
CODE = 'computing5_abstract_interpretation'
BOOK = {
    "title": 'Abstract Interpretation',
    "subtitle": 'Checking what a program can do by running it on simplified summaries',
    "chapters": [
        ('Summarising instead of running', 'A program may have more possible inputs than could ever be tested one by one. Abstract interpretation runs the program on summaries of values instead, such as "a positive number" rather than an exact number. The result is a safe picture of all the behaviours that could happen.'),
        ('Lattices', 'The summaries are arranged in a lattice, a set of levels with an order. At the bottom is an exact value, and higher up are broader summaries such as "any number". Moving up gives a less exact but safer summary, so the analysis always reaches an answer.'),
        ('Widening', 'Loops can make the analysis go round forever, getting ever more precise. Widening jumps to a broader summary once it sees growth, so the analysis finishes. The cost is that the answer may become less exact.'),
        ('Sound analysis', 'A sound analysis never misses a real problem: if it says a program is safe, it is. The price is false alarms, where the analysis warns about a problem that cannot really happen. Designers choose how many false alarms to accept.'),
        ('Precision versus cost', 'A more exact analysis takes longer and uses more memory. A fast, rough analysis can check millions of lines quickly but warn about many non-problems. Finding the right balance is the central design choice.'),
        ('Static analysers in industry', 'Tools based on these ideas check large programs for crashes and wrong memory use before release. Some safety-critical aircraft software has been checked this way. Most teams use such tools alongside tests rather than in place of them.'),
    ],
    "test": [
        ('What does abstract interpretation run the program on?',
         [('a', 'Summaries of values'), ('b', 'Every possible input'), ('c', 'A printer'), ('d', "Only the real user's data")], 'a'),
        ('What is a lattice used for here?',
         [('a', 'Building walls'), ('b', 'Counting words'), ('c', 'Ordering summaries from exact to broad'), ('d', 'Playing music')], 'c'),
        ('What does widening do?',
         [('a', 'Makes the program run faster for users'), ('b', 'Jumps to a broader summary so the analysis finishes'), ('c', 'Deletes loops'), ('d', 'Turns numbers into words')], 'b'),
        ('What is a sound analysis guaranteed to do?',
         [('a', 'Run in one second'), ('b', 'Never warn about anything'), ('c', 'Need no computer'), ('d', 'Never miss a real problem')], 'd'),
        ('What is the usual cost of a more precise analysis?',
         [('a', 'It is cheaper'), ('b', 'It takes longer and uses more memory'), ('c', 'It removes all tests'), ('d', 'It stops the program from running')], 'b'),
    ],
}
