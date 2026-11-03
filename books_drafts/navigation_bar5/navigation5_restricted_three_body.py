"""The Restricted Three-Body Problem: a simpler model of three bodies that explains many real spacecraft paths."""
CODE = 'navigation5_restricted_three_body'
BOOK = {
    "title": 'The Restricted Three-Body Problem',
    "subtitle": 'The reduced problem, the Jacobi integral, zero-velocity curves, equilibrium points, stability and design',
    "chapters": [
        ('The reduced problem',
         'The restricted three-body problem looks at two large bodies that circle each other. A third body has so little mass that it does not disturb them. This simpler model still captures much of the real motion.'),
        ('The Jacobi integral',
         'The Jacobi integral is a quantity that stays constant along an ideal path, when the problem is viewed in a rotating frame. It acts like an energy check. It limits where a spacecraft with a given value can go.'),
        ('Zero-velocity curves',
         'Zero-velocity curves are boundaries in the rotating frame. A body with a given energy cannot cross them unless its speed is zero there. They show which regions are open and which are closed to the body.'),
        ('Equilibrium points',
         'There are five equilibrium points in the rotating frame. At these points the pulls and the rotation balance. They are the places where a body could in principle stay still.'),
        ('Stability',
         'Some equilibrium points are stable, so small nudges die away. Others are unstable, so small nudges grow. Knowing which is which guides where to park and where to avoid.'),
        ('Design',
         'Mission designers use this model to find low-cost paths and good parking spots. It guides the search for natural routes between the bodies. Detailed designs then add the missing forces.'),
    ],
    "test": [
        ('What is the restricted three-body problem?',
         [('a', 'Three bodies in a bag'), ('b', 'A simplified version with one body of negligible mass'), ('c', 'A game of cards'), ('d', 'A type of tax')], 'b'),
        ('What is the Jacobi integral?',
         [('a', 'A cheap bill'), ('b', 'A formula for a song'), ('c', 'A quantity that stays constant along an ideal trajectory in the rotating frame'), ('d', 'A map of rivers')], 'c'),
        ('What are zero-velocity curves?',
         [('a', 'Curves in roads'), ('b', 'Curves in music'), ('c', 'Hills'), ('d', 'Boundaries that a body with a given energy cannot cross unless its speed is zero')], 'd'),
        ('How many equilibrium points are there in the rotating frame?',
         [('a', 'Five'), ('b', 'Two'), ('c', 'Ten'), ('d', 'None')], 'a'),
        ('What do equilibrium points tell us about stability?',
         [('a', 'Nothing'), ('b', 'That bodies always fall'), ('c', 'Some are stable and others are unstable'), ('d', 'That all are safe')], 'c'),
    ],
}
