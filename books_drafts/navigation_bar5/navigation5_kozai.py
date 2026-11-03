"""The Kozai-Lidov Mechanism: how a distant third body makes an orbit's shape and tilt rise and fall in cycles."""
CODE = 'navigation5_kozai'
BOOK = {
    "title": 'The Kozai-Lidov Mechanism',
    "subtitle": 'Eccentricity cycles, third bodies, inclination change, stability, examples and effects on satellites',
    "chapters": [
        ('Eccentricity cycles',
         'Eccentricity measures how stretched an orbit is. Under the right conditions, a distant body makes the eccentricity rise and fall in slow cycles. The orbit becomes more oval, then rounder, again and again.'),
        ('Third bodies',
         'The mechanism needs a third body, a distant star or planet that perturbs a two-body orbit. Its pull is steady but tilted, and that tilt drives the cycles. The third body does not have to be close.'),
        ('Inclination change',
         'As the eccentricity changes, the tilt of the orbit can change too. Eccentricity and inclination trade energy back and forth in a cycle. This can carry an orbit through large changes.'),
        ('Stability',
         'Strong cycles can make an orbit unstable. A high eccentricity can bring a body close enough to collide or to re-enter. Stability depends on the starting tilt and the distances involved.'),
        ('Examples',
         'The mechanism is thought to shape some orbits of distant bodies and some close binary pairs. It helps explain orbits that would otherwise be hard to account for. Models are checked against observations.'),
        ('Effects on satellites',
         'Satellites can feel these cycles from the Moon and the Sun. Over time, the orbit may grow more eccentric or change its tilt. Mission designers watch for this when planning long lives.'),
    ],
    "test": [
        ('What is the Kozai-Lidov mechanism?',
         [('a', 'Eccentricity and inclination exchanging over cycles because of a distant third body'), ('b', 'A dance'), ('c', 'A bank'), ('d', 'A recipe')], 'a'),
        ('What is a third body?',
         [('a', 'A bodyguard'), ('b', 'A fourth tree'), ('c', 'A distant body that perturbs a two-body orbit'), ('d', 'A photograph')], 'c'),
        ('What is inclination change?',
         [('a', 'Changing the paint'), ('b', 'The tilt of the orbit plane changing over time'), ('c', 'A speed bump'), ('d', 'A shop')], 'b'),
        ('Why does stability matter here?',
         [('a', 'For food'), ('b', 'For music'), ('c', 'For maps'), ('d', 'Because strong cycles can make orbits unstable, such as a collision or re-entry')], 'd'),
        ('What is an effect on a satellite?',
         [('a', 'Its colour'), ('b', 'Its paint'), ('c', 'Its noise'), ('d', 'Changes in eccentricity that can affect altitude and lifetime')], 'd'),
    ],
}
