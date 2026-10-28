"""Causal Consistency: keeping cause and effect in the right order, without one global order."""
CODE = 'computing5_causal_consistency'
BOOK = {
    "title": 'Causal Consistency',
    "subtitle": 'Keeping cause and effect in the right order, without one global order',
    "chapters": [
        ('Cause before effect', 'Causal consistency means that if one change could have caused another, everyone sees the first before the second. A reply to a message should never appear before the message it answers. Unrelated changes may appear in any order.'),
        ('Session guarantees', 'Session guarantees are simple promises to one user: you will see your own writes, and you will never see older data after newer data. Terry and colleagues described these in work on the Bayou system in the 1990s. They are a practical form of causal ordering.'),
        ('Causal delivery', 'A system that delivers messages in causal order holds back any message whose cause has not yet arrived. This keeps effects from showing up too early. The waiting costs a little delay but gives a clear sequence.'),
        ('Causal memory', 'Causal memory, studied by Ahamad and colleagues, applies this idea to shared memory. Processes agree on causal links but not on a single global order of writes. The model is weaker than linearizability but stronger than no guarantee at all.'),
        ('Practical stores', 'Several databases and replicated stores offer causal guarantees, because they are faster and can keep working during network splits. Designers choose them when users need sensible ordering without the cost of one global order.'),
        ('Comparison with eventual consistency', 'Eventual consistency only promises that copies will agree in time. Causal consistency promises more: the order of cause and effect is kept along the way. That makes apps feel less confusing, at a modest cost.'),
    ],
    "test": [
        ('What does causal consistency protect?',
         [('a', 'Cause coming before effect'), ('b', 'The colour of the screen'), ('c', 'Printer speed'), ('d', 'The number of users')], 'a'),
        ('What does a session guarantee promise to one user?',
         [('a', 'You never sign in'), ('b', 'Your phone never rings'), ('c', 'You see everything in the world'), ('d', 'You see your own writes')], 'd'),
        ('What does a system with causal delivery do with a message whose cause has not arrived?',
         [('a', 'Deletes it'), ('b', 'Holds it back'), ('c', 'Prints it'), ('d', 'Sends it to space')], 'b'),
        ('What does causal memory agree on?',
         [('a', 'Nothing'), ('b', 'The weather'), ('c', 'Causal links but not one global order of writes'), ('d', 'Colours')], 'c'),
        ('How does causal consistency compare with eventual consistency?',
         [('a', 'It keeps cause and effect in order along the way'), ('b', 'It removes all data'), ('c', 'It is slower in every case'), ('d', 'It has no copies')], 'a'),
    ],
}
