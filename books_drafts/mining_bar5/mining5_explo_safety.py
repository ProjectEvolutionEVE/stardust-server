"""Explosives storage and handling in mining: magazines, separation distances, inventory, transport, licensing and incidents."""
CODE = 'mining5_explo_safety'
BOOK = {
    'title': 'Explosives Storage and Handling',
    'subtitle': 'The strict rules for keeping, counting and moving explosives safely',
    "chapters": [
        ('Why this is strict', 'Explosives are stored and moved under strict rules, because a mistake can cause severe harm. The rules are set by the law and enforced by inspection.'),
        ('Magazines', 'Explosives are kept in purpose-built magazines. A magazine is secure, dry and clearly marked.'),
        ('Separation distances', 'Magazines must sit a set distance from people, buildings and other hazards. The distance depends on the quantity kept.'),
        ('Inventory', 'Stock is counted and recorded, so any shortfall is noticed at once. Stock records are checked against physical counts on a regular schedule.'),
        ('Transport and licensing', 'Explosives are moved only in approved vehicles, by licensed people, and under the rules of the local authority. Drivers and handlers must hold the licences that the local rules require.'),
        ('Incidents', 'Any incident is reported and investigated. The lessons are used to improve the rules and the training.'),
    ],
    "test": [
        ('Why are explosives handled under strict rules?', [('a', 'They are expensive to paint'), ('b', 'A mistake can cause severe harm'), ('c', 'They are heavy to lift'), ('d', 'They must always be kept in the sun')], 'b'),
        ('What does separation distance mean?', [('a', 'The gap between two drill rigs'), ('b', 'The space between shifts'), ('c', 'A set distance from people, buildings and other hazards'), ('d', 'The length of a haul road')], 'c'),
        ('What is inventory used for?', [('a', 'Noticing a shortfall at once'), ('b', 'Choosing paint colours'), ('c', 'Ordering new lunch boxes'), ('d', 'Counting the number of helmets in the canteen')], 'a'),
        ('Who may move explosives?', [('a', 'Anyone with a spare hour'), ('b', 'Only the cook'), ('c', 'Anyone who owns a car'), ('d', 'Licensed people in approved vehicles')], 'd'),
        ('What happens after an incident?', [('a', 'It is forgotten'), ('b', 'It is hidden from inspectors'), ('c', 'It is reported, investigated and used to improve the rules'), ('d', 'It is blamed on the weather')], 'c'),
    ],
}
