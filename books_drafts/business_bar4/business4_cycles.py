"""The Business Cycle: expansion and recession, peaks and troughs, leading indicators, how downturns are dated, and planning for them."""
CODE = 'business4_cycles'
BOOK = {
    "title": 'The Business Cycle',
    "subtitle": 'Expansion and recession, and how to plan for both',
    "chapters": [
        ('Booms and busts',
         'Economies do not grow in a straight line. They tend to move through phases: a period of growth, a peak, a fall, and a low point before the next climb. Economists call the full swing a business cycle. No two cycles are exactly alike in length or depth.'),
        ('Peaks and troughs',
         'A peak is the high point just before activity turns down. A trough is the low point just before it turns up again. A business that plans for the peak may find itself overbuilt when the trough arrives, so knowing where you stand in the cycle matters.'),
        ('Leading indicators',
         'Some measures change before the economy as a whole does. Orders for new factory goods, building permits, the number of new jobless claims and the shape of the yield curve are watched for this reason. A leading indicator is a warning, not a guarantee.'),
        ('How recessions are dated',
         'In the United States, a committee at the National Bureau of Economic Research looks at several measures together, such as jobs, incomes and output, before it names the dates of a recession. The dates are often confirmed long after they happen, which is why businesses cannot wait for the official word.'),
        ('Policy responses',
         'Governments and central banks often respond to downturns. They may lower interest rates, make borrowing cheaper, or spend more on public projects. These tools can soften a recession, though they work with a delay and cannot remove the cycle altogether.'),
        ('Planning for the downturn',
         'A sensible business builds a cash reserve in good years, keeps debts at a level it can carry in bad ones, and tests how it would fare with less revenue. Expansion is the time to prepare, because a recession is much harder to plan for once it has started.'),
    ],
    "test": [
        ('What is a business cycle?',
         [('a', 'A fixed yearly budget'), ('b', 'A rule about tax deadlines'), ('c', 'A single year of record sales'), ('d', 'The repeated rise and fall of economic activity')], 'd'),
        ('What is a trough?',
         [('a', 'The low point before activity turns up again'), ('b', 'The high point before activity turns down'), ('c', 'A kind of bank loan'), ('d', 'A type of stock market index')], 'a'),
        ('Which of these is an example of a leading indicator?',
         [('a', "Last year's total output"), ('b', 'Orders for new factory goods'), ('c', 'The date of a past recession'), ('d', "A company's audited profit from last year")], 'b'),
        ('What does the National Bureau of Economic Research do in the United States?',
         [('a', 'It sets the price of gold'), ('b', 'It lends money to small firms'), ('c', 'It dates the start and end of recessions'), ('d', "It collects everyone's income tax")], 'c'),
        ('Why should a business build a cash reserve in good years?',
         [('a', 'So it can pay out all profit at once'), ('b', 'Because reserves are never taxed'), ('c', 'Because reserves stop recessions from starting'), ('d', 'So it can get through a downturn with less strain')], 'd'),
    ],
}
