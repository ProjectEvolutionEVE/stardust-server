"""Structure from Motion: building a 3D picture of a scene from photographs taken from different places."""
CODE = 'navigation5_sfm'
BOOK = {
    "title": 'Structure from Motion',
    "subtitle": 'Camera poses, points, reconstruction, scale, uses and failures',
    "chapters": [
        ('What SfM does',
         'Structure from motion takes many photographs of one scene and works out where the scene is in 3D. It also works out where each camera was when it took each picture. The result is a 3D model built from ordinary images.'),
        ('Camera poses',
         'A camera pose is the position and direction of a camera at the moment of a photo. Finding every pose is a central part of the work. Each photo must be placed correctly relative to the others.'),
        ('Points',
         'The method finds matching points that appear in several photos. Each matched point is placed in 3D by working out where the rays from the cameras meet. A dense set of points forms the shape of the scene.'),
        ('Reconstruction',
         'The steps of matching, placing cameras and placing points are repeated and refined. The reconstruction grows as more photos are added. The final model is checked against the photos for errors.'),
        ('Scale',
         'Photos alone cannot fix the real size of the scene. A model of a small toy and a model of a large building can look the same. Real measurements, such as a known distance, are needed to set the scale.'),
        ('Uses and failures',
         'Structure from motion is used for mapping ground, buildings and sites. It can fail when there are few matching points, or when a scene is full of repeated patterns. Good photos with plenty of overlap give the best results.'),
    ],
    "test": [
        ('What is structure from motion?',
         [('a', 'Building houses'), ('b', 'Moving furniture'), ('c', 'Building 3D structure and camera positions from several images'), ('d', 'The motion of trains')], 'c'),
        ('What are camera poses?',
         [('a', 'The position and direction of each camera'), ('b', 'The shape of a lens'), ('c', 'The price of a camera'), ('d', 'The film type')], 'a'),
        ('Why is scale uncertain in SfM from images alone?',
         [('a', 'Cameras have no lens'), ('b', 'The images alone do not fix real-world size'), ('c', 'Pictures are always the same size'), ('d', 'Colours change')], 'b'),
        ('What makes SfM fail?',
         [('a', 'Bright sunlight only'), ('b', 'Having many matching points'), ('c', 'A clear view'), ('d', 'Very few matching features or repeated patterns')], 'd'),
        ('What is a common use of SfM?',
         [('a', 'Mapping ground and buildings from photographs'), ('b', 'Cooking'), ('c', 'Sending email'), ('d', 'Playing music')], 'a'),
    ],
}
