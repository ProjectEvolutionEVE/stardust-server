"""Designing a Fair Test: variables, sample size, random allocation, blinding, and planning before you test. Science career, bar 2 (Scientist)."""
CODE = 'science2_design'
BOOK = {
    "title": 'Designing a Fair Test',
    "subtitle": 'Variables, sample size, randomness and blinding',
    "chapters": [
        ('Three kinds of variable',
         'The independent variable is the thing you change on purpose. The dependent variable is what you measure in response. Controlled variables are everything else you keep the same, so the change in the result can be traced to the change you made.'),
        ('Why sample size matters',
         'A single measurement can be a fluke. With more samples, chance differences even out and a clearer pattern appears. A test on three samples can mislead you, while a test on thirty gives you far more to go on.'),
        ('Random allocation',
         'When you compare two methods on many samples, assign each sample to a group by chance. Random allocation means the groups start out alike, so any difference you find is more likely to come from the method and not from which samples happened to land in which group.'),
        ('Blinding',
         'In a blind test, the people who take the measurements do not know which sample received which treatment, so their expectations cannot bias the result. In a double-blind test, the people taking part are kept in the dark as well.'),
        ('Control groups and placebos',
         'A control group gets no treatment, or gets a placebo, which is an inactive treatment that looks the same. Without a control, a change could come from time passing or from expectation rather than from your method. The comparison is what makes the result meaningful.'),
        ('Plan before you test',
         'Write down your variables, your number of samples and what result would show your guess is wrong before you start. Changing the plan after you see the results is a common way to find false patterns, so keep the plan fixed.'),
    ],
    "test": [
        ('What is the dependent variable?',
         [('a', 'The thing you change on purpose'), ('b', 'The room temperature'), ('c', 'The controlled variables'), ('d', 'The thing you measure in response')], 'd'),
        ('Why use more samples in a test?',
         [('a', 'Chance differences even out, so a single result is less likely to be a fluke'), ('b', 'More samples always give a bigger number'), ('c', 'It makes the test cheaper'), ('d', 'Samples are needed to change the result')], 'a'),
        ('What does a blind test mean?',
         [('a', 'The test happens in the dark'), ('b', 'The results are never written down'), ('c', 'The people measuring do not know which sample received which treatment'), ('d', 'The samples cannot be seen')], 'c'),
        ('What is a placebo used for?',
         [('a', 'To make the result bigger'), ('b', 'To replace the control group'), ('c', 'As an inactive treatment, to compare against the real one'), ('d', 'To hide the samples')], 'c'),
        ('Why should you write the plan down before testing?',
         [('a', 'To avoid changing the test to fit the results'), ('b', 'So the test can be finished faster'), ('c', 'Because plans are required by law in every lab'), ('d', 'So the samples cannot change')], 'a'),
    ],
}
