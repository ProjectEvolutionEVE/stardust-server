"""Trunk-Based Development and CI/CD: keeping the main line of code always ready to release."""
CODE = 'computing4_trunk_cicd'
BOOK = {
    "title": 'Trunk-Based Development and CI/CD',
    "subtitle": 'Short branches, automatic checks, and a main line that is always ready',
    "chapters": [
        ('The trunk',
         'In trunk-based development, everyone works on one shared main line of code, called the trunk. Changes are merged into it often, usually every day. Long-lived branches that drift apart are avoided because they make joining work painful.'),
        ('Short-lived branches',
         'When a branch is used, it should live for hours or a few days, not weeks. Small changes are easier to review, easier to test and easier to undo. A branch that lives too long becomes a merge project of its own.'),
        ('Continuous integration rules',
         'Continuous integration means every change is built and tested automatically when it is merged. A simple rule helps: if the build is broken, fixing it comes first, before any new work. The main line should always be green.'),
        ('Pipeline stages',
         'A delivery pipeline is a series of stages, such as build, unit tests, integration tests and deployment. Each stage must pass before the next begins. Fast stages come first, so a mistake is caught in minutes rather than hours.'),
        ('Automated gates',
         'A gate is a check that decides whether a change may move on. Gates can test security, performance or basic health. Gates work best when they are automatic, quick and clear about why they failed.'),
        ('Deployment frequency',
         'Teams that merge and release often tend to find problems sooner and fix them more quickly. Frequent small releases are less risky than rare large ones. The aim is a main line that could be released at any time.'),
    ],
    "test": [
        ('What is the trunk in trunk-based development?',
         [('a', 'The shared main line that everyone merges into'), ('b', 'A large folder of paper notes'), ('c', 'A backup of the database'), ('d', 'The name of a programming language')], 'a'),
        ('Why are short-lived branches preferred?',
         [('a', 'They make merging harder'), ('b', 'They keep work secret from the team'), ('c', 'They are easier to review, test and undo'), ('d', 'They make releases slower')], 'c'),
        ('What should happen first when the main line build is broken?',
         [('a', 'New features are started'), ('b', 'The break is fixed before any new work'), ('c', 'The tests are deleted'), ('d', 'The branch is renamed')], 'b'),
        ('Why do pipelines put fast stages first?',
         [('a', 'So the slowest stage always runs first'), ('b', 'So nothing is ever tested'), ('c', 'So the team can go home early'), ('d', 'So a mistake is found in minutes rather than hours')], 'd'),
        ('What is an automated gate?',
         [('a', 'A check that decides whether a change may move on'), ('b', 'A physical gate at the office door'), ('c', 'A tool that writes documentation'), ('d', 'A type of network cable')], 'a'),
    ],
}
