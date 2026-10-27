"""Stuxnet: an industrial control worm, targeting of controllers, air gaps, discovery, attribution and lessons for critical systems."""
CODE = 'computing5_stuxnet'
BOOK = {
    "title": 'Stuxnet',
    "subtitle": 'A worm that aimed at machinery, not at data',
    "chapters": [
        ('An industrial control worm',
         'Stuxnet was a computer worm discovered in 2010 that targeted industrial control systems. It was unusual because it aimed to manipulate physical machinery rather than to steal data. Industrial targets are very different from office computers.'),
        ('Targeting controllers',
         'The worm searched for specific programmable logic controllers made by one manufacturer, which are used to run industrial processes. Only systems matching a precise profile were affected. Its design suggested a carefully planned attack.'),
        ('Air gaps',
         'Target systems were often separated from the internet, an arrangement called an air gap. Stuxnet reached them by spreading on removable USB drives. An air gap reduces the risk, but it does not remove it.'),
        ('Discovery',
         'Security researchers in several countries found the worm in 2010, and analysis revealed how complex it was. Its discovery brought wide attention to the security of critical infrastructure.'),
        ('Attribution',
         'Attribution means naming who is responsible. Many reports linked Stuxnet to the United States and Israel, though neither government formally confirmed it. Attribution in cyberspace is often hard and contested.'),
        ('Lessons for critical systems',
         'Critical systems need layered defences, careful control of removable media, monitoring for unusual behaviour, and planning for attacks that aim at physical effects.'),
    ],
    "test": [
        ('What did Stuxnet aim to manipulate?',
         [('a', 'Email inboxes'), ('b', 'Online games'), ('c', 'Cloud photo albums'), ('d', 'Industrial machinery through control systems')], 'd'),
        ('What kind of device did it target?',
         [('a', 'Programmable logic controllers from one manufacturer'), ('b', 'Kitchen toasters'), ('c', 'Wrist watches'), ('d', 'Garden sprinklers only')], 'a'),
        ('What is an air gap?',
         [('a', 'A gap in a road'), ('b', 'A hole in a wall'), ('c', 'A separation of a system from the internet'), ('d', 'A type of printer')], 'c'),
        ('How did Stuxnet often reach air-gapped systems?',
         [('a', 'By post'), ('b', 'On removable USB drives'), ('c', 'By carrier pigeon'), ('d', 'Through a radio tower only')], 'b'),
        ('Why is attribution hard?',
         [('a', 'Because it is always stated in the news'), ('b', 'Because computers never record anything'), ('c', 'Because naming who is responsible is often hard and contested'), ('d', 'Because only one country has computers')], 'c'),
    ],
}
