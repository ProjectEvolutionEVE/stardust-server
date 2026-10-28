"""Human Error and Automation: error types, automation surprise, alarm design, slips and mistakes, checklists and blameless analysis."""
CODE = 'computing5_human_error'
BOOK = {'title': 'Human Error and Automation',
 'subtitle': 'Why capable people make errors, and how systems can help',
 'chapters': [('Error types',
               'Researchers separate errors into types. A slip is doing the wrong action while meaning to do '
               'the right one. A mistake is choosing the wrong plan from the start. Each type needs '
               'different prevention.'),
              ('Automation surprise',
               'Automation surprise happens when a system does something the operator did not expect, and '
               'the operator is unsure why. It is common when automatic systems change modes without clear '
               'signals. Clear feedback helps people stay in control.'),
              ('Alarm design',
               'A system that raises too many alarms trains people to ignore them. Good alarm design gives '
               'fewer, clearer and more meaningful signals. An alarm should always ask for a useful action.'),
              ('Slips and mistakes',
               'Slips are often caused by habit, distraction or similar-looking controls. Mistakes come from '
               'a wrong understanding of the situation. Design can reduce slips by making controls distinct, '
               'and reduce mistakes by showing clearly what is going on.'),
              ('Checklists',
               'Checklists help people remember steps that are easy to skip under pressure. Aviation and '
               'medicine have used them widely to reduce preventable errors. A good checklist is short, '
               'clear and placed where it will be used.'),
              ('Blameless analysis',
               'After an incident, a blameless review asks why the system allowed the error, rather than who '
               'is at fault. People report problems more honestly when they are not punished for them, so '
               'the lessons are richer.')],
 'test': [('What is a slip?',
           [('a', 'Choosing a good plan on purpose'),
            ('b', 'Reading a manual aloud'),
            ('c', 'Sleeping at a desk'),
            ('d', 'Doing the wrong action while meaning to do the right one')],
           'd'),
          ('What is automation surprise?',
           [('a', 'A gift from a machine'),
            ('b', 'A system doing something the operator did not expect'),
            ('c', 'A system that never changes'),
            ('d', 'A cake served at a meeting')],
           'b'),
          ('What goes wrong when a system raises too many alarms?',
           [('a', 'Nothing at all'),
            ('b', 'Alarms become quieter'),
            ('c', 'People learn to ignore them'),
            ('d', 'Operators become faster')],
           'c'),
          ('Why have checklists been used in aviation and medicine?',
           [('a', 'To reduce preventable errors from skipped steps'),
            ('b', 'To make the work slower on purpose'),
            ('c', 'To replace all training'),
            ('d', 'To hide errors from patients')],
           'a'),
          ('What is the aim of a blameless review?',
           [('a', 'To find someone to punish'),
            ('b', 'To close the case without learning'),
            ('c', 'To hide the incident from everyone'),
            ('d', 'To understand why the system allowed the error')],
           'd')]}
