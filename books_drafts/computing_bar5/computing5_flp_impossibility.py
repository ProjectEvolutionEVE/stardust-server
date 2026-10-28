"""The FLP Impossibility Result: why agreement cannot be guaranteed in an asynchronous system if one process may fail."""
CODE = 'computing5_flp_impossibility'
BOOK = {
    "title": 'The FLP Impossibility Result',
    "subtitle": 'Why agreement cannot be guaranteed in an asynchronous system if one process may fail',
    "chapters": [
        ('Agreeing across machines', 'Several computers often need to agree on one value, such as which order transactions happened in. In 1985, Fischer, Lynch and Paterson showed a hard limit on this: when messages can be delayed by any amount, with no clock limits, agreement cannot always be guaranteed.'),
        ('One faulty process', 'The result says that even with only one process that may crash, no algorithm can guarantee agreement and always finish. The problem is not only about speed. An unlucky delay can always keep the group from deciding.'),
        ('Why timeouts help', 'Real systems use timeouts, so a slow machine can be given up on. A timeout is a guess, and it can be wrong, but it gives the group a way to move on. This sidesteps the impossibility in practice, though not in theory.'),
        ('Randomised escapes', 'Some algorithms use random choices so that, with probability one, the group eventually agrees. The guarantee is that agreement arrives eventually, not that it arrives by a set time. Ben-Or was an early example of this approach.'),
        ('Partial synchrony', 'Partial synchrony assumes that delays are unknown but eventually bounded and stable. Under that assumption, consensus can be solved, and many practical protocols rely on it. The model is a sensible middle ground.'),
        ('Practical implications', 'The result teaches designers that every consensus protocol makes a trade-off. It may pause for safety, use timeouts, or accept randomness. Knowing the limit helps engineers choose the right one for their system.'),
    ],
    "test": [
        ('In what year did Fischer, Lynch and Paterson publish the result?',
         [('a', '1066'), ('b', '1492'), ('c', '1985'), ('d', '2001')], 'c'),
        ('What does the FLP result say about one faulty process?',
         [('a', 'It is always easy to handle'), ('b', 'It can stop a group from ever guaranteeing agreement in an asynchronous system'), ('c', 'It makes agreement faster'), ('d', 'It cannot exist')], 'b'),
        ('Why do real systems use timeouts?',
         [('a', 'To colour the screen'), ('b', 'To give up on slow machines and move on, though this is a guess'), ('c', 'To stop time'), ('d', 'To print logs')], 'b'),
        ('What do randomised algorithms guarantee?',
         [('a', 'Nothing at all'), ('b', 'Agreement by a set time'), ('c', 'Faster networks'), ('d', 'Agreement eventually, with probability one')], 'd'),
        ('What does partial synchrony assume?',
         [('a', 'Delays are unknown but eventually bounded and stable'), ('b', 'Delays are infinite'), ('c', 'Clocks never run'), ('d', 'Messages never arrive')], 'a'),
    ],
}
