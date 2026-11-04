"""Adaptive Optics and Atmospheric Correction: how ground telescopes cancel out the shimmer of the air and see stars as sharp points."""
CODE = 'science5_astro_adaptive_optics'
BOOK = {
    "title": 'Adaptive Optics and Atmospheric Correction',
    "subtitle": 'Sharpening the view through moving air',
    "chapters": [
        ('Why stars twinkle',
         'Moving air in the atmosphere bends the light from a star unevenly. This is turbulence, and it makes stars shimmer and blur. Bigger telescopes are blurred just as much unless they correct for it.'),
        ('Wavefront sensing',
         'A wavefront sensor measures the distortions in the incoming light caused by the air. It checks the shape of the light wave many times each second. These measurements drive the correction.'),
        ('Deformable mirrors',
         'A deformable mirror has a surface that can change shape in tiny steps. The mirror is adjusted many times a second to cancel the distortions. The corrected light then forms a sharper image.'),
        ('Guide stars',
         'A guide star is a bright reference point used to measure the air\'s distortions. A natural star works if one is bright enough nearby. Otherwise a laser can make an artificial guide star high in the sky.'),
        ('The Strehl ratio',
         'The Strehl ratio measures how close an image is to the sharpest possible. A ratio of 1 is perfect. Adaptive optics raises the Strehl ratio, and it is a standard way to report image quality.'),
        ('Ground-layer correction',
         'Most of the turbulence is near the ground. Ground-layer correction targets this layer over a wider field of view. It helps astronomers study larger regions of sky.'),
    ],
    "test": [
        ('Why does turbulence blur images from ground telescopes?',
         [('a', 'Telescopes are too heavy'), ('b', 'Moving air in the atmosphere bends the light unevenly'), ('c', 'Stars are too cold'), ('d', 'Clouds are made of sugar')], 'b'),
        ('What does a wavefront sensor measure?',
         [('a', 'The distortions in incoming light caused by the air'), ('b', 'The weight of a telescope'), ('c', 'The colour of the grass'), ('d', 'The speed of a bus')], 'a'),
        ('What is a deformable mirror?',
         [('a', 'A mirror that cannot change'), ('b', 'A dressing-room mirror'), ('c', 'A toy mirror'), ('d', 'A mirror whose surface shape is adjusted many times a second to cancel distortions')], 'd'),
        ('What is a guide star used for?',
         [('a', 'A star to navigate by at sea only'), ('b', 'A decoration on a telescope'), ('c', 'A bright reference point used to measure the air\'s distortions'), ('d', 'A planet with no light')], 'c'),
        ('What is the Strehl ratio?',
         [('a', 'A type of cookie'), ('b', 'A measure of how close an image is to the sharpest possible'), ('c', 'A sound made by air'), ('d', 'The number of planets')], 'b'),
    ],
}
