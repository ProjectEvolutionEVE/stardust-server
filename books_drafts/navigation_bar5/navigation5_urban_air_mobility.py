"""Navigation for Urban Air Mobility: Flying small aircraft between city buildings."""
CODE = 'navigation5_urban_air_mobility'
BOOK = {
    'title': 'Navigation for Urban Air Mobility',
    'subtitle': 'Flying small aircraft between city buildings',
    'chapters': [
        ('Flying low over cities', 'Urban air mobility means small aircraft carrying people or goods over cities. They fly at low heights, among buildings, power lines and other obstacles.'),
        ('Vertiports', 'Vertiports are the landing and takeoff sites for these aircraft. They need space, power and clear approach paths.'),
        ('Sensors', 'Navigation uses satellite positioning, cameras, radar and other sensors. Several sensors together give a safer picture than any one of them alone.'),
        ('Obstacles', 'Towers, cranes and wires must be mapped and avoided. Accurate maps and sensors help the aircraft keep clear of them.'),
        ('Approvals', 'Regulators must approve the aircraft, the sites and the operating rules before flights begin. Each approval is checked against safety standards.'),
        ('Redundancy', 'Important systems are duplicated, so that one failure does not lead to loss of control. Backup systems keep the aircraft safe while the crew or the system responds.'),
    ],
    'test': [
        ('Where do urban air mobility aircraft fly?', [('a', 'Deep under the sea'), ('b', 'Low over cities'), ('c', 'On the Moon'), ('d', 'In a forest canopy only')], 'b'),
        ('What are vertiports?', [('a', 'Landing and takeoff sites for these aircraft'), ('b', 'Shops for fish'), ('c', 'Parks for boats'), ('d', 'Mountain huts')], 'a'),
        ('Why use several sensors together?', [('a', 'They make the aircraft heavier'), ('b', 'They remove the pilot'), ('c', 'They give a safer picture than one alone'), ('d', 'They cost nothing')], 'c'),
        ('What must be mapped and avoided?', [('a', 'Towers, cranes and wires'), ('b', 'Clouds only'), ('c', 'Sunlight'), ('d', 'Rainbows')], 'a'),
        ('What is redundancy?', [('a', 'Throwing away spare parts'), ('b', 'Turning off all sensors'), ('c', 'Painting the aircraft twice'), ('d', 'Duplicated important systems so one failure does not lead to loss of control')], 'd'),
    ],
}
