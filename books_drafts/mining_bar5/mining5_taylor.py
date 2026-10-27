"""Forest Hardening Theory: how tangled dislocations build up strength as a metal is deformed."""
CODE = 'mining5_taylor'
BOOK = {
    "title": 'Forest Hardening Theory',
    "subtitle": 'How tangled dislocations build strength as a metal is bent',
    "chapters": [
        ('Dislocations everywhere', 'As a metal is deformed, the number of dislocations grows very fast. The dislocations tangle with one another like the trunks of a forest. This is why a worked metal is harder than an annealed one.'),
        ('Dislocation forests', 'A moving dislocation must cut through the forest of others, which costs energy. The more dislocations there are, the harder it is to move any one of them. The stress needed to keep deforming goes up.'),
        ('Taylor factor', 'Real metals are made of many grains, each turning in a different way. The Taylor factor links the stress in a single crystal to the stress in the whole material. It is used to convert lab results into useful design numbers.'),
        ('Work hardening rates', 'The rate of hardening changes as deformation goes on. Early on, hardening is fast and then it slows. Engineers track this rate to predict how a part will behave.'),
        ('Stages', 'Many metals show stages of hardening. Each stage is linked to a change in how dislocations move or tangle. Knowing the stages helps predict where a metal will fail.'),
        ('Models and tests', 'Models of forest hardening are tested against tensile tests and careful lab work. A good model fits the data across many conditions. Models are only as good as the tests behind them.'),
    ],
    "test": [
        ('What happens to dislocations as a metal is deformed?', [('a', 'They disappear at once'), ('b', 'They turn into glass'), ('c', 'They are blown away'), ('d', 'Their number grows and they tangle')], 'd'),
        ('Why does a worked metal get harder?', [('a', 'Dislocations tangle, making them harder to move'), ('b', 'The metal gets lighter'), ('c', 'The metal melts'), ('d', 'The metal turns soft')], 'a'),
        ('What does the Taylor factor link?', [('a', 'The price and the weight of a metal'), ('b', 'The stress in one crystal to the stress in the whole material'), ('c', 'The colour and the smell'), ('d', 'The size of a truck and its driver')], 'b'),
        ('What do engineers track to predict behaviour?', [('a', 'The number of birds nearby'), ('b', 'The shape of the lid'), ('c', 'The work hardening rate'), ('d', 'The time of day')], 'c'),
        ('How are forest hardening models checked?', [('a', 'By guessing'), ('b', 'By reading a menu'), ('c', 'By counting coins'), ('d', 'Against tensile tests and careful lab work')], 'd'),
    ],
}
