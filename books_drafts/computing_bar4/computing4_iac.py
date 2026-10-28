"""Infrastructure as Code: describing servers and networks in files, so they can be planned, applied and checked."""
CODE = 'computing4_iac'
BOOK = {
    "title": 'Infrastructure as Code',
    "subtitle": 'Describing servers and networks in files that can be reviewed and repeated',
    "chapters": [
        ('Declarative infrastructure',
         'Infrastructure as code means writing down the servers, networks and storage you want in files, instead of clicking through a web console. You describe the end state, and a tool works out the steps to reach it. The files can be stored, reviewed and repeated.'),
        ('State files',
         'Many tools keep a state file that records what they have already built. The tool compares the state file with the files you wrote to decide what to change. A lost or damaged state file is serious, so it must be stored safely and locked during changes.'),
        ('Plan and apply',
         'A good workflow has two steps. The plan shows what would change, without changing anything. The apply step makes those changes. Reading the plan before applying it is one of the best habits a team can build.'),
        ('Drift detection',
         'Drift happens when someone changes a server by hand, and the real system no longer matches the files. Regular drift checks find these differences. The fix is either to update the files or to put the real system back the way the files say.'),
        ('Modules',
         'A module is a reusable package of infrastructure files, such as a standard database setup. Modules help teams avoid copying the same settings many times. Their interfaces should be small and clear, so that a change in one place does not break many others.'),
        ('Testing infrastructure code',
         'Infrastructure code can be tested. Static checks look for mistakes before anything runs. Short-lived test environments can be built and destroyed to prove the code works. Testing gives confidence that the next change will not take the system down.'),
    ],
    "test": [
        ('What does a declarative infrastructure file describe?',
         [('a', 'The steps to click in a web console'), ('b', 'The colour of the servers'), ('c', 'The end state you want'), ('d', 'The names of the staff')], 'c'),
        ('What is the purpose of a state file?',
         [('a', 'To record what the tool has already built'), ('b', 'To store the team lunch menu'), ('c', 'To hold the user passwords in plain text'), ('d', 'To print the network diagram')], 'a'),
        ('What does the plan step show?',
         [('a', 'The final invoice'), ('b', 'A list of old holidays'), ('c', 'The weather in the data centre'), ('d', 'What would change, without changing anything')], 'd'),
        ('What is drift?',
         [('a', 'A type of network cable'), ('b', 'The real system no longer matching the files'), ('c', 'A fast way to deploy'), ('d', 'A new programming language')], 'b'),
        ('Why keep module interfaces small and clear?',
         [('a', 'So the module is hard to read'), ('b', 'So the module can never be reused'), ('c', 'So a change in one place does not break many others'), ('d', 'So the module runs on paper')], 'c'),
    ],
}
