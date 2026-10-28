"""Control-Flow Integrity: stopping attackers from steering a program into code paths its designers never intended."""
CODE = 'computing5_cfi'
BOOK = {'title': 'Control-Flow Integrity',
 'subtitle': 'Code-reuse attacks, return-oriented programming, shadow stacks and overheads',
 'chapters': [('The path a program should take',
               'Every program has a set of legal paths through its code. Control-flow integrity '
               'checks that the program follows only those paths. A jump to an unexpected place is '
               'stopped.'),
              ('Code-reuse attacks',
               'Attackers sometimes avoid writing new code. They chain small pieces of existing '
               'code to do their work. Such chains are hard to spot with older defences.'),
              ('Return-oriented programming',
               'Return-oriented programming chains short snippets that end in a return '
               'instruction. The attacker controls the chain through data placed on the stack. It '
               'is a well-known technique in attacks.'),
              ('Shadow stacks',
               'A shadow stack keeps a protected copy of return addresses. On a return, the '
               'program checks that the address matches the copy. A changed address is caught.'),
              ('Compiler and hardware support',
               'Compilers can add checks to code automatically. Some processors add hardware '
               'support to make checks faster. Both reduce the work the programmer must do by '
               'hand.'),
              ('Overheads',
               'Checks cost time and sometimes memory. Designers choose how strict to be, weighing '
               'speed against protection. Well-built checks keep the overhead small for typical '
               'programs.')],
 'test': [('What does control-flow integrity check?',
           [('a', 'The font of the screen'),
            ('b', 'That a program follows only its legal paths'),
            ('c', 'The weight of the keyboard'),
            ('d', 'The age of the user')],
           'b'),
          ('What is a code-reuse attack?',
           [('a', 'Copying a song'),
            ('b', 'Recycling paper'),
            ('c', 'Chaining existing pieces of code to do the attacker work'),
            ('d', 'Repainting a wall')],
           'c'),
          ('What does a shadow stack keep?',
           [('a', 'A list of printers'),
            ('b', 'Old photographs'),
            ('c', 'Recipes'),
            ('d', 'A protected copy of return addresses')],
           'd'),
          ('What do compilers sometimes do to help?',
           [('a', 'Add checks to the code automatically'),
            ('b', 'Remove every function'),
            ('c', 'Print the source on paper'),
            ('d', 'Turn code into sound')],
           'a'),
          ('What is a cost of control-flow checks?',
           [('a', 'They make programs run backwards'),
            ('b', 'They delete the program'),
            ('c', 'Some extra time and memory'),
            ('d', 'They have no cost ever')],
           'c')]}
