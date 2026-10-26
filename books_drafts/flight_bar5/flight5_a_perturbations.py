"""Perturbing Forces: the small pushes and pulls that bend an orbit away from the ideal shape."""
CODE = 'flight5_a_perturbations'
BOOK = {
    "title": 'Perturbing Forces',
    "subtitle": 'The small pushes and pulls that bend an orbit',
    "chapters": [
        ('The ideal orbit',
         'The textbook orbit has one large body and nothing else. Real craft feel many smaller effects that bend the orbit away from that ideal. These effects are called perturbations, and they must be modelled to plan a mission well.'),
        ('Third bodies',
         "The Sun and the Moon pull on a satellite as well as the Earth. Their pulls change the orbit slowly over time. For a satellite near the Earth, the Moon's pull is often one of the larger effects."),
        ('Light pressure',
         'Sunlight carries a tiny amount of momentum, and it pushes gently on every surface it strikes. For a large, light craft, this push can add up over months. Solar sails use this effect on purpose.'),
        ('Tides and the shape of the Earth',
         'The Earth is not a perfect sphere, and its bulge pulls on an orbiting craft. This makes the orbit drift at certain rates. Planners include this shape in their models.'),
        ('Relativity',
         "Einstein's theory of relativity makes small changes to orbital timing. For Earth satellites these effects are tiny but measurable. Precise navigation systems must account for them."),
        ('Choosing a model',
         'Planners choose which effects to include based on how large they are and how accurate the mission must be. Including too few effects gives wrong answers. Including all of them costs time. The best model is the one that is good enough.'),
    ],
    "test": [
        ('What are perturbations in an orbit?',
         [('a', 'Small effects that bend the orbit away from the ideal shape'), ('b', 'Colours on a satellite'), ('c', 'Mistakes in a radio'), ('d', 'Holes in a solar panel')], 'a'),
        ('Which other body often gives a larger pull on a near-Earth satellite than the others?',
         [('a', 'The Moon'), ('b', 'Mars'), ('c', 'Jupiter'), ('d', 'A distant star')], 'a'),
        ('What is light pressure?',
         [('a', 'The heat inside a battery'), ('b', 'A tiny push from sunlight on a surface'), ('c', 'The weight of the crew'), ('d', 'The pressure in a fuel tank')], 'b'),
        ('What is a solar sail designed to use?',
         [('a', "The Moon's tides"), ('b', 'Air drag at ground level'), ('c', 'Light pressure from the Sun'), ('d', "The Earth's magnetic field only")], 'c'),
        ('Why do planners choose which effects to include in a model?',
         [('a', 'To make the drawings look nicer'), ('b', 'To hide the effects from the crew'), ('c', 'To make the craft heavier'), ('d', 'To balance accuracy against the time the model takes')], 'd'),
    ],
}
