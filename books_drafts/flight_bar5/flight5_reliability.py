"""Reliability Mathematics: how parts fail, how long they last, and how redundancy changes the odds."""
CODE = 'flight5_reliability'
BOOK = {
    'title': 'Reliability Mathematics',
    'subtitle': 'How often things fail, and how to make them last',
    'chapters': [
        ('Failure is a rate', 'Reliability asks how often something fails over time. A failure rate counts failures per unit of time, such as per thousand hours of use. Numbers like these let engineers compare parts fairly.'),
        ('The bathtub curve', 'Many parts fail often when new, then rarely for a long middle period, then more often again as they wear out. Drawn over time, this shape looks like a bathtub. Testing and burn-in aim to remove the early failures.'),
        ('Mean time between failures', 'Mean time between failures, or MTBF, is the average time a repairable item runs before it fails. It is useful, but it hides the spread. Two items with the same average can behave very differently.'),
        ('Series and parallel', 'Parts in series all have to work, so the total reliability is lower than any single part. Parts in parallel need only one to work, so the total reliability is higher. Redundancy is the use of parallel parts.'),
        ('The gain from redundancy', 'Adding a second independent unit can greatly improve the odds, but only if the two fail independently. A shared fault, such as a common power supply, can undo the gain.'),
        ('Testing the numbers', 'Reliability numbers come from tests and from data on real use. Test enough units for the results to mean something. A number with no test behind it is only a hope.'),
    ],
    'test': [
        ('What does a failure rate measure?', [('a', 'The colour of a part'), ('b', 'The weight of a part'), ('c', 'The price of a part'), ('d', 'Failures per unit of time')], 'd'),
        ('What shape does the bathtub curve describe?', [('a', 'Failures that never change'), ('b', 'Failures that are high when new, low in the middle, and rise again as parts wear out'), ('c', 'Failures that only happen at the end'), ('d', 'A rise that never stops')], 'b'),
        ('What does MTBF stand for?', [('a', 'Mean time between failures'), ('b', 'Main tank boost factor'), ('c', 'Minimum time before fuel'), ('d', 'Mass times bearing force')], 'a'),
        ('What happens to total reliability when parts are in series?', [('a', 'It is always higher than any part'), ('b', 'It does not change'), ('c', 'It is lower than any single part, since all must work'), ('d', 'It is always exactly zero')], 'c'),
        ('Why can a shared fault undo the gain from redundancy?', [('a', 'Because redundancy adds weight'), ('b', 'Because the two units then fail together, not independently'), ('c', 'Because spare units never work'), ('d', 'Because parallel parts always fail first')], 'b'),
    ],
}
