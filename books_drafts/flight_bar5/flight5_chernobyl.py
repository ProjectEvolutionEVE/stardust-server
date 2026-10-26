"""Case Study: Chernobyl. A safety test, design flaws, operators' choices, the blast, the response and the lessons."""
CODE = 'flight5_chernobyl'
BOOK = {
    "title": 'Case Study: Chernobyl',
    "subtitle": 'A reactor test, a design problem and the choices that made it worse',
    "chapters": [
        ('A safety test',
         'In April 1986 the operators of Reactor 4 at Chernobyl, in Ukraine, were running a test. The test was meant to see whether the turbines could keep power going during a power cut. It was carried out at a low power level, which the design had not been built to handle safely.'),
        ('Design flaws',
         'The reactor had design flaws that were not widely understood. Its control rods had tips that could add heat before they absorbed it, and it could become less stable as steam built up. These features made a sudden surge in power more dangerous than it should have been.'),
        ("Operators' choices",
         'The operators broke several rules during the test. They removed many control rods, and they switched off some safety systems to keep the test going. The reactor was pushed into a state where it was hard to control.'),
        ('The blast',
         'On 26 April 1986 the power surged in seconds. A steam explosion blew the top off the reactor, and a fire followed. The reactor was left open to the air and released radioactive material.'),
        ('The response',
         'Firefighters and workers went into the damaged plant without full knowledge of the danger. A large area was evacuated, and the town of Pripyat was emptied. A huge effort was then made to cover the reactor and limit the damage.'),
        ('Lessons',
         'The disaster taught the world that safety depends on design, on training and on a culture in which rules are respected. Operators must understand the limits of their machines. For players, the lesson is that a test is only safe when its limits are known and its safety systems stay on.'),
    ],
    "test": [
        ('In what year did the Chernobyl accident happen?',
         [('a', '1956'), ('b', '1999'), ('c', '2011'), ('d', '1986')], 'd'),
        ('What was the operators doing when the accident began?',
         [('a', 'A safety test on Reactor 4'), ('b', 'Opening a new town'), ('c', 'Launching a satellite'), ('d', 'Painting the plant')], 'a'),
        ('What did the operators do that made the reactor harder to control?',
         [('a', 'They added more fuel to the sea'), ('b', 'They removed many control rods and switched off safety systems'), ('c', 'They turned off all lights'), ('d', 'They left the plant unattended')], 'b'),
        ('What was the town evacuated after the blast?',
         [('a', 'Kitty Hawk'), ('b', 'Dayton'), ('c', 'Pripyat'), ('d', 'Tenerife')], 'c'),
        ('What does the book name as a key lesson of Chernobyl?',
         [('a', 'Reactors are safe if no one looks at them'), ('b', 'Tests should always be run at full power only'), ('c', 'Safety systems are never needed'), ('d', 'Safety depends on design, training and respect for rules')], 'd'),
    ],
}
