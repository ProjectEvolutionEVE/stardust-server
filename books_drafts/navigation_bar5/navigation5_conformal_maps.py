"""Conformal Maps and Complex Functions: angle preservation, the complex plane, holomorphic maps, the scale factor, the Cauchy-Riemann test and the construction of conformal maps."""
CODE = 'navigation5_conformal_maps'
BOOK = {
    "title": 'Conformal Maps and Complex Functions',
    "subtitle": 'Maps that keep every small angle true, and how mathematics builds them',
    "chapters": [
        ('Keeping angles',
         'A conformal map keeps the angles the same at every point. A small shape keeps its form, even though its size may change.'),
        ('The complex plane',
         'Points on the plane are written as complex numbers, x plus i times y. A map is then a rule that sends one complex number to another.'),
        ('Holomorphic maps',
         'A holomorphic function is a complex function that has a derivative. Such functions produce conformal maps wherever the derivative is not zero.'),
        ('The scale factor',
         'The local change of size at a point is given by the size of the derivative. This is called the scale factor, and it may differ from one point to another.'),
        ('The Cauchy-Riemann test',
         'Writing a complex function as u plus i times v, the Cauchy-Riemann equations give a test for whether the function is holomorphic. They are a simple pair of relations between the partial derivatives of u and v.'),
        ('Construction',
         'Mapmakers and mathematicians build conformal maps by choosing well-known functions and combining them, then checking the result against the required properties.'),
    ],
    "test": [
        ('What does a conformal map preserve?',
         [('a', 'Areas exactly'), ('b', 'Distances exactly'), ('c', 'Angles'), ('d', 'Colours')], 'c'),
        ('What is the complex plane?',
         [('a', 'Points written as x plus i times y'), ('b', 'A flat surface for flying'), ('c', 'A type of chart for sales'), ('d', 'A kind of bread')], 'a'),
        ('What is a holomorphic function?',
         [('a', 'A kind of food'), ('b', 'A type of ship'), ('c', 'A rock formation'), ('d', 'A complex function that has a derivative')], 'd'),
        ('What is the scale factor of a map?',
         [('a', 'The price of the map'), ('b', 'The size of the derivative, giving the local change in size'), ('c', 'The date of the map'), ('d', 'The number of corners on the map')], 'b'),
        ('What does the Cauchy-Riemann test check?',
         [('a', 'Whether a function is holomorphic'), ('b', 'Whether a map is painted correctly'), ('c', 'Whether a city exists'), ('d', 'Whether the sea is cold')], 'a'),
    ],
}
