"""Computational Materials Discovery: using computers to find promising new materials before a lab test."""
CODE = 'mining5_mat_discov'
BOOK = {
    "title": 'Computational Materials Discovery',
    "subtitle": 'Finding promising materials on a computer first',
    "chapters": [
        ('Density functional theory', 'Density functional theory, usually shortened to DFT, is a method for calculating how the electrons in a material are arranged. It predicts many properties from the atoms alone. It is one of the main tools of computational materials science.'),
        ('Screening', 'Screening means testing thousands of candidate materials on a computer and keeping the few that look promising. It is much cheaper and faster than making each material in a lab. The best candidates then go forward to experiments.'),
        ('Databases', 'Public databases collect the calculated and measured properties of many materials. Researchers search them to find starting points and to compare results. Good databases are checked and labelled with how each number was found.'),
        ('Validation', 'A predicted material must still be made and tested in the real world. Many promising candidates fail when someone tries to make them, because they are unstable or hard to produce. Experiment is the final judge.'),
        ('Machine learning', 'Machine learning models can learn patterns from existing data and predict new properties very quickly. They speed up screening, but they only work well for materials similar to those they were trained on. Their results still need checking.'),
        ('Limits', 'Calculations rely on approximations, and some properties, such as the size of an energy gap, are often estimated with less accuracy. Computers can narrow the search, but they cannot replace careful lab work. Honest reporting of uncertainty is part of good science.'),
    ],
    "test": [
        ('What does DFT help a researcher calculate?', [('a', 'The price of a metal'), ('b', 'The colour of a paint tin'), ('c', 'The age of a rock'), ('d', 'How the electrons in a material are arranged')], 'd'),
        ('What does screening mean in materials discovery?', [('a', 'Making a material by hand in a lab'), ('b', 'Testing many candidates on a computer and keeping the promising few'), ('c', 'Painting a sample grey'), ('d', 'Cutting a sample into thin sheets')], 'b'),
        ('Why must a predicted material still be tested in a lab?', [('a', 'Because computers cannot count'), ('b', 'Because labs are required by law to use paper'), ('c', 'Because many promising candidates fail when made'), ('d', 'Because models always give perfect answers')], 'c'),
        ('What is a limit of machine learning models for materials?', [('a', 'They only work well for materials similar to their training data'), ('b', 'They cannot run on any computer'), ('c', 'They only predict colours'), ('d', 'They never make errors')], 'a'),
        ('Why are public materials databases useful?', [('a', 'They sell metals on the market'), ('b', 'They collect properties of many materials for researchers to compare'), ('c', 'They replace all experiments'), ('d', 'They store only photographs')], 'b'),
    ],
}
