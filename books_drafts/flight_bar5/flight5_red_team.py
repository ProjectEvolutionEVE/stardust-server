"""Red Teaming: a team whose job is to attack a plan, so that the weak points show before the real attack does."""
CODE = 'flight5_red_team'
BOOK = {
    'title': 'Red Teaming',
    'subtitle': 'A team paid to find the weak points',
    'chapters': [
        ('What red teaming is', 'A red team is a group whose job is to challenge a plan, a design or a defence. It acts as the opponent. Its aim is to find the weak points while there is still time to fix them.'),
        ('Where it began', 'The idea grew out of military war games, where one side played the enemy. Later, governments and large companies used the same method to test their security and their plans.'),
        ("Devil's advocate and red team", "A devil's advocate argues one side inside the team. A red team is outside, has its own method, and looks for ways to break the plan. The two can be used together for more protection."),
        ('Examples', "Security teams test a building's locks and a network's defences by trying to get in. Engineers ask how a system could fail, and then test that failure on purpose. Each attack shows where the plan needs strengthening."),
        ('Rules for a good red team', 'The red team needs the freedom to say what is wrong. Its findings should reach the people who can act on them. Its members should be skilled and should not be punished for finding faults.'),
        ('Limits', 'A red team cannot find every weakness. It can be too narrow, or it can be ignored when the results are unwelcome. Use it as one check among several, not as a guarantee.'),
    ],
    'test': [
        ('What is the job of a red team?', [('a', 'To celebrate the plan'), ('b', 'To write the final report alone'), ('c', 'To challenge the plan and find its weak points'), ('d', 'To run the budget')], 'c'),
        ('Where did the idea of red teaming begin?', [('a', 'In military war games'), ('b', 'In the kitchens of ships'), ('c', 'In school examinations'), ('d', 'In the design of hats')], 'a'),
        ("How does a red team differ from a devil's advocate?", [('a', 'A red team never attacks'), ('b', 'A red team only works in the same room'), ('c', 'There is no difference'), ('d', 'A red team is outside the team and uses its own method to break the plan')], 'd'),
        ('What must a good red team have?', [('a', 'A promise that it will never find faults'), ('b', 'Freedom to say what is wrong and a route to people who can act'), ('c', 'A secret plan of its own'), ('d', 'No contact with the rest of the crew')], 'b'),
        ('What is a limit of red teaming?', [('a', 'It can be too narrow, and its findings can be ignored'), ('b', 'It always finds every fault'), ('c', 'It makes plans slower to build'), ('d', 'It costs nothing to run')], 'a'),
    ],
}
