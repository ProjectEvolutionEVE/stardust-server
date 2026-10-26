"""Probabilistic Risk Assessment: estimating the chance of failure, and its honest limits."""
CODE = 'flight5_probabilistic'
BOOK = {
    'title': 'Probabilistic Risk Assessment',
    'subtitle': 'Estimating the chance of failure, and its limits',
    'chapters': [
        ('What it is', 'Probabilistic risk assessment, or PRA, estimates how likely a bad outcome is. It builds a model of the system, lists many scenarios, and gives each a chance of happening.'),
        ("Rasmussen's report", 'The 1975 Reactor Safety Study, known as WASH-1400, was an early large PRA of nuclear plants. The statistician Norman Rasmussen led the work, which brought the method to wide attention.'),
        ('Scenarios', 'A scenario is a chain of events that could lead to an accident. PRA lists many scenarios, not just the one that the designers feared. A complete list is hard, so the model is only as good as its scenario set.'),
        ('Uncertainty', 'Every estimate has uncertainty. A good PRA shows the range, not only the single answer. A small change in an assumed input can change the answer a great deal.'),
        ('Using it in decisions', 'PRA helps compare options and find the biggest contributors to risk. It helps the leader spend money where it lowers risk most. It does not replace judgement about what level of risk is acceptable.'),
        ('Critics', 'Critics say that numbers can look more precise than they are, and that rare events are hard to estimate. Their point is fair. Treat a PRA as one honest input, and say clearly what it cannot show.'),
    ],
    'test': [
        ('What does PRA estimate?', [('a', 'How likely a bad outcome is'), ('b', 'The colour of a ship'), ('c', 'The number of crew'), ('d', 'The size of a planet')], 'a'),
        ('What was WASH-1400?', [('a', 'A cooking recipe'), ('b', "A ship's log"), ('c', 'A 1975 study of nuclear reactor safety'), ('d', 'A type of rocket fuel')], 'c'),
        ('What is a scenario in PRA?', [('a', 'A film used for training'), ('b', 'A chain of events that could lead to an accident'), ('c', 'A fixed price list'), ('d', 'A type of engine')], 'b'),
        ('Why should a PRA show a range?', [('a', 'Ranges are shorter to read'), ('b', 'Ranges are always exact'), ('c', 'Ranges avoid all risk'), ('d', 'Every estimate has uncertainty, and small input changes can change the answer a lot')], 'd'),
        ('What does a PRA not do?', [('a', 'Compare options'), ('b', 'Find the biggest contributors to risk'), ('c', 'Replace judgement about what level of risk is acceptable'), ('d', 'Help spend money where it lowers risk most')], 'c'),
    ],
}
