"""Plotting an Intercept: moving targets, lead angles, and the steady bearing that gives away a collision course."""
CODE = 'navigation2_intercept'
BOOK = {
    "title": 'Plotting an Intercept',
    "subtitle": 'Moving targets, lead angles, and the bearing that gives away a collision course',
    "chapters": [
        ('Two things moving',
         'Your craft and a target are both moving, so the picture changes as you go. It is easier to think about the target\'s motion relative to your own. Plot the target\'s track from its last known position, and plot your own track beside it.'),
        ('Relative motion',
         'Relative motion takes your own movement away from the target\'s. If you and a target both sail east at the same speed, the target seems not to move at all. Working in relative motion shows the true danger, and the true chance to meet.'),
        ('The lead angle',
         'To hit a moving target, you aim ahead of it, not at it. The lead angle depends on the target\'s speed and your own. A velocity triangle shows it: your speed, the target\'s speed and the path you need, and the angle between them is the lead.'),
        ('A collision course',
         'If another ship keeps the same bearing while the distance between you shrinks, you are on a collision course. Mariners call this constant bearing, decreasing range. The check is simple: take bearings a few minutes apart and watch whether the bearing changes.'),
        ('Time to meet',
         'Once you know the closing speed and the distance, the time to meet is the distance divided by the closing speed. Two craft closing at 10 km an hour, and 5 km apart, meet in half an hour.'),
        ('Plan early',
         'An intercept planned late needs sharp turns and wastes fuel. A calm plan made early, on a steady heading, is easier to correct on the way. Recheck the plan often, because a moving target can change its course.'),
    ],
    "test": [
        ('What is relative motion?',
         [('a', 'Motion measured against your own movement'), ('b', 'Motion measured by the clock'), ('c', 'The motion of the Moon alone'), ('d', 'The movement of the stars')], 'a'),
        ('To hit a moving target, where should you aim?',
         [('a', 'At the target\'s present position'), ('b', 'Ahead of the target, by the lead angle'), ('c', 'Behind the target'), ('d', 'Straight up')], 'b'),
        ('A second ship keeps the same bearing while the distance between you shrinks. What is the situation?',
         [('a', 'Safe passage'), ('b', 'A change of time zone'), ('c', 'A collision course'), ('d', 'Fog')], 'c'),
        ('Two craft are closing at 10 km an hour and are 5 km apart. How long until they meet?',
         [('a', '5 hours'), ('b', '30 minutes'), ('c', '2 hours'), ('d', '15 minutes')], 'b'),
        ('Why is an early, steady intercept plan easier to correct?',
         [('a', 'The target never changes course'), ('b', 'It needs no sensors'), ('c', 'Fog stops all movement'), ('d', 'It avoids sharp turns and wasted fuel')], 'd'),
    ],
}
