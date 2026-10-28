"""Earned Value Management: planned value, earned value, cost and schedule indices, forecasts and control actions."""
CODE = 'engineering5_earned_value'
BOOK = {'title': 'Earned Value Management',
 'subtitle': 'Measuring how much work is really done for the money spent',
 'chapters': [('Three numbers',
               'Earned value management compares three numbers. Planned value is the budgeted cost of the '
               'work scheduled to date. Earned value is the budgeted cost of the work actually done. Actual '
               'cost is the money really spent.'),
              ('Planned value and earned value',
               'Planned value shows what the plan said should be finished by now. Earned value shows what '
               'has actually been finished, measured at its budget. The gap between them shows whether the '
               'project is ahead or behind.'),
              ('Cost and schedule indices',
               'The cost performance index is earned value divided by actual cost. A value below one means '
               'the project is over budget. The schedule performance index is earned value divided by '
               'planned value. A value below one means it is behind schedule.'),
              ('Forecasts',
               'A common forecast of the final cost divides the total budget by the cost performance index. '
               'If the index is below one, the forecast is above the budget. Forecasts are updated each '
               'reporting period so trends are visible.'),
              ('Control actions',
               'When the indices fall, the team takes control actions. These might be changing the scope, '
               'adding resources or resetting the schedule. The actions are chosen by weighing their cost '
               'against the expected gain.'),
              ('The money side of control',
               'Early warnings from earned value save money, because problems caught early are cheaper to '
               'fix. A project that waits until the end learns about overruns too late. Regular reporting '
               'keeps spending linked to real progress.')],
 'test': [('What is planned value?',
           [('a', 'The price of the office chairs'),
            ('b', 'The budgeted cost of the work scheduled to date'),
            ('c', 'The number of days in a holiday'),
            ('d', 'The weight of the paperwork')],
           'b'),
          ('What is the cost performance index?',
           [('a', 'Actual cost multiplied by the weather'),
            ('b', 'The colour of the report'),
            ('c', 'Earned value divided by actual cost'),
            ('d', 'The number of staff in the lift')],
           'c'),
          ('A cost performance index below one means what?',
           [('a', 'The project is under budget by a lot'),
            ('b', 'The project has no costs'),
            ('c', 'The project is finished'),
            ('d', 'The project is over budget')],
           'd'),
          ('What does the schedule performance index compare?',
           [('a', 'Earned value with planned value'),
            ('b', 'Earned value with the colour of the sky'),
            ('c', 'Actual cost with lunch'),
            ('d', 'Planned value with the number of pens')],
           'a'),
          ('Why are early warnings from earned value valuable?',
           [('a', 'Early warnings remove all costs'),
            ('b', 'Problems caught early are cheaper to fix'),
            ('c', 'Early warnings are never needed'),
            ('d', 'Early warnings delay the project')],
           'b')]}
