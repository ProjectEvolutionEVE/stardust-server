"""Approximate query processing: sampling, confidence intervals, sketches such as HyperLogLog, and when exact answers are required."""
CODE = 'computing5_approximate_query'
BOOK = {
    "title": 'Approximate Query Processing',
    "subtitle": 'Trading a small, known error for answers that come back much faster',
    "chapters": [
        ('Why be approximate',
         'Some questions need the whole data set, which can take a long time on very large tables. For many dashboards, a close answer in seconds is more useful than an exact one in hours.'),
        ('Sampling',
         'One method reads a random sample of rows and scales the answer up. A sample of one row in a hundred can give a useful average much faster.'),
        ('Confidence intervals',
         'A good approximate answer comes with a range, such as about 4.2 million, give or take 50,000. That range is a confidence interval, and it tells the user how far the answer might be off.'),
        ('Sketches',
         'Sketches are small summaries built for one kind of question. HyperLogLog, for example, estimates how many distinct items there are using very little memory.'),
        ('Telling the user',
         'The user must know the answer is approximate. A chart without a note can mislead people who take the number as exact.'),
        ('Limits',
         'Approximation fails for some questions, such as finding one specific row or checking an exact total for a payment. Teams choose exact answers where money or safety depends on them.'),
    ],
    "test": [
        ('Why is approximate query processing used?',
         [('a', 'To make answers slower'), ('b', 'To get useful answers much faster on large data'), ('c', 'To hide the data'), ('d', 'To avoid storing numbers')], 'b'),
        ('What is sampling?',
         [('a', 'Reading a random subset of rows and scaling up'), ('b', 'Printing every row'), ('c', 'Deleting random rows'), ('d', 'Asking the user to guess')], 'a'),
        ('What does a confidence interval show?',
         [('a', 'The colour of the chart'), ('b', 'The number of users online'), ('c', 'A range of how far the answer might be off'), ('d', 'The date of the last backup')], 'c'),
        ('What is HyperLogLog used for?',
         [('a', 'Playing music'), ('b', 'Encrypting passwords'), ('c', 'Drawing maps'), ('d', 'Estimating distinct counts with little memory')], 'd'),
        ('When should a team use an exact answer?',
         [('a', 'For a total that a payment or a safety decision depends on'), ('b', 'Never'), ('c', 'Only for jokes'), ('d', 'Whenever the chart looks nice')], 'a'),
    ],
}
