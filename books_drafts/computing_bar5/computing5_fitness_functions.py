"""Architecture Fitness Functions: automated checks that keep a system's design rules true as the codebase changes."""
CODE = 'computing5_fitness_functions'
BOOK = {
    "title": 'Architecture Fitness Functions',
    "subtitle": 'Automated checks that keep design rules true over time',
    "chapters": [
        ('What a fitness function is',
         'A fitness function is an automated check of an architectural goal. It runs like a test and gives a clear pass or fail. Its purpose is to keep the design healthy as many people change the code.'),
        ('Automated checks on design rules',
         'A design rule might say that the web layer must never call the database directly. A check can scan the code for that dependency and fail the build if it appears. Rules written as checks are harder to forget than rules written on a wiki page.'),
        ('Dependency rules',
         'Dependency rules limit which parts of a system may depend on which others. Keeping a clear direction of dependency stops the system tangling into a knot. Tools can draw and check these dependencies automatically.'),
        ('Performance budgets',
         'A performance budget sets a limit, such as a maximum response time or memory use. A check runs regularly and reports when the budget is exceeded. This catches slow changes that no single pull request would reveal.'),
        ('Evolving architecture',
         'Architecture changes over time as needs change, so fitness functions must change with it. Teams review their checks when they review their design. A check that no longer matches the goal should be updated or removed.'),
        ('Tooling and false alarms',
         'Tools for these checks include dependency analysers, linters and load tests. False alarms wear down trust, so checks should be precise and explained. A check with a clear reason is much easier to live with.'),
    ],
    "test": [
        ('What is a fitness function?',
         [('a', 'A form for a job interview'), ('b', 'A type of office chair'), ('c', 'A song for a launch party'), ('d', 'An automated check of an architectural goal')], 'd'),
        ('What does a dependency rule limit?',
         [('a', 'How many screens a user owns'), ('b', 'Which parts of a system may depend on which others'), ('c', 'The colour of the logo'), ('d', 'The number of meetings')], 'b'),
        ('What is a performance budget?',
         [('a', 'A plan for a holiday'), ('b', 'A form for expenses'), ('c', 'A limit, such as a maximum response time, checked regularly'), ('d', 'A list of printers')], 'c'),
        ('Why do fitness functions need to change as the architecture evolves?',
         [('a', 'A check that no longer matches the goal should be updated or removed'), ('b', 'Checks never need any change'), ('c', 'Architecture never changes'), ('d', 'Checks are only for paper documents')], 'a'),
        ('Why must checks avoid false alarms?',
         [('a', 'False alarms make computers faster'), ('b', 'False alarms wear down trust in the checks'), ('c', 'False alarms remove all bugs'), ('d', 'False alarms are required by law')], 'b'),
    ],
}
