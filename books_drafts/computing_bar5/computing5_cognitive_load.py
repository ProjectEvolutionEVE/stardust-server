"""Cognitive Load in Programming: working memory limits, chunking, code readability, interruption costs, experimental evidence and team practices."""
CODE = 'computing5_cognitive_load'
BOOK = {'title': 'Cognitive Load in Programming',
 'subtitle': 'How much a mind can hold at once, and how code can help',
 'chapters': [('Working memory limits',
               "Working memory holds only a few items at once. George Miller's 1956 paper suggested about "
               'seven, plus or minus two. Modern research suggests the limit may be smaller in some tasks. '
               'Either way, programmers can keep only a small amount in mind.'),
              ('Chunking',
               'People group related items into chunks, so that one idea takes less room. A well-named '
               'function is a chunk: the reader thinks of its purpose rather than each step. Good naming and '
               'structure make chunking easier.'),
              ('Code readability',
               'Code that is hard to follow forces the reader to hold many details in mind at once. Clear '
               'names, short functions and consistent layout reduce this load. Readability is a practical '
               'aid to correct work, not only a matter of taste.'),
              ('Interruption costs',
               "Each interruption can break a programmer's train of thought, and returning to the task takes "
               'time and effort. Research on focus suggests that interruptions have real costs. Protected '
               'time for deep work pays for itself.'),
              ('Experimental evidence',
               'Studies of programmers have compared different code layouts, naming choices and '
               'documentation styles. Results are mixed in detail, but they generally support clear naming '
               'and simple structure. Good claims need careful experiments.'),
              ('Team practices',
               'Teams can reduce cognitive load through code reviews, shared style guides, sensible '
               "documentation and reasonable working habits. Caring for other people's attention is part of "
               'professional practice.')],
 'test': [('What did George Miller suggest about working memory in 1956?',
           [('a', 'That it holds exactly one thousand items'),
            ('b', 'That it has no limit'),
            ('c', 'That it works only at night'),
            ('d', 'That it holds about seven items, plus or minus two')],
           'd'),
          ('What is chunking?',
           [('a', 'Breaking a computer into pieces'),
            ('b', 'Deleting all comments'),
            ('c', 'Grouping related items so that one idea takes less room'),
            ('d', 'Making code longer on purpose')],
           'c'),
          ('How can code readability help a programmer?',
           [('a', 'By removing the need to think at all'),
            ('b', 'By reducing how many details the reader must hold at once'),
            ('c', 'By making code harder to change'),
            ('d', 'By hiding the function names')],
           'b'),
          ('What do interruptions cost a programmer?',
           [('a', 'Time and effort to get back into the task'),
            ('b', 'Nothing, ever'),
            ('c', 'Extra sleep'),
            ('d', 'A better memory')],
           'a'),
          ('Which team practice helps reduce cognitive load?',
           [('a', 'Hiding code from colleagues'),
            ('b', 'Code reviews and shared style guides'),
            ('c', 'Removing all documentation'),
            ('d', 'Never speaking to other staff')],
           'b')]}
