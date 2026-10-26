"""Trade Studies: comparing options against weighted criteria, and testing whether the choice holds up."""
CODE = 'flight5_trade_studies'
BOOK = {
    'title': 'Trade Studies',
    'subtitle': 'Comparing options fairly, and testing the choice',
    'chapters': [
        ('What a trade study is', 'A trade study compares two or more ways of meeting a need. It makes the choice visible, and it records the reasons. A good study can be read and checked by someone who was not there.'),
        ('The options list', 'Start with a full list of options, including the ones that seem unlikely. Leaving out a good option early can hide the best answer. Keep the list open until the criteria are set.'),
        ('Criteria and weights', 'Set the criteria before scoring: cost, mass, safety, time and so on. Give each criterion a weight that matches its importance to the mission. Agree the weights before anyone sees the scores.'),
        ('Scoring', 'Score each option against each criterion on one clear scale. Multiply each score by its weight and add up the totals. The highest total is not always the right choice, but it is a clear starting point.'),
        ('Sensitivity', 'Test whether the answer changes when the weights or scores change a little. If a small change flips the winner, the choice is close, and the leader should know it.'),
        ('Examples and limits', 'Trade studies are used for rockets, habitats and software alike. They cannot settle a question of values by arithmetic alone. Use them to inform the decision, not to replace it.'),
    ],
    'test': [
        ('What does a trade study compare?', [('a', 'Two or more ways of meeting a need'), ('b', 'Colours of paint'), ('c', 'Numbers of crew members'), ('d', 'Weather reports')], 'a'),
        ('Why should the criteria and weights be set before scoring?', [('a', 'So the scores are shorter'), ('b', 'So the options are hidden'), ('c', 'So the scores cannot be shaped to suit a favourite option'), ('d', 'So no one needs to read the study')], 'c'),
        ('What is the purpose of a sensitivity check?', [('a', 'To make the study longer'), ('b', 'To see whether a small change in weights or scores flips the winner'), ('c', 'To choose the cheapest paint'), ('d', 'To remove all criteria')], 'b'),
        ('Why keep unlikely options on the list early on?', [('a', 'Unlikely options are always best'), ('b', 'Lists must be as long as possible'), ('c', 'Options cannot be removed later'), ('d', 'A good option left out early can hide the best answer')], 'd'),
        ("Can a trade study replace the leader's judgement?", [('a', 'Yes, it always decides for you'), ('b', 'Yes, if it has many colours'), ('c', 'No, it informs the decision but cannot settle questions of value alone'), ('d', 'Yes, if it is written by a computer')], 'c'),
    ],
}
