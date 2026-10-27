"""Data quality frameworks: quality dimensions, automated rules and tests, scorecards, anomaly detection and ownership."""
CODE = 'computing5_data_quality'
BOOK = {
    "title": 'Data Quality Frameworks',
    "subtitle": 'Checking that data is accurate, complete and on time, and who fixes it when it is not',
    "chapters": [
        ('Why quality matters',
         'A report is only as good as the data behind it. A wrong number can lead to a bad decision made with full confidence.'),
        ('The usual dimensions',
         'Teams often measure accuracy, completeness, consistency, validity and timeliness. Accuracy asks whether a value is right, and timeliness asks whether it arrived in time.'),
        ('Rules and tests',
         "Simple rules, such as 'this field is never empty' or 'this date is in the past', are written as automated tests. Tests run every time new data arrives."),
        ('Scorecards',
         'A scorecard shows the results of the tests over time, so people can see whether quality is getting better or worse.'),
        ('Anomaly detection',
         'Some problems are unusual rather than wrong by a rule. A sudden drop in daily orders, for example, can flag a broken feed.'),
        ('Ownership and cost',
         'Each dataset needs an owner who acts on failed tests. Checks cost computing time and staff effort, so teams choose the checks that matter most.'),
    ],
    "test": [
        ('What does completeness check?',
         [('a', 'The price of paper'), ('b', 'The colour of tables'), ('c', 'Whether values are missing'), ('d', 'The number of users in a meeting')], 'c'),
        ('What does timeliness ask?',
         [('a', 'Whether the data arrived in time'), ('b', 'Whether the printer is warm'), ('c', 'How many fonts exist'), ('d', "What the company's logo looks like")], 'a'),
        ('What is an automated quality rule?',
         [('a', 'A paper checklist kept in a drawer'), ('b', "A test such as 'this field is never empty'"), ('c', 'A chart of staff moods'), ('d', 'A description of a room')], 'b'),
        ('What does a scorecard show?',
         [('a', 'Recipes'), ('b', 'Holiday photos'), ('c', 'The weather forecast'), ('d', 'Quality test results over time')], 'd'),
        ('Why does each dataset need an owner?',
         [('a', 'To name the server'), ('b', 'To act on failed tests'), ('c', 'To change the font'), ('d', 'To stop all checks')], 'b'),
    ],
}
