"""Chloride Ingress and Concrete Durability: diffusion, cover depth, service life, rebar corrosion and the money side of repair."""
CODE = 'engineering5_chloride'
BOOK = {'title': 'Chloride Ingress and Concrete Durability',
 'subtitle': 'How salt gets into concrete, how deep steel is buried, and what repairs cost',
 'chapters': [('Where chlorides come from',
               'Chlorides come from sea water, sea air and de-icing salt spread on roads. They can also '
               'enter through the mix itself. Once in the concrete, they can reach the steel reinforcing '
               'bars inside.'),
              ('Diffusion',
               'Chlorides move through concrete mainly by diffusion, which is slow movement from high '
               'concentration to low. The rate depends on the quality of the concrete. Dense, well-cured '
               'concrete slows the movement a great deal.'),
              ('Cover depth',
               'Cover is the thickness of concrete over the steel. More cover means chlorides must travel '
               'further before reaching the bar. Cover is one of the simplest and most effective protections '
               'in design.'),
              ('Service life models',
               'A service life model splits life into two stages. The first is the time for chlorides to '
               'reach the steel. The second is the time for corrosion to damage the structure. Designers use '
               'both stages when they set the expected life.'),
              ('Rebar corrosion',
               'When chlorides reach the steel, the bar can begin to corrode. Rust takes up more space than '
               'the steel it replaces, so it cracks and spalls the concrete. The damage is hard to see until '
               'it is well advanced.'),
              ('The money side of repair',
               'Repairing corroded concrete costs far more than protecting it at the start. Repairs may need '
               'the concrete cut out and replaced, and the work can close a structure for weeks. Good cover '
               'and dense concrete are the cheaper choice over the life.')],
 'test': [('Where do chlorides in concrete mainly come from?',
           [('a', 'Sugar in the cement'),
            ('b', 'Sea water, sea air and de-icing salt'),
            ('c', 'Sunlight on the surface'),
            ('d', 'Wind through the trees')],
           'b'),
          ('What is cover in reinforced concrete?',
           [('a', 'The paint on the surface'),
            ('b', 'The lid of a skip'),
            ('c', 'The thickness of concrete over the steel'),
            ('d', 'The name of the builder')],
           'c'),
          ('What happens to steel bars when chlorides reach them?',
           [('a', 'They turn into glass'),
            ('b', 'They become lighter'),
            ('c', 'They disappear overnight'),
            ('d', 'They can begin to corrode')],
           'd'),
          ('What does rust do to the concrete around it?',
           [('a', 'It cracks and spalls the concrete as it expands'),
            ('b', 'It makes the concrete stronger'),
            ('c', 'It fills every crack'),
            ('d', 'It changes the concrete to wood')],
           'a'),
          ('Why is protection at the start cheaper than repair?',
           [('a', 'Because repairs are always free'),
            ('b', 'Because repairs may need concrete cut out and replaced'),
            ('c', 'Because repairs never happen'),
            ('d', 'Because concrete does not need protecting')],
           'b')]}
