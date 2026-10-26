"""Relative Dating: working out which thing came first in rock and on a planet's surface, without a clock."""
CODE = 'science3a_relative_dating'
BOOK = {
    "title": 'Reading Layers and Craters',
    "subtitle": 'Relative dating: which thing came first, without needing a clock',
    "chapters": [
        ("Which came first",
         "You can work out the order of events in rock without knowing their exact ages. Geologists use a few simple rules to put events in sequence, like the pages of a story in order."),
        ("Superposition",
         "In an undisturbed stack of rock layers, the lowest layer is the oldest. The Danish scientist Nicolas Steno stated this idea in 1669, and it is still the first rule taught to geologists."),
        ("Cutting across",
         "A fault, or a body of molten rock that pushes into other rock, is younger than the layers it cuts through. The cut must happen after the layers were already there."),
        ("Inclusions",
         "A fragment of one rock trapped inside another is older than the rock that holds it. The fragment had to exist before it was caught up in the new rock."),
        ("Counting craters",
         "On a planet's surface, an area with many craters is usually older than one with few. Craters keep piling up over time. On the Moon, the dark lava plains have fewer craters than the bright, rugged highlands, so they are younger."),
        ("Order, not years",
         "Relative dating gives a sequence of events, not a number of years. To put an actual age on a rock, scientists need a radioactive clock, which is the subject of the next book."),
    ],
    "test": [
        ("Which rule says the lowest layer in an undisturbed stack is the oldest?",
         [('a', 'Cross-cutting'), ('b', 'Superposition'), ('c', 'Inclusion'), ('d', 'Half-life')], 'b'),
        ("A fault cuts through three rock layers. How old is the fault compared with those layers?",
         [('a', 'Older than all of them'), ('b', 'The same age as the bottom layer'), ('c', 'Younger than the layers it cuts'), ('d', 'Impossible to tell'), ], 'c'),
        ("On a planet's surface, which area is generally older?",
         [('a', 'The area with few craters'), ('b', 'The area with the most ice'), ('c', 'The area with the most lava flows'), ('d', 'The area with many craters')], 'd'),
        ("What does relative dating tell you?",
         [('a', 'The order in which events happened'), ('b', 'The exact age in years'), ('c', 'The weight of a rock'), ('d', 'The temperature of the core')], 'a'),
        ("A rock fragment is trapped inside a larger rock. Which is older?",
         [('a', 'The larger rock that holds it'), ('b', 'The fragment, which had to exist first'), ('c', 'Neither, they are the same age'), ('d', 'It depends on the colour')], 'b'),
    ],
}
