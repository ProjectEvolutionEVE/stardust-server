"""Level of Detail: showing simpler versions of distant objects, so a busy scene stays fast without looking wrong."""
CODE = 'computing5_level_of_detail'
BOOK = {
    "title": 'Level of Detail',
    "subtitle": 'Simpler versions for distant objects, chosen by how big they look',
    "chapters": [
        ('Why LOD exists',
         'Far-away objects cover only a few pixels, so their fine detail is wasted. Level of detail swaps in simpler versions as objects get farther away. The scene can then hold far more objects at the same speed.'),
        ('Mesh decimation',
         'Decimation removes triangles from a mesh while keeping its overall shape. Artists or tools produce several versions, each with fewer triangles. The simplest version is used when the object is smallest on screen.'),
        ('Impostors',
         'An impostor replaces a distant object with a flat image that always faces the camera. It costs very little to draw. Impostors look best from a distance and are noticed up close.'),
        ('Popping and blending',
         'Switching between versions can cause a visible jump, called popping. Smoother transitions blend or dither between two levels over a short distance. Good blending hides the change from the viewer.'),
        ('Streaming',
         'Large worlds cannot keep every detail in memory at once. Streaming loads the detail a player is likely to need and unloads the rest. Good prediction of movement avoids pauses while data arrives.'),
        ('Screen-space error',
         'Screen-space error measures how many pixels a simplification would change on screen. A level is chosen so this error stays below a set limit. This ties the choice to what the player can actually see.'),
    ],
    "test": [
        ('Why is detail wasted on distant objects?',
         [('a', 'They are always invisible'), ('b', 'They are made of water'), ('c', 'They cover only a few pixels on screen'), ('d', 'They are printed on paper')], 'c'),
        ('What does mesh decimation remove?',
         [('a', 'Triangles, while keeping the overall shape'), ('b', "The player's name"), ('c', 'The sound effects'), ('d', 'The camera')], 'a'),
        ('What is an impostor?',
         [('a', 'A real player in the scene'), ('b', 'A type of battery'), ('c', 'A map of the sea'), ('d', 'A flat image that always faces the camera')], 'd'),
        ('What is popping?',
         [('a', 'A sound made by a bubble'), ('b', 'A visible jump when switching between detail levels'), ('c', 'A game crash on start-up'), ('d', 'A type of texture')], 'b'),
        ('What does screen-space error measure?',
         [('a', 'The weight of the disk'), ('b', 'The number of users online'), ('c', 'How many pixels a simplification would change on screen'), ('d', 'The price of the graphics card')], 'c'),
    ],
}
