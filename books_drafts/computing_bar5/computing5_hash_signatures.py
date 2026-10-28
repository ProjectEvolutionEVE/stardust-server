"""Hash-Based Signatures: digital signatures built from hash functions alone, one-time keys, Merkle trees and state management hazards."""
CODE = 'computing5_hash_signatures'
BOOK = {'title': 'Hash-Based Signatures',
 'subtitle': 'Signatures that rest on hash functions alone',
 'chapters': [('Signatures from hashes',
               'A hash function turns any data into a short fixed-size fingerprint. Hash-based signatures build a digital signature using only hash functions. Their security '
               'rests on the hash function, which is the most conservative assumption in this field.'),
              ('One-time keys',
               'A basic hash-based scheme uses each key pair to sign only one message. Signing a second message with the same key reveals enough to forge signatures. Practical '
               'schemes bundle many one-time keys together.'),
              ('Merkle-tree schemes',
               'A Merkle tree combines many one-time public keys into one short root value. The signer proves that a one-time key belongs to the root with a short path of hashes. '
               'Merkle trees are the core of most practical hash-based signatures.'),
              ('State management hazards',
               'Stateful schemes must track which one-time keys have been used. Reusing a key, after a backup restore or a cloned machine, can break security completely. Careful '
               'state handling is essential.'),
              ('Long-lived keys',
               'Hash-based signatures suit keys that must last for decades, such as software update signing or firmware. Their long-term security does not depend on the hardness '
               'of number problems. The trade-off is larger signatures and careful key tracking.'),
              ('Trade-offs',
               'Hash-based signatures are fast to verify and rely on very well-studied building blocks. They have large signatures and need state management. Designers choose '
               'them when a conservative assumption matters more than size.')],
 'test': [('What does a hash function produce?',
           [('a', 'A full copy of the data'), ('b', 'A colour image'), ('c', 'A new keyboard'), ('d', 'A short fixed-size fingerprint of any data')],
           'd'),
          ('Why is a basic one-time hash-based key limited to one message?',
           [('a', 'The key erases itself after printing'),
            ('b', 'Signing a second message reveals enough to forge signatures'),
            ('c', 'The key must be shorter each time'),
            ('d', 'Hashes cannot be used twice')],
           'b'),
          ('What does a Merkle tree do in these schemes?',
           [('a', 'Combines many one-time public keys into one short root value'),
            ('b', 'Draws a picture of the signer'),
            ('c', 'Encrypts the whole disk'),
            ('d', 'Deletes old messages')],
           'a'),
          ('What is the main hazard of stateful schemes?',
           [('a', 'Using too many colours'),
            ('b', 'Signing too slowly on purpose'),
            ('c', 'Reusing a one-time key, for example after a cloned machine'),
            ('d', 'Keys that are too short to read')],
           'c'),
          ('What do hash-based signatures trade for their conservative security?',
           [('a', 'Slower checking of every message'), ('b', 'Larger signatures and careful key tracking'), ('c', 'Loss of all security'), ('d', 'Use of only paper')],
           'b')]}
