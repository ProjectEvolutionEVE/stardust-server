"""On-orbit Servicing: repairing, extending and refuelling craft that are already in space."""
CODE = 'flight5_a_servicing'
BOOK = {
    "title": 'On-orbit Servicing',
    "subtitle": 'Repairing and extending craft that are already in space',
    "chapters": [
        ('Why service in orbit',
         'Some craft are too valuable to lose, and some cannot be replaced quickly. Servicing lets a team repair or upgrade a craft where it flies. This can save a mission and the money spent on it.'),
        ('Hubble',
         'Astronauts from the Space Shuttle serviced the Hubble Space Telescope several times. They replaced instruments, batteries and gyroscopes, and the telescope became far more capable. It is the best-known example of crewed servicing.'),
        ('Solar Max and Intelsat 603',
         'In 1984 a Shuttle crew caught and repaired the Solar Maximum satellite, which had stopped working. In 1992 another crew rescued the Intelsat 603 communications satellite, which had been stranded in the wrong orbit. These rescues showed what was possible.'),
        ('Robotic servicers',
         'Robotic servicers are craft that can dock with another craft without a crew. Some have been built to extend the life of satellites by docking and providing a boost. This may become a regular service in future.'),
        ('Refuelling',
         'Refuelling a craft in orbit would let it keep working longer. Several designs have been developed, and the techniques are being tested. The main challenge is to join and transfer fuel safely.'),
        ('Economics',
         'Servicing costs money, but it can be cheaper than building a replacement. The value depends on the cost of the craft and the cost of a launch. Each case is worked out with care.'),
    ],
    "test": [
        ('Which craft was serviced by astronauts several times?',
         [('a', 'The Hubble Space Telescope'), ('b', 'A hot air balloon'), ('c', 'A paper kite'), ('d', 'A bicycle')], 'a'),
        ('What did the 1984 Shuttle crew do with Solar Maximum?',
         [('a', 'Caught and repaired it'), ('b', 'Painted it red'), ('c', 'Sank it'), ('d', 'Sold it')], 'a'),
        ('What is a robotic servicer?',
         [('a', 'A robot that cooks'), ('b', 'A craft that can dock with another craft without a crew'), ('c', 'A toy for the crew'), ('d', 'A ground vehicle')], 'b'),
        ('Why is refuelling in orbit useful?',
         [('a', 'It makes the craft heavier for no reason'), ('b', 'It stops the craft from moving'), ('c', 'It lets a craft keep working longer'), ('d', 'It stops the radio')], 'c'),
        ('What decides whether servicing is worth it?',
         [('a', 'The colour of the craft'), ('b', 'The weather at the launch site'), ('c', 'The name of the crew'), ('d', 'The cost of servicing compared with the cost of a replacement')], 'd'),
    ],
}
