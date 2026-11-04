"""Matrix Exponentials for Motion: how the state of a moving craft is carried forward in time using matrices."""
CODE = 'navigation5_matrix_exponential'
BOOK = {
    "title": 'Matrix Exponentials for Motion',
    "subtitle": 'State equations, transition matrices, discretisation, attitude and numerics',
    "chapters": [
        ('The state of a craft',
         'The state of a craft is a list of numbers that describes it, such as position, velocity and attitude. A state equation says how the state changes over time. Engineers use this idea to predict where a craft will be.'),
        ('Transition matrices',
         'For a linear system, a transition matrix carries the state forward by a set amount of time. The matrix is found from the system equations. Multiplying the current state by it gives the next state.'),
        ('Matrix exponentials',
         'The transition matrix for continuous motion is the matrix exponential of the system matrix times the time. It is written as a series, and it can be computed in several reliable ways.'),
        ('Discretisation',
         'A computer works in steps, not in continuous time. Discretisation turns the continuous model into a step model. The step size must be small enough that the answers stay accurate.'),
        ('Attitude',
         'Attitude describes the orientation of a craft. It can be carried forward with matrix methods, though the attitude is a rotation and must stay a valid rotation after each step. Small numerical errors can slowly break that rule.'),
        ('Numerics and uses',
         'Matrix exponentials are used in navigation filters, control systems and simulations. Good software checks that the matrix stays well behaved and tests the results against known cases.'),
    ],
    "test": [
        ('What does a state describe for a craft?',
         [('a', 'Its colour and paint'), ('b', 'Its name only'), ('c', 'Its position, velocity and attitude as a list of numbers'), ('d', 'Its fuel price')], 'c'),
        ('What does a transition matrix do?',
         [('a', 'It erases the state'), ('b', 'It carries the state forward in time'), ('c', 'It draws a map'), ('d', 'It counts the crew')], 'b'),
        ('How is the transition matrix for continuous motion found?',
         [('a', 'By adding the time to the matrix'), ('b', 'By guessing it'), ('c', 'By reading the weather'), ('d', 'As the matrix exponential of the system matrix times the time')], 'd'),
        ('What does discretisation do?',
         [('a', 'Turns a continuous model into a step model a computer can run'), ('b', 'Removes the time from the model'), ('c', 'Makes the model into a picture'), ('d', 'Stops the craft')], 'a'),
        ('Why must an attitude stay a valid rotation after each step?',
         [('a', 'Because rotations must be painted'), ('b', 'Because a broken rotation gives a wrong orientation'), ('c', 'Because it is always heavier'), ('d', 'Because it has no effect')], 'b'),
    ],
}
