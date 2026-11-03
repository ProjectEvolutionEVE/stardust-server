"""Rover Localisation on Other Worlds: wheel and visual odometry, slip on loose ground, Sun sensors, ties to orbital imagery, error drift and fixes."""
CODE = 'navigation5_rover_localisation'
BOOK = {
    "title": 'Rover Localisation on Other Worlds',
    "subtitle": 'How a rover works out where it is when no GPS signal reaches it',
    "chapters": [
        ('Counting wheel turns',
         'Wheel odometry counts how far the wheels have turned. On firm ground it works well. But each turn may not move the rover as far as the wheel size suggests.'),
        ('Slip on loose ground',
         'Wheels can spin on sand or loose soil. This slip makes the wheel count overstate the distance travelled, and the error builds with every slip.'),
        ('Watching the view',
         'Visual odometry tracks features in camera images from one frame to the next, to estimate how far and in which direction the rover has moved. It works best on ground with plenty of texture.'),
        ('Sun sensors',
         'When the Sun is visible, its position in the sky gives a fixed direction. Sun sensors help correct the heading of the rover, which otherwise drifts over time.'),
        ('Ties to orbital imagery',
         'Scientists match rover photos to images taken from orbit. When a landmark is seen in both, the rover position can be fixed on the orbital map.'),
        ('Error drift and fixes',
         'Errors build up as the rover travels. Regular fixes from orbital matches and Sun sightings keep the estimate close to the truth.'),
    ],
    "test": [
        ('What does wheel odometry measure?',
         [('a', 'The colour of the rocks'), ('b', 'The speed of the wind'), ('c', 'The battery voltage'), ('d', 'How far the wheels have turned')], 'd'),
        ('Why is slip a problem for a rover?',
         [('a', 'Wheel counts then overstate how far the rover has gone'), ('b', 'It makes the rover quieter'), ('c', 'It makes the rover brighter'), ('d', 'It cleans the wheels')], 'a'),
        ('What does visual odometry track?',
         [('a', 'Clouds in the sky'), ('b', 'Features in camera images from one frame to the next'), ('c', 'Radio music from Earth'), ('d', 'Stars at night only')], 'b'),
        ('What do Sun sensors help correct?',
         [('a', 'The paint on the rover'), ('b', 'The battery of the rover'), ('c', 'The heading of the rover, which drifts over time'), ('d', 'The engine sound of the rover')], 'c'),
        ('How is a rover position fixed on an orbital map?',
         [('a', 'By matching a landmark seen both by the rover and from orbit'), ('b', 'By guessing from memory'), ('c', 'By weighing the rover'), ('d', 'By listening for wind')], 'a'),
    ],
}
