"""Plotting a Course: planning a route, how WARP bends around the Sun, and how real navigators plan ahead."""
CODE = 'navigation1_courses'
BOOK = {
    "title": 'Plotting a Course',
    "subtitle": 'Routes, bends around the Sun, and planning ahead like a real navigator',
    "chapters": [
        ('What a course is',
         'A course is the route from where you are to where you want to go. Real navigators plot it on a chart before they set off, then check their position as they travel. A good plan saves time and fuel.'),
        ('The straight line',
         'The shortest route between two points is a straight line. WARP follows a straight line whenever it can. A much longer trip takes only a little longer, because WARP\'s travel time grows slowly as the distance grows.'),
        ('When the Sun is in the way',
         'Sometimes the straight line passes close to the Sun. If it passes within 0.25 AU of the Sun, WARP does not cut through that space. Real missions keep well clear of the Sun too, because of its heat and its pull on the craft.'),
        ('The bend',
         'In that case the route swings out round the outside of the Sun, to a point at least 0.6 AU from it, on the side you are already on. Think of walking round a lake instead of straight across the middle of it.'),
        ('Planning ahead',
         'Planets keep moving, so a craft aimed at where a planet is now will miss it. Real mission planners aim at where the planet will be when the craft arrives. Good navigation is about the future position, not only the present one.'),
        ('Moving between orbits',
         'A real way to move from one orbit to another is the Hohmann transfer. It uses two engine burns, with a long coast between them along an oval path. It is one of the most fuel-efficient ways to move between near-circular orbits, which is why planners use it so often.'),
    ],
    "test": [
        ('What does WARP do when the straight line passes within 0.25 AU of the Sun?',
         [('a', 'It stops the craft'), ('b', 'It bends the route around the Sun'), ('c', 'It sends you to Jupiter'), ('d', 'It speeds up the Sun')], 'b'),
        ('How far from the Sun does a bent route swing out, at least?',
         [('a', '0.1 AU'), ('b', '0.25 AU'), ('c', '0.6 AU'), ('d', '9.6 AU')], 'c'),
        ('Why does a real navigator aim at where a planet will be, not where it is now?',
         [('a', 'Planets are invisible'), ('b', 'Planets are always standing still'), ('c', 'The planet pulls the craft back'), ('d', 'Planets keep moving, so a craft aimed at the old spot would miss')], 'd'),
        ('How does WARP\'s travel time change on a much longer trip?',
         [('a', 'It grows slowly, so a much longer trip takes only a little longer'), ('b', 'It doubles each time the distance doubles'), ('c', 'It stays exactly the same'), ('d', 'It is shorter for a longer trip')], 'a'),
        ('What is a Hohmann transfer?',
         [('a', 'A kind of map projection'), ('b', 'A radar range'), ('c', 'A way to move between orbits with two burns and a long coast'), ('d', 'A type of debris')], 'c'),
    ],
}
