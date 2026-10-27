"""Communication Complexity: two parties with a limited link, deterministic and randomised protocols, the disjointness problem and fooling sets."""
CODE = 'computing5_communication_complexity'
BOOK = {'title': 'Communication Complexity',
 'subtitle': 'How many bits two parties must exchange',
 'chapters': [('Two parties and a link',
               'In communication complexity, two parties each hold part of the input and must agree on a function of the whole. They can only talk over a link, and each bit sent '
               'costs something. The question is the least number of bits they must exchange.'),
              ('Deterministic protocols',
               "A deterministic protocol fixes the order and content of messages in advance, depending on each party's input. Its cost is the worst case over all inputs. Lower "
               'bounds show that some functions force many bits to move.'),
              ('Randomised protocols',
               'A randomised protocol lets the parties use shared or private random bits. It can use far fewer bits for some problems, while still being correct with high '
               'probability. The trade-off between error and cost is central.'),
              ('The disjointness problem',
               'In disjointness, each party holds a set and they must decide whether the sets share an element. This problem needs about n bits of communication when '
               'deterministic. With randomness, the cost falls sharply, which shows the power of shared coins.'),
              ('Fooling sets',
               'A fooling set is a collection of input pairs with a special pattern that forces any protocol to send enough bits. Finding one gives a lower bound. It is one of '
               'the main tools for proving limits.'),
              ('Links to data structures',
               'Communication lower bounds can be turned into limits on data structures, because a fast structure gives a cheap protocol. Hard communication problems therefore '
               'show that some queries cannot be answered fast. Bits must move, and that cost is real.')],
 'test': [('What do the two parties in communication complexity do?',
           [('a', 'They play a game of chess'),
            ('b', 'Each hold part of the input and must agree on a function of the whole'),
            ('c', 'They share a single printer'),
            ('d', 'They draw pictures')],
           'b'),
          ('What is the cost of a deterministic protocol measured as?',
           [('a', 'The average colour of the messages'), ('b', 'The number of parties in the room'), ('c', 'The time of day'), ('d', 'The worst case over all inputs')],
           'd'),
          ('What does disjointness ask the parties to decide?',
           [('a', 'Which set is larger in colour'), ('b', 'The name of the first set'), ('c', 'Whether their sets share an element'), ('d', 'Whether a clock is correct')],
           'c'),
          ('What does a fooling set give?', [('a', 'A lower bound on communication'), ('b', 'A faster network'), ('c', 'A password'), ('d', 'A prettier chart')], 'a'),
          ('Why does a lower bound on communication matter for data structures?',
           [('a', 'Data structures never use memory'),
            ('b', 'It makes all queries free'),
            ('c', 'It bans data structures'),
            ('d', 'A fast structure would give a cheap protocol, so hard problems limit queries')],
           'd')]}
