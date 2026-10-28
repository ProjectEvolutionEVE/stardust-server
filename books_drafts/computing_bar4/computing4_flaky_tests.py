"""Flaky Tests at Scale: tests that fail at random, why they happen, and what they cost a team."""
CODE = 'computing4_flaky_tests'
BOOK = {
    "title": 'Flaky Tests at Scale',
    "subtitle": 'Tests that fail at random, why they happen, and what they cost a team',
    "chapters": [
        ('Nondeterministic failures',
         'A flaky test passes and fails on the same code without any change. Such tests make results hard to trust. A failure may be a real bug, or it may be nothing at all, and the team cannot tell which.'),
        ('Root causes',
         'Common causes include timing assumptions, shared state between tests, unordered data, and dependence on a live network. Tests that depend on the clock or on random numbers can also flicker. Finding the cause usually needs careful reading and a repeatable run.'),
        ('Quarantine policies',
         'A quarantine moves a known flaky test out of the main gate, so it no longer blocks everyone, while it is fixed. A quarantine needs an owner, a deadline and a clear limit. Without those, the quarantine becomes a place where tests go to be forgotten.'),
        ('Retry trade-offs',
         'Automatic retries can hide flakiness, and a test that passes on the third try is not proof of correctness. Retries can also slow the pipeline and mask real intermittent bugs. Use them carefully, and record every retry so the cost stays visible.'),
        ('Detection tools',
         'Some tools run tests many times to measure how often they flip. Others track history and flag tests with mixed results. Detection is useful only when the findings lead to someone fixing the test.'),
        ('The cultural cost',
         'Flaky tests teach people to ignore red builds, and then real failures get ignored too. Trust in the test suite is a shared asset that is slow to build and quick to lose. Treat flakiness as a real defect, with the same respect as a bug.'),
    ],
    "test": [
        ('What is a flaky test?',
         [('a', 'A test that always fails'), ('b', 'A test that passes and fails on the same code with no change'), ('c', 'A test written on paper'), ('d', 'A test that is never run')], 'b'),
        ('Which is a common root cause of flakiness?',
         [('a', 'Having a clean, isolated test environment'), ('b', 'Using a colour scheme'), ('c', 'Writing comments'), ('d', 'Shared state between tests')], 'd'),
        ('What does a quarantine do?',
         [('a', 'Moves a flaky test out of the main gate while it is fixed'), ('b', 'Deletes the entire test suite'), ('c', 'Stops the computer'), ('d', 'Makes tests run twice as slow for everyone')], 'a'),
        ('What is the risk of automatic retries?',
         [('a', 'They make the tests more accurate'), ('b', 'They remove all failures'), ('c', 'They can hide real intermittent bugs'), ('d', 'They cost nothing at all')], 'c'),
        ('Why does flakiness have a cultural cost?',
         [('a', 'It makes meetings shorter'), ('b', 'It means the team never writes code'), ('c', 'It changes the company name'), ('d', 'People learn to ignore red builds, so real failures get ignored too')], 'd'),
    ],
}
