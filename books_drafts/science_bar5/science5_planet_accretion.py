"""Accretion Models and N-body Simulations: how tiny solid bodies stuck together to build planets, and how computers follow the crowd of growing bodies."""
CODE = 'science5_planet_accretion'
BOOK = {
    "title": 'Accretion Models and N-body Simulations',
    "subtitle": 'Building planets one collision at a time',
    "chapters": [
        ('Planetesimals',
         'Planetesimals are the small solid bodies that formed early in a planetary disc. They grew from dust grains that stuck together. Each planetesimal is a building block of a planet.'),
        ('Planetesimal growth',
         'Small bodies grow by sticking together after gentle collisions. Growth is slow at first. The process builds larger and larger bodies over time.'),
        ('Runaway accretion',
         'A body that grows fastest also gathers material fastest. It then grows faster still. This feedback is called runaway accretion, and it can quickly create a few large bodies.'),
        ('N-body integration',
         'N-body integration calculates the gravitational motion of many bodies over time. Each body pulls on all the others. The computer steps forward in small time increments.'),
        ('Collision outcomes',
         'When two bodies collide, they can merge, bounce apart or break up. The outcome depends on their speeds and sizes. Models must include all these outcomes.'),
        ('Model validation',
         'Accretion models must match what we see in the Solar System and around other stars. Their predictions for planet sizes, orbits and timing are tested. Models that fail these tests are revised.'),
    ],
    "test": [
        ('What are planetesimals?',
         [('a', 'Small solid bodies that grew from dust and formed early in a disc'), ('b', 'Growth of trees'), ('c', 'Balloons getting bigger'), ('d', 'A type of rock')], 'a'),
        ('What is runaway accretion?',
         [('a', 'A race of cars'), ('b', 'A fire spreading in grass'), ('c', 'Bodies that grow fastest also gather material fastest, so they keep growing faster'), ('d', 'Planets shrinking over time')], 'c'),
        ('What does N-body integration do?',
         [('a', 'Measures the mass of paint'), ('b', 'Plays music'), ('c', 'Cooks food'), ('d', 'Calculates the gravitational motion of many bodies over time')], 'd'),
        ('What can happen when two bodies collide?',
         [('a', 'Bodies always vanish'), ('b', 'Bodies can merge, bounce apart or break up'), ('c', 'Bodies always turn into gas only'), ('d', 'Bodies never touch')], 'b'),
        ('Why must accretion models be validated?',
         [('a', 'Because planets are made of cheese'), ('b', 'So computers can stop'), ('c', 'Because models are always right'), ('d', 'Because predictions must match the observed Solar System and other planets')], 'd'),
    ],
}
