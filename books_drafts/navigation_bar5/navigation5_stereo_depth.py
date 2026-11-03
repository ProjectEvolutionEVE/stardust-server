"""Stereo Depth Estimation: finding how far away things are by comparing two side-by-side views."""
CODE = 'navigation5_stereo_depth'
BOOK = {
    "title": 'Stereo Depth Estimation',
    "subtitle": 'Disparity, baseline, matching cost, semi-global matching, errors and range',
    "chapters": [
        ('Disparity',
         'Disparity is the shift of the same point between the left and right images. Near things shift more than far things. Measuring the shift gives the distance.'),
        ('Baseline',
         'The baseline is the distance between the two cameras. A wider baseline gives a larger shift for the same depth. This makes the depth easier to measure.'),
        ('Matching cost',
         'The matching cost is a score for how well a patch in one image agrees with a patch in the other. Low cost means a good match. The method looks for the shift with the lowest cost.'),
        ('Semi-global matching',
         'Semi-global matching smooths the costs along several directions across the image. This keeps the depth consistent and fills in gaps. It gives cleaner results than matching each pixel alone.'),
        ('Errors',
         'Plain areas with no texture are hard to match. Repeated patterns can also confuse the method. Errors grow for objects far away, since their shift is small.'),
        ('Range',
         'The usable range depends on the baseline, the focal length and the image quality. Wider baselines reach farther with good accuracy. Stereo is a practical way to sense the shape of nearby terrain.'),
    ],
    "test": [
        ('What is disparity?',
         [('a', 'The shift of the same point between left and right images'), ('b', 'A type of camera'), ('c', 'The lens focal length'), ('d', 'The image size')], 'a'),
        ('What does baseline mean?',
         [('a', 'The bottom of a page'), ('b', 'The time between frames'), ('c', 'The distance between the two cameras'), ('d', 'The lens colour')], 'c'),
        ('How does a wider baseline help?',
         [('a', 'It makes objects smaller'), ('b', 'It improves depth accuracy at a given range'), ('c', 'It removes shadows'), ('d', 'It stops motion')], 'b'),
        ('What is matching cost?',
         [('a', 'A shop price'), ('b', 'A painting cost'), ('c', 'The cost of the cameras'), ('d', 'A number that scores how well patches from the two images match')], 'd'),
        ('What is semi-global matching?',
         [('a', 'A method that smooths matching costs along several directions'), ('b', 'A sort of game'), ('c', 'A camera brand'), ('d', 'A map of cities')], 'a'),
    ],
}
