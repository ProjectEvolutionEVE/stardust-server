"""Phase Transitions and Critical Phenomena: order parameters, critical exponents, universality, scaling laws, the Ising model and renormalisation ideas."""
CODE = 'science5_phys_critical'
BOOK = {
    "title": 'Phase Transitions and Critical Phenomena',
    "subtitle": 'How matter changes state, and why very different systems behave alike at the edge',
    "chapters": [
        ('Changes of state',
         'Water boils, ice melts and magnets lose their pull when heated. Each of these is a phase transition, a sudden change in the overall form of a material. Physicists describe the change with a few key quantities that stay sharp at the transition point.'),
        ('Order parameters',
         'An order parameter measures how ordered a system is. In a magnet it is the average alignment of the tiny spins. It is zero above the transition temperature and grows as the system cools below it.'),
        ('Critical exponents',
         'Near the critical point, many quantities follow simple power laws, with exponents that describe how fast they change. These exponents tell us how the system behaves right at the edge of the transition.'),
        ('Universality',
         'Very different systems, such as a magnet and a fluid near its critical point, share the same exponents. This is called universality. It means the details of the material matter less than the basic symmetry and dimension of the problem.'),
        ('The Ising model',
         'The Ising model is a simple grid of spins that can point up or down, with neighbours favouring the same direction. It captures a phase transition with only a few rules. Solving it in two dimensions was a landmark achievement.'),
        ('Renormalisation ideas',
         'The renormalisation group studies how a system looks when examined at larger and larger scales. Ideas from it explain why exponents are shared across systems. Kenneth Wilson used these ideas and received the Nobel Prize in Physics in 1982.'),
    ],
    "test": [
        ('What is a phase transition?',
         [('a', 'A change of colour in paint'), ('b', 'A change in the size of a room'), ('c', 'A ripple on a pond'), ('d', 'A sudden change in the overall form of a material')], 'd'),
        ('What does an order parameter measure?',
         [('a', 'How long a train is'), ('b', 'How loud a crowd is'), ('c', 'How ordered a system is'), ('d', 'How hot a kitchen is')], 'c'),
        ('What is universality?',
         [('a', 'Very different systems sharing the same critical exponents'), ('b', 'All materials being exactly the same'), ('c', 'A rule that every metal is magnetic'), ('d', 'Every system having the same mass')], 'a'),
        ('What is the Ising model?',
         [('a', 'A type of engine'), ('b', 'A map of rivers'), ('c', 'A grid of spins that can point up or down, with neighbours favouring alignment'), ('d', 'A recipe for bread')], 'c'),
        ('What does the renormalisation group study?',
         [('a', 'How a system looks when examined at larger and larger scales'), ('b', 'How to paint a house'), ('c', 'How to tune a piano'), ('d', 'How to count coins')], 'a'),
    ],
}
