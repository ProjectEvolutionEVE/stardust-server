"""Operational Semantics: defining a language by the steps a program takes when it runs."""
CODE = 'computing5_operational_semantics'
BOOK = {
    "title": 'Operational Semantics',
    "subtitle": 'Defining a language by the steps a program takes when it runs',
    "chapters": [
        ('Steps of running', 'Operational semantics describes a language by the steps a program takes. Each step rule says how one piece of the program changes into the next. Putting the steps together describes the whole run.'),
        ('Big-step and small-step', 'Big-step rules jump from a program straight to its final result. Small-step rules show every individual move. Small-step is more detailed, which helps when the process itself matters, such as with concurrency.'),
        ('Evaluation contexts', 'An evaluation context marks the place in an expression where the next step happens. It lets the rules name the part to work on without writing out each surrounding piece. This keeps rule sets short.'),
        ('Proving type safety', 'A common proof shows that a well-typed program never gets stuck in an error. It works by showing that each step keeps the types right, and that a program that is not finished can always take a next step. This style of proof is often called progress and preservation.'),
        ('Language specifications', 'A language specification written as operational rules leaves little room for guessing. Two implementers who follow the same rules should get the same results. This is why careful language designs often include such rules.'),
        ('The link to implementations', 'Interpreters and compilers can be checked against the rules: each run should match what the rules say. Operational semantics gives a clear yardstick, which helps builders find where their code disagrees with the intended language.'),
    ],
    "test": [
        ('What does an operational semantics describe?',
         [('a', 'The steps a program takes when it runs'), ('b', 'The paint colours'), ('c', 'The price of cloud storage'), ('d', 'The sizes of shirts')], 'a'),
        ('What is the difference between big-step and small-step?',
         [('a', 'Big-step is in colour'), ('b', 'Small-step has no rules'), ('c', 'Big-step jumps to the final result; small-step shows each move'), ('d', 'There is no difference')], 'c'),
        ('What does an evaluation context mark?',
         [('a', 'A shop counter'), ('b', 'A map of the moon'), ('c', 'A date'), ('d', 'The place where the next step happens')], 'd'),
        ('What does a type-safety proof show?',
         [('a', 'Programs run in red'), ('b', 'A well-typed program never gets stuck in a type error'), ('c', 'Computers never sleep'), ('d', 'Keyboards never break')], 'b'),
        ('What is a benefit of operational rules in a language specification?',
         [('a', 'Implementers following them get the same results'), ('b', 'Programs get longer'), ('c', 'Languages get more colours'), ('d', 'Users need no computers')], 'a'),
    ],
}
