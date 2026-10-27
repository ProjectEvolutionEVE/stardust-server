"""Refinement Types: types with predicates attached, so a checker can prove rules such as never out of bounds."""
CODE = 'computing5_refinement_types'
BOOK = {
    "title": 'Refinement Types',
    "subtitle": 'Types with rules attached, so a checker can prove things like never out of bounds',
    "chapters": [
        ('A type with a rule', 'A normal type says a value is an integer. A refinement type adds a rule, such as "an integer greater than zero". The checker then confirms that the code keeps that rule true everywhere the value is used.'),
        ('Checking with solvers', 'The checker turns refinement rules into questions for a solver, which says whether the rules always hold. That is why refinement types depend on solvers, and why the checks can run automatically.'),
        ('Liquid types', 'Liquid types are a practical version that limits the rules to a simple set, so the solver answers quickly. Research projects have used them to check existing programs with only modest changes.'),
        ('Contracts', 'A refinement can act as a contract on a function: the input must not be empty, and the output is promised to be sorted. Callers are checked against it, and the function is checked against its own promise, so each side knows what to expect.'),
        ('Array bounds proofs', 'A common use is proving that an array index is always inside the array. That removes a whole class of crashes and security holes, because the program can never read past the end of the list.'),
        ('The learning curve', 'Writing refinements takes effort, and the rules can be hard to get right. Teams often start with a few key functions and add more over time. The payoff is strong checking that catches errors early.'),
    ],
    "test": [
        ('What does a refinement type add to a normal type?',
         [('a', 'A rule the value must satisfy'), ('b', 'A colour'), ('c', 'A picture'), ('d', 'A second name')], 'a'),
        ('What checks refinement rules automatically?',
         [('a', 'A chef'), ('b', 'A camera'), ('c', 'A printer'), ('d', 'A solver')], 'd'),
        ('What can a refinement type prove about an array access?',
         [('a', 'The index is always inside the array'), ('b', 'The array is painted'), ('c', 'The array is sorted by colour'), ('d', 'The array has a name')], 'a'),
        ('What is a common use of refinement contracts?',
         [('a', 'Writing letters to friends'), ('b', 'Storing photos'), ('c', 'Stating what a function needs as input and promises as output'), ('d', 'Counting clouds')], 'c'),
        ('What is a known drawback?',
         [('a', 'It makes programs run in colour'), ('b', 'It takes effort, and the rules can be hard to get right'), ('c', 'It removes all bugs'), ('d', 'It needs no computer')], 'b'),
    ],
}
