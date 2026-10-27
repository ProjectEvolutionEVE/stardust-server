"""Cluster Schedulers: deciding which job runs on which machine, and how to share a large cluster fairly."""
CODE = 'computing5_cluster_schedulers'
BOOK = {'title': 'Cluster Schedulers',
 'subtitle': 'Packing jobs, fairness, preemption and gang scheduling',
 'chapters': [('Packing jobs onto machines',
               'A cluster scheduler decides where each job runs. Good placement keeps machines '
               'busy without overloading any one of them. The scheduler is one of the most '
               'important parts of a large cluster.'),
              ('Bin packing',
               'Placing jobs is like packing boxes into a set of bins. Finding the best packing is '
               'very hard in general, so schedulers use good rules of thumb. The aim is to waste '
               'as little space as possible.'),
              ('Fairness',
               'Many teams share one cluster, and each expects a fair share. Fair schedulers give '
               'each group its share and let spare capacity flow to whoever needs it. Fairness '
               'rules must be easy to explain.'),
              ('Preemption',
               'Preemption stops a running job so that a more important one can start. The stopped '
               'job is saved or restarted later. Preemption keeps urgent work moving at some cost '
               'to the stopped job.'),
              ('Gang scheduling',
               'Some jobs need all their parts to run together, or none at all. Gang scheduling '
               'starts them as a group. Without it, half-started jobs can sit waiting and waste '
               'the cluster.'),
              ('Lessons from large clusters',
               'Large cluster managers have shown that simple rules, careful measurement and clear '
               'priorities work better than clever ideas alone. Teams that run clusters learn to '
               'expect failure and plan for it.')],
 'test': [('What does a cluster scheduler decide?',
           [('a', 'The colour of the racks'),
            ('b', 'Which machine each job runs on'),
            ('c', 'The weather outside'),
            ('d', 'The menu in the canteen')],
           'b'),
          ('What is bin packing?',
           [('a', 'Packing lunch boxes'),
            ('b', 'Storing paper files'),
            ('c', 'Fitting items into containers with as little waste as possible'),
            ('d', 'Shipping cars')],
           'c'),
          ('What does preemption do?',
           [('a', 'Starts every job at once'),
            ('b', 'Turns off the cluster for ever'),
            ('c', 'Deletes all logs'),
            ('d', 'Stops a running job so a more important one can start')],
           'd'),
          ('What does gang scheduling do?',
           [('a', 'Starts all parts of a job together, or none at all'),
            ('b', 'Puts jobs in a gang of thieves'),
            ('c', 'Runs each part a day apart'),
            ('d', 'Stops every job for lunch')],
           'a'),
          ('What is the aim of a fair scheduler?',
           [('a', 'The biggest group always wins'),
            ('b', 'Nobody ever gets any work'),
            ('c', 'Each group gets its share, and spare capacity can be used'),
            ('d', 'Jobs run in alphabetical order only')],
           'c')]}
