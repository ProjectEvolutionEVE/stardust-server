"""Visual-Inertial Fusion: combining a camera with an inertial unit so each covers the other's weaknesses."""
CODE = 'navigation5_visual_inertial'
BOOK = {
    "title": 'Visual-Inertial Fusion',
    "subtitle": 'Camera and IMU, synchronisation, scale, initialisation, tuning and robustness',
    "chapters": [
        ('Camera and IMU',
         'An inertial measurement unit, or IMU, has accelerometers and gyroscopes that measure motion very often. A camera sees the scene but updates more slowly. Together they give a fuller picture of movement.'),
        ('Synchronisation',
         'The camera and IMU readings must be lined up in time. Even a small timing offset causes errors in the motion estimate. Careful synchronisation is a basic step.'),
        ('Scale',
         'The accelerometer measures real-world acceleration, which fixes the scale of the motion. A camera alone cannot do this. Fusing the two gives a path in true metres.'),
        ('Initialisation',
         'Before tracking begins, the system needs a first estimate of its motion, its sensor biases and the scene. A good start makes the rest of the estimate settle quickly. A poor start can lead to a wrong path.'),
        ('Tuning',
         'The noise levels of the camera and the IMU must be set. Wrong values make the filter trust one sensor too much. Tuning is usually done with recorded data and checked on new trips.'),
        ('Robustness',
         'The two sensors cover each other\'s weaknesses. The camera is good for direction and landmarks, while the IMU bridges short gaps. The combined system copes better than either one alone.'),
    ],
    "test": [
        ('What is an IMU?',
         [('a', 'A sporting event'), ('b', 'A kind of paper'), ('c', 'A type of engine'), ('d', 'A unit with accelerometers and gyroscopes that measure motion')], 'd'),
        ('Why is synchronisation needed?',
         [('a', 'So the screen is bright'), ('b', 'So the camera is cold'), ('c', 'So camera and IMU readings line up in time'), ('d', 'So the lens is clean')], 'c'),
        ('How does an IMU help with scale?',
         [('a', 'Its accelerometer gives real-world acceleration, which fixes the scale'), ('b', 'It changes the colour'), ('c', 'It stops the camera'), ('d', 'It is a clock')], 'a'),
        ('What is initialisation?',
         [('a', 'Turning the power off'), ('b', 'The first estimate of the state, such as motion and bias, before tracking starts'), ('c', 'Painting the case'), ('d', 'The final test')], 'b'),
        ('Why is visual-inertial fusion robust?',
         [('a', 'Because the camera is never used'), ('b', 'Because the IMU is never used'), ('c', 'Because the two sensors cover each other\'s weaknesses'), ('d', 'Because it uses no data')], 'c'),
    ],
}
