"""The Pre-mortem: imagine the failure before it happens, and find the causes while there is still time."""
CODE = 'flight5_pre_mortem'
BOOK = {
    'title': 'The Pre-mortem',
    'subtitle': 'Imagine the failure first, then prevent it',
    'chapters': [
        ('What a pre-mortem is', 'A pre-mortem is a meeting held before a plan starts. The team imagines that the plan has already failed badly, and then writes down why. It is the opposite of a post-mortem, which looks back after the damage is done.'),
        ('The idea behind it', 'The psychologist Gary Klein developed the technique and wrote about it for business leaders. People are often shy about raising doubts about a plan the boss likes. Imagining failure as a settled fact frees people to speak.'),
        ('How to run one', 'Ask everyone to write down the reasons the plan failed, alone and in silence first. Collect the reasons without judging them. Then sort them by how likely they are and how much harm they would do.'),
        ('Turn causes into guards', 'For each cause on the list, decide what will stop it or warn you early. Give each guard an owner and a date. A cause with no guard is a risk you have chosen to accept, and that choice should be made on purpose.'),
        ('An example', 'Imagine a mining run that comes back with an empty hold. The team might list a fuel gauge that was misread, a route that was not checked, or a crew that was too tired. Each of those becomes a check before the next run.'),
        ('When to use it', 'Use a pre-mortem before any big launch, a new design, or a major purchase. Repeat it at key stages. Keep the list where the team can see it while the work goes on.'),
    ],
    'test': [
        ('When is a pre-mortem held?', [('a', 'After the project has failed'), ('b', 'Before the plan starts'), ('c', 'Only during a launch'), ('d', 'Never, because it is bad luck')], 'b'),
        ('Who developed the pre-mortem technique?', [('a', 'Isaac Asimov'), ('b', 'Rachel Carson'), ('c', 'Gregor Mendel'), ('d', 'Gary Klein')], 'd'),
        ('What does a pre-mortem ask the team to imagine?', [('a', 'That the plan has already succeeded'), ('b', 'That nothing will ever change'), ('c', 'That the plan has already failed and why'), ('d', 'That the team will be replaced')], 'c'),
        ('Why are people helped by the pre-mortem frame?', [('a', 'Imagining failure as settled lets people raise doubts more freely'), ('b', 'It makes meetings shorter'), ('c', 'It removes the need for a budget'), ('d', 'It lets the boss decide alone')], 'a'),
        ('What should happen to each cause on the list?', [('a', 'It should be deleted at once'), ('b', 'It should be kept secret'), ('c', 'It should be left to chance'), ('d', 'It should get a guard, an owner and a date')], 'd'),
    ],
}
