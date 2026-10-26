"""Mars Rovers: from the small Sojourner to Perseverance and Zhurong, and how rovers learned to drive themselves."""
CODE = 'flight5_mars_rovers'
BOOK = {'title': 'Mars Rovers',
 'subtitle': 'Explorers that drive across another planet',
 'chapters': [('Sojourner',
               'Sojourner was the first rover to drive on Mars, in 1997. It was small, about the size of a '
               'microwave oven. It showed that a rover could explore the surface of another planet.'),
              ('Spirit and Opportunity',
               'Spirit and Opportunity landed in 2004 and drove far beyond their planned lifetimes. They '
               'found evidence that water once flowed on Mars. Their long missions taught engineers much '
               'about rover design.'),
              ('Curiosity',
               'Curiosity landed in 2012 using a sky crane. It is much larger than the earlier rovers and '
               'carries many instruments. It has studied the rocks of an ancient lake bed.'),
              ('Perseverance',
               'Perseverance landed in 2021 and carries tools to look for signs of past life. It collects '
               'rock samples in sealed tubes. Those samples are planned for return to Earth in future '
               'missions.'),
              ('Zhurong',
               "Zhurong landed in 2021 as part of China's Tianwen-1 mission. It explored a plain on Mars and "
               'sent back data. Its work added to the global picture of the planet.'),
              ('Driving autonomy',
               'Mars is far away, so signals take many minutes to travel each way. Rovers therefore need to '
               'make some decisions by themselves. Their autonomous systems help them avoid rocks and choose '
               'safe paths.')],
 'test': [('Which was the first rover to drive on Mars?',
           [('a', 'Curiosity'), ('b', 'Sojourner'), ('c', 'Perseverance'), ('d', 'Zhurong')],
           'b'),
          ('What did Spirit and Opportunity find evidence of?',
           [('a', 'That Mars has oceans of oil'),
            ('b', 'That Mars is made of ice cream'),
            ('c', 'That water once flowed on Mars'),
            ('d', 'That Mars has no rocks')],
           'c'),
          ('How does Curiosity land?',
           [('a', 'By parachute into the sea'),
            ('b', 'By bouncing on airbags only'),
            ('c', 'By landing on a train'),
            ('d', 'With a sky crane')],
           'd'),
          ('Why must Mars rovers make some decisions on their own?',
           [('a', 'Radio signals take many minutes each way'),
            ('b', 'They have no wheels'),
            ('c', 'They are powered by wind'),
            ('d', 'They cannot see')],
           'a'),
          ('What does Perseverance collect in sealed tubes?',
           [('a', 'Sea water'), ('b', 'Rock samples'), ('c', 'Sand from beaches'), ('d', 'Ice cream')],
           'b')]}
