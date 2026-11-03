"""Low-Energy Transfers and Invariant Manifolds: using natural paths in the Sun and Moon's gravity to save fuel."""
CODE = 'navigation5_low_energy'
BOOK = {
    "title": 'Low-Energy Transfers and Invariant Manifolds',
    "subtitle": 'Manifolds, transfer cost, time, Lagrange points and missions',
    "chapters": [
        ('Invariant manifolds',
         'An invariant manifold is a set of paths in a three-body system that flow toward or away from a point. Following these paths lets a spacecraft move with very little push. The paths are shaped by the gravity of the bodies together.'),
        ('Low-energy transfers',
         'A low-energy transfer is a route that uses little fuel by following these natural paths. The spacecraft coasts along the flow with only small corrections. The route is usually slower than a direct burn.'),
        ('Lagrange points',
         'Lagrange points are places in a rotating two-body system where the pulls balance. A spacecraft can stay near them with small effort. They are natural places for observatories and relays.'),
        ('Transfer cost',
         'The cost of a transfer is measured in fuel and in the speed change it needs. Low-energy routes cut the fuel needed for some trips. The savings are real, but they come with a price.'),
        ('Time',
         'The main trade-off is time. A low-energy transfer may take months where a direct route takes days. Mission planners weigh the fuel saved against the time lost.'),
        ('Missions',
         'Several missions have used low-energy routes to reach distant points. These flights show that small fuel budgets can still reach far targets. The method is now a standard tool for planners.'),
    ],
    "test": [
        ('What is an invariant manifold?',
         [('a', 'An empty room'), ('b', 'A painted wall'), ('c', 'A shelf'), ('d', 'A set of paths in the three-body system that flow toward or away from a point')], 'd'),
        ('What is a low-energy transfer?',
         [('a', 'A slow car'), ('b', 'A cheap taxi'), ('c', 'A route that uses little fuel by following natural paths'), ('d', 'A bank loan')], 'c'),
        ('What are Lagrange points?',
         [('a', 'Equilibrium points where the pulls balance in a rotating system'), ('b', 'Cities'), ('c', 'Lamps'), ('d', 'Tickets')], 'a'),
        ('What is the trade-off with low-energy transfers?',
         [('a', 'They are always fast'), ('b', 'They usually take longer'), ('c', 'They cannot be used'), ('d', 'They need no fuel')], 'b'),
        ('Why use these transfers?',
         [('a', 'To save paint'), ('b', 'To save fuel in exchange for more time'), ('c', 'To visit shops'), ('d', 'To avoid stars')], 'b'),
    ],
}
