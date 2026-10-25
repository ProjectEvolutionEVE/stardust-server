"""Measuring and Tolerances: units, precision and the small gaps that decide whether a part fits."""
CODE = 'engineering1_measuring'
BOOK = {
    "title": 'Measuring and Tolerances',
    "subtitle": 'Units, precision and the small gaps that decide whether a part fits',
    "chapters": [
        ('One set of units',
         'Every measurement needs a unit, and everyone on a job must use the same one. The metre is the standard unit of '
         'length, the kilogram the unit of mass, and the second the unit of time. The blueprint form works in kilograms, so '
         'write your amounts the same way.'),
        ('Accuracy and precision',
         'Accuracy is how close a measurement is to the true value. Precision is how finely you can read it, and how well '
         'repeated readings agree. A ruler marked in millimetres can be read to about half a millimetre by eye. A micrometer '
         'can read to a hundredth of a millimetre.'),
        ('Tolerance',
         'A tolerance is how much a size may vary and still work. A shaft drawn at 20.00 mm with a tolerance of plus or minus '
         '0.05 mm can measure anywhere from 19.95 to 20.05 mm and still fit. Tight tolerances cost more to make, so engineers '
         'set them only where a part needs them.'),
        ('Measure twice, cut once',
         'Check every measurement before you cut or drill. Mark clearly with a sharp pencil or scriber, measure from one '
         'reference edge, and check that your square is square. Write the number down and read it back, which catches most '
         'mistakes.'),
        ('Allowing for the cut and the heat',
         'A saw blade removes a little material, called the kerf, so leave it out of your count and every cut comes up short. '
         'Metal also grows when hot. Steel grows about 12 millionths of its length for each degree Celsius, so a 1 m steel bar '
         'grows about 0.012 mm for each degree.'),
        ('Real practice',
         'Working engineers check their measuring tools against a known standard, measure at the temperature the part will '
         'really be used, and record every result. Write each number with its unit, and round only at the very end.'),
    ],
    "test": [
        ("What is the standard unit of length?",
         [("a", "The foot"), ("b", "The metre"), ("c", "The kilogram"), ("d", "The second")], "b"),
        ("What does a tolerance describe?",
         [("a", "The colour of a part"), ("b", "The price of a material"), ("c", "How much a size may vary and still work"), ("d", "How long a build takes")], "c"),
        ("Which of these can read to about a hundredth of a millimetre?",
         [("a", "A micrometer"), ("b", "A ruler marked in centimetres"), ("c", "A paving slab"), ("d", "The length of your arm")], "a"),
        ("What does 'measure twice, cut once' mean?",
         [("a", "Cut twice as often"), ("b", "Check each measurement before you cut, to avoid waste"), ("c", "Measure with two different tools"), ("d", "Cut two pieces at once")], "b"),
        ("What happens to a 1 m steel bar as it gets hotter?",
         [("a", "It shrinks"), ("b", "It stays exactly the same"), ("c", "It grows by about 0.012 mm for each degree Celsius"), ("d", "It turns to gas")], "c"),
    ],
}
