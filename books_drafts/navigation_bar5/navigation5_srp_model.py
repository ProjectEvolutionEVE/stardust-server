"""Solar Radiation Pressure Models: estimating the small push that sunlight gives a spacecraft."""
CODE = 'navigation5_srp_model'
BOOK = {
    "title": 'Solar Radiation Pressure Models',
    "subtitle": 'Momentum transfer, area-to-mass ratio, box-wing models, estimation and errors',
    "chapters": [
        ('Momentum transfer',
         'Light carries momentum. When sunlight hits a spacecraft and is absorbed or reflected, it gives the spacecraft a small push. This push is solar radiation pressure.'),
        ('Area-to-mass ratio',
         'The area-to-mass ratio compares how much sunlit area a spacecraft presents with its mass. A large, light craft feels a bigger push than a small, heavy one. This ratio is a key input to the model.'),
        ('Box-wing models',
         'A box-wing model is a simple shape model of a spacecraft, built from boxes and flat panels. Each panel has its own size, direction and surface type. The model gives the total push from the sum of the panels.'),
        ('Estimation',
         'The model\'s values can be estimated from tracking data. Adding them to the orbit estimate improves predictions. The estimate is updated as more data arrives.'),
        ('Errors',
         'Surface properties and the spacecraft\'s attitude are often uncertain. Solar output also varies over time. These errors can change the predicted path over weeks or months.'),
        ('Practice',
         'Model the largest effects first and check the results against tracking. Keep the model as simple as the mission allows. Report the uncertainty of the push together with the orbit.'),
    ],
    "test": [
        ('What is solar radiation pressure?',
         [('a', 'A small push from sunlight\'s momentum'), ('b', 'Heat from a stove'), ('c', 'A camera'), ('d', 'Noise')], 'a'),
        ('What is the area-to-mass ratio?',
         [('a', 'The size of a map'), ('b', 'How much area a spacecraft presents per unit of mass, which affects the push'), ('c', 'Paper weight'), ('d', 'Price per kilo')], 'b'),
        ('What is a box-wing model?',
         [('a', 'A shipping crate'), ('b', 'A box of cereal'), ('c', 'A game'), ('d', 'A simplified shape model of a spacecraft\'s panels and body used to compute the push')], 'd'),
        ('Why estimate the push from sunlight?',
         [('a', 'To paint it'), ('b', 'To sell it'), ('c', 'To predict orbit changes accurately'), ('d', 'To remove the Sun')], 'c'),
        ('What is a source of error in this model?',
         [('a', 'The Sun is never hot'), ('b', 'The spacecraft\'s surface properties and attitude are often uncertain'), ('c', 'The stars'), ('d', 'The sky')], 'b'),
    ],
}
