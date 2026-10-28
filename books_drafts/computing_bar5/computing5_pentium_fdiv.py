"""The Pentium Division Bug: a lookup table error, discovery by researchers, recall costs, public trust, verification gaps and lessons."""
CODE = 'computing5_pentium_fdiv'
BOOK = {
    "title": 'The Pentium Division Bug',
    "subtitle": 'A rare arithmetic fault that cost a chip maker dearly',
    "chapters": [
        ('A lookup table error',
         'In 1994 it became known that some Intel Pentium processors gave wrong answers to certain division problems. The fault lay in a lookup table used by the division circuit, where a few entries were missing. Ordinary use rarely showed the error, but it was real.'),
        ('Discovery by researchers',
         'Thomas Nicely, a number theory researcher, noticed inconsistent results while working on calculations and reported them publicly. Others tested their own chips and confirmed the problem. Discussion spread quickly through the early internet.'),
        ('Recall costs',
         'At first the company said most users would seldom meet the error. It later changed course and offered replacement chips to anyone who needed them. The charge to the company ran to hundreds of millions of dollars.'),
        ('Public trust',
         'The episode damaged the company\'s reputation for a time. Customers learned that an excellent product could still hide a serious flaw. Trust was rebuilt through clearer communication and stronger testing.'),
        ('Verification gaps',
         'The fault had passed through design and testing without being caught. Checking arithmetic circuits needs thorough test sets that include unusual edge cases, not just the common ones.'),
        ('Lessons',
         'Rare errors can still matter greatly. Companies should be open about faults, plan replacements in advance, and test the boundary cases of mathematical operations.'),
    ],
    "test": [
        ('What caused the Pentium division error?',
         [('a', 'A paper jam in a printer'), ('b', 'A lookup table in the division circuit with missing entries'), ('c', 'Too much sunlight on the chips'), ('d', 'A typing mistake in a magazine')], 'b'),
        ('Who first reported the inconsistent results publicly?',
         [('a', 'A number theory researcher, Thomas Nicely'), ('b', 'A stage magician'), ('c', 'A restaurant chef'), ('d', 'A local bus driver')], 'a'),
        ('What did the company eventually offer to affected customers?',
         [('a', 'A refusal of all requests'), ('b', 'Replacement chips for anyone who needed them'), ('c', 'A closed factory'), ('d', 'Chips at double the price')], 'b'),
        ('What is a verification gap?',
         [('a', 'A missing page in a manual'), ('b', 'A flaw that passed design and testing because the checks missed it'), ('c', 'A hole in a wall'), ('d', 'A space between two postage stamps')], 'b'),
        ('What lesson does this case teach?',
         [('a', 'Rare errors never matter'), ('b', 'Companies should hide all faults'), ('c', 'Rare errors can still matter, so test the boundary cases'), ('d', 'Only software can have errors')], 'c'),
    ],
}
