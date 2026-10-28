"""Feature Flags and Progressive Delivery: switching features on for some users, and turning them off when needed."""
CODE = 'computing4_feature_flags'
BOOK = {
    "title": 'Feature Flags and Progressive Delivery',
    "subtitle": 'Switching features on for some people first, with a way to turn them off',
    "chapters": [
        ('What a feature flag is',
         'A feature flag is a switch in the code or its configuration that turns a feature on or off without a new release. It lets the code for a new feature sit in production while only some people can see it. The switch is read when the program runs.'),
        ('Percentage rollouts',
         'A team can show a feature to one per cent of users, then ten, then all of them. Each step gives the team time to watch errors, speed and customer reaction. If something goes wrong, the rollout stops at once.'),
        ('Kill switches',
         'A kill switch is a flag whose only job is to turn a feature off quickly during an incident. Teams prepare kill switches for risky features before they launch, so that switching off does not need a new release.'),
        ('Flag debt',
         'Flags left in the code after a rollout finishes become flag debt. Each old flag adds a branch that must be understood and tested. Good teams set a date to remove a flag once it has served its purpose.'),
        ('Experiments and cohorts',
         'Flags can split users into groups, called cohorts, to compare two versions of a feature. Fair comparison needs each user to stay in the same group for the whole test. Teams also need to know how long a test must run before the results can be trusted.'),
        ('Governance',
         'Someone should own each flag, and changes to important flags should be recorded. Flags that control money, privacy or safety need stricter rules than a button colour. A short written rule for who may change what keeps the system safe as it grows.'),
    ],
    "test": [
        ('What does a feature flag let a team do?',
         [('a', 'Print paper copies of the code'), ('b', 'Delete the database'), ('c', 'Skip all testing forever'), ('d', 'Turn a feature on or off without a new release')], 'd'),
        ('Why roll out a feature to one per cent of users first?',
         [('a', 'So the feature is never seen'), ('b', 'So the feature can be watched while the impact is small'), ('c', 'Because one per cent is the legal limit'), ('d', 'Because the other users are not allowed to use computers')], 'b'),
        ('What is a kill switch?',
         [('a', 'A lock on the server room door'), ('b', 'A tool that deletes old users'), ('c', 'A flag that quickly turns a feature off during an incident'), ('d', 'A way to speed up the database')], 'c'),
        ('What is flag debt?',
         [('a', 'Old flags left in the code that add branches to understand and test'), ('b', 'Money owed to the flag company'), ('c', 'A debt for printing flags on paper'), ('d', 'A bug in the browser')], 'a'),
        ('Why should each user stay in the same cohort during an experiment?',
         [('a', 'So the users can be charged more'), ('b', 'So the comparison between the groups stays fair'), ('c', 'So the flags never change'), ('d', 'So the server runs more slowly')], 'b'),
    ],
}
