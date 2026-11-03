"""Closest Point of Approach: Working out how close two ships will pass."""
CODE = 'navigation5_cpa_tcpa'
BOOK = {
    'title': 'Closest Point of Approach',
    'subtitle': 'Working out how close two ships will pass',
    'chapters': [
        ('Relative motion', 'Two moving ships form a picture of relative motion. It shows how one ship appears to move when seen from the other.'),
        ('Closest distance', 'The closest point of approach, CPA, is the least distance the ships will be from each other if they keep their courses and speeds. It shows how close a meeting could be.'),
        ('Time to closest', 'TCPA is the time left until that closest point. It tells the watchkeeper how soon the meeting happens.'),
        ('Plots', "A radar plot draws the other ship's track over time. Watching it shows whether a ship will pass ahead, astern or on a collision course."),
        ('Alarms', 'Radar and electronic chart systems can set alarms for a CPA or TCPA limit. Alarms help the watch, but they are not a substitute for looking out.'),
        ('Limits', 'CPA assumes steady courses and speeds. Real ships change course, so the figures must be checked again as the situation develops.'),
    ],
    'test': [
        ('What is CPA?', [('a', "A ship's cargo"), ('b', 'The least distance two ships will be apart if they keep course and speed'), ('c', "A kind of ship's bell"), ('d', 'A tide name')], 'b'),
        ('What does TCPA tell the watchkeeper?', [('a', 'Time left until the closest point'), ('b', "The ship's colour"), ('c', 'The name of the cook'), ('d', 'The price of fuel')], 'a'),
        ('What does a radar plot show?', [('a', 'Wind on the mountains'), ('b', 'The price of tea'), ('c', "The other ship's track over time"), ('d', 'Sea salt')], 'c'),
        ('Why are alarms not a substitute for looking out?', [('a', 'They support the watch but do not replace it'), ('b', 'They are always wrong'), ('c', 'They remove the need for lookouts entirely'), ('d', 'They stop the ship')], 'a'),
        ('What does CPA assume?', [('a', 'Steady courses and speeds'), ('b', 'That ships always change course wildly'), ('c', 'That no ships exist'), ('d', 'That it is always night')], 'a'),
    ],
}
