"""Secure Multi-Party Computation: several parties computing one answer without revealing their inputs, with secret sharing, garbled circuits and oblivious transfer."""
CODE = 'computing5_secure_mpc'
BOOK = {'title': 'Secure Multi-Party Computation',
 'subtitle': 'Several parties, one answer, and private inputs',
 'chapters': [('Several parties, one answer',
               "In secure multi-party computation, several parties compute a shared result from their private inputs. Each party learns the answer and nothing about the others' "
               'inputs beyond what the answer reveals. A common example is computing an average salary without revealing any one salary.'),
              ('Secret sharing',
               'Secret sharing splits a value into pieces, one for each party, so that a group must combine enough pieces to recover it. Each piece alone reveals nothing. Many '
               'MPC protocols compute directly on shares.'),
              ('Garbled circuits',
               "A garbled circuit encodes a Boolean circuit so that one party can evaluate it on another party's encrypted input. The evaluator learns only the output. Yao "
               'introduced the idea in the 1980s.'),
              ('Oblivious transfer',
               'In oblivious transfer, a sender offers several messages and a receiver gets exactly one of them, without the sender learning which. It is a basic building block '
               'for many MPC protocols. It can be built from standard public-key assumptions.'),
              ('Security models',
               'Security models describe what an adversary may do. A semi-honest adversary follows the protocol but studies the messages. A malicious adversary may deviate in any '
               'way. Protocols are designed for a chosen model.'),
              ('Private set intersection and statistics',
               'Private set intersection lets two parties learn which items they share, without revealing the rest of their sets. Private statistics let groups learn totals and '
               'averages from their combined data. These tools support privacy-preserving analysis.')],
 'test': [('What do parties in secure multi-party computation learn?',
           [('a', 'Every input'), ('b', 'The password of each party'), ('c', 'The colour of the room'), ('d', "The agreed answer, and nothing about others' inputs beyond it")],
           'd'),
          ('What does secret sharing do?',
           [('a', 'Copies a secret to everyone'),
            ('b', 'Splits a value so that enough pieces are needed to recover it'),
            ('c', 'Prints the secret on paper'),
            ('d', 'Deletes the secret')],
           'b'),
          ('What does a garbled circuit let an evaluator learn?', [('a', 'Only the output'), ('b', 'Every input'), ('c', "The sender's password"), ('d', 'The time of day')], 'a'),
          ('What does oblivious transfer give the receiver?',
           [('a', 'All messages'), ('b', 'None of the messages'), ('c', 'Exactly one of several messages, without the sender learning which'), ('d', "A copy of the sender's key")],
           'c'),
          ('What does a semi-honest adversary do?',
           [('a', 'Deletes all messages'), ('b', 'Follows the protocol but studies the messages'), ('c', 'Changes the colour of the messages'), ('d', 'Refuses to join')],
           'b')]}
