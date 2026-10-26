"""Reliability: how often parts fail, what the averages mean, and why records matter."""
CODE = 'engineering3c_reliability'
BOOK = {
    "title": 'Reliability: How Often Things Fail',
    "subtitle": 'Failure rates, mean time between failures and the bathtub curve',
    "chapters": [
        ('Reliability is a chance',
         "Reliability is the chance that a part keeps working for a set time under set conditions. No part is perfect, so engineers describe failures with rates and averages. A reliable part is one that fails rarely, not one that never fails."),
        ('Failure rate and MTBF',
         "The failure rate is how many failures happen per unit of working time, for example per thousand hours. When failures happen at random, the mean time between failures (MTBF) is roughly the inverse of that rate. An MTBF is an average across many parts, not a promise for one part."),
        ('The bathtub curve',
         "Many products fail often when new, from poor assembly or weak parts. They then settle into a long quiet period with few random failures. Near the end of their life, wear makes failures rise again. Plotted over time, the curve is shaped like a bathtub."),
        ('Parts in a chain',
         "A system that fails if any one part fails is a series system. Its reliability is the product of its parts' reliabilities, so it is always lower than that of its weakest part alone. Many good parts in a chain can still add up to a poor system."),
        ('Money and failure',
         "Failures cost money in repairs, lost work and spares. A part that costs a little more but fails far less often can save much more than its extra price. Work out the expected cost of failure, not only the price of the part."),
        ('Measuring reliability',
         "Reliability comes from records: when each part was fitted, how long it ran and how it failed. Keep those records for every part and review them regularly. Without records, the numbers are only guesses."),
    ],
    "test": [
        ('What is reliability?',
         [('a', 'The chance a part keeps working for a set time under set conditions'), ('b', 'The weight of a part'), ('c', 'The price of a part'), ('d', 'The number of parts in a machine')], 'a'),
        ('When failures happen at random, the mean time between failures is roughly what?',
         [('a', 'The failure rate multiplied by ten'), ('b', 'The number of parts in the system'), ('c', 'The inverse of the failure rate'), ('d', 'The price of the part')], 'c'),
        ('What does the bathtub curve show?',
         [('a', 'The shape of a bath'), ('b', 'Failures high early, low for a long middle period, and rising again near the end of life'), ('c', 'A cleaning schedule'), ('d', 'A type of motor')], 'b'),
        ('In a series system, how does reliability compare with the weakest part alone?',
         [('a', 'It is higher'), ('b', 'It is the same'), ('c', 'It equals zero'), ('d', 'It is always lower')], 'd'),
        ('Why keep records of every part?',
         [('a', 'So the paint matches'), ('b', 'To lower the weight'), ('c', 'Without records, reliability numbers are only guesses'), ('d', 'For the market price')], 'c'),
    ],
}
