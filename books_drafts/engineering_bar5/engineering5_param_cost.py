"""Parametric Cost Estimating: cost-estimating relationships, weight and size drivers, inflation indices and estimate ranges."""
CODE = 'engineering5_param_cost'
BOOK = {'title': 'Parametric Cost Estimating',
 'subtitle': 'Estimating cost from the size and weight of what you build, with honest ranges',
 'chapters': [('What parametric estimating is',
               'Parametric estimating predicts cost from a few measurable features of a design, such as '
               'weight, size or power. It is quick and useful early on, before every part has been drawn. It '
               'relies on data from past projects.'),
              ('Cost-estimating relationships',
               'A cost-estimating relationship, or CER, is a formula that links cost to a driver. For '
               'example, cost might rise with weight raised to a set power. The formula is fitted to past '
               'projects and is only trusted within the range of that data.'),
              ('Weight and size drivers',
               'Weight, size, power and complexity are common drivers. The right driver is the one that best '
               'explains past costs. Using a driver far outside its range gives poor estimates.'),
              ('Inflation indices',
               'Past costs must be adjusted to today’s prices using an inflation index. The index turns old '
               'costs into current money. Choosing the right index for the type of work matters.'),
              ('Estimate ranges',
               'Early estimates are uncertain, so they are given as a range. The range narrows as the design '
               'becomes more detailed. Showing the range is more honest than giving one number as if it were '
               'certain.'),
              ('The money side of early estimates',
               'Early estimates guide the decision on whether a project is worth starting. A wrong estimate '
               'can cost a great deal later. Updating the estimate as the design grows keeps the budget '
               'honest.')],
 'test': [('What does parametric estimating predict cost from?',
           [('a', 'The number of windows in a room'),
            ('b', 'A few measurable features such as weight, size or power'),
            ('c', 'The name of the project manager'),
            ('d', 'The day of the week')],
           'b'),
          ('What is a cost-estimating relationship?',
           [('a', 'A friendship between two engineers'),
            ('b', 'A contract with a supplier'),
            ('c', 'A formula that links cost to a driver'),
            ('d', 'A type of bolt')],
           'c'),
          ('Why is an inflation index used?',
           [('a', 'To make costs disappear'),
            ('b', 'To choose the colour of a project'),
            ('c', 'To count the staff'),
            ('d', 'To adjust past costs to today’s prices')],
           'd'),
          ('Why are early estimates given as a range?',
           [('a', 'Because early estimates are uncertain'),
            ('b', 'Because ranges are cheaper to print'),
            ('c', 'Because one number is always illegal'),
            ('d', 'Because the range never changes')],
           'a'),
          ('When is a CER trusted?',
           [('a', 'For any project of any size'),
            ('b', 'Only within the range of the past data it was fitted to'),
            ('c', 'Only on a Friday'),
            ('d', 'Always, without checks')],
           'b')]}
