"""Explanations for Users: why-explanations, counterfactuals, trust calibration, testing explanations, information overload and design choices."""
CODE = 'computing5_explainability'
BOOK = {'title': 'Explanations for Users',
 'subtitle': 'Helping people understand why a system decided what it did',
 'chapters': [('Why-explanations',
               'A why-explanation tells a person what led to a decision. A system might say which factors '
               'weighed most in a result. Clear reasons help people understand a decision and check whether '
               'it was fair.'),
              ('Counterfactuals',
               'A counterfactual explanation says what would have had to be different for the outcome to '
               'change, such as a higher income leading to approval. Counterfactuals give people something '
               'they can act on.'),
              ('Trust calibration',
               'Explanations should help people trust a system to the right degree, not blindly. An '
               'explanation that sounds confident but is wrong can increase trust in the wrong places.'),
              ('Testing explanations',
               'Explanations must be tested with real users, to see whether they understand them and can use '
               'them. An explanation that nobody reads does no good at all.'),
              ('Information overload',
               'Too much detail can overwhelm people and hide the key point. Good explanations are short by '
               'default, with more detail available when someone asks for it.'),
              ('Design choices',
               'Designers decide when, how and in what words to explain. Those choices should be made '
               'openly, and they should match the stakes of the decision.')],
 'test': [('What does a why-explanation tell a person?',
           [('a', 'The weather forecast'),
            ('b', 'The colour of the screen'),
            ('c', 'The price of a train ticket'),
            ('d', 'What led to a decision')],
           'd'),
          ('What is a counterfactual explanation?',
           [('a', 'A story that is known to be false'),
            ('b', 'What would have had to be different for the outcome to change'),
            ('c', 'A list of software versions'),
            ('d', 'A warning about the weather')],
           'b'),
          ('Why can a confident but wrong explanation be harmful?',
           [('a', 'It can increase trust in the wrong places'),
            ('b', 'It makes the screen brighter'),
            ('c', 'It removes all data'),
            ('d', 'It makes the system faster')],
           'a'),
          ('Why must explanations be tested with users?',
           [('a', 'To count the words'),
            ('b', 'To remove all detail'),
            ('c', 'To check that people understand and can use them'),
            ('d', 'To avoid any feedback')],
           'c'),
          ('How long should explanations be by default?',
           [('a', 'Short, with more detail available on request'),
            ('b', 'As long as possible always'),
            ('c', 'Written only in code'),
            ('d', 'Never shown at all')],
           'a')]}
