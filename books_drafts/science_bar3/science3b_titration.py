"""Titration: Finding an Unknown Amount: adding a known solution until a colour change shows how much is there. Science career, bar 3 (Senior Scientist), part B."""
CODE = 'science3b_titration'
BOOK = {
    "title": 'Titration: Finding an Unknown Amount',
    "subtitle": 'Adding a known solution until a colour change shows how much is there',
    "chapters": [
        ('A known solution and an unknown one',
         'Titration measures the amount of a substance in a sample. You add a solution of known concentration, called the titrant, until the reaction is complete. The exact point where the amounts match is the equivalence point.'),
        ('The indicator shows the end',
         'An indicator is a substance that changes colour near the end of the reaction. You watch for that change and stop adding titrant. A good indicator changes colour very close to the equivalence point.'),
        ('Read the burette',
         'The titrant sits in a burette, a long glass tube with a tap and fine markings. Read the level at the bottom of the curve, with your eye level with the mark, and write it down at once. A careless reading ruins the whole result.'),
        ('Working out the answer',
         'Multiply the titrant concentration by the volume added, in litres, to get the moles of titrant. Use the balanced equation to find the moles of the unknown, then convert to grams or to a concentration. Each step is one simple calculation.'),
        ('A simple example',
         'Suppose 20.0 millilitres of 0.10-molar hydrochloric acid is neutralised exactly by 20.0 millilitres of sodium hydroxide. The ratio is one to one, so the sodium hydroxide must also be 0.10 molar.'),
        ('Repeat for confidence',
         'Run a titration several times and average the results that agree closely. Repeats show whether a reading is reliable. One lucky result proves nothing.'),
    ],
    "test": [
        ('What is the titrant?',
         [('a', 'The unknown sample'), ('b', 'The solution of known concentration that is added'), ('c', 'The indicator'), ('d', 'The burette tap')], 'b'),
        ('What does an indicator do in a titration?',
         [('a', 'Measures the mass of the sample'), ('b', 'Makes the solution hotter'), ('c', 'Changes colour near the end of the reaction to show when to stop'), ('d', 'Turns the sample into gas')], 'c'),
        ('How should you read a burette?',
         [('a', 'Read the level at the bottom of the curve, eye level with the mark, and record it at once'), ('b', 'Read it from above the tube'), ('c', 'Guess the level by the colour'), ('d', 'Read it only at the very end')], 'a'),
        ('In the simple example, 20.0 mL of 0.10-molar acid is exactly cancelled by 20.0 mL of base. What is the base concentration?',
         [('a', '0.20 molar'), ('b', '0.10 molar'), ('c', '0.05 molar'), ('d', '1.0 molar')], 'b'),
        ('Why repeat a titration?',
         [('a', 'To use up more titrant'), ('b', 'To spend more of the budget'), ('c', 'Repeats show whether a result is reliable, so one lucky result is not trusted'), ('d', 'Repeats make the indicator change colour')], 'c'),
    ],
}
