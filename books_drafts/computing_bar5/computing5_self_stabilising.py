"""Self-Stabilising Systems: systems that recover to correct behaviour from any starting state."""
CODE = 'computing5_self_stabilising'
BOOK = {
    "title": 'Self-Stabilising Systems',
    "subtitle": 'Systems that recover to correct behaviour from any starting state',
    "chapters": [
        ('Recovering from any state', 'A self-stabilising system returns to correct behaviour from any starting state, even after faults have scrambled its memory. It does not need a person to reset it. Edsger Dijkstra introduced the idea in 1974.'),
        ('Legitimate states', 'A legitimate state is one where the system behaves as specified. The system may start in an illegitimate state, but it must always move towards a legitimate one, and once there it must stay there. These two promises define the design.'),
        ("Dijkstra's token ring", "In Dijkstra's token ring, the machines sit in a circle, and each holds a number. Simple local rules let the numbers settle until exactly one machine holds the token. It is a classic example of a system that heals itself."),
        ('Convergence proofs', 'To prove a self-stabilising system works, one shows that from any start it reaches a legitimate state in a finite number of steps. The proof often counts a quantity that always goes down, so it must eventually reach its lowest value.'),
        ('Transient faults', 'A transient fault is a short upset, such as a memory bit flipped by radiation. A self-stabilising system treats any such upset as a new starting point and corrects itself without a restart. This is valuable in space and other harsh places.'),
        ('Use cases', 'Self-stabilising ideas are used in networks that must heal after failures, such as routing and clock synchronisation, and in systems that are hard to reach. The cost is that the system may take time to recover, and the design must be carefully proved.'),
    ],
    "test": [
        ('Who introduced self-stabilisation in 1974?',
         [('a', 'Edsger Dijkstra'), ('b', 'Ada Lovelace'), ('c', 'Alan Turing'), ('d', 'Grace Hopper')], 'a'),
        ('What is a legitimate state?',
         [('a', 'A state with no data'), ('b', 'A state where it is raining'), ('c', 'A state with no machines'), ('d', 'One where the system behaves as specified')], 'd'),
        ('What must a convergence proof show?',
         [('a', 'The system never changes'), ('b', 'Machines are all identical'), ('c', 'Reaching a legitimate state in a finite number of steps from any start'), ('d', 'The screen stays on')], 'c'),
        ('What is a transient fault?',
         [('a', 'A short upset, such as a flipped memory bit'), ('b', 'A permanent crack in the building'), ('c', 'A slow printer'), ('d', 'A missing keyboard')], 'a'),
        ('What must a self-stabilising system do with any upset?',
         [('a', 'Restart the universe'), ('b', 'Treat it as a new starting point and correct itself'), ('c', 'Ignore it forever'), ('d', 'Print a report')], 'b'),
    ],
}
