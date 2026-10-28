"""Hazard mapping for mine sites: hazard registers, risk matrices, zone maps, updating and audits."""
CODE = 'mining5_hazard_map'
BOOK = {
    'title': 'Hazard Mapping for Mine Sites',
    'subtitle': 'Knowing where harm could happen, and keeping that knowledge current',
    "chapters": [
        ('What is a hazard', 'A hazard is something that could cause harm, such as a steep wall, a fuel spill or moving machinery. Knowing a hazard is the first step to controlling it.'),
        ('The hazard register', 'A hazard register lists each hazard, where it is and who could be harmed. It is the master list the map is built from.'),
        ('Risk matrices', 'A risk matrix rates each hazard by how likely it is and how severe the harm could be. The rating shows which hazards need action first.'),
        ('Zone mapping', 'Zones on a map show where each hazard applies. People can see which areas need care, a permit or a closure.'),
        ('Keeping it current', 'A map is updated when the site changes, and after any incident or near miss. An old map can be more dangerous than no map.'),
        ('Communicating and auditing', 'Workers must be told about the map and its changes. Audits check that the map matches what really happens on site.'),
    ],
    "test": [
        ('What is a hazard?', [('a', 'A type of rock'), ('b', 'A shift pattern'), ('c', 'Something that could cause harm'), ('d', 'A kind of truck tyre')], 'c'),
        ('What does a hazard register list?', [('a', 'The price of each hazard'), ('b', 'Each hazard, where it is and who could be harmed'), ('c', 'The names of the trucks'), ('d', 'The weather for each week')], 'b'),
        ('What does a risk matrix rate?', [('a', 'The colour of each zone'), ('b', 'The number of lights on a shaft'), ('c', 'The age of each machine'), ('d', 'How likely a hazard is and how severe the harm could be')], 'd'),
        ('When should a hazard map be updated?', [('a', 'When the site changes and after an incident or near miss'), ('b', 'Only once a decade'), ('c', 'Only when the auditors visit'), ('d', 'Never, once it is printed')], 'a'),
        ('What do audits check?', [('a', 'How many pens the office has'), ('b', 'The brightness of the screens'), ('c', 'Whether the map is printed in colour'), ('d', 'That the map matches what happens on site')], 'd'),
    ],
}
