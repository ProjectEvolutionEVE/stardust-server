"""Attack trees: goals as root nodes, OR and AND branches, costing attacks, placing mitigations and using trees with threat models."""
CODE = 'computing5_attack_trees'
BOOK = {
    "title": 'Attack Trees',
    "subtitle": 'Drawing the paths an attacker could take, and the cost of each',
    "chapters": [
        ('The idea',
         'An attack tree starts with one goal at the top, such as stealing customer records. Below it, the tree breaks the goal into smaller ways to reach it.'),
        ('OR and AND',
         'An OR branch offers several separate ways to reach a goal, and the attacker needs only one. An AND branch lists steps that must all succeed together.'),
        ('Costing the attack',
         'Each leaf of the tree gets an estimate, such as the money, time or skill needed. The cheapest path through the tree shows where an attacker would most likely go.'),
        ('Adding defences',
         'Mitigations are placed on the branches they block. A defence on the cheapest path changes the whole picture, while a defence on an expensive path may add little.'),
        ('Using with threat models',
         'Attack trees work well with threat models. The threat model says who the attacker is, and the tree shows the detailed routes that attacker might take.'),
        ('Limits',
         'Trees grow large fast, and their numbers are only estimates from expert judgement. They do not capture every surprise, so they are a guide to thinking, not a full proof.'),
    ],
    "test": [
        ('What sits at the top of an attack tree?',
         [('a', 'A list of prices'), ('b', 'A map of the office'), ('c', "The attacker's goal"), ('d', 'The date of the last update')], 'c'),
        ('What does an AND branch mean?',
         [('a', 'Any one step is enough'), ('b', 'All the steps below must succeed'), ('c', 'The attacker must pay twice'), ('d', 'The branch is ignored')], 'b'),
        ('What is the cheapest path used for?',
         [('a', 'To show the most likely route an attacker would take'), ('b', 'To decorate the tree'), ('c', 'To hide the goal'), ('d', 'To delete the lowest leaves')], 'a'),
        ('Where is a mitigation placed?',
         [('a', 'At the bottom of the printer'), ('b', 'In the goal box only'), ('c', 'On the branch it blocks'), ('d', 'In a different company')], 'c'),
        ('Why are attack tree costs called estimates?',
         [('a', 'They are printed on paper'), ('b', 'They are always exact'), ('c', 'They are set by law'), ('d', 'They come from expert judgement, not exact measurement')], 'd'),
    ],
}
