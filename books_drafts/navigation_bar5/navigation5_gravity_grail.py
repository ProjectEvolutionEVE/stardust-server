"""Gravity Mapping with Twin Spacecraft: inter-satellite ranging, the gravity field, mass anomalies, resolution, the Moon interior and uses of the maps."""
CODE = 'navigation5_gravity_grail'
BOOK = {
    "title": 'Gravity Mapping with Twin Spacecraft',
    "subtitle": 'Two craft that measured the gravity of the Moon by flying one behind the other',
    "chapters": [
        ('Two craft, one measurement',
         'The GRAIL mission used two spacecraft flying one after the other around the Moon. The distance between them changed as they passed over areas of stronger or weaker gravity.'),
        ('Inter-satellite ranging',
         'The two craft measured the distance between them with microwave signals. They could detect changes far smaller than the width of a human hair, which gave a very sharp view of the gravity field.'),
        ('The gravity field',
         'From those changes, scientists built a detailed map of the gravity field of the Moon. The map reflects how mass is spread beneath the surface.'),
        ('Mass anomalies',
         'Places with extra mass show up as areas of stronger gravity. These anomalies are linked to dense material and to the ancient impacts that shaped the Moon.'),
        ('Resolution',
         'The maps revealed structures many kilometres across in the crust, giving far more detail than any earlier map. Finer structures need closer measurements.'),
        ('The Moon interior and uses',
         'The maps help scientists estimate how thick the crust of the Moon is and how its interior has changed over time. They also help plan landings and navigation around the Moon.'),
    ],
    "test": [
        ('How did GRAIL map the gravity of the Moon?',
         [('a', 'With a camera on the ground'), ('b', 'By sending a boat across the surface'), ('c', 'With two craft that measured the distance between them as they flew'), ('d', 'By listening to the Moon')], 'c'),
        ('What did the GRAIL ranging detect?',
         [('a', 'Sound from the Moon'), ('b', 'Smells in space'), ('c', 'Colours on the surface'), ('d', 'Changes in distance far smaller than the width of a hair')], 'd'),
        ('What does a mass anomaly do to gravity?',
         [('a', 'It makes gravity stronger in that place'), ('b', 'It makes gravity vanish'), ('c', 'It switches gravity off'), ('d', 'It turns gravity sideways')], 'a'),
        ('What did the GRAIL map reveal about the Moon?',
         [('a', 'That it is made mostly of water'), ('b', 'Details of its crust and interior structure'), ('c', 'That it is hollow inside'), ('d', 'That it has no gravity at all')], 'b'),
        ('What are the uses of the maps?',
         [('a', 'Painting posters'), ('b', 'Choosing music for missions'), ('c', 'Cooking food for astronauts'), ('d', 'Planning landings and navigation around the Moon')], 'd'),
    ],
}
