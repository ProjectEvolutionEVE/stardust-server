"""Deorbit and Disposal: how spacecraft are brought down safely, or moved out of the way."""
CODE = 'flight5_a_deorbit'
BOOK = {
    "title": 'Deorbit and Disposal',
    "subtitle": 'Bringing spacecraft down safely, or moving them out of the way',
    "chapters": [
        ('Controlled and uncontrolled',
         'A craft that is brought down on purpose, aimed at a remote part of the ocean, is a controlled reentry. A craft left to fall on its own, with no plan for where it lands, is an uncontrolled one. Planners prefer control, because it keeps people on the ground safe.'),
        ('How a deorbit burn works',
         'To come down, a craft fires its engine against its direction of travel. This lowers the far side of its orbit until the air takes over. The air then slows it further as it falls.'),
        ('The space station',
         'When the International Space Station reaches the end of its life, it is planned to be brought down in a controlled way. The plan reduces the risk to people on the ground by aiming the debris over a remote ocean.'),
        ('Graveyard orbits',
         'Some craft do not come down. They are moved to a graveyard orbit, a place where they are out of the way of useful orbits. This is common for high satellites that cannot easily be brought back down.'),
        ('The spacecraft cemetery',
         'The South Pacific, around a point far from any land, is used as a disposal area for old craft. It is the most remote part of the oceans, so debris that survives reentry is least likely to hit anyone.'),
        ('Rules and risk',
         'Space agencies and countries set rules that limit the risk from falling debris. The goal is to keep the chance of harm to people very low. Good disposal plans are part of building any mission.'),
    ],
    "test": [
        ('What is a controlled reentry?',
         [('a', 'A craft brought down on purpose, aimed at a remote ocean'), ('b', 'A craft that falls with no plan at all'), ('c', 'A craft that never comes back'), ('d', 'A craft that burns on the pad')], 'a'),
        ('How does a craft fire its engine to start coming down?',
         [('a', 'Along its direction of travel'), ('b', 'Against its direction of travel'), ('c', 'Sideways only'), ('d', 'It does not use the engine')], 'b'),
        ('Where is the old spacecraft cemetery?',
         [('a', 'In the middle of a large desert'), ('b', 'On the Moon'), ('c', 'In the South Pacific, far from land'), ('d', 'On the top of a mountain')], 'c'),
        ('What is a graveyard orbit?',
         [('a', 'The orbit used for landing'), ('b', 'A training route for crews'), ('c', 'The lowest orbit around the Earth'), ('d', 'A place where a craft is moved to be out of the way of useful orbits')], 'd'),
        ('Why do planners prefer controlled reentry?',
         [('a', 'It keeps the risk to people on the ground low'), ('b', 'It is cheaper to watch on the news'), ('c', 'It makes the craft heavier'), ('d', 'It stops the Earth turning')], 'a'),
    ],
}
