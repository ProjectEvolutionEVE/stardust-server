"""Lindbergh's Atlantic flight: the prize, the plane, the planning, the crossing and the navigation lessons."""
CODE = 'flight5_lindbergh'
BOOK = {
    "title": "Lindbergh's Atlantic Flight",
    "subtitle": 'The nonstop crossing from New York to Paris in 1927',
    "chapters": [
        ('The prize',
         'In 1919 a hotel owner named Raymond Orteig offered a prize of $25,000 for the first nonstop flight between New York and Paris. Many pilots tried for it, and several were lost. The prize drew great attention to long-distance flying.'),
        ('The plane',
         'Charles Lindbergh chose a single-engine plane built for the trip and named it the Spirit of St. Louis. It had no radio and no forward window, so he flew with a periscope and a compass. The plane was built light, with extra fuel carried in place of comforts.'),
        ('The planning',
         'Lindbergh planned the route with great care, and he studied the weather before he flew. He chose a route that gave him the best winds and the shortest distance over the sea. He flew alone, so every choice was his to make.'),
        ('The flight',
         'He took off from New York on 20 May 1927 and landed in Paris about 33 and a half hours later. He stayed awake through the night by keeping busy and using his instruments. His landing in Paris drew a huge crowd.'),
        ('Navigation',
         'Without modern radio beacons, he used dead reckoning, working out his position from his speed, heading and time flown. He also used stars and the sea to check the course. Careful calculation kept him on track across the whole ocean.'),
        ('Lessons',
         'His flight showed the value of preparation, simple tools used well, and steady calculation. A small team of planners and engineers helped him get ready. The lesson for players is that a long journey is won by planning each leg before you leave the ground.'),
    ],
    "test": [
        ('How much was the Orteig Prize?',
         [('a', '$25,000'), ('b', '$2,500'), ('c', '$250,000'), ('d', '$1,000')], 'a'),
        ("What was the name of Lindbergh's plane?",
         [('a', 'Flying Eagle'), ('b', 'Spirit of St. Louis'), ('c', 'Atlantic Star'), ('d', 'Paris Arrow')], 'b'),
        ('Roughly how long did the crossing take?',
         [('a', 'About 3 hours'), ('b', 'About 3 days'), ('c', 'About 33 and a half hours'), ('d', 'About 3 weeks')], 'c'),
        ('What is dead reckoning?',
         [('a', 'Flying by radio beacon only'), ('b', 'Landing without wheels'), ('c', 'Following other planes'), ('d', 'Working out a position from speed, heading and time')], 'd'),
        ('Which lesson did the flight teach most clearly?',
         [('a', 'Good preparation and steady calculation make long journeys possible'), ('b', 'Flights are best flown with no planning'), ('c', 'Fast planes never need weather checks'), ('d', 'Long flights need a crowd on board')], 'a'),
    ],
}
