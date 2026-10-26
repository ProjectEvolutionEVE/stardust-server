"""Holes That Line Up: how small errors in several places can add up to one bad flight, and how a crew breaks the chain."""
CODE = 'flight3b_swiss_cheese'
BOOK = {
    "title": 'Holes That Line Up',
    "subtitle": 'How small errors in different places can add up to one bad flight',
    "chapters": [
        ('Many layers of defence',
         'A flight has many layers of defence: the plan, the checks, the instruments, the crew, the Tower and your own judgement. Each layer catches most mistakes. No single layer catches every one, and that is why pilots build several.'),
        ('The cheese picture',
         'The safety researcher James Reason described each layer as a slice of Swiss cheese. Every slice has holes, and the holes move about. Most of the time a hole in one slice is covered by a solid part of the next. A problem gets through only when the holes in several slices line up.'),
        ('Active and hidden errors',
         'Some errors happen at the controls, such as a number keyed in wrongly. Others sit quietly in the background, such as a setting left wrong after the last flight or a check that was skipped. The hidden errors are the risky ones, because they wait for a second problem to join them.'),
        ('Break the chain',
         'When something goes wrong, ask what else had to go wrong for it to become serious. Fix the cause that is easiest to fix. Then add a check at the point where the chain was weakest, so the next flight has one more slice of cheese in the way.'),
        ('Report the near miss',
         'A crew that fears blame stops reporting its small errors, and the holes stay open. Report a near miss plainly: what happened, what you did and what you would change. The people who speak up are the ones who keep the next flight safe.'),
        ('Your slice',
         'Be one of the layers that holds. Check your settings, read the readings and say out loud when something feels wrong. A pilot who catches a small problem early is often the reason a chain never grows.'),
    ],
    "test": [
        ('What does the Swiss cheese model describe?',
         [('a', 'A recipe for a meal aboard the Starship'), ('b', 'The shape of the docking bay'), ('c', 'How holes in several defences can line up and let a problem through'), ('d', 'A way to measure fuel')], 'c'),
        ('Why are hidden errors especially risky?',
         [('a', 'They make a loud noise at once'), ('b', 'They always cause a crash by themselves'), ('c', 'They only affect the paint on the craft'), ('d', 'They wait quietly until a second problem joins them')], 'd'),
        ('What is the best response when a crew member reports a near miss?',
         [('a', 'Thank them and look for the cause so the hole can be closed'), ('b', 'Ignore it, since nothing happened'), ('c', 'Find someone to blame at once'), ('d', 'Hide it from the Tower')], 'a'),
        ('Which action best breaks a chain of errors?',
         [('a', 'Waiting for the next flight to see what happens'), ('b', 'Asking what else must go wrong, then adding a check where the chain was weakest'), ('c', 'Turning off the instruments'), ('d', 'Adding more speed to finish sooner')], 'b'),
        ('Why does a blame-first culture make flying less safe?',
         [('a', 'It makes the craft heavier'), ('b', 'It gives more time to read the stars'), ('c', 'It stops people reporting small errors, so the holes stay open'), ('d', 'It lowers the cost of fuel')], 'c'),
    ],
}
