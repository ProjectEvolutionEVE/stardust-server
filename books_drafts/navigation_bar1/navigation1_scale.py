"""Scale and Distance: what a map scale means, how the game measures in metres, and how far things really are."""
CODE = 'navigation1_scale'
BOOK = {
    "title": 'Scale and Distance',
    "subtitle": 'Map scales, metres, kilometres and AU, and the game at true scale',
    "chapters": [
        ('What a scale tells you',
         'A scale says how much real distance one unit of a drawing stands for. A map marked 1:100,000 means that one centimetre on paper is one kilometre on the ground. The bigger the second number, the more ground fits on the page, and the less detail you see.'),
        ('Metres, kilometres and the game',
         'The game measures everything in metres, so one unit in the game is one real metre. A kilometre is a thousand metres. The game writes the number that suits the distance: metres for the very short, kilometres for the nearby, and AU once the distances get very large.'),
        ('How the game writes a distance',
         'Under 1,000 metres the game shows whole metres. Up to 100 km it shows kilometres with one decimal place. Past that it shows whole kilometres, and once a distance passes about 7.5 million km it switches to AU, with two decimal places. The same distance always reads the same way, so you can compare the lists.'),
        ('True size, true distance',
         'The Sun has a true radius of about 695,700 km, and the rings and gas giants sit at their true distances from it. The numbers are exact to scale. Bodies farther than 200 km away are drawn closer in, but at their true apparent size, so they look exactly as large as they would from where you are.'),
        ('Far things look small',
         'In real life, a thing looks smaller the farther away it is. Move ten times farther from a debris field and it looks about one tenth as wide. That is why a distant object can look tiny even when it is huge, and why the labels give the real distance.'),
        ('Distance from speed',
         'The info line shows your speed in metres per second. Multiply the speed by the number of seconds you travel to get the distance you cover. At 60 metres a second, a craft covers 3.6 km in one minute.'),
    ],
    "test": [
        ('On a map at a scale of 1:100,000, what does one centimetre on paper stand for?',
         [('a', '1 metre'), ('b', '10 metres'), ('c', '1 kilometre'), ('d', '100 kilometres')], 'c'),
        ('What unit does the game measure its distances in?',
         [('a', 'Miles'), ('b', 'Metres, with one game unit equal to one metre'), ('c', 'Light-years'), ('d', 'Screen pixels')], 'b'),
        ('If you move ten times farther from an object, how does its apparent size change?',
         [('a', 'It looks about the same'), ('b', 'It looks twice as big'), ('c', 'It looks ten times bigger'), ('d', 'It looks about one tenth as wide')], 'd'),
        ('At 60 metres a second, how far does a craft travel in one minute?',
         [('a', '3.6 km'), ('b', '36 km'), ('c', '600 metres'), ('d', '60 km')], 'a'),
        ('Past about 7.5 million km, which unit does the game switch to?',
         [('a', 'Metres'), ('b', 'Kilometres'), ('c', 'AU'), ('d', 'Light-years')], 'c'),
    ],
}
