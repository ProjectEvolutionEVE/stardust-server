"""Engineering Organisation Design: grouping by product or function, Conway's law, span of control, platform teams, reorganisation costs and design reviews."""
CODE = 'computing5_org_design'
BOOK = {'title': 'Engineering Organisation Design',
 'subtitle': 'How to group engineers so that the work flows well',
 'chapters': [('Grouping by product or function',
               'Teams can be grouped around a product, such as one customer service, or around a function, '
               'such as all the engineers together. Each choice makes some communication easy and other '
               'communication hard.'),
              ("Conway's law",
               'In 1968 Melvin Conway observed that systems tend to mirror the communication structure of '
               "the organisations that build them. This is called Conway's law, and it is a useful warning "
               'when designing teams.'),
              ('Span of control',
               'Span of control is the number of people one manager leads directly. Too wide a span can '
               'leave people without support, while too narrow a span adds layers that slow decisions.'),
              ('Platform teams',
               'Platform teams provide shared tools and services that other product teams use. The 2019 book '
               'Team Topologies, by Matthew Skelton and Manuel Pais, describes how such teams can reduce the '
               'load on others.'),
              ('Reorganisation costs',
               'Reorganising a company takes time, causes uncertainty and can slow work for months. Changes '
               'should be weighed against these costs, not made only because they are fashionable.'),
              ('Design reviews',
               'Reviewing an organisation design, as one would review a system design, helps spot unclear '
               'ownership and bottlenecks. The review should involve the people who will live with the '
               'result.')],
 'test': [('What does grouping teams around a product or a function change?',
           [('a', 'The colour of the office carpet'),
            ('b', 'The price of coffee'),
            ('c', 'Which communication is easy and which is hard'),
            ('d', 'The number of windows')],
           'c'),
          ("What does Conway's law say?",
           [('a', 'Every system is built in one day'),
            ('b', 'Systems tend to mirror the communication structure of the organisations that build them'),
            ('c', 'Organisations never affect systems'),
            ('d', 'Systems must always be painted')],
           'b'),
          ('What is span of control?',
           [('a', 'The number of people one manager leads directly'),
            ('b', 'The length of a cable'),
            ('c', 'The height of an office door'),
            ('d', 'The number of computers in a room')],
           'a'),
          ('What do platform teams provide?',
           [('a', 'Only paper forms'),
            ('b', 'Nothing to anyone'),
            ('c', 'Tickets to a film'),
            ('d', 'Shared tools and services that other product teams use')],
           'd'),
          ('What should be weighed against the benefits of reorganising?',
           [('a', 'The number of biscuits in the kitchen'),
            ('b', 'The time, uncertainty and slowdown it can bring'),
            ('c', 'The name of the building'),
            ('d', 'The weather in the city')],
           'b')]}
