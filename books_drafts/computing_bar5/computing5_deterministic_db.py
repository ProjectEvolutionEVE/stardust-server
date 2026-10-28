"""Deterministic Databases: fixing the order of transactions in advance, so copies replay the same result."""
CODE = 'computing5_deterministic_db'
BOOK = {
    "title": 'Deterministic Databases',
    "subtitle": 'Fixing the order of transactions in advance, so copies replay the same result',
    "chapters": [
        ('A fixed order in advance', 'In a deterministic database, the order of transactions is agreed before they run. Every copy then runs the same transactions in the same order and gets the same result. Nothing depends on which copy happened to be faster.'),
        ('Replay', 'Because the order is fixed, a log of transactions can be replayed to rebuild the data exactly. This makes recovery and copying simple, since the log is the record of truth.'),
        ('Avoiding nondeterministic aborts', 'In many systems, transactions may abort at random when they clash. A fixed order removes that randomness, so the same transaction behaves the same on each copy. Systems can then avoid surprise failures between copies.'),
        ('Calvin-style ideas', 'The Calvin system, published by Thomson and colleagues in 2012, sorts transactions first and then runs them with little coordination. This shows that a fixed order can give high throughput in some workloads.'),
        ('Replicas that agree', 'Replicas that run the same ordered log stay in step without exchanging every detail. This lowers the traffic between them, and makes agreement a natural result rather than an extra step.'),
        ('Throughput', 'Fixing the order up front has a cost: transactions must declare what data they touch, and popular items can slow others. Designers weigh these costs against the benefits of predictable, identical copies.'),
    ],
    "test": [
        ('When is the transaction order fixed in a deterministic database?',
         [('a', 'Before transactions run'), ('b', 'After the power cut'), ('c', 'Never'), ('d', 'At random')], 'a'),
        ('What does replaying a log rebuild?',
         [('a', 'A photo'), ('b', 'A song'), ('c', 'A map'), ('d', 'The data exactly')], 'd'),
        ('What randomness does a fixed order remove?',
         [('a', 'Music'), ('b', 'Random colours'), ('c', 'Nondeterministic aborts when transactions clash'), ('d', 'Users names')], 'c'),
        ('Who published the Calvin system work in 2012?',
         [('a', 'Hopper and Lovelace'), ('b', 'Knuth and Bendix'), ('c', 'Lamport alone'), ('d', 'Thomson and colleagues')], 'd'),
        ('What does a fixed order cost?',
         [('a', 'Replicas cannot agree'), ('b', 'Logs cannot be kept'), ('c', 'Nothing at all'), ('d', 'Transactions must declare what data they touch')], 'd'),
    ],
}
