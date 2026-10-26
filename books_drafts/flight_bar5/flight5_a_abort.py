"""Launch Aborts: the safety options a crew has if something goes wrong during the climb."""
CODE = 'flight5_a_abort'
BOOK = {
    "title": 'Launch Aborts',
    "subtitle": 'The safety options when something goes wrong on the climb',
    "chapters": [
        ('Why aborts matter',
         'A launch is the most dangerous part of most spaceflights. An abort system lets the crew escape from a failing rocket. Designers plan a set of abort options, each for a different point in the climb.'),
        ('Launch escape towers',
         'Some craft have a launch escape tower on top. If the rocket fails, the tower pulls the crew capsule away at high speed. The Apollo missions had this kind of tower, and so do Soyuz craft.'),
        ('Shuttle options',
         'The Space Shuttle had several abort options, depending on when a problem appeared. Some led to a landing at a runway, and some to a landing in the ocean. The options narrowed as the Shuttle climbed.'),
        ('Soyuz',
         'Soyuz craft have a launch escape system that has been used more than once to save crews. A successful abort on the pad in 1983 showed the system working as designed. Soyuz is one of the most reliable crew launch vehicles.'),
        ('Crew Dragon',
         'Crew Dragon uses engines built into its capsule for launch aborts. In an abort test in 2020 the capsule flew away from a failing rocket on its own power. This allows escape at many points during the climb.'),
        ('Trade-offs',
         'Abort systems add weight and cost, and they are designed with trade-offs in mind. The aim is to keep the crew safe across the most likely failures, without making the rocket too heavy to fly.'),
    ],
    "test": [
        ('What is the main purpose of a launch abort system?',
         [('a', 'To let the crew escape from a failing rocket'), ('b', 'To make the rocket faster'), ('c', 'To paint the capsule'), ('d', 'To cook food')], 'a'),
        ('What does a launch escape tower do?',
         [('a', 'It holds the rocket still for ever'), ('b', 'It pulls the crew capsule away from a failing rocket'), ('c', 'It sends radio songs'), ('d', 'It makes fuel')], 'b'),
        ('Which crew launch vehicle has used its escape system more than once to save crews?',
         [('a', 'A hot air balloon'), ('b', 'A ferry'), ('c', 'Soyuz'), ('d', 'A bicycle')], 'c'),
        ('What do the abort options depend on?',
         [('a', 'The colour of the rocket'), ('b', 'The weather at a restaurant'), ('c', "The crew's favourite music"), ('d', 'When a problem appears during the climb')], 'd'),
        ('What is a trade-off in abort design?',
         [('a', 'Safety gains are weighed against extra weight and cost'), ('b', 'Speed is traded for paint'), ('c', 'Crew is traded for fuel'), ('d', 'Radio is traded for food')], 'a'),
    ],
}
