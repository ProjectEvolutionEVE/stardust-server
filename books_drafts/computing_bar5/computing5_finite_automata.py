"""Finite Automata and Regular Languages: machines with a fixed set of states, regular expressions and the pumping lemma."""
CODE = 'computing5_finite_automata'
BOOK = {'title': 'Finite Automata and Regular Languages',
 'subtitle': 'Machines with a fixed set of states',
 'chapters': [('States and transitions',
               'A finite automaton is a machine with a fixed set of states. It reads input one symbol at a time and moves between states along labelled transitions. When the '
               'input ends, it accepts or rejects depending on whether it stands in an accepting state.'),
              ('Deterministic machines',
               'In a deterministic automaton, each state and symbol has exactly one next state. Running it takes time proportional to the input length and a fixed amount of '
               'memory. It is a simple model of a very limited computer.'),
              ('Nondeterministic machines',
               'A nondeterministic automaton may have several choices for a symbol, or none. It accepts if some path ends in an accepting state. Every such machine can be '
               'converted into an equivalent deterministic one, although the conversion may add many states.'),
              ('Regular expressions',
               'A regular expression describes a pattern built from letters, joining, choice and repetition. The languages it describes are exactly the ones that finite automata '
               'recognise. Search tools use this equivalence to match text quickly.'),
              ('The pumping lemma',
               'The pumping lemma says that a long enough string in a regular language contains a middle section that can be repeated any number of times and stay in the '
               'language. It is often used to prove that a language is not regular. It is a necessary test, not a full description of regular languages.'),
              ('Minimisation and software',
               'Every regular language has a smallest equivalent automaton, found by merging states that behave the same way. Automata appear inside the scanners of compilers and '
               'in input checks. Their small size keeps these checks fast.')],
 'test': [('What does a finite automaton have?',
           [('a', 'An endless memory tape'), ('b', 'A monitor and a keyboard'), ('c', 'A random number generator'), ('d', 'A fixed set of states')],
           'd'),
          ('In a deterministic automaton, how many next states does each state and symbol have?',
           [('a', 'None'), ('b', 'Exactly one'), ('c', 'Two'), ('d', 'As many as there are letters')],
           'b'),
          ('What do regular expressions describe?',
           [('a', 'The same languages that finite automata recognise'),
            ('b', 'Pictures of machines'),
            ('c', 'Network speeds'),
            ('d', 'Any language at all, including every computable one')],
           'a'),
          ('What is the pumping lemma mainly used for?',
           [('a', 'Speeding up a printer'), ('b', 'Counting pixels'), ('c', 'Showing that a language is not regular'), ('d', 'Encrypting files')],
           'c'),
          ('What does minimisation of an automaton do?',
           [('a', 'Adds random states'), ('b', 'Merges states that behave the same way'), ('c', 'Deletes the input'), ('d', 'Turns it into a picture')],
           'b')]}
