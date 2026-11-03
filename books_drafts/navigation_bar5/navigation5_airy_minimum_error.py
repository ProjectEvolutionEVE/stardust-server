"""Airy's Minimum-Error Projection: the 1861 idea, balancing errors, choosing the boundary, the mathematical solution, worked examples and the legacy."""
CODE = 'navigation5_airy_minimum_error'
BOOK = {
    "title": "Airy's Minimum-Error Projection",
    "subtitle": 'An early plan for laying out a map so that its errors are as small as possible',
    "chapters": [
        ('The 1861 idea',
         'In 1861 George Biddell Airy, the Astronomer Royal of Britain, proposed a way to lay out a map so that its errors were as small as possible over a chosen region.'),
        ('Balancing errors',
         'Every flat projection has some error. The idea of Airy was to spread the errors so that the largest of them is as small as possible, rather than letting them pile up in one place.'),
        ('The boundary',
         'The choice of boundary matters. Airy set the edge of the region with care, because errors often grow near the edge of a map.'),
        ('The solution',
         'The solution is found by mathematical minimisation. The projection is adjusted until no small change can reduce the total error that the method is designed to limit.'),
        ('Worked examples',
         'Airy applied his method to small regions. The examples show how the errors are distributed, and how they are smallest near the centre of the map.'),
        ('Legacy',
         'The work of Airy is one of the early examples of a mapmaker deliberately minimising errors. Later projections built on similar ideas of balancing error.'),
    ],
    "test": [
        ('In what year did Airy propose his idea?',
         [('a', '1861'), ('b', '1961'), ('c', '1801'), ('d', '1916')], 'a'),
        ('What was the main goal of the method?',
         [('a', 'To make maps bigger'), ('b', 'To remove the sea from the map'), ('c', 'To balance errors across the region'), ('d', 'To paint the land in colour')], 'c'),
        ('Why is the boundary of the region chosen carefully?',
         [('a', 'To change the colour of the map'), ('b', 'To hide the sea'), ('c', 'To add another city to the map'), ('d', 'Because errors often grow near the edge')], 'd'),
        ('How is the solution found?',
         [('a', 'By guessing the best shape'), ('b', 'By mathematical minimisation'), ('c', 'By painting the map'), ('d', 'By asking a bird')], 'b'),
        ("What is Airy's legacy?",
         [('a', 'A type of ship'), ('b', 'A popular song'), ('c', 'An early example of deliberately minimising map errors'), ('d', 'The discovery of a new planet')], 'c'),
    ],
}
