"""Physics Simulation and Integrators: turning forces into motion step by step, and keeping that motion stable and repeatable."""
CODE = 'computing5_physics_integrators'
BOOK = {
    "title": 'Physics Simulation and Integrators',
    "subtitle": 'From forces to motion, one small time step at a time',
    "chapters": [
        ('Forces to motion',
         "A physics engine applies forces to objects and works out how they move. Newton's laws give the basic relation between force, mass and acceleration. The engine repeats this calculation for every object at every time step."),
        ('Euler integration',
         'Euler integration updates position and velocity using the current rate of change. It is simple and fast. Over large or stiff steps it can drift away from the correct motion.'),
        ('Verlet integration',
         'Verlet integration updates position from the previous two positions and the forces acting on the object. It handles many simulations, such as cloth and ropes, with good stability. It does not store velocity directly.'),
        ('Stability and time steps',
         'A simulation that takes steps too large can explode, with objects shooting off. Smaller steps are more accurate but cost more time. Engines often use a fixed time step to keep the results steady.'),
        ('Constraint solving',
         'Constraints keep objects connected, such as a hinge or a rope of fixed length. The solver adjusts positions and forces to satisfy every constraint. More constraints make the solver work harder.'),
        ('Determinism',
         'A deterministic simulation gives the same result from the same starting state and inputs. Determinism matters for replays and for networked games. Floating-point rounding and changing the order of operations can break it.'),
    ],
    "test": [
        ('What does an integrator do in a physics engine?',
         [('a', 'It prints the scene'), ('b', 'It plays the music'), ('c', "It stores the player's name"), ('d', 'It moves objects forward in time from their forces')], 'd'),
        ('What is a known weakness of simple Euler integration?',
         [('a', 'It cannot run on any computer'), ('b', 'It can drift away from the correct motion over large steps'), ('c', 'It removes all forces'), ('d', 'It only works in black and white')], 'b'),
        ('What does a time step that is too large risk?',
         [('a', 'A brighter screen'), ('b', 'A smaller file size'), ('c', 'The simulation becoming unstable and objects flying apart'), ('d', 'A quieter sound')], 'c'),
        ('What does a constraint do?',
         [('a', 'Keeps objects connected, such as a hinge or rope'), ('b', 'Makes objects invisible'), ('c', 'Doubles the mass of every object'), ('d', 'Changes the colour of the sky')], 'a'),
        ('What is determinism in a simulation?',
         [('a', 'The simulation always chooses a random result'), ('b', 'The same starting state and inputs give the same result'), ('c', 'The simulation can only run once'), ('d', 'The simulation has no forces')], 'b'),
    ],
}
