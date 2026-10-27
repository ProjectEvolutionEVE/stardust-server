"""Cryptographic Agility and Migration: algorithms that retire, versioned formats, negotiation, an inventory of cryptography, migration plans and hybrid schemes."""
CODE = 'computing5_crypto_agility'
BOOK = {'title': 'Cryptographic Agility and Migration',
 'subtitle': 'Designing systems that can change their locks',
 'chapters': [('Algorithms that retire',
               'Cryptographic algorithms are retired when they become weak, when attacks improve, or when computers grow strong enough to threaten them. Systems that cannot '
               'change algorithms are stuck with broken protection. Planning for change is part of good design.'),
              ('Versioned formats',
               'A versioned format labels the algorithms used in stored data and messages. Readers can then choose the right method for each version. Without labels, old data '
               'becomes hard to handle when algorithms change.'),
              ('Negotiation',
               'In a negotiation, two parties agree on the strongest algorithm they both support. Protocols must avoid downgrade attacks, where an attacker forces a weaker '
               'choice. Strong defaults and checks on negotiation are important.'),
              ('An inventory of cryptography',
               'An organisation should list every place cryptography is used, including certificates, stored data and devices. An inventory shows which algorithms need replacing '
               'first. Many organisations find old uses they had forgotten.'),
              ('Migration plans',
               'A migration plan sets priorities, owners and deadlines for each system. It tests new algorithms in parallel before switching. Long-lived data may need '
               're-protection before the threat arrives.'),
              ('Hybrid schemes',
               'Hybrid schemes combine a classical algorithm and a newer one, so that security holds if either remains unbroken. They are a common bridge during migration. The '
               'cost is extra size and complexity.')],
 'test': [('Why are cryptographic algorithms retired?',
           [('a', 'They become too colourful'), ('b', 'They become weak or a threat grows'), ('c', 'They are printed too often'), ('d', 'They run on a Monday')],
           'b'),
          ('What does a versioned format do?',
           [('a', 'Hides all data'), ('b', 'Deletes old files'), ('c', 'Prints the version on paper'), ('d', 'Labels the algorithms used so readers can choose the right method')],
           'd'),
          ('What is a downgrade attack?',
           [('a', 'A faster computer attack'), ('b', 'A printer error'), ('c', 'An attacker forces a weaker algorithm to be chosen'), ('d', 'A lost password reset')],
           'c'),
          ('What should an inventory of cryptography list?',
           [('a', 'Every place cryptography is used'), ('b', 'Only the office printers'), ('c', 'Only the homepage colours'), ('d', 'Only the staff names')],
           'a'),
          ('What do hybrid schemes combine?',
           [('a', 'Two copies of the same key'), ('b', 'Two printers'), ('c', 'Two passwords written on paper'), ('d', 'A classical algorithm and a newer one')],
           'd')]}
