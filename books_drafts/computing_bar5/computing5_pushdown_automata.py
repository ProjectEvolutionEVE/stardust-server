"""Pushdown Automata and Context-Free Languages: a machine with a stack, grammars, parse trees and ambiguity."""
CODE = 'computing5_pushdown_automata'
BOOK = {'title': 'Pushdown Automata and Context-Free Languages',
 'subtitle': 'A machine with a stack, and the grammars it reads',
 'chapters': [('A stack in a machine',
               'A pushdown automaton is a finite automaton with one extra memory: a stack. It can push a symbol on top, pop the top symbol, or leave the stack alone. The stack '
               'lets the machine remember nested structure that a plain automaton cannot.'),
              ('Context-free grammars',
               'A context-free grammar builds strings from rules that replace one symbol at a time, regardless of what surrounds it. Rules such as a sentence made of a noun '
               'phrase and a verb phrase describe many languages. Programming languages are mostly described this way.'),
              ('Parse trees',
               'A parse tree shows how a grammar produces a string, with each branch a rule applied. Compilers build parse trees to understand the structure of code. A tree makes '
               'the meaning of nested brackets or expressions clear.'),
              ('Ambiguity',
               'A grammar is ambiguous if some string has two different parse trees. Ambiguity can give one sentence two meanings, which is a problem for programming languages. '
               'Good language design removes it with precedence rules and clear syntax.'),
              ('Pumping for context-free languages',
               'A pumping lemma for context-free languages says that long enough strings contain two matching parts that can be repeated together. It is used to show that some '
               'languages are not context-free. Like the regular version, it gives a test, not a complete description.'),
              ('Limits of grammars',
               'Context-free languages cannot match every pattern a computer must check. For example, a language that needs three matching counts in one string goes beyond them. '
               'Such checks need a more powerful machine.')],
 'test': [('What extra memory does a pushdown automaton have?', [('a', 'A stack'), ('b', 'A printer'), ('c', 'A second screen'), ('d', 'A clock with no ticks')], 'a'),
          ('What does a context-free grammar replace at each step?',
           [('a', 'The whole machine'), ('b', 'Only the last line of input'), ('c', 'One symbol, whatever surrounds it'), ('d', 'Every letter in the alphabet')],
           'c'),
          ('What does a parse tree show?',
           [('a', 'The weather forecast'), ('b', 'How a grammar produces a string'), ('c', 'The price of memory'), ('d', 'The colour of the input')],
           'b'),
          ('What is an ambiguous grammar?',
           [('a', 'A grammar with no rules'),
            ('b', 'A grammar that only uses numbers'),
            ('c', 'A grammar that is always correct'),
            ('d', 'A grammar where some string has two different parse trees')],
           'd'),
          ('Which kind of check needs a more powerful machine than a context-free grammar?',
           [('a', 'Matching a nested pair of brackets'),
            ('b', 'Checking a single fixed word'),
            ('c', 'Matching three counts that must agree in one string'),
            ('d', 'Reading a plain list of numbers')],
           'c')]}
