"""The Metre and Length Standards: the metre's definition, the speed of light, traceability, interferometry, standards and errors."""
CODE = 'navigation5_length_standard'
BOOK = {
    "title": 'The Metre and Length Standards',
    "subtitle": 'How the metre is defined, and how every length measurement links back to it',
    "chapters": [
        ('The metre\'s definition',
         'Since 1983 the metre has been defined by light. It is the distance light travels in a vacuum in a set fraction of a second. The definition is fixed, so the metre does not depend on any physical bar.'),
        ('The speed of light',
         'The speed of light is fixed at an exact value by definition. Because of this, a measured time can be turned into a length, and a length can be linked back to time with great precision.'),
        ('Traceability',
         'Traceability is an unbroken chain of calibrations that links a measurement back to a standard. Each link is checked, and each one adds a stated uncertainty. Without traceability, a measurement cannot be trusted across borders or over time.'),
        ('Interferometry',
         'Interferometry compares light waves to measure length very precisely. It is the method that makes the link between light and the metre practical in the workshop and the laboratory.'),
        ('Standards',
         'Standards are the reference artefacts and instruments that everyday measurements are compared against. They must be kept stable, checked regularly, and stored with care.'),
        ('Errors',
         'Length measurements are affected by instrument drift, temperature, air pressure and poor setup. Each error source should be listed, reduced where possible, and included in the stated uncertainty.'),
    ],
    "test": [
        ('How is the metre defined today?',
         [('a', 'As a bar kept in a vault'), ('b', 'As the distance light travels in a set fraction of a second'), ('c', 'As the length of a foot'), ('d', 'As the width of a hand')], 'b'),
        ('Why does the speed of light matter to the metre?',
         [('a', 'It fixes the definition, so length links to time'), ('b', 'It makes the metre longer'), ('c', 'It changes with the seasons'), ('d', 'It is irrelevant')], 'a'),
        ('What is traceability?',
         [('a', 'Tracing a lost ship'), ('b', 'Drawing lines on a map'), ('c', 'A type of paper'), ('d', 'An unbroken chain of calibrations linking a measurement back to a standard')], 'd'),
        ('What is interferometry used for?',
         [('a', 'Heating water'), ('b', 'Playing music'), ('c', 'Measuring length very precisely using light waves'), ('d', 'Growing food')], 'c'),
        ('What are main sources of error in length measurement?',
         [('a', 'Instrument drift, temperature and poor setup'), ('b', 'The colour of the room'), ('c', 'The name of the operator'), ('d', 'Clear weather')], 'a'),
    ],
}
