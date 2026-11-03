"""Planetary Coordinate Systems: IAU rotation models, the prime meridian, the pole direction, model variants, mission use and standards."""
CODE = 'navigation5_planetary_coords'
BOOK = {
    "title": 'Planetary Coordinate Systems',
    "subtitle": 'The agreed rules for saying where something is on a planet or moon',
    "chapters": [
        ('Why a body needs a frame',
         'To describe where something is on a planet, you need a frame: a rotation model, a prime meridian and a north pole. Without these, two teams could describe the same spot in two different ways.'),
        ('The IAU rotation models',
         'The International Astronomical Union, through a working group, publishes rotation models for planets and moons. Each model gives how fast the body turns and where its pole points.'),
        ('The prime meridian',
         'Each body needs a zero line of longitude. For Mars it passes through a chosen crater. For other bodies it is set by a chosen feature or by a fixed rule.'),
        ('The pole direction',
         'The pole is the direction of the rotation axis, given as an angle on the sky. The direction changes slowly over time, and precise work must include those changes.'),
        ('Variants',
         'Some bodies have several versions of their rotation model, based on different data. Mission teams must say which version they use, because different versions can give different coordinates.'),
        ('Mission use and standards',
         'Missions use these models to make maps, to plan spacecraft orbits and to compare results. Shared standards make the data from different missions fit together.'),
    ],
    "test": [
        ('Why does a body need a frame?',
         [('a', 'To hold its paint'), ('b', 'To describe positions on it consistently'), ('c', 'To keep it warm'), ('d', 'To make it look bigger')], 'b'),
        ('Who publishes rotation models for planets?',
         [('a', 'A national sports club'), ('b', 'A car maker'), ('c', 'The IAU working group on cartographic coordinates'), ('d', 'The Sun')], 'c'),
        ('What is the pole direction?',
         [('a', 'Where the body is brightest'), ('b', 'The side that faces the Sun'), ('c', 'The name of a crater'), ('d', 'The direction of the rotation axis')], 'd'),
        ('Why must mission teams state which model version they use?',
         [('a', 'Because different versions can give different coordinates'), ('b', 'Because versions have different colours'), ('c', 'Because models make sounds'), ('d', 'Because no version is real')], 'a'),
        ('What do shared standards do?',
         [('a', 'Hide the data from other teams'), ('b', 'Stop maps from being drawn'), ('c', 'Make data from different missions fit together'), ('d', 'Make the planets move faster')], 'c'),
    ],
}
