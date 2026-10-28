"""Substituting Scarce Materials: when one material can replace another, what it costs in performance, and the risks of switching."""
CODE = "mining5_substitution"
BOOK = {'title': 'Substituting Scarce Materials',
 'subtitle': 'Swapping a scarce material for another, and what the swap costs',
 'chapters': [('Why substitute',
               'Engineers substitute when a material becomes scarce or expensive. A cheaper, more available '
               'material can keep a product affordable and reduce supply risk.'),
              ('Substitution limits',
               "Not every material can be replaced. Some jobs need a metal's special properties, such as its "
               'conductivity or its strength at high heat. Substitutes often fall short in those cases.'),
              ('Performance trade-offs',
               'A substitute may be heavier, weaker or less efficient. Engineers test the swap to see '
               'whether the product still works well enough for its purpose.'),
              ('Cost',
               'The cheapest material on paper may not be the cheapest product. Redesign, testing and '
               'certification all add cost, so the full cost of the switch must be counted.'),
              ('Examples',
               'Aluminium is used in some electrical cables where copper is too costly, and fibre-optic '
               'cable has replaced copper in many communication links. Each swap was judged on performance '
               'and price.'),
              ('Risks',
               'A switch can create new risks, such as a new supply chain or a material with its own '
               'environmental impact. A careful study checks the whole life of the substitute.')],
 'test': [('Why do engineers substitute materials?',
           [('a', 'The material is too bright'),
            ('b', 'The factory has too many windows'),
            ('c', 'A material becomes scarce or expensive'),
            ('d', 'The staff prefer another colour')],
           'c'),
          ('Why can some metals not be substituted easily?',
           [('a', 'Their special properties are needed for the job'),
            ('b', 'They are always free'),
            ('c', 'They are too small to see'),
            ('d', 'They are illegal to use')],
           'a'),
          ('What is a common trade-off of a substitute?',
           [('a', 'It always lasts longer and weighs less'),
            ('b', 'It costs nothing to test'),
            ('c', 'It removes all risk'),
            ('d', 'It may be heavier, weaker or less efficient')],
           'd'),
          ('Why must the full cost of a switch be counted?',
           [('a', 'Costs are never added up'),
            ('b', 'Redesign, testing and certification all add cost'),
            ('c', 'Cheapest material always wins'),
            ('d', 'Costs only matter on Sundays')],
           'b'),
          ('What can a switch create?',
           [('a', 'A guaranteed lower price for ever'),
            ('b', 'No change at all'),
            ('c', 'New supply-chain or environmental risks'),
            ('d', 'A ban on all metals')],
           'c')]}
