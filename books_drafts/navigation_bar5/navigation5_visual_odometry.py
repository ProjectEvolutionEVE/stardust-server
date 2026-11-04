"""Visual Odometry: working out how far a camera has moved by watching how the scene shifts."""
CODE = 'navigation5_visual_odometry'
BOOK = {
    "title": 'Visual Odometry',
    "subtitle": 'Feature tracking, frame-to-frame motion, the scale problem, drift, stereo and drones',
    "chapters": [
        ('Feature tracking',
         'Visual odometry picks out distinctive points in an image, such as corners and textured spots. It then follows those same points from one frame to the next. The pattern of their movement reveals how the camera moved.'),
        ('Frame-to-frame motion',
         'From matched points in two frames, the computer works out the camera\'s rotation and direction of travel. Repeating this frame after frame builds up the path. Each step is small, so each step is quick to compute.'),
        ('The scale problem',
         'A single camera cannot tell how large the motion is in metres from the images alone. Moving a little close to the scene looks the same as moving a lot far away. Some other source of scale is needed.'),
        ('Drift',
         'Small errors in each step add up over time. After a long trip, the estimated path can be well away from the true one. Checking against landmarks or other sensors limits the drift.'),
        ('Stereo',
         'Two cameras with a known gap between them give depth and scale directly. The gap is called the baseline. The images from the two cameras are compared to measure distance.'),
        ('Drones',
         'Drones often use visual odometry where GPS is weak, such as under bridges or indoors. The camera and a small computer are light enough to fly. The method works best when the scene has plenty of texture.'),
    ],
    "test": [
        ('What is visual odometry?',
         [('a', 'Reading a speed sign'), ('b', 'Counting wheels'), ('c', 'Camera paint'), ('d', 'Estimating motion from the changes in a camera\'s images')], 'd'),
        ('What is feature tracking?',
         [('a', 'Recording sound'), ('b', 'Painting features'), ('c', 'Following the same points from one frame to the next'), ('d', 'Printing images')], 'c'),
        ('What is the scale problem for a single camera?',
         [('a', 'A single camera cannot tell how large the motion is in metres from images alone'), ('b', 'The camera is too large'), ('c', 'The screen is too small'), ('d', 'The lens is blue')], 'a'),
        ('How does a stereo pair help?',
         [('a', 'By removing light'), ('b', 'By using two views with a known gap to measure distance and scale'), ('c', 'By stopping movement'), ('d', 'By changing colours')], 'b'),
        ('Why does drift matter in visual odometry?',
         [('a', 'It makes images brighter'), ('b', 'It speeds the drone up'), ('c', 'It keeps the map fixed'), ('d', 'Small errors add up over time')], 'd'),
    ],
}
