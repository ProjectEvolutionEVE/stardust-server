"""Denotational Semantics: giving a program's meaning as a mathematical object."""
CODE = 'computing5_denotational_semantics'
BOOK = {
    "title": 'Denotational Semantics',
    "subtitle": 'Giving a program meaning as a mathematical object',
    "chapters": [
        ('Meaning as a thing', 'Denotational semantics gives each program a mathematical meaning, such as a function from inputs to outputs. The meaning does not depend on how a computer runs the program. It describes what the program is, not how it steps through its work.'),
        ('Domains', 'Domains are sets of values with an order that says one value carries more information than another. A partial result sits lower in the order than a finished one. This lets the theory talk about programs that may never finish.'),
        ('Fixed points', 'A loop or recursive definition has a meaning found as a fixed point: a value that the definition maps back to itself. Scott theory of domains shows that such a point exists under the right conditions, so the meaning is well defined.'),
        ('Compositionality', 'Meaning is compositional: the meaning of a whole is built from the meanings of its parts. So if two parts have the same meaning, swapping one for the other does not change the whole. This makes reasoning about large programs easier.'),
        ('Full abstraction', 'A semantics is fully abstract if two program pieces get the same meaning exactly when no context can tell them apart. Finding such a semantics for real languages is hard, and it has been a rich research area.'),
        ('Reading semantics papers', 'Papers in this area use notation for sets, orders and functions. Start with the examples, then read the rules slowly. The reward is a clear picture of what a language means, which helps designers and compiler writers.'),
    ],
    "test": [
        ('What does denotational semantics give a program?',
         [('a', 'A mathematical meaning'), ('b', 'A colour'), ('c', 'A song'), ('d', 'A time zone')], 'a'),
        ('What does a domain order capture?',
         [('a', 'The price of food'), ('b', 'The size of the screen'), ('c', 'The speed of a printer'), ('d', 'How much information a value carries')], 'd'),
        ('What is a fixed point?',
         [('a', 'A fixed price'), ('b', 'A value a definition maps back to itself'), ('c', 'A broken pixel'), ('d', 'A point on a map')], 'b'),
        ('What does compositionality mean?',
         [('a', 'Programs must be written in poetry'), ('b', 'Each part is painted red'), ('c', 'The meaning of a whole is built from the meanings of its parts'), ('d', 'Parts are sold separately')], 'c'),
        ('When is a semantics fully abstract?',
         [('a', 'When two pieces have the same meaning exactly when no context can tell them apart'), ('b', 'When it is written in colour'), ('c', 'When it runs faster'), ('d', 'When it has no numbers')], 'a'),
    ],
}
