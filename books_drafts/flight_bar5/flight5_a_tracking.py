"""Tracking Networks: the ground stations and relay satellites that keep in touch with craft."""
CODE = 'flight5_a_tracking'
BOOK = {
    "title": 'Tracking Networks',
    "subtitle": 'Ground stations and relay satellites that keep in touch',
    "chapters": [
        ('Ground stations',
         'A craft can only talk to the ground when a station can see it. Ground stations are large antennas placed around the world, so that some station is always close to a craft that is in orbit. Each station has its own schedule and its own limits.'),
        ('Relay satellites',
         'A relay satellite sits in a high orbit and passes messages between a low craft and the ground. The Tracking and Data Relay Satellite System, known as TDRS, is a well-known example. Relay satellites fill gaps that ground stations cannot cover.'),
        ('Coverage gaps',
         'Even with many stations, some parts of an orbit can be out of sight of every station. A craft may have to wait for a pass before it can send its data. Mission planners design around these gaps.'),
        ('Scheduling',
         'Stations and relays are shared by many missions. A schedule decides which craft gets time on which antenna at what moment. Good scheduling keeps every mission on track without wasting time on the antennas.'),
        ('Data',
         'Tracking is not only about position. It also carries commands up to the craft and science or health data down to the ground. The link must be reliable and must not drop data, so the team checks it often.'),
        ('The deep space network',
         'For craft far from the Earth, a set of large stations spread around the world, often called the Deep Space Network, does the tracking. Its stations are placed so that a distant craft can be followed as the Earth turns.'),
    ],
    "test": [
        ('Why do craft need ground stations?',
         [('a', 'To make the craft lighter'), ('b', 'To paint the orbit'), ('c', 'To talk to the craft and track its position'), ('d', 'To stop the Sun')], 'c'),
        ('What is a relay satellite?',
         [('a', 'A satellite that cooks food'), ('b', 'A satellite that gives light to the Moon'), ('c', 'A satellite with no radio'), ('d', 'A satellite that passes messages between a low craft and the ground')], 'd'),
        ('What do coverage gaps mean for a mission?',
         [('a', 'Some parts of an orbit may be out of sight of every station'), ('b', 'The orbit is fully hidden from the Sun'), ('c', 'The craft cannot be heard at all'), ('d', 'The craft never needs fuel')], 'a'),
        ('Why does a station schedule matter?',
         [('a', 'Stations and relays are shared, so time must be allotted'), ('b', 'Stations never need time'), ('c', 'Schedules change the weather'), ('d', 'Schedules make craft heavier')], 'a'),
        ('What does tracking carry besides position?',
         [('a', 'Only music'), ('b', 'Commands up to the craft and data down to the ground'), ('c', 'Only paint'), ('d', 'Only heat')], 'b'),
    ],
}
