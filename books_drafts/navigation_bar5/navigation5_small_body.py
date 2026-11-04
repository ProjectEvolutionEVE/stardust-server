"""Small-Body Shape Models: shapes from radar and lidar, the spin state, gravity fields, uncertainty, mission use and the models themselves."""
CODE = 'navigation5_small_body'
BOOK = {
    "title": 'Small-Body Shape Models',
    "subtitle": 'How scientists work out the shape of an asteroid or comet they cannot easily see up close',
    "chapters": [
        ('Shapes from radar',
         'Radar sent at a small body bounces back, and the timing and frequency shift of the echo reveal its shape and spin. Radar works even when light is poor, which makes it very useful for small bodies.'),
        ('Shapes from lidar',
         'A spacecraft can fire laser pulses at the surface to measure distances. Those distances build a detailed height map. Lidar gives very fine detail when the spacecraft is close.'),
        ('The spin state',
         'The spin state of a body, including its rotation period and the tilt of its axis, is often found by watching how its brightness changes over time, or by timing radar echoes. Some small bodies tumble in complicated ways.'),
        ('Gravity fields',
         'Shape and mass decide the gravity around a body. For a lumpy body the gravity field is irregular, so a spacecraft must model it carefully in order to orbit safely.'),
        ('Uncertainty',
         'No shape model is perfect. Each model comes with an estimate of its error, and mission planners must include that error in their plans.'),
        ('Mission use and models',
         'Shape models help plan orbits, choose landing sites and time sample collection. The models are shared between research teams so that everyone works from the same version.'),
    ],
    "test": [
        ('What can radar echoes reveal about an asteroid?',
         [('a', 'Its favourite food'), ('b', 'Its colour only'), ('c', 'The temperature of its water'), ('d', 'Its shape and spin, from the timing and frequency shift of the echo')], 'd'),
        ('What is lidar used for in shape work?',
         [('a', 'Sending radio music'), ('b', 'Measuring distances to the surface to build a height map'), ('c', 'Heating the surface'), ('d', 'Counting craters by hand from Earth')], 'b'),
        ('How is the spin of a small body often found?',
         [('a', 'By watching how its brightness changes over time'), ('b', 'By tasting the dust'), ('c', 'By weighing the body on a scale'), ('d', 'By listening for sound in space')], 'a'),
        ('Why does an irregular body give an irregular gravity field?',
         [('a', 'It has no mass'), ('b', 'Its gravity is always even'), ('c', 'Its shape and mass make the gravity field uneven'), ('d', 'It pushes spacecraft away')], 'c'),
        ('Why does a shape model carry an error estimate?',
         [('a', 'Because no model is perfect, and planners must allow for the error'), ('b', 'To decorate the model'), ('c', 'To count the stars behind it'), ('d', 'Because models are always right')], 'a'),
    ],
}
