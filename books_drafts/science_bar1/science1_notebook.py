"""The Lab Notebook and Safety: recording observations, repeatability, honest results, and basic lab safety. Science career, bar 1 (Research Assistant)."""
CODE = 'science1_notebook'
BOOK = {
    "title": 'The Lab Notebook and Safety',
    "subtitle": 'Recording what you see honestly, and staying safe in the lab',
    "chapters": [
        ('Write it down at once',
         'Record each observation as it happens, with the date, the time, what you did and the numbers you read. Memory fades and shifts, but a notebook keeps what you actually saw. Write in ink, and cross out mistakes with a single line so they can still be read.'),
        ('Record the results that go wrong',
         'A failed test is still a result. Write down what went wrong, what you changed and what happened next. Leaving out a failure makes the next person waste the same time, and it hides something you may need to know.'),
        ('Repeatability',
         'Run the test again with the same method, and write down each run. If the results match, you can trust them more. If they differ, look for the reason before you claim anything, such as a different sample, a different scale or a change in temperature.'),
        ('Honest results',
         'Report the numbers you got, how sure you are of them, and what you did not measure. Never change a number to match what you expected. Anyone who reads your notes depends on them being true.'),
        ('Basic lab safety',
         'Wear eye protection and gloves when the job needs them. Label every container, and never taste or sniff a sample to find out what it is. Keep food and drink out of the lab, and know where the exits and the first-aid kit are.'),
        ('Handling samples safely',
         'Read the label before you open a container. Never mix chemicals unless you know exactly what will happen. Some minerals, such as uraninite, are radioactive, so keep them in their own labelled box and ask before you handle them.'),
    ],
    "test": [
        ('When should you write down an observation?',
         [('a', 'At the end of the week'), ('b', 'When someone asks'), ('c', 'As it happens, with the date and the numbers'), ('d', 'Never, if you remember it')], 'c'),
        ('What should you do with a result that did not go as planned?',
         [('a', 'Leave it out'), ('b', 'Record it honestly, with what went wrong'), ('c', 'Change the numbers'), ('d', 'Throw the notebook away')], 'b'),
        ('What does repeatability mean?',
         [('a', 'The test is always the same colour'), ('b', 'One result is always enough'), ('c', 'You can ignore the second run'), ('d', 'You can run the same test again and get the same result')], 'd'),
        ('What is the safe rule for an unlabelled sample?',
         [('a', 'Do not taste, sniff or guess; ask, and label it before you use it'), ('b', 'Taste a little to check'), ('c', 'Mix it with another sample to see what happens'), ('d', 'Store it with the food')], 'a'),
        ('Which is good lab practice?',
         [('a', 'Keeping food in the lab for a snack'), ('b', 'Keeping samples labelled, and wearing eye protection when the job needs it'), ('c', 'Mixing chemicals to save time'), ('d', 'Working where you cannot see the exits')], 'b'),
    ],
}
