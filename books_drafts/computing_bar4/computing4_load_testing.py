"""Load and Performance Testing: testing how a system behaves under realistic demand, and reading its numbers fairly."""
CODE = 'computing4_load_testing'
BOOK = {
    "title": 'Load and Performance Testing',
    "subtitle": 'Testing how a system behaves under realistic demand, and reading its numbers fairly',
    "chapters": [
        ('Workload models',
         'A workload model describes the work real users create, such as the mix of page views, searches and purchases over a day. A good model comes from real logs. A test that sends only one kind of request tells you very little.'),
        ('Ramp profiles',
         'A ramp profile increases the load slowly, step by step, to see where the system starts to struggle. Sudden spikes test a different thing, the ability to recover. Choose the profile that matches the question you need answered.'),
        ('Test environments',
         'The test environment should be as close to production as practical, with similar sizes, data volumes and settings. Results from a much smaller setup can mislead. Note every difference, so the numbers are read with the right care.'),
        ('Reading percentiles',
         'An average hides the slow experiences. The ninety-fifth or ninety-ninth percentile shows the time that most users stay under, and the slowest tail of requests. Teams usually set targets on percentiles, not on averages.'),
        ('Capacity limits',
         'Every system has a point where adding load makes response times climb sharply. Load tests find that point, which is the capacity limit. Knowing it lets a team plan growth, and decide when to add servers.'),
        ('Regression gates',
         'A regression gate runs a fixed performance test on each change and fails it if the numbers get noticeably worse. Gates catch slow changes before they reach users. Keep the threshold stable and the test repeatable, or the gate will be ignored.'),
    ],
    "test": [
        ('What does a workload model describe?',
         [('a', 'The paint on the office walls'), ('b', 'The number of staff in a team'), ('c', 'The price of a server'), ('d', 'The mix of work real users create')], 'd'),
        ('Why do teams read percentiles rather than only averages?',
         [('a', 'Averages are always wrong'), ('b', 'Averages can hide the slow experiences some users have'), ('c', 'Percentiles are always smaller'), ('d', 'Averages cannot be calculated')], 'b'),
        ('What is a ramp profile?',
         [('a', 'A road for cars in the car park'), ('b', 'A way to delete logs'), ('c', 'A gradual increase in load to find where the system struggles'), ('d', 'A type of network card')], 'c'),
        ('What is a capacity limit?',
         [('a', 'The point where adding load makes response times climb sharply'), ('b', 'The number of letters in a name'), ('c', 'The size of a hard disk in the office'), ('d', 'The number of staff allowed in a meeting')], 'a'),
        ('What does a regression gate do?',
         [('a', 'Opens the office door'), ('b', 'Fails a change if performance gets noticeably worse'), ('c', 'Prints the test report'), ('d', 'Writes new features automatically')], 'b'),
    ],
}
