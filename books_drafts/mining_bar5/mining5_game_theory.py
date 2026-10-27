"""Game Theory in Mineral Markets: how producers think about each other when they choose how much to produce and at what price."""
CODE = "mining5_game_theory"
BOOK = {'title': 'Game Theory in Mineral Markets',
 'subtitle': "How producers' choices depend on what their rivals will do",
 'chapters': [('Thinking about rivals',
               "Game theory studies choices where each side's result depends on the others' choices. In a "
               'market with few big producers, each one must think about what the others will do before '
               'deciding its own output or price.'),
              ('Cartels',
               'A cartel is a group of producers that agrees to limit output to keep prices high. Cartels '
               'are illegal in many countries, and they often break down because each member is tempted to '
               'produce more.'),
              ('Price setting',
               'When producers set prices, they weigh a higher price against losing customers to rivals. '
               'Their choices can lead to prices that look stable but hide competition.'),
              ('Entry deterrence',
               'An established producer may expand capacity to make it unprofitable for a newcomer to enter. '
               'This is called entry deterrence. It works only when the threat is believable.'),
              ('Cooperation',
               'Producers sometimes cooperate on safety, standards or shared infrastructure. Cooperation '
               'that is open and legal can help the whole market, while secret deals can break the law.'),
              ('Limits',
               'Game theory gives a way of thinking, not exact answers. Real markets have many players, '
               'changing costs and surprises, so the models are simplified guides.')],
 'test': [('What does game theory study?',
           [('a', 'The rules of football only'),
            ('b', 'The colour of rock'),
            ('c', "Choices where each side's result depends on the others' choices"),
            ('d', 'The speed of trucks')],
           'c'),
          ('What is a cartel?',
           [('a', 'A group of producers agreeing to limit output to keep prices high'),
            ('b', 'A map of a mine'),
            ('c', 'A type of drill'),
            ('d', 'A bank with no customers')],
           'a'),
          ('Why do cartels often break down?',
           [('a', 'Metal stops being valuable'),
            ('b', 'Mines close at noon'),
            ('c', 'Prices never change'),
            ('d', 'Each member may be tempted to produce more')],
           'd'),
          ('What is entry deterrence?',
           [('a', 'Locking the mine gate'),
            ('b', 'Expanding capacity so a newcomer finds entry unprofitable'),
            ('c', 'Selling the mine to a school'),
            ('d', 'Hiring fewer workers')],
           'b'),
          ('Why is secret cooperation a problem?',
           [('a', 'It makes ore heavier'),
            ('b', 'It makes trucks faster'),
            ('c', 'It can break the law'),
            ('d', 'It has no effect at all')],
           'c')]}
