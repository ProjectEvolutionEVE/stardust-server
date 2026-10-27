"""Resource Block Models: building a block model from geology and estimates, checking it, keeping versions under audit, and handing it to planners."""
CODE = 'mining4_block_models'
BOOK = {'title': 'Resource Block Models',
 'subtitle': 'A checked 3D model of ore that planners can trust',
 'chapters': [('Domains and geology',
               'A block model starts with geology. The ore body is split into domains, each with its own '
               'rock types and grade range. Domains keep estimates within the rocks that actually control '
               'the ore.'),
              ('Estimation passes',
               'Grades are estimated in passes. The first pass uses the closest and best-supported samples. '
               'Later passes fill the blocks that remain, using wider search limits. Each pass is recorded '
               'in the model.'),
              ('Block size',
               'Blocks are the small cells that make up the model. Their size must suit the drill spacing '
               'and the mining method. Blocks that are too large hide detail, and blocks that are too small '
               'add noise.'),
              ('Model checks',
               'The model is checked against the input samples, the domains and the statistics. Estimated '
               'averages should match the data, and the model should not hide high-grade pockets. Checks are '
               'repeated after every change.'),
              ('Versioning and audit',
               'Each version of the model is saved with a date, a reason for the change and the person who '
               'made it. An audit trail shows how the model changed over time. Clear records protect the '
               'team and its investors.'),
              ('Handing models to planners',
               'When a model is handed to planners, it comes with its notes, its checks and its uncertainty. '
               'Planners use it to design pits or underground stopes and to schedule production. A clear '
               'handover prevents costly mistakes.')],
 'test': [('What is the first step in building a block model?',
           [('a', 'Splitting the ore body into domains based on geology'),
            ('b', 'Painting the blocks red'),
            ('c', 'Choosing a holiday'),
            ('d', 'Buying a new truck')],
           'a'),
          ('What do later estimation passes do?',
           [('a', 'Delete all the samples'),
            ('b', 'Change the rock to water'),
            ('c', 'Fill the blocks that remain, with wider search limits'),
            ('d', 'Stop the model from being saved')],
           'c'),
          ('Why must block size suit the drill spacing?',
           [('a', 'Block size has no effect'),
            ('b', 'Blocks too large hide detail and blocks too small add noise'),
            ('c', 'Blocks must always be one metre'),
            ('d', 'Blocks must be shaped like stars')],
           'b'),
          ('What does a model check compare?',
           [('a', 'The model with the weather'),
            ('b', 'The model with a recipe book'),
            ('c', 'The model with a sports score'),
            ('d', 'The model with the input samples, domains and statistics')],
           'd'),
          ('What does an audit trail show?',
           [('a', 'How the model changed over time, and who changed it'),
            ('b', 'The colour of each block'),
            ('c', 'The number of birds nearby'),
            ('d', 'The price of coffee')],
           'a')]}
