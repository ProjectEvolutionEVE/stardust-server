"""Spreadsheet Risk and End-User Software: why spreadsheets that run real decisions need the same care as other software."""
CODE = 'computing5_spreadsheet_risk'
BOOK = {
    "title": 'Spreadsheet Risk and End-User Software',
    "subtitle": 'When a spreadsheet becomes production software',
    "chapters": [
        ('Spreadsheets as software',
         'Many important decisions are made with spreadsheets that were built for quick use and then kept for years. They are real software, even though they seldom look like it. Their risks deserve the same attention as any program.'),
        ('Famous errors',
         'Researchers have published several well-known cases where a spreadsheet error changed a public or scientific result. One example involved a formula range that left out rows, and was found only when others re-checked the work. Such cases show that small mistakes can carry large consequences.'),
        ('Formula audits',
         'A formula audit checks how each important calculation is built, following the links between cells. Auditors look for hidden constants, copied formulas that no longer match, and ranges that miss data. Clear labels make an audit faster.'),
        ('Version control gaps',
         'Spreadsheets are often copied into many files with names such as final version two. Nobody knows which copy is current, and changes are hard to track. Proper version control reduces this confusion.'),
        ('Controls',
         'Controls include locked cells, separated inputs and outputs, reviews of changes and checks that totals reconcile. They reduce the chance of error and make errors easier to spot. Controls should match the importance of the decision.'),
        ('Migration',
         'Moving a critical spreadsheet into a proper system is a project in itself. The old results must be reproduced exactly before the old file is retired. Keeping both running for a period is a common way to check.'),
    ],
    "test": [
        ('What is a risk of treating spreadsheets as casual tools?',
         [('a', 'Spreadsheets cannot hold numbers'), ('b', 'Spreadsheets always make decisions by themselves'), ('c', 'Spreadsheets only open on Mondays'), ('d', 'Important decisions may rest on software that is never properly checked')], 'd'),
        ('What does a formula audit look for?',
         [('a', 'Pictures of the staff'), ('b', 'Hidden constants, copied formulas that no longer match and ranges that miss data'), ('c', 'The font size of the title'), ('d', 'The office plants')], 'b'),
        ('Why are files named final version two a problem?',
         [('a', 'They open faster'), ('b', 'They are automatically deleted'), ('c', 'Nobody can tell which copy is current or track changes'), ('d', 'They add colour to the grid')], 'c'),
        ('Which is an example of a spreadsheet control?',
         [('a', 'Locked cells and reviews of changes'), ('b', 'A bigger monitor'), ('c', 'A louder keyboard'), ('d', 'A decorative border')], 'a'),
        ('What should happen before an old critical spreadsheet is retired?',
         [('a', 'It should be deleted the same day'), ('b', 'Its results must be reproduced exactly in the new system'), ('c', 'It should be printed on a poster'), ('d', 'It should be sent to a stranger')], 'b'),
    ],
}
