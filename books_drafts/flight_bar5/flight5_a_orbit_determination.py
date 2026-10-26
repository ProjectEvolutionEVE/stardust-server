"""Determining an Orbit: fitting a path to observations, and how the first orbit was worked out from few sightings."""
CODE = 'flight5_a_orbit_determination'
BOOK = {
    "title": 'Determining an Orbit',
    "subtitle": 'Fitting a path to observations',
    "chapters": [
        ('From observations to a path',
         'To find an orbit, a team starts from observations: angles, distances or speeds measured at known times. From these they work out the path that best fits what was seen. This is called orbit determination.'),
        ('Least squares',
         'With more observations than the minimum, no single path fits them all perfectly. The method of least squares finds the path that makes the total error as small as possible. It is the standard tool for fitting many measurements.'),
        ('Gauss and the first orbit',
         'In 1801 the mathematician Carl Friedrich Gauss used a few observations of the small planet Ceres to work out its orbit. Its position was then predicted well enough for astronomers to find it again. His methods still inform orbit work.'),
        ('Angles only',
         'Sometimes a team has only angles to a target, measured at a few times. From these angles alone the path can be estimated, but only with more uncertainty. This is common when a new object is first seen.'),
        ('Tracking data',
         'Modern orbit work uses radio tracking, which gives range and speed as well as angles. This data is far more precise. Teams combine it with optical observations to refine their estimates.'),
        ('Accuracy',
         'The accuracy of an orbit depends on the quality and number of observations, and on the models used. A good orbit is one that predicts future positions well. Teams check their orbits against new data as it arrives.'),
    ],
    "test": [
        ('What does orbit determination start from?',
         [('a', 'Guesses about the weather'), ('b', 'The colour of the craft'), ('c', 'The number of crew'), ('d', 'Observations of angles, distances or speeds at known times')], 'd'),
        ('What does the method of least squares do?',
         [('a', 'Finds the path that makes the total error as small as possible'), ('b', 'Counts the stars'), ('c', 'Sets the launch time'), ('d', 'Paints the orbit')], 'a'),
        ('What did Carl Friedrich Gauss use to find an orbit in 1801?',
         [('a', 'Observations of the small planet Ceres'), ('b', 'Photos of a cake'), ('c', 'The sound of a rocket'), ('d', 'A tide table')], 'a'),
        ('Why is an orbit from angles alone less certain?',
         [('a', 'Because angles are always wrong'), ('b', 'Because angles alone leave more uncertainty in distance and speed'), ('c', 'Because angles are colourless'), ('d', 'Because angles stop the craft')], 'b'),
        ('What does modern radio tracking give that angles alone do not?',
         [('a', 'Only the time of day'), ('b', 'Only the weather'), ('c', 'Range and speed as well as angles'), ('d', 'Only the name of the craft')], 'c'),
    ],
}
