"""Reverse Engineering Binaries: taking compiled programs apart to see how they work, within legal and ethical limits."""
CODE = 'computing5_reverse_engineering'
BOOK = {'title': 'Reverse Engineering Binaries',
 'subtitle': 'Disassembly, control-flow graphs, decompilers, protocols and limits',
 'chapters': [('Starting from the finished program',
               'Reverse engineering studies a compiled program to understand how it works, without '
               'its source code. It is used for security research, interoperability and fixing old '
               'software. Its methods need care and good reasons.'),
              ('Disassembly',
               'A disassembler turns machine code back into readable instructions. Each '
               'instruction shows what the processor will do. Reading them takes patience and '
               'practice.'),
              ('Control-flow graphs',
               'A control-flow graph draws the blocks of code and the jumps between them. It helps '
               'the analyst see the program structure at a glance. Large programs are much easier '
               'to study this way.'),
              ('Decompilers',
               'A decompiler tries to produce higher-level code from machine code. The result is '
               'useful but often imperfect. Analysts check its output against the instructions.'),
              ('Protocol reverse engineering',
               'Analysts can work out a network protocol by watching the messages it sends. They '
               'look for fields, lengths and patterns. This can reveal how two programs talk to '
               'each other.'),
              ('Legal and ethical limits',
               'Reverse engineering can break licence terms or laws in some places. Many countries '
               'allow it for security research or interoperability under conditions. Responsible '
               'work follows the rules and reports flaws to the makers.')],
 'test': [('What does reverse engineering study?',
           [('a', 'Old photographs'),
            ('b', 'A compiled program, to learn how it works'),
            ('c', 'Road maps'),
            ('d', 'Cooking recipes')],
           'b'),
          ('What does a disassembler produce?',
           [('a', 'Sound from a speaker'),
            ('b', 'Paper books'),
            ('c', 'Readable instructions from machine code'),
            ('d', 'Coloured lights')],
           'c'),
          ('What does a control-flow graph show?',
           [('a', 'The weather for a week'),
            ('b', 'The number of pages in a book'),
            ('c', 'The price of a bus ticket'),
            ('d', 'The blocks of code and the jumps between them')],
           'd'),
          ('Why check a decompiler output?',
           [('a', 'Because its result is useful but often imperfect'),
            ('b', 'Because it is always perfect'),
            ('c', 'Because it cannot run'),
            ('d', 'Because it makes the code smaller')],
           'a'),
          ('What can reverse engineering of licence terms bring?',
           [('a', 'A guaranteed prize'),
            ('b', 'Free holidays'),
            ('c', 'Possible legal problems, depending on place and purpose'),
            ('d', 'Nothing at all, ever')],
           'c')]}
