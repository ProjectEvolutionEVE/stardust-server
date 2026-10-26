"""Earned Value: comparing the work planned, the work done and the money spent, to see where a project really stands."""
CODE = 'flight5_earned_value'
BOOK = {
    'title': 'Earned Value',
    'subtitle': 'Planned work, earned work and money spent',
    'chapters': [
        ('Three numbers', 'Earned value uses three figures. The planned value is the budgeted cost of work scheduled to date. The earned value is the budgeted cost of work actually completed. The actual cost is the money really spent.'),
        ('Cost performance', 'The cost performance index is the earned value divided by the actual cost. A value above one means the work is costing less than planned. A value below one means it is costing more.'),
        ('Schedule performance', 'The schedule performance index is the earned value divided by the planned value. A value above one means the work is ahead of schedule. A value below one means it is behind.'),
        ('Forecasts', 'Earned value can forecast the final cost of a project by using past performance. The forecast is only as good as the data, but it gives an early warning when the trend is poor.'),
        ('Where it is useful', 'Earned value shows the true state of a project in numbers, which helps the leader act early. It is used widely in large government and defence projects.'),
        ('Its flaws', 'Earned value depends on how fairly the work is measured. A task can look half done for a long time. Judge the numbers alongside a clear look at the actual work.'),
    ],
    'test': [
        ('What is the earned value?', [('a', 'The budgeted cost of the work actually completed'), ('b', 'The money really spent'), ('c', 'The price of a ticket'), ('d', 'The planned hours of sleep')], 'a'),
        ('What does a cost performance index above one mean?', [('a', 'The work has stopped'), ('b', 'The work costs more than planned'), ('c', 'The work is costing less than planned'), ('d', 'The index is not real')], 'c'),
        ('What is the schedule performance index?', [('a', 'Planned value divided by the crew size'), ('b', 'Earned value divided by planned value'), ('c', 'Actual cost multiplied by time'), ('d', 'The number of tasks in a list')], 'b'),
        ('What can earned value forecast?', [('a', 'The weather in orbit'), ('b', 'The colour of the hull'), ('c', 'The next election'), ('d', 'The final cost of a project, based on past performance')], 'd'),
        ('What is a flaw of earned value?', [('a', 'It can never be calculated'), ('b', 'It only works on paper ships'), ('c', 'It depends on how fairly the work is measured'), ('d', 'It always shows the truth exactly')], 'c'),
    ],
}
