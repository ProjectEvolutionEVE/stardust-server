"""Human Reliability Analysis: task analysis, error probabilities, performance shaping factors and design fixes."""
CODE = 'engineering5_hra'
BOOK = {'title': 'Human Reliability Analysis',
 'subtitle': 'Task analysis, human error, the conditions that shape it and the fixes that help',
 'chapters': [('People are part of the system',
               'Human reliability analysis looks at the tasks people do in a system and how those tasks can '
               'go wrong. Operators, maintainers and drivers all make errors. A good design expects errors '
               'and limits the harm they cause.'),
              ('Task analysis',
               'A task analysis breaks a job into its steps. It shows what the person must see, decide and '
               'do at each step. Each step is a place where an error could happen, and the analysis counts '
               'those places.'),
              ('Error probabilities',
               'Analysts estimate how likely each step is to go wrong. The estimates come from data on '
               'similar tasks and from expert judgment. They are rough, so they are used to compare options '
               'rather than to predict exact numbers.'),
              ('Performance shaping factors',
               'Performance shaping factors are conditions that make errors more or less likely. Examples '
               'include time pressure, poor labels, tiredness, noise and unclear procedures. Each factor can '
               'raise or lower the error estimate for a task.'),
              ('Design fixes',
               'The most useful result is a list of design fixes. Clear labels, a checklist, a second check '
               'or a better layout can cut the error chance a lot. Fixing the design is usually better than '
               'blaming the person.'),
              ('The money side',
               'A good fix costs less than the harm of the error it prevents. Compare the cost of a new '
               'label or training course with the cost of an incident. Small, cheap changes often give the '
               'biggest return.')],
 'test': [('What does task analysis do?',
           [('a', 'It breaks a job into steps and shows where errors could happen'),
            ('b', 'It sets the price of the job'),
            ('c', 'It picks the colour of the uniform'),
            ('d', 'It counts the number of breaks')],
           'a'),
          ('Which of these is a performance shaping factor?',
           [('a', 'The shape of the moon'),
            ('b', 'Time pressure'),
            ('c', 'The name of the company'),
            ('d', 'The number of pages in the manual')],
           'b'),
          ('Why are human error estimates used?',
           [('a', 'To predict exact numbers'),
            ('b', 'To set staff pay'),
            ('c', 'To compare options, since they are rough'),
            ('d', 'To choose the paint')],
           'c'),
          ('Which is a typical design fix?',
           [('a', 'Blaming the person who made the error'),
            ('b', 'Removing all labels'),
            ('c', 'Making the procedure longer and vaguer'),
            ('d', 'Adding a clear label or a second check')],
           'd'),
          ('Why compare a fix against the cost of an incident?',
           [('a', 'Because a good fix costs less than the harm it prevents'),
            ('b', 'Because incidents are always free'),
            ('c', 'Because fixes are always the most expensive'),
            ('d', 'Because labels are illegal')],
           'a')]}
