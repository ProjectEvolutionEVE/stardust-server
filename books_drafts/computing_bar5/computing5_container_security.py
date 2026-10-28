"""Container and Kubernetes Security: keeping packaged applications and their clusters safe from image to runtime."""
CODE = 'computing5_container_security'
BOOK = {'title': 'Container and Kubernetes Security',
 'subtitle': 'Image scanning, least-privilege pods, admission control, network policies and '
             'runtime checks',
 'chapters': [('Packaged applications',
               'A container packs an application with what it needs to run. A cluster such as '
               'Kubernetes runs many containers across many machines. Each layer adds its own '
               'security questions.'),
              ('Image scanning',
               'Container images are built from layers of software that can carry known flaws. '
               'Scanning checks each image against lists of known weaknesses before it is used. '
               'Teams rebuild images when a fix arrives.'),
              ('Least-privilege pods',
               'A pod is the smallest unit of work in Kubernetes. It should run with only the '
               'rights and access it needs. Running as root or with extra powers gives an attacker '
               'more room.'),
              ('Admission control',
               'Admission control checks each request to create or change a workload and can '
               'refuse ones that break the rules. It is a gate that enforces policy automatically. '
               'Good rules are written down and tested.'),
              ('Network policies and secrets',
               'Network policies limit which pods may talk to which. Secrets such as passwords '
               'should be stored and shared with care, not written into images. Limiting both '
               'reduces the damage of a breach.'),
              ('Runtime detection',
               'Runtime tools watch running containers for unusual behaviour, such as an '
               'unexpected program starting. Detection gives a chance to respond before harm '
               'spreads. It complements scanning, which happens before running.')],
 'test': [('What does a container package?',
           [('a', 'A box of biscuits'),
            ('b', 'An application with what it needs to run'),
            ('c', 'A parcel of paper'),
            ('d', 'A bottle of water')],
           'b'),
          ('What does image scanning check?',
           [('a', 'The colour of the logo'),
            ('b', 'The weight of the server'),
            ('c', 'Images against lists of known weaknesses'),
            ('d', 'The number of coffee cups')],
           'c'),
          ('What does least privilege mean for a pod?',
           [('a', 'It runs with every right possible'),
            ('b', 'It runs without a name'),
            ('c', 'It runs only on Sundays'),
            ('d', 'It runs with only the rights and access it needs')],
           'd'),
          ('What does admission control do?',
           [('a', 'Checks requests to create workloads and can refuse ones that break rules'),
            ('b', 'Admits guests to a concert'),
            ('c', 'Counts the number of containers'),
            ('d', 'Paints the cluster')],
           'a'),
          ('What is runtime detection?',
           [('a', 'Timing a race on a track'),
            ('b', 'Measuring rainfall'),
            ('c', 'Watching running containers for unusual behaviour'),
            ('d', 'Checking the spelling of names')],
           'c')]}
