"""Oblivious RAM: hiding access patterns, the overhead of obliviousness, path ORAM, trusted hardware and the limits of the approach."""
CODE = 'computing5_oblivious_ram'
BOOK = {'title': 'Oblivious RAM',
 'subtitle': 'Hiding which memory a program touches',
 'chapters': [('Hiding access patterns',
               'Even when data is encrypted, the pattern of memory accesses can reveal secrets. An observer who sees which locations are read can infer what the program is doing. '
               'Oblivious RAM hides this access pattern.'),
              ('The overhead of obliviousness',
               'Hiding access patterns costs extra work, usually a factor of about log n for good schemes. Every access must look the same whatever the real request is. The '
               'overhead is the price of privacy in memory.'),
              ('Path ORAM',
               'Path ORAM is a practical scheme that stores data in a tree and reads a whole path on each access. Blocks are reshuffled after each access so their positions stay '
               'hidden. It is one of the most widely studied designs.'),
              ('Trusted hardware',
               'Some systems run oblivious algorithms inside a trusted processor enclave, which protects data from the operating system. The enclave still needs care, because '
               'outside observers can see some memory traffic. Hardware and software design must work together.'),
              ('Uses in secure enclaves',
               'Oblivious RAM is used in designs where a program handles secret data in a shared environment. Examples include private search and some secure databases. Each use '
               'must justify the cost of the extra work.'),
              ('Limits',
               'Oblivious RAM hides access patterns, but not the total amount of data or other side channels such as timing outside the protocol. Designers must also consider '
               'failures and the cost of updates. The protection is strong but specific.')],
 'test': [('What can an observer learn from access patterns even with encryption?',
           [('a', 'The colour of the memory chips'), ('b', 'The name of the programmer'), ('c', 'What the program is doing, from which locations are read'), ('d', 'Nothing ever')],
           'c'),
          ('What is the typical overhead of good oblivious RAM schemes?',
           [('a', 'About a factor of log n'), ('b', 'Exactly zero'), ('c', 'About a factor of one million'), ('d', 'Only in colour')],
           'a'),
          ('What does path ORAM store data in?', [('a', 'A single number'), ('b', 'A paper map'), ('c', 'A colour palette'), ('d', 'A tree')], 'd'),
          ('Why use trusted hardware with oblivious algorithms?',
           [('a', 'To make the program print faster'),
            ('b', 'To protect data from the operating system inside an enclave'),
            ('c', 'To remove all memory'),
            ('d', 'To store passwords in plain text')],
           'b'),
          ('What does oblivious RAM not hide?',
           [('a', 'The total amount of data and other side channels outside the protocol'),
            ('b', 'Which location is read'),
            ('c', 'The pattern of accesses'),
            ('d', 'Nothing at all is hidden in any case')],
           'a')]}
