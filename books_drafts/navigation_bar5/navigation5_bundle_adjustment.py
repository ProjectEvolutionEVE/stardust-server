"""Bundle Adjustment: refining camera positions and 3D points together so they agree with every photo."""
CODE = 'navigation5_bundle_adjustment'
BOOK = {
    "title": 'Bundle Adjustment',
    "subtitle": 'Joint optimisation, reprojection error, sparse structure, solvers, cost and uses',
    "chapters": [
        ('Joint optimisation',
         'Bundle adjustment adjusts all the camera positions and all the 3D points at the same time. Each part influences the others. The aim is one set of values that fits every photo as well as possible.'),
        ('Reprojection error',
         'Reprojection error is the gap between where a 3D point would appear in an image and where it was really seen. Bundle adjustment reduces the total of these gaps. A small total means the model agrees with the photos.'),
        ('Sparse structure',
         'Each point is seen by only a few cameras, so most of the links in the problem are empty. The problem is sparse. Solvers use this structure to work much faster.'),
        ('Solvers',
         'Most bundle adjustment uses iterative least-squares methods, such as Gauss-Newton or Levenberg-Marquardt. Each step improves the estimate a little. The process stops when the improvement is very small.'),
        ('Cost',
         'Bundle adjustment can be slow when there are very many images and points. Good starting values make it faster and less likely to fail. Large projects often split the work into smaller pieces.'),
        ('Uses',
         'Bundle adjustment is used in mapping, robot navigation and 3D modelling. It gives the most accurate version of a reconstruction. Other methods often run it as a final polish.'),
    ],
    "test": [
        ('What does bundle adjustment do?',
         [('a', 'Sells bundles'), ('b', 'Refines camera poses and 3D points together'), ('c', 'Counts pixels'), ('d', 'Paints the scene')], 'b'),
        ('What is reprojection error?',
         [('a', 'An error in printing'), ('b', 'A clock error'), ('c', 'The cost of projection screens'), ('d', 'The gap between a point\'s predicted image position and where it was measured')], 'd'),
        ('Why is the structure sparse?',
         [('a', 'Most points are in one image'), ('b', 'The points are all empty'), ('c', 'Each point is seen by only a few cameras, so most links are empty'), ('d', 'The matrix is small')], 'c'),
        ('What kind of solver is commonly used?',
         [('a', 'An iterative least-squares method such as Gauss-Newton or Levenberg-Marquardt'), ('b', 'A voting method'), ('c', 'A painting tool'), ('d', 'A sorting game')], 'a'),
        ('What is a main cost of bundle adjustment?',
         [('a', 'It uses no computer'), ('b', 'It can be slow for very large numbers of images and points'), ('c', 'It is free'), ('d', 'It needs no data')], 'b'),
    ],
}
