"""Mutation Testing: planting small faults on purpose to see whether the tests notice them."""
CODE = 'computing4_mutation_testing'
BOOK = {
    "title": 'Mutation Testing',
    "subtitle": 'Planting small faults on purpose, to see whether the tests notice them',
    "chapters": [
        ('Seeded faults',
         'Mutation testing makes many copies of the program, each with one small fault seeded on purpose. A fault might flip a greater-than sign or remove a line. Each copy is a mutant, and the tests are run against every mutant.'),
        ('Killing mutants',
         'A mutant is killed when a test fails because of its fault. A mutant that survives all tests shows a gap in the test suite. The share of killed mutants is a rough score of how strong the tests are.'),
        ('Test suite strength',
         'Many tests with high coverage can still miss faults if they never check the results. Mutation testing asks a sharper question: would the tests catch a wrong result? It shows whether tests really check behaviour, or only run the code.'),
        ('Equivalent mutants',
         'Some mutants behave exactly like the original, so no test could ever kill them. These are equivalent mutants. They lower the score unfairly, and a person must judge them by reading the code.'),
        ('Cost control',
         'Running every mutant against every test is slow. Teams limit the cost by testing only changed code, sampling mutants, or running the full check at night. Keep the check fast enough that people will act on its results.'),
        ('Using the results',
         'Surviving mutants point to specific places where a new test would help. Use them as a guide for writing better assertions, not as a target to chase at any cost. A high score that nobody reads is worth less than a small, honest report.'),
    ],
    "test": [
        ('What is a mutant in this kind of testing?',
         [('a', 'A copy of the program with one small fault seeded on purpose'), ('b', 'A type of computer virus'), ('c', 'A new team member'), ('d', 'A cloud server')], 'a'),
        ('When is a mutant killed?',
         [('a', 'When the mutant is deleted by hand'), ('b', 'When the mutant passes every test'), ('c', 'When a test fails because of its fault'), ('d', 'When the office closes')], 'c'),
        ('What does a surviving mutant suggest?',
         [('a', 'That the tests are perfect'), ('b', 'A gap in the test suite'), ('c', 'That the code is too fast'), ('d', 'That the mutant should be merged')], 'b'),
        ('What is an equivalent mutant?',
         [('a', 'A mutant that is twice as large'), ('b', 'A mutant written by a second company'), ('c', 'A mutant that crashes the computer'), ('d', 'A mutant that behaves exactly like the original')], 'd'),
        ('Why can a high coverage score still miss faults?',
         [('a', 'Because tests may run the code without checking the results'), ('b', 'Because coverage counts the number of mutants'), ('c', 'Because coverage is always zero'), ('d', 'Because tests never run')], 'a'),
    ],
}
