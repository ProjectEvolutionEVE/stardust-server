"""Gauss's Theorema Egregium: curved surfaces, intrinsic curvature, why no flat map is perfect, Gaussian curvature, the idea of the proof and its consequences for maps."""
CODE = 'navigation5_theorema_egregium'
BOOK = {
    "title": "Gauss's Theorema Egregium",
    "subtitle": 'Why a sphere can never be laid flat without some distortion',
    "chapters": [
        ('Curved surfaces',
         'A sphere is a curved surface. A sheet of paper is flat. The two differ in a deep way, and that difference matters for every map ever drawn.'),
        ('Intrinsic curvature',
         'Gauss showed that curvature can be measured by someone living on the surface, using only distances and angles on that surface. It does not depend on the space around the surface.'),
        ('Why no flat map is perfect',
         'Because the curvature of a sphere is not zero, no flat map can keep all distances and angles correct. Every flat map must distort something.'),
        ('Gaussian curvature',
         'The Gaussian curvature at a point is the product of the two principal curvatures there. A sphere has the same positive value at every point.'),
        ('The proof idea',
         'Gauss found a formula for curvature that uses only how distances are measured on the surface. A map that keeps all distances would have to keep the curvature, and a flat plane has none.'),
        ('Consequences',
         'The theorem explains why every map projection must trade off shape, area, distance and direction. It shaped how geodesy and cartography are done.'),
    ],
    "test": [
        ('What is a curved surface?',
         [('a', 'A flat sheet of paper'), ('b', 'A table top'), ('c', 'A straight wall'), ('d', 'A sphere')], 'd'),
        ('What does intrinsic curvature mean?',
         [('a', 'Curvature that comes from paint'), ('b', 'Curvature measured on the surface itself, from distances and angles'), ('c', 'A type of tide'), ('d', 'The curve of the sky over a city')], 'b'),
        ('Why is no flat map perfect for the whole Earth?',
         [('a', 'Because maps are too small'), ('b', 'Because paper is too thin'), ('c', 'Because the curvature of a sphere is not zero, so some distortion is unavoidable'), ('d', 'Because maps are too bright')], 'c'),
        ('What is Gaussian curvature?',
         [('a', 'The product of the two principal curvatures'), ('b', 'A sum of letters in a word'), ('c', 'A colour on a map'), ('d', 'The distance to the Moon')], 'a'),
        ('What does the theorem show about map projections?',
         [('a', 'They are always perfect'), ('b', 'They must trade off shape, area, distance or direction'), ('c', 'They need no mathematics at all'), ('d', 'They are made of gold')], 'b'),
    ],
}
