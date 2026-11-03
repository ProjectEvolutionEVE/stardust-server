"""Sensitivity Analysis in Project Appraisal: key variables, tornado charts, break-even points, scenarios, communication and limits."""
CODE = 'navigation5_sensitivity_appraisal'
BOOK = {
    "title": 'Sensitivity Analysis in Project Appraisal',
    "subtitle": 'Finding the inputs that matter most, and showing how firm the answer really is',
    "chapters": [
        ('Key variables',
         'Some inputs affect the result far more than others. These key variables deserve the most care, and the best data. Find them first, before you spend time on the rest.'),
        ('Tornado charts',
         'A tornado chart ranks the inputs by how much each one moves the result. The longest bar is the input that matters most. The chart makes the main risks easy to see at a glance.'),
        ('Break-even',
         'The break-even value of an input is the value at which the net benefit is exactly zero. If the true value is likely to fall on the wrong side of that point, the project is at risk.'),
        ('Scenarios',
         'Scenarios test the result under different sets of assumptions, such as a slow, a central and a fast case. They show how the answer changes when several inputs move together.'),
        ('Communication',
         'Explain the results in plain words that decision makers can use. Show the ranges and the main drivers, not only a single number. A clear message builds trust in the appraisal.'),
        ('Limits',
         'Sensitivity analysis tests changes one at a time or in sets. It cannot predict every event, and it does not replace good data. Use it as a guide to the risks, not as a promise.'),
    ],
    "test": [
        ('What are key variables in an appraisal?',
         [('a', 'The inputs that most affect the result'), ('b', 'Any colours used in the report'), ('c', 'Typing errors in the text'), ('d', 'The names of the staff')], 'a'),
        ('What does a tornado chart show?',
         [('a', 'Weather forecasts'), ('b', 'Which inputs move the result most, ranked from largest to smallest'), ('c', 'The number of staff'), ('d', 'Travel times to the site')], 'b'),
        ('What is a break-even value?',
         [('a', 'The point where costs are at their highest'), ('b', 'The day a project starts'), ('c', 'The day a project ends'), ('d', 'The value of an input at which the net benefit is exactly zero')], 'd'),
        ('Why use scenarios in an appraisal?',
         [('a', 'To avoid all thinking'), ('b', 'To test a single guess'), ('c', 'To show how the result changes under different sets of assumptions'), ('d', 'To hide the risk')], 'c'),
        ('What are the limits of sensitivity analysis?',
         [('a', 'It proves the answer is correct'), ('b', 'It tests changes one at a time or in sets, and cannot predict every event'), ('c', 'It removes the need for data'), ('d', 'It is always exact')], 'b'),
    ],
}
