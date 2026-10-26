"""Estimating software work: how long a job takes, what it costs, and why early guesses are wide."""
CODE = 'computing3a_estimating'
BOOK = {
    "title": 'Estimating Software Work',
    "subtitle": 'How long a job takes, what it costs, and why early guesses are wide',
    "chapters": [
        ('An estimate is a range',
         'An estimate is a best guess with a range around it, such as two to four weeks. Early in a project the range is wide, because much is still unknown. A single exact date is a promise nobody can keep, so give a range.'),
        ('Break it into pieces',
         'A big job is easier to estimate in small pieces. Write down each task, estimate each one on its own, and add them up. Any piece that is still too big to estimate should be split again.'),
        ('Optimism and buffer',
         'People tend to underestimate, and tasks often grow. A buffer of extra time, sometimes called contingency, covers the unknowns. Show the buffer on purpose, as its own line, rather than hiding it inside each task.'),
        ('Time and cost go together',
         'Most of the cost of software work is people\'s time multiplied by their rate, plus tools, testing and the work of fixing mistakes. A plan that runs longer costs more, even when the code is the same. Estimate cost and time together.'),
        ('Track what really happens',
         'After each task, compare the actual time with the estimate. Over several tasks, the gaps show whether your guesses run high or low, and you can adjust the next ones. Honest records make the next estimate better.'),
        ('Money in your own plans',
         'The same skills work for your own money. Estimate the cost of a goal, add a buffer, and track what you actually spend. Saving for a big purchase works like a software plan: a range, a buffer, and a check each month.'),
    ],
    "test": [
        ('Why is an early estimate usually given as a range?',
         [('a', 'Ranges are required by law'), ('b', 'Much is still unknown, so one exact date would be a promise nobody can keep'), ('c', 'Ranges are quicker to type'), ('d', 'Exact dates are never used')], 'b'),
        ('What is the best way to estimate a big job?',
         [('a', 'Guess the total in one number'), ('b', 'Start coding and guess later'), ('c', "Copy last year's number"), ('d', 'Break it into small pieces, estimate each one, then add them up')], 'd'),
        ('What is a buffer, or contingency, in an estimate?',
         [('a', 'A file that stores old code'), ('b', 'The cost of the computer'), ('c', 'Extra time or money set aside for the unknowns'), ('d', 'A promise to finish early')], 'c'),
        ('What does the cost of software work mainly depend on?',
         [('a', "People's time and rate, plus tools, testing and fixing mistakes"), ('b', 'The colour of the screen'), ('c', 'The number of words in the title'), ('d', 'Only the price of the computer')], 'a'),
        ('Why compare actual times with estimates after each task?',
         [('a', 'To find someone to blame'), ('b', 'It shows whether your guesses run high or low, so later estimates improve'), ('c', 'To avoid writing any code'), ('d', 'Estimates can never be changed')], 'b'),
    ],
}
