"""Symbolic Execution: running a program on unknown inputs and finding the ones that cause trouble."""
CODE = 'computing5_symbolic_execution'
BOOK = {
    "title": 'Symbolic Execution',
    "subtitle": 'Running a program on unknown inputs to find the ones that cause trouble',
    "chapters": [
        ('Symbols instead of numbers', 'A normal test feeds in one number and checks the result. Symbolic execution feeds in a symbol, such as x, that stands for any value. The program is followed step by step while the symbol carries its unknown nature along.'),
        ('Path constraints', 'Each time the program makes a choice, such as "if x is above 10", the choice adds a rule to a list, called a path constraint. Following one route through the program gives one list of rules that describes all the inputs taking that route.'),
        ('Solver queries', 'To find a real input, the tool asks a solver whether the rules can all be true together. The solver answers yes and gives a sample value, or no. These queries are the heart of the method.'),
        ('Path explosion', 'Every choice doubles the number of routes, so a program with many choices has far too many paths to try. This is called path explosion. Tools handle it by choosing the paths most likely to matter and by simplifying the rules.'),
        ('Concolic testing', 'Concolic testing mixes real and symbolic runs. The program runs on a real input, the tool records the rules along the way, and then it flips one rule to explore a new route. This keeps the work manageable while still reaching hidden paths.'),
        ('Finding bugs', 'Symbolic execution is good at finding inputs that cause a crash, a wrong result or a broken check. It cannot prove that a program is always correct, but a found input is a real, repeatable problem that a developer can fix.'),
    ],
    "test": [
        ('What does a symbol such as x stand for?',
         [('a', 'Any value at all'), ('b', 'Always the number zero'), ('c', 'The screen'), ('d', 'A file name')], 'a'),
        ('What is a path constraint?',
         [('a', 'A kind of password'), ('b', 'A rule that a route through the program requires'), ('c', 'A type of printer'), ('d', 'A timer')], 'b'),
        ('What does a solver answer for a set of rules?',
         [('a', 'The users name'), ('b', 'The weather'), ('c', 'Whether they can be true together, and a sample value if so'), ('d', 'The colour of the code')], 'c'),
        ('What is path explosion?',
         [('a', 'A kind of screen bug'), ('b', 'Routes multiplying with each choice, so there are too many to try'), ('c', 'A crash of the solver power supply'), ('d', 'A kind of backup')], 'b'),
        ('What can a found input from symbolic execution show?',
         [('a', 'That the program is perfect'), ('b', 'A real, repeatable problem'), ('c', 'That no bugs exist'), ('d', 'The price of the hardware')], 'b'),
    ],
}
