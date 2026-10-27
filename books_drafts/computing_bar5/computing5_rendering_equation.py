"""The Rendering Equation: the physics of light that every realistic image is trying to estimate, and why it is so hard to compute."""
CODE = 'computing5_rendering_equation'
BOOK = {
    "title": 'The Rendering Equation',
    "subtitle": 'How light arrives, bounces and leaves a surface',
    "chapters": [
        ('What it describes',
         'The rendering equation describes how light leaves a point on a surface. The light that leaves depends on the light that arrives from every direction. Almost every realistic renderer is an attempt to solve this equation.'),
        ('Light transport and radiance',
         'Radiance measures the light travelling along a ray, per unit area and per unit of solid angle. Light transport is the path it takes as it bounces between surfaces. Each bounce adds to the total brightness of a point.'),
        ('Reflectance functions',
         'A reflectance function, often called the BRDF, says how a surface scatters light arriving from one direction into another. A matte surface spreads light widely. A mirror sends it almost entirely in one direction.'),
        ('Monte Carlo estimation',
         'The integral in the equation has no simple closed-form answer for real scenes. Monte Carlo methods estimate it by sampling many random light paths and averaging the results. More samples give a cleaner estimate, with random noise that falls slowly.'),
        ('Importance sampling',
         'Importance sampling chooses paths more often where they contribute the most, such as toward bright lights or along likely reflections. This reaches a good estimate with fewer samples. The choice of sampling strategy has a large effect on image quality.'),
        ('Path tracing',
         'Path tracing follows random light paths from the camera, or from lights, until they end. It is simple and general, and it handles many effects together. Its cost is noise, so denoising and many samples are usually needed.'),
    ],
    "test": [
        ('What does the rendering equation describe?',
         [('a', 'How the price of a screen changes'), ('b', 'How light leaves a point on a surface'), ('c', 'How a sound is recorded'), ('d', 'How a file is compressed')], 'b'),
        ('What does radiance measure?',
         [('a', 'The number of pixels on a screen'), ('b', 'The temperature of a cable'), ('c', 'The speed of a mouse'), ('d', 'Light travelling along a ray, per unit area and solid angle')], 'd'),
        ('What does a BRDF describe?',
         [('a', 'How a surface scatters light from one direction into another'), ('b', 'How many people use a renderer'), ('c', 'The battery life of a laptop'), ('d', 'The size of a font')], 'a'),
        ('Why do renderers use Monte Carlo methods?',
         [('a', 'They make images smaller on disk'), ('b', 'They turn off all light'), ('c', 'The integral has no simple answer for real scenes, so it is estimated by sampling'), ('d', 'They remove the need for a camera')], 'c'),
        ('What is the usual cost of path tracing?',
         [('a', 'No cost at all'), ('b', 'Images that cannot have colour'), ('c', 'A fixed picture that never changes'), ('d', 'Random noise that needs many samples or denoising')], 'd'),
    ],
}
