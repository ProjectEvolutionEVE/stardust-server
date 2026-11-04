"""Trajectory-Based Operations: Flying to a shared plan in four dimensions."""
CODE = 'navigation5_trajectory_ops'
BOOK = {
    'title': 'Trajectory-Based Operations',
    'subtitle': 'Flying to a shared plan in four dimensions',
    'chapters': [
        ('Four dimensions', 'A trajectory describes where an aircraft will be in three dimensions and when. Those are latitude, longitude and altitude, and the fourth is time.'),
        ('Shared plans', 'Airlines, controllers and pilots agree on a planned trajectory. Everyone works from the same picture of the flight.'),
        ('Agreements', 'Once the plan is agreed, the aircraft is expected to fly it. Changes are made through set procedures, so that every party stays informed.'),
        ('Conformance', 'Conformance means how closely the aircraft flies its agreed trajectory. Systems check this and warn when the aircraft drifts from the plan.'),
        ('Airspace', 'Shared trajectories let airspace be used more closely and efficiently. Routes can be shaped around the plan rather than fixed corridors.'),
        ('Benefits and implementation', 'Trajectory-based operations can reduce fuel use, flight time and delays. Introducing them takes equipment, data links and new procedures.'),
    ],
    'test': [
        ('What are the four dimensions of a trajectory?', [('a', 'Colour, sound, smell and taste'), ('b', 'Price, weight, speed and fuel'), ('c', 'Dog, cat, bird and fish'), ('d', 'Latitude, longitude, altitude and time')], 'd'),
        ('What is conformance?', [('a', 'How closely the aircraft flies its agreed trajectory'), ('b', 'The paint on the wings'), ('c', 'The number of seats'), ('d', 'The cost of tickets')], 'a'),
        ('Who agrees on the planned trajectory?', [('a', 'Passengers only'), ('b', 'The weather alone'), ('c', 'Airlines, controllers and pilots'), ('d', 'Nobody')], 'c'),
        ('What do shared trajectories allow for airspace?', [('a', 'More efficient use'), ('b', 'Less use'), ('c', 'Closing the sky'), ('d', 'Ignoring plans')], 'a'),
        ('What is needed to introduce trajectory-based operations?', [('a', 'Only a kite'), ('b', 'Only a coffee machine'), ('c', 'Equipment, data links and new procedures'), ('d', 'Only a paintbrush')], 'c'),
    ],
}
