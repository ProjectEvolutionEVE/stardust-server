"""Zero-Knowledge Proof Systems: proving a statement without revealing the secret, interactive proofs, SNARKs and STARKs compared."""
CODE = 'computing5_zk_proof_systems'
BOOK = {'title': 'Zero-Knowledge Proof Systems',
 'subtitle': 'Proving you know something without showing it',
 'chapters': [('Proving without revealing',
               'A zero-knowledge proof convinces a checker that a statement is true, without revealing anything beyond its truth. A prover might show they know a password without '
               'saying it. The idea is counterintuitive, but precise.'),
              ('Interactive proofs',
               'In an interactive proof, a prover and a verifier exchange messages, and the verifier uses random challenges. A false claim is caught with high probability. '
               'Repeating the exchange makes the error chance as small as needed.'),
              ('SNARKs',
               'A SNARK is a succinct non-interactive argument of knowledge. The proof is short and quick to check, and it needs no interaction. Many SNARKs need a trusted setup, '
               'a one-time step that must be done honestly.'),
              ('STARKs',
               'A STARK avoids a trusted setup and relies on hash functions for its security. Its proofs are larger than SNARK proofs, but they are transparent. The two families '
               'make different trade-offs.'),
              ('Practical costs',
               'Generating proofs can be expensive in computing time, even when checking them is cheap. Engineers must weigh proof size, setup assumptions, and prover speed. The '
               'best choice depends on the task.'),
              ('Where they are used',
               'Zero-knowledge proofs are used to protect privacy in identity checks and to compress large computations into quick checks. Some digital currencies and '
               'verification systems use them. Their use is growing, and their design needs expert review.')],
 'test': [('What does a zero-knowledge proof reveal beyond the truth of a statement?',
           [('a', 'The full secret'), ('b', 'Nothing extra'), ('c', 'The password in plain text'), ('d', "The checker's private key")],
           'b'),
          ('What do interactive proofs use to catch false claims?',
           [('a', 'A printed signature'), ('b', 'A list of colours'), ('c', 'A single fixed number'), ('d', 'Random challenges from the verifier')],
           'd'),
          ('What is the trusted setup of some SNARKs?',
           [('a', 'A weekly backup'), ('b', 'A kind of printer'), ('c', 'A one-time step that must be done honestly'), ('d', 'A test of speed')],
           'c'),
          ('What does a STARK avoid compared with some SNARKs?', [('a', 'A trusted setup'), ('b', 'Any security at all'), ('c', 'Hash functions'), ('d', 'Verification')], 'a'),
          ('What is often expensive even when checking is cheap?',
           [('a', 'Reading the statement'), ('b', 'Saving a file'), ('c', 'Naming the proof'), ('d', 'Generating the proof')],
           'd')]}
