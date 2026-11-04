"""Camera Calibration Models: finding the inner settings of a camera so its images can be trusted for measurement."""
CODE = 'navigation5_camera_calibration'
BOOK = {
    "title": 'Camera Calibration Models',
    "subtitle": 'Intrinsics, distortion, checkerboard targets, bundle methods, testing and accuracy',
    "chapters": [
        ('Intrinsics',
         'Intrinsics are the internal settings of a camera, such as its focal length and the centre of its image. They describe how the lens turns the scene into pixels. Knowing them is needed before measuring anything from an image.'),
        ('Distortion',
         'Lenses bend straight lines near the edge of the image. This is called distortion. A calibration model includes a few numbers that describe the bending, so it can be removed.'),
        ('Checkerboard targets',
         'A printed checkerboard is shown to the camera from many angles. The software finds the corners on the board, which have known spacing. From these corners it works out the camera model.'),
        ('Bundle methods',
         'Bundle methods refine all the camera parameters and the target positions together. They use many views to reduce the errors. The result is a more accurate and stable model.'),
        ('Testing',
         'A calibration should be tested on images that were not used to build it. A good result matches the known target positions closely on new views. Poor results call for more or better views.'),
        ('Accuracy',
         'The accuracy of a calibrated camera sets the accuracy of every measurement made with it. Keep the focus and the lens settings fixed after calibration. Recalibrate if anything changes.'),
    ],
    "test": [
        ('What are intrinsics?',
         [('a', 'The inside of a shop'), ('b', 'The lens paint'), ('c', 'The internal parameters of a camera, such as focal length and image centre'), ('d', 'The price of pixels')], 'c'),
        ('What is distortion?',
         [('a', 'A bright light'), ('b', 'The bending of straight lines in an image by the lens'), ('c', 'A camera crash'), ('d', 'A broken screen')], 'b'),
        ('What is a checkerboard target used for?',
         [('a', 'Cooking'), ('b', 'A game'), ('c', 'A board for chess'), ('d', 'Known patterns that let the software find corners and fit the camera model')], 'd'),
        ('What do bundle methods do in calibration?',
         [('a', 'Refine all parameters together from many views'), ('b', 'Remove the camera'), ('c', 'Paint frames'), ('d', 'Store films')], 'a'),
        ('Why test a calibration?',
         [('a', 'To make a sound'), ('b', 'To break the camera'), ('c', 'To get the film'), ('d', 'To check accuracy on new images before trusting it')], 'd'),
    ],
}
