"""Provable Security and Security Games: security games, reductions, the random oracle model, advantage and what proofs do and do not promise."""
CODE = 'computing5_provable_security'
BOOK = {'title': 'Provable Security and Security Games',
 'subtitle': 'What a security proof promises, and what it does not',
 'chapters': [('Security games',
               'A security game defines a challenge between an adversary and a challenger. The scheme is secure if every efficient adversary has only a negligible chance of '
               'winning. The game makes the security goal exact and testable in principle.'),
              ('Reductions',
               'A security proof often works by reduction: if an adversary could break the scheme, it could also solve a hard problem. Since the problem is believed hard, the '
               'scheme is believed secure. The quality of a proof depends on how tight the reduction is.'),
              ('The random oracle model',
               'The random oracle model treats a hash function as a perfectly random function that everyone can query. It makes some proofs possible that are otherwise out of '
               'reach. The model is an idealisation, and real hash functions may behave differently.'),
              ('Advantage',
               'The advantage of an adversary is how much better than random guessing it does in the security game. A proof shows the advantage is negligible under stated '
               'assumptions. Advantage is the usual measure of security in proofs.'),
              ('What proofs do promise',
               'A proof shows that a scheme is secure in a specific model, under specific assumptions. It rules out attacks that break those assumptions. A proof is a strong '
               'argument, not a guarantee against every possible attack.'),
              ('What proofs do not promise',
               'A proof does not guarantee good implementation, safe parameter choices, or security against side channels. Many real breaks came from code or assumptions outside '
               'the proof. Reading a security paper means checking the model, the assumptions and the scope.')],
 'test': [('What does a security game set up?',
           [('a', 'A card game for two'), ('b', 'A race between two printers'), ('c', 'A quiz on colours'), ('d', 'A challenge between an adversary and a challenger')],
           'd'),
          ('What is a reduction in a security proof?',
           [('a', 'Shortening the password'),
            ('b', 'Showing that breaking the scheme would also solve a hard problem'),
            ('c', 'Deleting the proof'),
            ('d', 'Lowering the screen brightness')],
           'b'),
          ('What does the random oracle model treat a hash function as?',
           [('a', 'A perfectly random function everyone can query'), ('b', 'A printed table'), ('c', 'A broken lock'), ('d', 'A keyboard layout')],
           'a'),
          ("What is an adversary's advantage?",
           [('a', 'The number of its computers'), ('b', 'Its size on a disk'), ('c', 'How much better than random guessing it does'), ('d', 'Its favourite colour')],
           'c'),
          ('What does a proof not guarantee?',
           [('a', 'Security within its stated model'),
            ('b', 'Safe implementation and side-channel resistance'),
            ('c', 'Precise definitions'),
            ('d', 'A clear statement of assumptions')],
           'b')]}
