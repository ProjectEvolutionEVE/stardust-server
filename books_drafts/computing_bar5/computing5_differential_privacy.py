"""Differential Privacy: privacy as a guarantee on outputs, noise mechanisms, the privacy budget, composition and the trade-off with accuracy."""
CODE = 'computing5_differential_privacy'
BOOK = {'title': 'Differential Privacy',
 'subtitle': 'A guarantee about outputs, not promises about data',
 'chapters': [('Privacy as a guarantee on outputs',
               "Differential privacy is a promise about the output of an analysis. Adding or removing one person's record changes the output distribution only slightly. An "
               'observer cannot tell with confidence whether any one person was included.'),
              ('Noise mechanisms',
               'The usual way to achieve differential privacy is to add carefully scaled random noise to a result. The Laplace mechanism adds noise scaled to how much one record '
               'can change the answer. The noise hides individuals and keeps the statistics useful.'),
              ('The privacy budget',
               'Each released answer uses up part of a privacy budget, often written as epsilon. A smaller epsilon means stronger privacy and more noise. Once the budget is '
               'spent, no more queries can be answered without more privacy loss.'),
              ('Composition',
               'Composition theorems say how privacy losses add up across several analyses. Running many queries uses more budget than running one. Careful accounting keeps the '
               'total loss within a stated limit.'),
              ('Trade-offs with accuracy',
               'Stronger privacy means more noise, and so less accurate answers. Large datasets make noise matter less, because its effect on averages shrinks. Choosing the '
               'budget is a policy decision as much as a technical one.'),
              ('Releasing statistics safely',
               'Agencies and companies use differential privacy to publish census-style totals and usage statistics. The guarantee holds even against an attacker with outside '
               'knowledge. Designers should document the budget and the queries they allow.')],
 'test': [('What does differential privacy promise?',
           [('a', "The output changes only slightly if one person's record is added or removed"),
            ('b', 'Data is never stored'),
            ('c', 'Results are always exact'),
            ('d', 'No one can ever read a file')],
           'a'),
          ('What is the usual way to get differential privacy?',
           [('a', 'Deleting half the data'), ('b', 'Printing the data in colour'), ('c', 'Adding carefully scaled random noise to a result'), ('d', 'Sending data by post')],
           'c'),
          ('What does a smaller epsilon mean?',
           [('a', 'Weaker privacy and no noise'), ('b', 'Stronger privacy and more noise'), ('c', 'A larger dataset'), ('d', 'A faster computer')],
           'b'),
          ('What happens to privacy loss when many queries are run?',
           [('a', 'It always disappears'), ('b', 'It stays the same as one query'), ('c', 'It is measured in colours'), ('d', 'It adds up across the queries')],
           'd'),
          ("What happens to noise's effect on averages in large datasets?",
           [('a', 'It matters more'), ('b', 'It doubles every record'), ('c', 'It matters less'), ('d', 'It makes averages negative')],
           'c')]}
