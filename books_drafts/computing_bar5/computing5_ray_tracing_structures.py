"""Ray Tracing Acceleration Structures: the nested boxes that let a computer find what a ray hits without testing every triangle."""
CODE = 'computing5_ray_tracing_structures'
BOOK = {
    "title": 'Ray Tracing Acceleration Structures',
    "subtitle": "Nested boxes that make finding a ray's target fast",
    "chapters": [
        ('Why structures are needed',
         'A scene can hold millions of triangles, and testing a ray against each one would be far too slow. Acceleration structures organise the geometry so most of it can be skipped. The ray only checks the parts it could possibly hit.'),
        ('Bounding volume hierarchies',
         'A bounding volume hierarchy wraps groups of objects in simple boxes, and groups those boxes in larger boxes. The result is a tree of nested boxes. A ray that misses a box skips everything inside it.'),
        ('Ray-box tests',
         'The core test checks whether a ray passes through a box. These tests are cheap and run many times for every ray. Their speed is why a well-built tree is worth the effort.'),
        ('Build cost',
         'Building the hierarchy takes time, and better trees are usually slower to build. Scenes that change every frame need faster builds or partial updates. Designers balance build time against how quickly rays can be traced.'),
        ('Hardware and denoising',
         'Modern GPUs include dedicated units that speed up ray-box and ray-triangle tests. Fewer rays per pixel still produce noise, so denoising is used to clean up the picture. Hardware and denoising work together.'),
        ('Dynamic scenes',
         'When objects move, the hierarchy must be updated or rebuilt. Refitting the existing boxes is quick but gradually loses quality. Full rebuilds are slower but keep the tree tidy.'),
    ],
    "test": [
        ('Why are acceleration structures used?',
         [('a', 'To make the scene colourless'), ('b', "To store the user's password"), ('c', 'To skip most of the geometry a ray could not hit'), ('d', 'To print the scene on paper')], 'c'),
        ('What is a bounding volume hierarchy?',
         [('a', 'Nested boxes that group objects in a tree'), ('b', 'A list of the lights in a room'), ('c', 'A type of spreadsheet'), ('d', 'A video game controller')], 'a'),
        ('What happens when a ray misses a box in the tree?',
         [('a', 'The ray must test every triangle'), ('b', 'The program stops'), ('c', 'The screen turns black'), ('d', 'Everything inside that box can be skipped')], 'd'),
        ('What is the trade-off with building a better tree?',
         [('a', 'It makes rays disappear'), ('b', 'It is usually slower to build'), ('c', 'It uses no memory'), ('d', 'It removes all shadows')], 'b'),
        ('Why do moving objects make the structure harder to keep up to date?',
         [('a', 'Moving objects cannot be drawn'), ('b', 'Motion removes the need for rays'), ('c', 'The boxes must be refitted or rebuilt each time things move'), ('d', 'Objects that move are always invisible')], 'c'),
    ],
}
