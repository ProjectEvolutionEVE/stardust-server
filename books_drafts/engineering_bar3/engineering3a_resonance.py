"""Resonance and Damping: when a push arrives in time with a structure, and how to calm it."""
CODE = 'engineering3a_resonance'
BOOK = {
    "title": 'Resonance and Damping',
    "subtitle": 'When a push arrives at the right rhythm, and how to calm it down',
    "chapters": [
        ('Pushing in time',
         'Resonance happens when an outside push repeats at the same rate as a system\'s natural frequency. Each small push then adds to the last, so the swing grows. Anyone who has pushed a playground swing knows the trick: push in time and it goes higher.'),
        ('A bridge that swayed',
         'The Millennium Bridge in London opened in 2000 and began to sway sideways when crowds walked across it. Pedestrians unconsciously matched their steps to the sway, and the push grew. The bridge was closed within days, and dampers were fitted before it reopened in 2002.'),
        ('Damping takes the energy out',
         'Damping is anything that turns the energy of a motion into heat or sound. Friction, the oil in a shock absorber and rubber mounts all damp vibration. Damping limits how high a resonant swing can grow, though it never removes resonance entirely.'),
        ('Three ways to deal with resonance',
         'The first is to move the natural frequency away from the rate of the push, by changing the stiffness or the mass. The second is to reduce or remove the push itself. The third is to add damping, so that any build-up is held down.'),
        ('Tuned mass dampers',
         'A tuned mass damper is an extra weight on a spring, set to the natural frequency of the structure. When the structure sways, the extra weight swings against it and takes energy out. Tall buildings and long bridges sometimes use them.'),
        ('Find it before it finds you',
         'Test a structure or a machine across its full range of speeds, and watch for a speed where the shaking suddenly grows. A rotating shaft that shakes hard at one speed may be running near a critical speed. Note that speed on the drawing, and design to stay well clear of it.'),
    ],
    "test": [
        ('When does resonance occur?',
         [('a', 'When an outside push repeats at a system\'s natural frequency'), ('b', 'When a part is painted'), ('c', 'When a part is cooled to zero'), ('d', 'When a bolt is removed')], 'a'),
        ('Why did the Millennium Bridge begin to sway?',
         [('a', 'Crowds stepped in time with the sway, and the push grew'), ('b', 'The bridge was built of wood'), ('c', 'The river rose under it'), ('d', 'The bridge was painted green')], 'a'),
        ('What does damping do?',
         [('a', 'It turns the energy of a motion into heat or sound'), ('b', 'It adds energy to a swing'), ('c', 'It makes a part heavier'), ('d', 'It changes the colour of a part')], 'a'),
        ('Which of these is NOT a good way to deal with resonance?',
         [('a', 'Moving the natural frequency away from the push'), ('b', 'Reducing or removing the push'), ('c', 'Making the push stronger on purpose'), ('d', 'Adding damping')], 'c'),
        ('What is a tuned mass damper?',
         [('a', 'A paint used on bridges'), ('b', 'A weight on a spring, set to the structure\'s natural frequency'), ('c', 'A kind of rubber glove'), ('d', 'A fuel tank')], 'b'),
    ],
}
