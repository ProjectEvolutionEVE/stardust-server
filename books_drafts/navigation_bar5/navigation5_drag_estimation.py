"""Estimating Atmospheric Drag: how air resistance high above Earth slowly lowers a satellite's orbit."""
CODE = 'navigation5_drag_estimation'
BOOK = {
    "title": 'Estimating Atmospheric Drag',
    "subtitle": 'Density models, ballistic coefficients, solar activity, orbit decay, estimates and errors',
    "chapters": [
        ('Density models',
         'Even high above Earth, the air is thin enough to slow a satellite a little. A density model gives the air density at each height. Drag estimates depend on this model.'),
        ('Ballistic coefficients',
         'The ballistic coefficient links a craft\'s mass, its shape and its drag. A compact, heavy craft has a high coefficient and feels less drag. A light, broad craft feels more.'),
        ('Solar activity',
         'The Sun\'s activity heats the upper atmosphere and makes it swell. A swollen atmosphere is denser at satellite heights. Solar activity changes the drag over days and years.'),
        ('Orbit decay',
         'Drag removes energy from the orbit, so the orbit slowly lowers. Eventually the satellite re-enters the atmosphere. The rate of decay grows as the orbit gets lower.'),
        ('Estimates',
         'Tracking data is used to estimate the drag and the density. The estimates are updated as new data arrives. Good estimates help predict when a satellite will re-enter.'),
        ('Errors',
         'The density models and solar activity are uncertain. Errors in them lead to errors in the predicted orbit. Predictions should carry a range that reflects this.'),
    ],
    "test": [
        ('What is a ballistic coefficient?',
         [('a', 'A sports score'), ('b', 'A fuel number'), ('c', 'A value linking a craft\'s mass, shape and drag'), ('d', 'A camera setting')], 'c'),
        ('Why does solar activity matter for drag?',
         [('a', 'It changes paint'), ('b', 'It changes music'), ('c', 'It changes shops'), ('d', 'It changes the density of the upper atmosphere')], 'd'),
        ('What is orbit decay?',
         [('a', 'Rotting fruit'), ('b', 'A slow lowering of an orbit caused by drag'), ('c', 'A rising orbit'), ('d', 'A broken camera')], 'b'),
        ('Why do drag estimates have errors?',
         [('a', 'The density models and solar activity are uncertain'), ('b', 'Satellites are always in shadow'), ('c', 'Paper is thin'), ('d', 'Drag is never felt')], 'a'),
        ('How are drag estimates used?',
         [('a', 'To predict re-entry and plan manoeuvres'), ('b', 'To cook meals'), ('c', 'To paint walls'), ('d', 'To measure rain')], 'a'),
    ],
}
