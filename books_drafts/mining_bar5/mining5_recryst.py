"""Recrystallisation and Grain Growth: how heat lets new, strain-free grains replace the worked ones, and then grow."""
CODE = 'mining5_recryst'
BOOK = {
    "title": 'Recrystallisation and Grain Growth',
    "subtitle": 'How heat swaps worked grains for fresh ones, and then lets them grow',
    "chapters": [
        ('Annealing', 'Annealing heats a worked metal so that its strain can be released. New grains form and take over the old, deformed ones. The metal becomes softer and easier to shape again.'),
        ('Nucleation', 'New grains start, or nucleate, in the most strained places in the metal. These spots have the most stored energy. Once a tiny new grain forms, it can begin to grow.'),
        ('Growth', 'The new grains grow into the strained material around them, because their boundaries move. Growth continues until the whole metal is covered. Heat, time and the amount of strain set how far it goes.'),
        ('Zener pinning', 'Tiny particles in the metal can pin grain boundaries and slow their movement. This is called Zener pinning. It keeps grains small and helps the metal stay strong.'),
        ('Annealing textures', 'Recrystallisation can leave a preferred direction in the grains, called a texture. Textures change how the metal behaves when it is shaped later. Engineers choose the anneal to get the texture they need.'),
        ('Practice', 'Mills plan their anneals with heat, time and strain in mind. Too much heat can grow grains too large and lower strength. Good control keeps the grain size where the job needs it.'),
    ],
    "test": [
        ('What does annealing do to a worked metal?', [('a', 'It turns the metal into paper'), ('b', 'It lets new, strain-free grains form and take over'), ('c', 'It makes the metal liquid at once'), ('d', 'It adds weight to the metal')], 'b'),
        ('Where do new grains usually start?', [('a', 'In the calmest corner'), ('b', 'Outside the metal'), ('c', 'In the most strained places'), ('d', 'In the air above it')], 'c'),
        ('What is Zener pinning?', [('a', 'A sharp needle that makes holes'), ('b', 'A type of paint'), ('c', 'A way to cool the metal fast'), ('d', 'Tiny particles slow the movement of grain boundaries')], 'd'),
        ('What is a texture in annealed metal?', [('a', 'A preferred direction in the grains'), ('b', 'The shine of the surface'), ('c', 'The smell of the metal'), ('d', 'The weight of the bar')], 'a'),
        ('What happens if the heat is too high for too long?', [('a', 'Grains shrink to dust'), ('b', 'Grains grow too large and strength can drop'), ('c', 'Strength always rises'), ('d', 'The metal gets lighter')], 'b'),
    ],
}
