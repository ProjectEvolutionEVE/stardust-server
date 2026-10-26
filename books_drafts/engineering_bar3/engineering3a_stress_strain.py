"""Stress and Strain: how hard a material is loaded, and how far it moves in return."""
CODE = 'engineering3a_stress_strain'
BOOK = {
    "title": 'Stress and Strain',
    "subtitle": 'How hard a material is loaded, and how far it stretches in return',
    "chapters": [
        ('Stress is force on an area',
         'Stress is the force on a part divided by the area that force is spread over. The same push on a sharp point gives far more stress than on a broad pad. Stress is measured in pascals, which are newtons per square metre.'),
        ('Strain is how far it moves',
         'Strain is the change in length divided by the original length. It has no unit, because a metre divided by a metre is just a number. A one metre bar that stretches by one millimetre has a strain of 0.001.'),
        ('Springing back',
         "Within its elastic limit, a material springs back to its old length when the load is removed. Stress and strain rise together in a straight line. The steepness of that line is called Young's modulus, and steel has about 200 gigapascals of it, while aluminium has about 70."),
        ('Past the yield point',
         'Load a metal past its yield point and it stays bent or stretched when the load comes off. That change is permanent. Designers keep working stresses well below yield, so a part never reaches the point where it changes shape for good.'),
        ('A worked example',
         'A steel rod with a cross section of one square centimetre carries 1,000 newtons. Its stress is 10 million pascals, or 10 megapascals. Its strain is then 0.00005, so a 2 metre rod stretches by about 0.1 millimetres.'),
        ('Why it matters',
         'Every load path is checked for stress and strain before a part is built. A part that is too thin where the load runs through it can stretch too far or yield, even if it never snaps. Get the forces and the material figures right, and the rest follows.'),
    ],
    "test": [
        ('What is stress?',
         [('a', 'The colour of a part'), ('b', 'Force divided by the area it is spread over'), ('c', 'Length divided by time'), ('d', 'The weight of the part')], 'b'),
        ('What unit does strain have?',
         [('a', 'Newtons'), ('b', 'Pascals'), ('c', 'None, because it is a plain ratio'), ('d', 'Metres')], 'c'),
        ('Within the elastic limit, what happens when the load is removed?',
         [('a', 'The part springs back to its original length'), ('b', 'The part stays permanently stretched'), ('c', 'The part gets heavier'), ('d', 'The part melts')], 'a'),
        ('What happens if a metal is loaded past its yield point?',
         [('a', 'It stays permanently bent or stretched'), ('b', 'It springs back perfectly'), ('c', 'Its density doubles'), ('d', 'It stops having any stress')], 'a'),
        ('What is the stress on a 2 square centimetre pad under a 1,000 newton load?',
         [('a', '500 pascals'), ('b', '5 kilopascals'), ('c', '50 megapascals'), ('d', '5 megapascals')], 'd'),
    ],
}
