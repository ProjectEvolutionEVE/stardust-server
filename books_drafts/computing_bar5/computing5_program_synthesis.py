"""Program Synthesis: having a computer write a program that meets a stated specification."""
CODE = 'computing5_program_synthesis'
BOOK = {
    "title": 'Program Synthesis',
    "subtitle": 'Having a computer write a program that meets a stated specification',
    "chapters": [
        ('Writing programs from goals', 'Program synthesis is the task of producing a program from a specification of what it should do. The specification might be a rule, a list of examples, or a logical statement. The computer searches for a program that fits.'),
        ('Examples as specifications', 'A simple way to say what you want is to show examples: this input gives that output. Synthesis tools search for a program that fits all the examples. Many examples can still fit several programs, so the choice needs care.'),
        ('Search spaces', 'The set of possible programs is huge, so the search must be guided. Tools limit the size of the programs they try, and they use rules to skip programs that cannot work. Good limits make the search practical.'),
        ('Enumerative and SMT-based synthesis', 'Enumerative synthesis tries programs from smallest to largest until one fits. SMT-based synthesis uses a solver to find values that complete a program template. Both are used, and each suits different problems.'),
        ('Verifying results', 'A synthesised program still needs checking against the full specification, since examples may not cover every case. Tools combine synthesis with verification so that the final program is shown to meet the rules.'),
        ('Limits', 'Synthesis works well for small, clearly stated tasks, such as data transformations. For large, vague goals it is far harder, and the results can be hard to read. The field grows steadily, but people still play the central role.'),
    ],
    "test": [
        ('What is program synthesis?',
         [('a', 'Making a program from a specification of what it should do'), ('b', 'Making a sandwich'), ('c', 'Painting a wall'), ('d', 'Cleaning a printer')], 'a'),
        ('What can a set of examples serve as?',
         [('a', 'A weather report'), ('b', 'A menu'), ('c', 'A specification'), ('d', 'A shopping list')], 'c'),
        ('Why must the search space be limited?',
         [('a', 'Programs are too many to try without limits'), ('b', 'Computers cannot count'), ('c', 'Programs must be short poems'), ('d', 'Examples are forbidden')], 'a'),
        ('What does enumerative synthesis do?',
         [('a', 'Tries programs from smallest to largest until one fits'), ('b', 'Deletes all programs'), ('c', 'Prints a list of colours'), ('d', 'Asks the user to type code')], 'a'),
        ('Why check a synthesised program against the full specification?',
         [('a', 'The printer needs it'), ('b', 'It is always wrong'), ('c', 'The screen must match'), ('d', 'Examples may not cover every case')], 'd'),
    ],
}
