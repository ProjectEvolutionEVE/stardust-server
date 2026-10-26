"""Dead Reckoning: working out where you are from where you started, your heading, your speed and the time you have sailed."""
CODE = 'navigation2_deadreckoning'
BOOK = {
    "title": 'Dead Reckoning',
    "subtitle": 'Finding your place from a known start, a heading, a speed and a time',
    "chapters": [
        ('A position from a known start',
         'Dead reckoning begins at a position you already know, then adds the distance and direction travelled since. The name is often said to come from "deduced reckoning": the navigator works out the present position by calculation, not by sighting anything. It works in fog, at night, and far from land.'),
        ('Heading, speed and time',
         'To reckon, you need three things: the heading you have steered, the speed you have made, and the time you have sailed. Multiply speed by time to get the distance. Then move that distance along the heading from your last known point, and mark the new point on the chart.'),
        ('The log line',
         'Before electronics, a sailor measured speed with a log line. A wooden float was thrown over the stern, and the knots run out on the line were counted during a timed sand glass. A knot is one nautical mile an hour, and a nautical mile is about 1.85 km.'),
        ('Allowing for current and wind',
         'Water moves, and so does air. A current carries a ship sideways over the ground, and wind can push it off its heading. Navigators allow for these, using known currents and wind, so the reckoned position stays close to the truth.'),
        ('Resetting the reckoning',
         'Dead reckoning is always an estimate, so navigators mark it on the chart and check it. Each time a fix comes from the sky, a landmark or a radio beacon, the reckoning is reset from that better position. Then the work begins again from there.'),
        ('Its weak spot',
         'Every small error in heading or speed is carried into the next step. The longer you go without a fix, the further the reckoned position may drift from where you really are. Checks are what keep it honest.'),
    ],
    "test": [
        ('What three things does a navigator need for dead reckoning?',
         [('a', 'Heading, speed and time'), ('b', 'Colour, weight and height'), ('c', 'Latitude, longitude and altitude'), ('d', 'Radio, radar and sonar')], 'a'),
        ('What is a knot?',
         [('a', 'One metre per second'), ('b', 'One nautical mile per hour'), ('c', 'One kilometre per minute'), ('d', 'One degree of latitude per day')], 'b'),
        ('What does a current do to a ship\'s reckoned position?',
         [('a', 'Makes it turn into the wind'), ('b', 'Sets its clock back'), ('c', 'Carries the ship sideways over the ground'), ('d', 'Removes the need for a heading')], 'c'),
        ('When should a navigator reset the reckoning?',
         [('a', 'Never, once it has started'), ('b', 'Only at the end of the voyage'), ('c', 'When the wind changes'), ('d', 'When a better fix is available from the sky, a landmark or a beacon')], 'd'),
        ('Why does dead reckoning still work in fog or at night?',
         [('a', 'It uses the Sun'), ('b', 'It needs a lighthouse'), ('c', 'It only works in clear weather'), ('d', 'It needs no view of the outside world')], 'd'),
    ],
}
