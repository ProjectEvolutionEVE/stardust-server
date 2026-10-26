"""GAAP and IFRS: why accounting rules exist, principles against rules, major differences, consolidation, convergence efforts, and reading a note."""
CODE = 'business4_gaap'
BOOK = {
    "title": 'GAAP and IFRS',
    "subtitle": 'The rulebooks that tell firms how to record and report their money',
    "chapters": [
        ('Why rules exist',
         "Accounting rules exist so that different firms report in comparable ways. Without them, investors could not tell whether one company's profit was measured like another's. The rules make reports useful for lenders, owners and regulators."),
        ('Principles against rules',
         'IFRS, the International Financial Reporting Standards, is more principle-based. It sets broad aims and expects judgement in applying them. GAAP, the generally accepted accounting principles used in the United States, is more rule-based, with many detailed instructions for specific cases.'),
        ('Major differences',
         'The two systems differ on several points, such as how inventory is valued, how some development costs are handled, and how certain asset values may be revised upward. These differences can change reported profit, so readers must know which rules a company follows.'),
        ('Consolidation',
         'Consolidation means combining the accounts of a parent company and the firms it controls into one set of statements. Both systems require it, but the tests for control and the treatment of some joint arrangements can differ. Groups must decide which firms belong in the figures.'),
        ('Convergence efforts',
         'Regulators have worked for many years to bring GAAP and IFRS closer together. Some differences have narrowed, while others remain. Many countries outside the United States now use IFRS in full, and the United States has kept GAAP for its own companies.'),
        ('Reading a note',
         'Financial statements come with notes that explain how figures were measured and what the risks are. A careful reader checks the accounting policies and the notes before trusting the headline numbers. The notes often say more than the table does.'),
    ],
    "test": [
        ('What does IFRS stand for?',
         [('a', 'Internal Fund Review System'), ('b', 'International Financial Reporting Standards'), ('c', 'International Forecast and Rate Schedule'), ('d', 'Institute of Financial Risk Sharing')], 'b'),
        ('What does GAAP stand for in the United States?',
         [('a', 'General Audit Accounting Protocols'), ('b', 'Government Auditing Act Provisions'), ('c', 'Generally Accepted Accounting Principles'), ('d', 'Global Asset and Good Practice')], 'c'),
        ('Which system is described as more principle-based?',
         [('a', 'GAAP'), ('b', 'Both are equally rule-based'), ('c', 'Neither applies to companies'), ('d', 'IFRS')], 'd'),
        ('What is consolidation?',
         [('a', "Combining a parent company's accounts with those of the firms it controls"), ('b', 'Merging two bank accounts'), ('c', 'Paying off a loan early'), ('d', 'Printing all reports in one colour')], 'a'),
        ('Why should a reader check the notes to the accounts?',
         [('a', 'Because the notes are always wrong'), ('b', 'Because they explain how figures were measured and what the risks are'), ('c', 'Because the notes replace the balance sheet'), ('d', 'Because notes are never published')], 'b'),
    ],
}
