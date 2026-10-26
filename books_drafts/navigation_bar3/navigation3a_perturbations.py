"""Perturbations: the small pushes and pulls that bend an orbit away from its clean oval, and how navigators allow for them."""
CODE = 'navigation3a_perturbations'
BOOK = {
    "title": 'Perturbations: Why Orbits Drift',
    "subtitle": 'The small pushes that bend a clean orbit, and how to allow for them',
    "chapters": [
        ('A clean oval is an ideal',
         "The orbit of Kepler's laws assumes one body pulling on another and nothing else. Real orbits have many small pushes and pulls. These add up and bend the path, and astronomers call them perturbations."),
        ('Other planets pull too',
         'Jupiter is by far the largest planet, and its pull nudges the orbits of the others. Over long spans, these nudges change the shape and the tilt of the orbits. Planners include them in every long-range ephemeris.'),
        ('Pressure from sunlight',
         'Sunlight carries a little momentum, and it pushes gently on any surface it hits. For a craft with a large, light sail or panel, this push is large enough to change its path over time. For most large bodies it is much smaller.'),
        ('The bulge of a planet',
         'The Earth is slightly flattened and bulges at the equator. This bulge pulls harder on satellites in some orbits than a perfect sphere would, which turns the orbit slowly. A sun-synchronous satellite uses exactly this turning, so that it passes overhead at the same local time each day.'),
        ('Drag where there is air',
         'Close to a planet with air, even a thin layer slows a craft and lowers its orbit. Far from any air, this drag is gone. A navigator in deep space therefore has to plan for different pushes than one in low Earth orbit.'),
        ('Plan the correction',
         'A good navigator checks the orbit against new data and plans small corrections early. A small correction made soon costs less fuel than a large one made late. This is where error budgets and fuel plans meet.'),
    ],
    "test": [
        ('What is a perturbation in an orbit?',
         [('a', 'A type of rocket'), ('b', 'A kind of star'), ('c', 'A fault in a chart'), ('d', 'A small push or pull that bends the orbit away from a clean oval')], 'd'),
        ('Which planet is by far the largest, and so has the biggest pull on the others?',
         [('a', 'Mars'), ('b', 'Jupiter'), ('c', 'Mercury'), ('d', 'Venus')], 'b'),
        ('Why does sunlight push on a craft?',
         [('a', 'Because light carries a little momentum'), ('b', 'Because light is heavy'), ('c', 'Because the Sun is cold'), ('d', 'Because craft are magnetic')], 'a'),
        ('What does the bulge of a planet do to a satellite orbit?',
         [('a', 'It stops the orbit'), ('b', 'It makes the satellite hotter'), ('c', 'It turns the orbit slowly, as used by sun-synchronous satellites'), ('d', "It reverses the satellite's direction")], 'c'),
        ('Why does a navigator plan for drag only near a planet with air?',
         [('a', 'Because drag only acts on the Moon'), ('b', 'Because drag is caused by the Sun'), ('c', 'Because drag makes craft faster in deep space'), ('d', 'Because drag acts only where there is air to slow a craft')], 'd'),
    ],
}
