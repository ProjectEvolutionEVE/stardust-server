"""Epidemic Broadcast Theory: spreading news through a group by rumour, the way an illness spreads."""
CODE = 'computing5_epidemic_broadcast'
BOOK = {
    "title": 'Epidemic Broadcast Theory',
    "subtitle": 'Spreading news through a group by rumour, the way an illness spreads',
    "chapters": [
        ('Spreading by rumour', 'In a gossip protocol, each member tells a few random others about new information. Those members then tell a few more. The news spreads through the group much as a rumour does, with no central sender.'),
        ('Infection models', 'The spread can be described by an infection model: members are either aware or not, and each round some unaware members become aware. Researchers use these models to predict how fast news travels and how many members it reaches.'),
        ('Logarithmic rounds', 'With random partners, news reaches almost everyone in about the logarithm of the group size in rounds. Doubling the group adds only about one more round. That is why gossip scales well to large groups.'),
        ('Anti-entropy', 'Anti-entropy is a repair method where two members compare their data and fill in what the other is missing. It is slower than rumour spreading, but it catches anything the rumours missed. Many systems use both together.'),
        ('Fanout choices', 'The fanout is how many partners each member contacts per round. A larger fanout spreads news faster but costs more messages. Designers choose a number that reaches almost everyone without flooding the network.'),
        ('Gossip membership', 'Gossip can also share who is in the group, so members learn about joins and leaves. The list is never exact, but it is close enough to find partners. This is how many large systems keep track of their members.'),
    ],
    "test": [
        ('How does news spread in a gossip protocol?',
         [('a', 'Through one central sender only'), ('b', 'By post'), ('c', 'By radio only'), ('d', 'Each member tells a few random others, who tell more')], 'd'),
        ('How many rounds does news take in a gossip group, roughly?',
         [('a', 'The logarithm of the group size'), ('b', 'The group size squared'), ('c', 'One round exactly'), ('d', 'Forever')], 'a'),
        ('What does anti-entropy do?',
         [('a', 'Stops all messages'), ('b', 'Sends pictures'), ('c', 'Deletes members'), ('d', 'Two members compare data and fill gaps')], 'd'),
        ('What does a larger fanout do?',
         [('a', 'Spreads news faster but costs more messages'), ('b', 'Slows news'), ('c', 'Removes members'), ('d', 'Changes colours')], 'a'),
        ('What does gossip membership share?',
         [('a', 'Nothing about the group'), ('b', 'Members never learn of joins'), ('c', 'Who is in the group'), ('d', 'The group is always exact')], 'c'),
    ],
}
