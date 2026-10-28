"""Material Flow Analysis: tracking how much of a material enters, sits in, and leaves an economy, and checking that the books balance."""
CODE = "mining5_mfa"
BOOK = {'title': 'Material Flow Analysis',
 'subtitle': 'Following a material through the economy, from source to stock to waste',
 'chapters': [('Stocks and flows',
               'Material flow analysis counts the material that moves into and out of a process, and the '
               'stock that stays in place. Stocks grow when inflow is larger than outflow.'),
              ('Mass balance',
               'Mass balance is the rule that matter cannot vanish. The inputs must equal the outputs plus '
               'any change in stock. If the numbers do not balance, a flow has been missed or measured '
               'wrongly.'),
              ('Uncertainty',
               'Some flows are hard to measure, such as metal lost in small products. Analysts give a range '
               'for these values and say how confident they are.'),
              ('Data sources',
               'Sources include trade statistics, production records, surveys and company reports. Each '
               'source has its own gaps and biases, so analysts check them against each other.'),
              ('Use of the results',
               'Results show where a material is lost, where stocks are building up and where recycling '
               'could help. They guide policy and business choices.'),
              ('Keeping it simple',
               'A simple, clear map of flows is more useful than a complex one that nobody reads. Start with '
               'the largest flows and add detail where it changes the answer.')],
 'test': [('What does material flow analysis count?',
           [('a', 'The number of birds at a mine'),
            ('b', 'The colour of the logo'),
            ('c', 'Material moving into and out of a process, and the stock that stays'),
            ('d', 'The price of coffee')],
           'c'),
          ('What is mass balance?',
           [('a', 'Matter cannot vanish, so inputs equal outputs plus any change in stock'),
            ('b', 'A scale used to weigh staff'),
            ('c', 'A bank loan rule'),
            ('d', 'A shape of a truck')],
           'a'),
          ('What do analysts do with uncertain flows?',
           [('a', 'Leave them out and never mention them'),
            ('b', 'Guess one number and stop'),
            ('c', 'Rename them'),
            ('d', 'Give a range and say how confident they are')],
           'd'),
          ('What does it mean when the numbers do not balance?',
           [('a', 'The material has been destroyed'),
            ('b', 'A flow has been missed or measured wrongly'),
            ('c', 'The results are final'),
            ('d', 'The metal is valueless')],
           'b'),
          ('What makes a flow map most useful?',
           [('a', 'Making it as complex as possible'),
            ('b', 'Hiding the sources'),
            ('c', 'Starting with the largest flows and adding detail where it changes the answer'),
            ('d', 'Drawing it in one colour only')],
           'c')]}
