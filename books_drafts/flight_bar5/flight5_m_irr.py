"""Internal Rate of Return: the rate at which a project exactly breaks even, and why it must be used with care."""
CODE = 'flight5_m_irr'
BOOK = {
    'title': 'Internal Rate of Return',
    'subtitle': 'The rate that makes a project break even',
    'chapters': [
        ('What IRR means', "The internal rate of return, or IRR, is the discount rate at which a project's net present value is exactly zero. It is the project's own rate of return."),
        ('Calculating it', 'IRR is usually found by trial: try a rate, see whether the NPV is above or below zero, and adjust until it reaches zero. A spreadsheet or calculator does this quickly.'),
        ('IRR against NPV', 'IRR is easy to compare with a cost of money, such as a loan rate. NPV gives a size of value in money. For a single project with ordinary flows, both usually point the same way.'),
        ('Multiple answers', 'A project with cash flows that switch sign more than once can have more than one IRR. Then the figure is misleading. In such cases, rely on NPV.'),
        ('Payback period', 'Payback period is the time needed to get the money back. It ignores timing within the payback and everything after it. It is a rough safety test, not a full measure of value.'),
        ('Using them together', 'Use NPV as the main test and IRR as a helpful check. Use payback for a quick sense of risk. Explain the choice to the crew in plain words.'),
    ],
    'test': [
        ('What is the internal rate of return?', [('a', 'The rate of interest in a bank'), ('b', 'The rate of crew pay'), ('c', 'The rate of fuel use'), ('d', "The rate at which the project's NPV is exactly zero")], 'd'),
        ('When can a project have more than one IRR?', [('a', 'When it has only one crew member'), ('b', 'When its cash flows switch sign more than once'), ('c', 'When it is painted twice'), ('d', 'When it is sold on a Monday')], 'b'),
        ('What does payback period measure?', [('a', 'The time needed to get the money back'), ('b', 'The number of stars seen'), ('c', 'The weight of the craft'), ('d', 'The colour of the invoice')], 'a'),
        ('Which measure gives the size of value in money?', [('a', 'The colour code'), ('b', 'The crew list'), ('c', 'NPV'), ('d', 'The weather')], 'c'),
        ('What is a weakness of payback period?', [('a', 'It counts every penny exactly'), ('b', 'It ignores what happens after the payback point'), ('c', 'It uses no numbers at all'), ('d', 'It is always the best measure')], 'b'),
    ],
}
