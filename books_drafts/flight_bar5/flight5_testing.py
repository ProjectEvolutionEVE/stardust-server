"""Testing Philosophy: test the way the mission will fly, and learn from what the tests show."""
CODE = 'flight5_testing'
BOOK = {
    'title': 'Testing Philosophy',
    'subtitle': 'Test the way the mission will fly',
    'chapters': [
        ('Test as you fly', 'The rule is simple: test the item the way it will be used. Conditions should match the real mission as closely as is practical, including heat, cold, vibration and load.'),
        ('Qualification and acceptance', 'Qualification tests use a design to a higher stress than it will meet, to prove the design has margin. Acceptance tests check each built unit at the level it will meet in use. The two answer different questions.'),
        ('Life tests', 'A life test runs an item for a long time to find how it wears. Some faults only show up after many hours. A short test can pass a part that will later fail.'),
        ('When tests fail', 'A failed test is information. Find the true cause before the fix. A quick repair that hides the cause can leave the same fault waiting for the next flight.'),
        ('The Hubble mirror', "The Hubble Space Telescope's main mirror was ground to the wrong shape around 1980. A testing device was assembled with a small error, and the error was not caught until launch in 1990. Its images were blurred until a corrective optic was fitted in 1993."),
        ('Lessons', 'Test early and often. Keep test equipment checked against a standard. When a test and a model disagree, find out why before trusting either.'),
    ],
    'test': [
        ('What is the main rule of testing?', [('a', 'Test everything in a laboratory only'), ('b', 'Test the item the way it will be used'), ('c', 'Test only the cheapest parts'), ('d', 'Never test at all')], 'b'),
        ('What is the purpose of a qualification test?', [('a', 'To set the price of a part'), ('b', 'To choose a name for the part'), ('c', 'To find the colour of the paint'), ('d', 'To prove a design has margin by testing it above the stress it will meet')], 'd'),
        ('What does a life test show?', [('a', 'How fast a part can be painted'), ('b', 'The price of a part'), ('c', 'How an item wears over a long time'), ('d', 'How many colours it has')], 'c'),
        ('What did the Hubble mirror case show?', [('a', 'A testing device with a small error can hide a large fault until launch'), ('b', 'Mirrors never need tests'), ('c', 'Testing always finds every fault'), ('d', 'Launch is the best place to test')], 'a'),
        ('What should happen when a test fails?', [('a', 'Ignore the result'), ('b', 'Hide the result from the crew'), ('c', 'Repeat the test until it passes'), ('d', 'Find the true cause before the fix')], 'd'),
    ],
}
