"""Proof-of-Work Consensus: puzzles that cost energy, the longest-chain rule, difficulty adjustment, forks and security thresholds."""
CODE = 'computing5_proof_of_work'
BOOK = {'title': 'Proof-of-Work Consensus',
 'subtitle': 'Agreeing on a ledger by spending computing effort',
 'chapters': [('Puzzles that cost energy',
               'In proof-of-work, participants compete to find a number that makes a hash of the block start with a required pattern. Finding it takes many tries, but anyone can '
               'check it with one hash. The effort is the cost that makes cheating expensive.'),
              ('The longest-chain rule',
               'Nodes accept the chain with the most accumulated work as the valid history. Honest miners extend the longest chain, so a faster attacker must outpace them. The '
               'rule lets a network settle on one ledger.'),
              ('Difficulty adjustment',
               'The difficulty of the puzzle is adjusted so that blocks arrive at a roughly steady rate, even as total computing power changes. Bitcoin adjusts difficulty about '
               'every two weeks. Steady timing keeps the system predictable.'),
              ('Forks and orphan blocks',
               'Two miners may find blocks at nearly the same time, creating a fork. The network resolves it by following the longer chain, and the other block becomes an orphan. '
               'Orphans are a normal part of operation, though they waste effort.'),
              ('Security thresholds',
               'An attacker who controls more than half of the total work can rewrite recent history. Below that level, the chance of success falls rapidly as confirmations grow. '
               'Waiting for several confirmations is the usual defence.'),
              ('Energy costs',
               'Proof-of-work uses a large amount of electricity, because the puzzle work is the security. Supporters argue the cost makes attacks expensive. Critics point out '
               'the cost is paid whether or not the network needs the extra security.')],
 'test': [('What does a miner search for in proof-of-work?',
           [('a', 'A colour for the block'), ('b', "A user's password"), ('c', 'A number that makes the block hash start with a required pattern'), ('d', 'A date on a calendar')],
           'c'),
          ('Which chain do honest nodes accept under the longest-chain rule?',
           [('a', 'The chain with the most accumulated work'),
            ('b', 'The chain with the most colours'),
            ('c', 'The chain with the oldest timestamp only'),
            ('d', 'The chain printed first')],
           'a'),
          ('Why is difficulty adjusted?',
           [('a', 'To make blocks slower forever'), ('b', 'To remove all miners'), ('c', 'To print more money'), ('d', 'To keep blocks arriving at a roughly steady rate')],
           'd'),
          ('What is an orphan block?',
           [('a', 'A block with no data'),
            ('b', 'A block that loses a fork and is left out of the main chain'),
            ('c', 'A block that was never sent'),
            ('d', 'A block written in colour')],
           'b'),
          ('What does an attacker need to rewrite recent history?',
           [('a', 'More than half of the total work'), ('b', 'A single computer with a red screen'), ('c', 'A copy of the printer'), ('d', 'Nothing at all')],
           'a')]}
