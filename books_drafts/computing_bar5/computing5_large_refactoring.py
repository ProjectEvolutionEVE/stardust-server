"""Large-Scale Refactoring: changing a big codebase safely, in steps that keep it working and let many teams move together."""
CODE = 'computing5_large_refactoring'
BOOK = {
    "title": 'Large-Scale Refactoring',
    "subtitle": 'Changing a big codebase in safe, measured steps',
    "chapters": [
        ('Why large refactoring is different',
         'A small refactoring touches one file, but a large one touches hundreds of files and many teams. Mistakes spread quickly and are costly to undo. The work must be planned as a series of safe steps.'),
        ('Codemods',
         'A codemod is a program that rewrites code automatically in a consistent way. It can change thousands of call sites in minutes. Good codemods are tested on sample code before they touch the real codebase.'),
        ('Branch by abstraction',
         'Branch by abstraction adds an interface in front of the old code, moves callers to it, and then swaps the implementation behind it. The system keeps working throughout. The old code is removed at the end.'),
        ('Parallel change',
         'Parallel change, also called expand and contract, first adds the new form alongside the old one. Users move across at their own pace, and the old form is removed once nobody needs it. This avoids a risky single switch-over.'),
        ('Measuring progress',
         'Teams track how many call sites, modules or old patterns remain. A visible count keeps the work honest and shows when it is near done. Progress that is not measured is easy to misjudge.'),
        ('Team coordination and risk control',
         'Many people changing the same code need clear ownership and frequent integration. Feature flags, staged rollouts and fast rollbacks control the risk. Communication keeps every team aware of the changes that affect them.'),
    ],
    "test": [
        ('What does a codemod do?',
         [('a', 'It writes a poem about the code'), ('b', 'It sends invoices'), ('c', 'It rewrites code automatically in a consistent way'), ('d', 'It paints the office walls')], 'c'),
        ('What is the core step of branch by abstraction?',
         [('a', 'Adding an interface in front of the old code and swapping the implementation behind it'), ('b', 'Deleting the whole system at once'), ('c', 'Printing the code on paper'), ('d', 'Renaming every user')], 'a'),
        ('What is parallel change also called?',
         [('a', 'Stop and start'), ('b', 'Copy and forget'), ('c', 'Shout and wait'), ('d', 'Expand and contract')], 'd'),
        ('Why should progress in a large refactoring be measured?',
         [('a', 'So the code gets longer'), ('b', 'So the team can see what remains and avoid misjudging progress'), ('c', 'So no one needs to test'), ('d', 'So the project can be hidden')], 'b'),
        ('Which practice helps control risk in a large change?',
         [('a', 'Releasing everything at once with no backup'), ('b', 'Turning off all tests'), ('c', 'Staged rollouts with feature flags and fast rollbacks'), ('d', 'Working on it alone for a year with no review')], 'c'),
    ],
}
