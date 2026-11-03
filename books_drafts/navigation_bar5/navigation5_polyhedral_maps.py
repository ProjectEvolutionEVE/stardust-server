"""Polyhedral and Cube Maps: a sphere cut into faces, face-by-face projection, seams, uses in data and games, distortion, and standard layouts."""
CODE = 'navigation5_polyhedral_maps'
BOOK = {
    "title": 'Polyhedral and Cube Maps',
    "subtitle": 'Covering a whole sphere with flat faces, one at a time',
    "chapters": [
        ('A sphere cut into faces',
         'A polyhedral map covers a sphere with flat faces, such as the six faces of a cube. Each face is a flat piece with its own simple grid.'),
        ('Face-by-face projection',
         'Each point on the sphere is projected onto the face it falls on. Within any one face the map is simple and flat.'),
        ('Seams',
         'Where two faces meet there is a seam. Points on either side of a seam must be joined carefully, or lines and textures will break.'),
        ('Uses in data and games',
         'Cube maps are used in games for sky backgrounds and environment images. They are also used in some data systems that need to cover the whole globe.'),
        ('Errors',
         'Every face introduces some distortion, and it is usually largest near the corners of the faces. Smart layouts keep the error low over the area of greatest interest.'),
        ('Standards',
         'Standard layouts exist for common uses. Following them makes it easier for software to read the same map in the same way.'),
    ],
    "test": [
        ('What is a polyhedral map?',
         [('a', 'A map of a pond'), ('b', 'A sphere covered by flat faces, such as a cube'), ('c', 'A paper folding puzzle'), ('d', 'A road map of a city')], 'b'),
        ('How are points handled on a face of a cube map?',
         [('a', 'They are ignored'), ('b', 'They are painted over'), ('c', 'They are sung aloud'), ('d', 'Each point is projected onto the face it falls on')], 'd'),
        ('What is a seam?',
         [('a', 'The line where two faces meet'), ('b', 'A sewing thread'), ('c', 'A type of crater'), ('d', 'A river on a map')], 'a'),
        ('Where is distortion usually largest on a cube map?',
         [('a', 'At the centre of each face'), ('b', 'Nowhere at all'), ('c', 'Near the corners of the faces'), ('d', 'Under the sea')], 'c'),
        ('Why follow standard layouts?',
         [('a', 'To make maps heavier'), ('b', 'To stop software from working'), ('c', 'To hide the errors'), ('d', 'So that software can read the same map in the same way')], 'd'),
    ],
}
