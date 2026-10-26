"""Changing the Plane of an Orbit: why tilting an orbit costs speed, and where in the path the cheapest tilt happens."""
CODE = 'flight3a_plane_changes'
BOOK = {
    "title": 'Changing the Plane of an Orbit',
    "subtitle": 'Tilting an orbit costs fuel, and the place you choose to do it decides how much',
    "chapters": [
        ('Orbits have a tilt',
         "Every orbit lies in a flat plane that passes through the centre of the body it circles. The tilt of that plane, measured against the equator, is called its inclination. Two craft at the same height can fly in planes tilted a few degrees apart, or at a right angle to each other."),
        ('Why a tilt costs speed',
         "To move a craft into a new plane, you must change the direction of its velocity. Turning the direction takes a push, even if your speed stays exactly the same. The bigger the angle between the two planes, the bigger the push needed."),
        ('Pick the cheapest spot',
         "A plane change costs least when the craft is moving slowest, which is at the highest point of an oval orbit. The same tilt done at a low, fast point costs much more. A good pilot plans the tilt for the top of the path, not the bottom."),
        ('Combine the pushes',
         "A tilt can be combined with a change of speed in one burn. Doing both together is often cheaper than doing them apart. The planner works out the single push that makes both changes at once."),
        ('Why it matters to a pilot',
         "Every tilt you add to a route is paid for in fuel, and fuel is paid for in credits. A route that avoids a needless tilt flies more cheaply. Work out the tilt on the chart before you light any thrusters."),
        ('Keep the tilt small',
         "Choose routes that stay in one plane wherever you can. Ask whether the tilt is needed at all, because many targets can be reached from the plane you already fly in. The cheapest tilt is the one you never make."),
    ],
    "test": [
        ('What is the inclination of an orbit?',
         [('a', 'How fast the craft is moving'), ('b', 'The tilt of the orbit plane against the equator'), ('c', 'How far the craft is from the Starship'), ('d', 'The number of moons nearby')], 'b'),
        ('Why does changing an orbit\'s plane cost fuel even when speed stays the same?',
         [('a', 'Turning the direction of the velocity needs a push'), ('b', 'Air drags on the craft'), ('c', 'Gravity pulls harder on tilted orbits'), ('d', 'The hold must be emptied first')], 'a'),
        ('At which point of an oval orbit is a change of plane cheapest?',
         [('a', 'The lowest, fastest point'), ('b', 'The moment of launch'), ('c', 'Anywhere, since the cost never changes'), ('d', 'The highest, slowest point')], 'd'),
        ('What does combining a plane change with a speed change in one burn usually do?',
         [('a', 'Doubles the cost'), ('b', 'Stops the engines'), ('c', 'Often costs less than doing the two apart'), ('d', 'Makes the craft drift')], 'c'),
        ('Why should a pilot avoid adding a needless tilt to a route?',
         [('a', 'It costs extra fuel, and fuel costs credits'), ('b', 'It makes the view prettier'), ('c', 'It makes the Starship turn faster'), ('d', 'It shortens the flight time')], 'a'),
    ],
}
