"""Symplectic Integrators: computing long orbits without the energy slowly wandering off."""
CODE = 'navigation5_symplectic'
BOOK = {
    "title": 'Symplectic Integrators',
    "subtitle": 'Energy drift, structure preservation, leapfrog, long-term accuracy, step size and orbit propagation',
    "chapters": [
        ('Energy drift',
         'When a computer steps an orbit forward, small errors can make the calculated energy creep away from its true value. This energy drift is not real physics. It makes long simulations untrustworthy.'),
        ('Structure preservation',
         'A symplectic integrator keeps the underlying structure of orbital motion. The energy error stays bounded instead of growing steadily. This matters most over many orbits.'),
        ('Leapfrog',
         'The leapfrog method is a simple symplectic step. It alternates updates of position and velocity, like taking turns. It is easy to program and fast to run.'),
        ('Long-term accuracy',
         'Over thousands of orbits, a symplectic method can stay close to the true path. A standard method may drift far from it. The difference can decide whether a long study is useful.'),
        ('Step size',
         'The step size is the time between calculated steps. Smaller steps are more accurate but cost more computing time. The right size balances accuracy and speed.'),
        ('Orbit propagation',
         'Propagation means carrying an orbit forward in time. Symplectic methods are a common choice for long propagations. They are used in mission planning and in research on orbital stability.'),
    ],
    "test": [
        ('What is energy drift?',
         [('a', 'A gift'), ('b', 'A lost ship'), ('c', 'A steady increase in the speed of light'), ('d', 'A slow change in a simulated system\'s energy that is not real physics')], 'd'),
        ('What is a symplectic integrator?',
         [('a', 'A numerical method that keeps the structure of orbital motion, so energy errors stay bounded'), ('b', 'A bird'), ('c', 'A sport'), ('d', 'A dance')], 'a'),
        ('What is the leapfrog method?',
         [('a', 'A jump game'), ('b', 'A dog\'s trick'), ('c', 'A simple symplectic step that alternates updates of position and velocity'), ('d', 'A dance step on a ship')], 'c'),
        ('What does step size control?',
         [('a', 'The colour'), ('b', 'The paint'), ('c', 'The time between calculated steps, and so the accuracy'), ('d', 'The number of stars')], 'c'),
        ('Why are symplectic methods used for long orbit propagation?',
         [('a', 'They are slow'), ('b', 'They keep errors from growing too fast over many orbits'), ('c', 'They stop orbits'), ('d', 'They are rarely accurate')], 'b'),
    ],
}
