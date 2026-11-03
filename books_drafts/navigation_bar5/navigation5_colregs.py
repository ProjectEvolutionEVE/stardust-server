"""The COLREGs Rules of the Road: The rules that keep ships from colliding."""
CODE = 'navigation5_colregs'
BOOK = {
    'title': 'The COLREGs Rules of the Road',
    'subtitle': 'The rules that keep ships from colliding',
    'chapters': [
        ('Rules for every ship', 'The International Regulations for Preventing Collisions at Sea set out how vessels must act to avoid collisions. They apply to almost all ships on the open sea.'),
        ('Crossing', 'When two power-driven vessels are crossing, the one that has the other on its starboard side generally gives way. The other keeps its course and speed.'),
        ('Overtaking', 'A vessel overtaking another must keep clear, even if the other is moving at a different speed. The overtaking vessel is responsible for keeping out of the way.'),
        ('Head-on', 'When two power-driven vessels meet head-on, each generally alters course to starboard, so that they pass port to port.'),
        ('Lights and shapes', 'Ships show lights and shapes so others can judge their size, direction and activity. Reading them correctly is part of safe navigation.'),
        ('Judgement and limits', 'The rules cannot cover every situation. Good seamanship and early action are needed, and the rules are a framework, not a guarantee.'),
    ],
    'test': [
        ('Which situation is covered as crossing?', [('a', 'A ship in dry dock'), ('b', 'A boat on a trailer'), ('c', 'Two vessels crossing paths, one with the other on its starboard side'), ('d', 'Two ships sitting at anchor')], 'c'),
        ('In a head-on meeting, what do vessels generally do?', [('a', 'Both stop in the middle'), ('b', 'Both turn to port'), ('c', 'Both reverse at once'), ('d', 'Each alters course to starboard')], 'd'),
        ('Who keeps clear when overtaking?', [('a', 'The overtaking vessel'), ('b', 'The vessel being overtaken always'), ('c', 'Neither'), ('d', 'A passenger')], 'a'),
        ('What do lights and shapes show?', [('a', 'The menu'), ('b', 'The lunch time'), ('c', 'The size, direction and activity of a vessel'), ('d', "The owner's name")], 'c'),
        ('How are the COLREGs best described?', [('a', 'A guarantee against all accidents'), ('b', 'A recipe for dinner'), ('c', 'A tide table'), ('d', 'A framework that needs good seamanship')], 'd'),
    ],
}
