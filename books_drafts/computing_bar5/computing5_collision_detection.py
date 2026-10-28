"""Collision Detection and Broadphase: finding which objects might touch, cheaply, before checking exactly where they touch."""
CODE = 'computing5_collision_detection'
BOOK = {
    "title": 'Collision Detection and Broadphase',
    "subtitle": 'Quickly finding likely pairs, then checking them exactly',
    "chapters": [
        ('Two phases',
         'Collision detection usually runs in two phases. The broadphase quickly finds pairs of objects that might touch. The narrowphase then checks those pairs exactly.'),
        ('Sweep and prune',
         'Sweep and prune sorts objects along an axis by the start and end of their extent. Objects whose ranges overlap become candidate pairs. It works well when objects move little from frame to frame.'),
        ('Spatial hashing',
         'Spatial hashing divides space into a grid of cells and records which objects lie in each cell. Objects that share a cell are candidates. Cell size is a key choice: too large and many false pairs appear, too small and objects span many cells.'),
        ('Narrowphase tests',
         'The narrowphase tests the actual shapes, such as sphere against sphere or convex hull against convex hull. These tests are more costly than the broadphase. Running them only on candidate pairs keeps the frame fast.'),
        ('Continuous detection',
         'Objects moving very fast can pass through each other between two frames. Continuous detection tests the path of motion, not just the positions at the start and end. It is more expensive but prevents missed hits.'),
        ('Tunnelling and performance',
         'Tunnelling is the name for an object passing through a thin wall without being stopped. Smaller steps, continuous tests and thicker walls reduce it. Performance comes from keeping the candidate lists small.'),
    ],
    "test": [
        ('What does the broadphase do?',
         [('a', 'Paints the walls'), ('b', 'Plays the sound effects'), ('c', 'Quickly finds pairs of objects that might touch'), ('d', "Stores the player's score")], 'c'),
        ('How does sweep and prune find candidate pairs?',
         [('a', 'By sorting along an axis and finding overlapping ranges'), ('b', 'By counting the words in a file'), ('c', 'By drawing a circle around each light'), ('d', 'By asking the user to guess')], 'a'),
        ('What is the main choice in spatial hashing?',
         [('a', 'The colour of the floor'), ('b', 'The number of keyboard keys'), ('c', 'The name of the engine'), ('d', 'The size of the grid cells')], 'd'),
        ('What is tunnelling?',
         [('a', 'A train under a river'), ('b', 'An object passing through a thin wall without being stopped'), ('c', 'A type of texture'), ('d', 'A way to save a file')], 'b'),
        ('What does continuous detection test?',
         [('a', 'The number of pixels in a sprite'), ('b', 'The volume of the music'), ('c', 'The path of motion between frames'), ('d', 'The age of the player')], 'c'),
    ],
}
