"""Fatigue Crack Growth and the Paris Law: how a small crack grows a little more with each load cycle, and how to predict it."""
CODE = 'mining5_paris'
BOOK = {
    "title": 'Fatigue Crack Growth and the Paris Law',
    "subtitle": 'How a small crack grows a little more with each load cycle',
    "chapters": [
        ('Cracks that grow slowly', 'Many parts carry repeated loads, such as wings, bridges and shafts. A small crack can start and then grow a little with each cycle. Engineers plan inspections around this slow growth.'),
        ('Crack growth rate', 'The crack growth rate is how much the crack lengthens for each load cycle. It is very small at first and speeds up as the crack gets longer. Measuring it is the first step in any life estimate.'),
        ('Stress intensity range', 'The stress intensity range describes how hard the load is pulling at the crack tip. It depends on the load range, the crack length and the shape of the part. It is the quantity that drives the Paris law.'),
        ('Inspection intervals', 'The Paris law lets engineers estimate how many cycles a crack can take before it is too long. From that, they set inspection intervals. Regular checks catch a crack while it is still safe to repair.'),
        ('Testing and thresholds', 'A test shows the crack growth rate over a range of loads. Below a threshold, cracks may not grow at all. Testing finds both the rate and the threshold for each material.'),
        ('Design', 'Designers choose materials, shapes and surface finish to slow crack growth. Good finish and careful joints help too. A design that ignores crack growth can fail long before its planned life.'),
    ],
    "test": [
        ('What do repeated loads risk in parts like wings and bridges?', [('a', 'A sudden change of colour'), ('b', 'Small cracks that can grow with each cycle'), ('c', 'A quieter ride'), ('d', 'Lighter weight')], 'b'),
        ('What is the crack growth rate?', [('a', 'The speed of the wind'), ('b', 'The price of steel'), ('c', 'How much the crack lengthens per load cycle'), ('d', 'The number of bolts')], 'c'),
        ('What does the stress intensity range describe?', [('a', 'How many fish are in a river'), ('b', 'How loud a motor is'), ('c', 'The colour of a bridge'), ('d', 'How hard the load pulls at the crack tip')], 'd'),
        ('Why are inspections timed using the Paris law?', [('a', 'To catch a crack while it is still safe to repair'), ('b', 'To paint the part'), ('c', 'To make the part heavier'), ('d', 'To stop all loads forever')], 'a'),
        ('What is a threshold in crack testing?', [('a', 'A door to the lab'), ('b', 'A load below which cracks may not grow at all'), ('c', 'A type of bolt'), ('d', 'A paint colour')], 'b'),
    ],
}
