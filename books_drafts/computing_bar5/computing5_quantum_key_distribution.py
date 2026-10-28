"""Quantum Key Distribution: photons carrying keys, the BB84 protocol, detecting eavesdroppers, device limits and comparison with post-quantum cryptography."""
CODE = 'computing5_quantum_key_distribution'
BOOK = {'title': 'Quantum Key Distribution',
 'subtitle': 'Sending keys as single particles of light',
 'chapters': [('Photons carrying keys',
               'Quantum key distribution sends a secret key as individual photons of light. Each photon carries a bit encoded in its polarisation or phase. Two parties can agree '
               'on a shared key over an optical link.'),
              ('The BB84 protocol',
               'BB84, proposed by Charles Bennett and Gilles Brassard in 1984, lets a sender encode bits in one of two measurement bases chosen at random. The receiver measures '
               'in random bases too. They then keep only the bits where the bases matched.'),
              ('Detecting eavesdroppers',
               'Measuring a photon in the wrong basis disturbs it. An eavesdropper therefore causes errors that the two parties can detect by comparing a sample of their bits. If '
               'the error rate is too high, they discard the key.'),
              ('Device limits',
               'Real devices emit imperfect light sources and detectors with noise and losses. Attacks can exploit these imperfections, so careful engineering and testing are '
               'needed. Practical systems have limited distance and speed.'),
              ('Comparison with post-quantum cryptography',
               'Quantum key distribution needs special optical hardware and dedicated links. Post-quantum cryptography uses classical software and can run on ordinary networks. '
               'The two approaches address the same goal in very different ways.'),
              ('Network deployments',
               'Quantum key distribution has been deployed on some dedicated fibre links and in trial networks. Its use is specialised and remains an active area of research. '
               'Organisations should weigh cost, range and the security assumptions involved.')],
 'test': [('What carries the bits in quantum key distribution?',
           [('a', 'Sheets of paper'), ('b', 'Electric kettles'), ('c', 'Sound waves in air'), ('d', 'Single photons of light')],
           'd'),
          ('Who proposed the BB84 protocol in 1984?',
           [('a', 'Alan Turing and Alonzo Church'),
            ('b', 'Charles Bennett and Gilles Brassard'),
            ('c', 'Ada Lovelace and Grace Hopper'),
            ('d', 'Richard Hamming and Claude Shannon')],
           'b'),
          ('What does measuring a photon in the wrong basis do?',
           [('a', 'Disturbs it, so an eavesdropper causes detectable errors'), ('b', 'Makes the photon invisible'), ('c', 'Doubles the key length'), ('d', 'Deletes the receiver')],
           'a'),
          ('What do real devices introduce that attacks can exploit?',
           [('a', 'Perfect light sources'), ('b', 'Silence'), ('c', 'Imperfect light sources and noisy detectors'), ('d', 'Nothing at all')],
           'c'),
          ('How does quantum key distribution compare with post-quantum cryptography?',
           [('a', 'They are identical in every way'),
            ('b', 'It needs special optical hardware, while post-quantum runs as classical software'),
            ('c', 'Post-quantum needs photons'),
            ('d', 'Neither can protect anything')],
           'b')]}
