"""Optical Flow: measuring how the pixels in a camera image move from one frame to the next."""
CODE = 'navigation5_optical_flow'
BOOK = {
    "title": 'Optical Flow',
    "subtitle": 'Brightness constancy, the flow field, the aperture problem, image pyramids, speed estimates and uses',
    "chapters": [
        ('Brightness constancy',
         'Optical flow assumes that a point keeps its brightness as it moves from one image to the next. This simple rule lets the computer match a point in one frame with the same point in the next. When the rule holds, the matching is reliable.'),
        ('The flow field',
         'A flow field is a map of how each pixel moves between two images. Arrows show the direction and size of each movement. Together they describe how the scene shifted.'),
        ('The aperture problem',
         'A small window on an edge can show motion only across the edge, not along it. The true motion is therefore uncertain. Using larger windows or several points helps solve this.'),
        ('Image pyramids',
         'Large motions are hard to follow in full-size images. The method first works on small, blurred copies of the image, where the motion looks smaller. It then refines the estimate step by step back to full size.'),
        ('Speed estimates',
         'If the frame rate and the scene distance are known, the flow gives a speed estimate. Flow is a quick way to tell how fast the camera is moving. Its accuracy depends on the scene and the lighting.'),
        ('Uses',
         'Optical flow is used in drones, video stabilisation and robot motion. It helps a machine keep a steady course and avoid obstacles. It is often one part of a larger navigation system.'),
    ],
    "test": [
        ('What is brightness constancy?',
         [('a', 'A brightness setting on a monitor'), ('b', 'The assumption that a point keeps its brightness as it moves'), ('c', 'The sun\'s brightness'), ('d', 'A light bulb')], 'b'),
        ('What is a flow field?',
         [('a', 'A river'), ('b', 'A shop'), ('c', 'A cleaning tool'), ('d', 'A map of how each pixel moves between two images')], 'd'),
        ('What is the aperture problem?',
         [('a', 'A small window cannot show motion along an edge, only across it'), ('b', 'The camera lens is too big'), ('c', 'Light does not enter'), ('d', 'Pictures are too small')], 'a'),
        ('What is an image pyramid for?',
         [('a', 'Storing paint'), ('b', 'Building houses'), ('c', 'Handling large motions by working from small blurred images to full size'), ('d', 'Playing music')], 'c'),
        ('What is optical flow used for?',
         [('a', 'Cooking'), ('b', 'Painting walls'), ('c', 'Estimating speed and motion from camera images'), ('d', 'Selling cameras')], 'c'),
    ],
}
