"""Designing a Planetary Flyby: approach geometry, the target, closest approach, gravity bending, image timing and risks."""
CODE = 'navigation5_flyby_design'
BOOK = {
    "title": 'Designing a Planetary Flyby',
    "subtitle": 'Aiming a spacecraft past a world at high speed, and catching the best pictures',
    "chapters": [
        ('The approach',
         'A flyby begins with a long approach. The path of the spacecraft is aimed so that it passes the target at a chosen distance and from a chosen direction.'),
        ('The target',
         'The target might be a planet, a moon or an asteroid. Its position must be known precisely, because the aim depends on where the target will be at closest approach.'),
        ('Closest approach',
         'At the closest point the craft is nearest the target, and it sees the most detail. Timing and distance at this moment are critical to the mission success.'),
        ('Gravity bending',
         'The gravity of the target bends the path of the spacecraft. Engineers use this bending to change speed and direction, which is the basis of gravity assists.'),
        ('Image timing',
         'Cameras must take pictures at exactly the right moments, because the craft is moving very fast. Pictures are timed to catch the surface at the best angle and in good light.'),
        ('Risks',
         'Dust, radiation and small errors in aim can all cause trouble during a flyby. Teams plan safe distances and backup plans in case something goes wrong.'),
    ],
    "test": [
        ('What does the approach set?',
         [('a', 'The aim, so the craft passes the target at a chosen distance and direction'), ('b', 'The colour of the spacecraft'), ('c', 'The type of fuel to use'), ('d', 'The paint on the craft')], 'a'),
        ('Why must the target position be known well?',
         [('a', 'To feed the scientists'), ('b', 'Because the aim depends on where the target will be at closest approach'), ('c', 'Because the target always moves backward'), ('d', 'To choose its name')], 'b'),
        ('What happens at closest approach?',
         [('a', 'The craft lands on the target'), ('b', 'The craft stops moving'), ('c', 'The craft is nearest the target and sees the most detail'), ('d', 'The craft turns off its cameras')], 'c'),
        ('What is gravity bending used for?',
         [('a', 'Making noise'), ('b', 'Painting the craft'), ('c', 'Cooling the craft'), ('d', 'Changing speed and direction, as in gravity assists')], 'd'),
        ('What must image timing manage?',
         [('a', 'The colour of the sky'), ('b', 'Catching the surface at the best moment and angle'), ('c', 'The weight of the rocks'), ('d', 'The sound of the wind')], 'b'),
    ],
}
