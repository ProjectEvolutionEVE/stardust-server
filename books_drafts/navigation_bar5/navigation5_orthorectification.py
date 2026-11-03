"""Orthorectification of Images: correcting a photograph so that distances on it match the real ground."""
CODE = 'navigation5_orthorectification'
BOOK = {
    "title": 'Orthorectification of Images',
    "subtitle": 'The camera model, terrain, resampling, ground control, accuracy and products',
    "chapters": [
        ('The camera model',
         'A camera model describes how a point on the ground maps to a pixel in the image. It includes the lens and the camera\'s position and tilt. Orthorectification uses this model to undo the distortions.'),
        ('Terrain',
         'Hills and valleys shift points in an image, so distant ground can look wrong. A height model of the terrain is used to correct these shifts. Each point is moved to where it would appear from straight above.'),
        ('Resampling',
         'After the points are moved, new pixel values must be calculated on a regular grid. This step is called resampling. The result is an image where distances can be measured directly.'),
        ('Ground control',
         'Known positions on the ground, called ground control points, are used to check and correct the image. Their positions are measured accurately beforehand. The corrected image is then tied to real coordinates.'),
        ('Accuracy',
         'The final accuracy depends on the camera, the height model, and the control points. Errors in any of them carry through to the result. Accuracy should be stated with every product.'),
        ('Products',
         'Orthorectified images are used for maps, land records, planning and disaster response. Because distances can be measured on them, they are more useful than raw photos. They must be made with care for the results to be trusted.'),
    ],
    "test": [
        ('What is orthorectification?',
         [('a', 'Painting an image'), ('b', 'Removing distortions from camera tilt and terrain relief to make an accurate, map-like image'), ('c', 'Shrinking files'), ('d', 'Turning photos black and white')], 'b'),
        ('What is a digital elevation model used for?',
         [('a', 'Recipes'), ('b', 'Sounds'), ('c', 'Stamps'), ('d', 'To describe the height of the terrain')], 'd'),
        ('What is resampling?',
         [('a', 'Changing the price'), ('b', 'Removing a camera'), ('c', 'Calculating new pixel values on a regular grid'), ('d', 'Deleting maps')], 'c'),
        ('What are ground control points?',
         [('a', 'Known positions on the ground used to check and correct the image'), ('b', 'Control buttons'), ('c', 'Traffic lights'), ('d', 'Towers on hills')], 'a'),
        ('What is an orthorectified image good for?',
         [('a', 'Playing games'), ('b', 'Cooking'), ('c', 'Sending mail'), ('d', 'Measuring distances and areas accurately')], 'd'),
    ],
}
